from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(declarative_base()):
    pass


async def get_session():
    async with async_session() as session:
        yield session
