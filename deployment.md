# FastAPI Project - Deployment

You can deploy the project using Docker Compose to a remote server.

## Preparation

* Have a remote server ready and available.
* Configure the DNS records of your domain to point to the IP of the server you just created.
* Install and configure [Docker](https://docs.docker.com/engine/install/) on the remote server (Docker Engine, not Docker Desktop).

## Environment Variables

You need to set some environment variables first.

Set the `ENVIRONMENT`, by default `local` (for development), but when deploying to a server you would put something like `staging` or `production`:

```bash
export ENVIRONMENT=production
```

You can set several variables, like:

* `PROJECT_NAME`: The name of the project, used in the API for the docs and emails.
* `BACKEND_CORS_ORIGINS`: A list of allowed CORS origins separated by commas.
* `SECRET_KEY`: The secret key for the FastAPI project, used to sign tokens.
* `FIRST_SUPERUSER`: The email of the first superuser, this superuser will be the one that can create new users.
* `FIRST_SUPERUSER_PASSWORD`: The password of the first superuser.
* `SMTP_HOST`: The SMTP server host to send emails, this would come from your email provider (E.g. Mailgun, Sparkpost, Sendgrid, etc).
* `SMTP_USER`: The SMTP server user to send emails.
* `SMTP_PASSWORD`: The SMTP server password to send emails.
* `EMAILS_FROM_EMAIL`: The email account to send emails from.
* `POSTGRES_SERVER`: The hostname of the PostgreSQL server. You can leave the default of `db`, provided by the same Docker Compose.
* `POSTGRES_PORT`: The port of the PostgreSQL server. You can leave the default.
* `POSTGRES_PASSWORD`: The Postgres password.
* `POSTGRES_USER`: The Postgres user, you can leave the default.
* `POSTGRES_DB`: The database name to use for this application.
* `SENTRY_DSN`: The DSN for Sentry, if you are using it.

### Generate Secret Keys

Some environment variables in the `.env` file have a default value of `changethis`.

You have to change them with a secret key, to generate secret keys you can run the following command:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the content and use that as password / secret key. And run that again to generate another secure key.

## Production Setup

For production, you should:

1. Set up SSL/TLS certificates (using Let's Encrypt or your preferred provider)
2. Configure a reverse proxy (like Nginx) to handle HTTPS and domain routing
3. Set appropriate security headers
4. Configure proper CORS settings in the backend
5. Set up monitoring and logging
6. Configure backups for the database

### Example Nginx Configuration

Here's a basic Nginx configuration example:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Adminer
    location /adminer {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Deploy with Docker Compose

With the environment variables in place, you can deploy with Docker Compose:

```bash
docker compose up -d
```

The following services will be available:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Adminer (DB Management): http://localhost:8080

## GitHub Actions Environment Variables

There are some environment variables only used by GitHub Actions that you can configure:

* `LATEST_CHANGES`: Used by the GitHub Action [latest-changes](https://github.com/tiangolo/latest-changes) to automatically add release notes based on the PRs merged.
* `SMOKESHOW_AUTH_KEY`: Used to handle and publish the code coverage using [Smokeshow](https://github.com/samuelcolvin/smokeshow).
