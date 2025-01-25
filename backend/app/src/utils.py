import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import emails  # type: ignore
import jwt
from jinja2 import Template
from jwt.exceptions import InvalidTokenError
from klaviyo_api import KlaviyoAPI
import mailgun
from src.core import security
from src.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class EmailData:
    html_content: str
    subject: str


def render_email_template(*, template_name: str, context: dict[str, Any]) -> str:
    template_str = (
        Path(__file__).parent.parent / "email-templates" / "build" / template_name
    ).read_text()
    html_content = Template(template_str).render(context)
    return html_content


async def send_klaviyo_event(
    *,
    event_name: str,
    customer_properties: dict[str, Any],
    properties: dict[str, Any] | None = None,
    timestamp: datetime | None = None
) -> bool:
    """
    Send an event to Klaviyo using their API.
    
    Args:
        event_name: Name of the event to track
        customer_properties: Dict containing at minimum an email or phone number
        properties: Optional properties related to the event
        timestamp: Optional timestamp for the event
    """
    try:

        if not settings.KLAVIYO_API_KEY:
            logger.warning("Klaviyo API key not set, skipping event tracking")
            return False

        api = KlaviyoAPI(settings.KLAVIYO_API_KEY)
        
        event_data = {
            "type": "event",
            "attributes": {
                "metric": {
                    "name": event_name
                },
                "profile": customer_properties,
                "properties": properties or {},
                "time": timestamp.isoformat() if timestamp else datetime.now(timezone.utc).isoformat()
            }
        }

        await api.Events.create(event_data)
        logger.info(f"Successfully sent event '{event_name}' to Klaviyo")
        return True

    except Exception as e:
        logger.error(f"Failed to send Klaviyo event: {str(e)}")
        return False


async def send_email(
    *,
    email_to: str,
    subject: str = "",
    html_content: str = "",
) -> bool:
    """
    Send an email using Mailgun API.
    
    Args:
        email_to: Recipient email address
        subject: Email subject
        html_content: HTML content of the email
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        if settings.emails_enabled:
             
            # Initialize Mailgun client
            mg = mailgun.Client(settings.MAILGUN_API_KEY)
            
            # Prepare email data
            email_data = {
                "from": f"{settings.PROJECT_NAME} <{settings.EMAILS_FROM_EMAIL}>",
                "to": [email_to],
                "subject": subject,
                "html": html_content,
            }
            
            # Send email using Mailgun domain
            response = mg.domains(settings.MAILGUN_DOMAIN).messages.send(**email_data)
            
            logger.info(f"Email sent successfully. Response: {response}")
            return True
        else:
            logger.info("Emails disabled, skipping send")
            return False
            
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False

def generate_test_email(email_to: str) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    html_content = render_email_template(
        template_name="test_email.html",
        context={"project_name": settings.PROJECT_NAME, "email": email_to},
    )
    return EmailData(html_content=html_content, subject=subject)


async def generate_reset_password_email(email_to: str, email: str, token: str) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    link = f"{settings.FRONTEND_HOST}/reset-password?token={token}"
   
    send_klaviyo_event(
        event_name="Reset Password Request",
        customer_properties={
            "email": email_to,
        },
        properties={
            "source": "webapp",
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        }
    )

    
    html_content = render_email_template(
        template_name="reset_password.html",
        context={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )

    send_email(email_to=email_to, subject= subject ,html_content=html_content ) 
    
    return True


def generate_new_account_email(
    email_to: str, username: str, password: str
) -> EmailData:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    html_content = render_email_template(
        template_name="new_account.html",
        context={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": settings.FRONTEND_HOST,
        },
    )
    return EmailData(html_content=html_content, subject=subject)


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.now(timezone.utc)
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email},
        settings.SECRET_KEY,
        algorithm=security.ALGORITHM,
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> str | None:
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        return str(decoded_token["sub"])
    except InvalidTokenError:
        return None
