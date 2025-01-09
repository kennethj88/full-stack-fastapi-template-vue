# FastAPI Project Template

A full-stack FastAPI template with:

Backend:
- ⚡️ [FastAPI](https://fastapi.tiangolo.com/) for the backend API
- 🐘 [PostgreSQL](https://www.postgresql.org/) for the database
- 🔍 [SQLAlchemy](https://www.sqlalchemy.org/) for ORM and database migrations
- 🔒 JWT token authentication
- 📧 Email verification and password recovery
- 🔄 Async database operations

Frontend:
- 🎨 [Vue 3](https://v3.vuejs.org/) with [Nuxt 3](https://nuxt.com/) for the frontend
- 💅 [TailwindCSS](https://tailwindcss.com/) and [DaisyUI](https://daisyui.com/) for styling
- 📦 [Pinia](https://pinia.vuejs.org/) for state management
- 🔧 [VueUse](https://vueuse.org/) for composables

Development:
- 🐋 [Docker Compose](https://docs.docker.com/compose/) for development and deployment
- 🧪 [Pytest](https://docs.pytest.org/) for backend testing
- 🎭 [Playwright](https://playwright.dev/) for frontend testing
- 📝 [Alembic](https://alembic.sqlalchemy.org/) for database migrations
- 🔍 [Adminer](https://www.adminer.org/) for database management

## Quick Start

1. Clone this repository
2. Have Docker and Docker Compose installed
3. Run the development server:
```bash
docker compose watch
```

## Services

The following services will be available:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Adminer (DB Management): http://localhost:8080
- Mailcatcher (Email Testing): http://localhost:1080

## Documentation

- [Development Guide](development.md)
- [Deployment Guide](deployment.md)
- [Release Notes](release-notes.md)
