from sqlalchemy.ext.asyncio import create_async_engine
from db.models import Base


def create_connection(address):
    engine = create_async_engine(
        'postgresql+asyncpg://' + address,
        echo = False,
    )
    return engine


async def create_all(engine):
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
