import sentry_sdk
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
import logging
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.models import SecurityScheme, SecuritySchemeType

from src.config import settings
from src.auth.router import router as auth_router
from src.items.router import router as items_router
from src.users.router import router as users_router
from src.core.router import router as core_router
from fastapi import APIRouter

from src.core import router





def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


if settings.SENTRY_DSN and settings.ENVIRONMENT != "local":
    sentry_sdk.init(dsn=str(settings.SENTRY_DSN), enable_tracing=True)

# Setup logging
logging.basicConfig(
    level=logging.DEBUG if settings.ENVIRONMENT == "local" else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Update the OAuth2 scheme with correct token URL
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login/access-token"
)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    generate_unique_id_function=custom_generate_unique_id,
)

logger.info(f"Starting {settings.PROJECT_NAME} in {settings.ENVIRONMENT} environment cors {settings.all_cors_origins}")

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.openapi_schema = None  # Clear any existing schema
#app.add_middleware(CORSMiddleware, *settings.BACKEND_CORS_ORIGINS)

# Add security scheme to OpenAPI
app.openapi_components = {
    "securitySchemes": {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": f"{settings.API_V1_STR}/auth/login/access-token",
                    "scopes": {}
                }
            }
        },
        "Bearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter your bearer token in the format: Bearer <token>"
        }
    }
}

# Update security requirements to include both schemes
app.openapi_security = [
    {"OAuth2PasswordBearer": []},
    {"Bearer": []}
]

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(items_router, prefix="/items", tags=["items"])
api_router.include_router(core_router,prefix="/utils", tags=["utils"])


app.include_router(api_router, prefix=settings.API_V1_STR)
