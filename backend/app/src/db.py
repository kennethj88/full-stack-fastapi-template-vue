from typing import AsyncGenerator

from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.config import settings
from src.core.security import get_password_hash

# Create sync engine for migrations and sync operations
engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True,
)

# Create async engine for main application
async_engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI).replace("postgresql://", "postgresql+asyncpg://"),
    pool_pre_ping=True,
)

# Session factories
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)

class Base(DeclarativeBase):
    """Base class for all database models"""
    pass

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async database sessions"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

def get_session() -> Session:
    """Get a synchronous database session"""
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

async def init_db() -> None:
    """Initialize database tables and initial data"""
    async with async_engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as session:
        from src.models import User
        from src.config import settings
        
        # Check if superuser exists
        result = await session.execute(
            select(User).where(User.email == settings.FIRST_SUPERUSER)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            user = User(
                email=settings.FIRST_SUPERUSER,
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
                is_superuser=True,
                is_active=True
            )
            session.add(user)
            await session.commit()
