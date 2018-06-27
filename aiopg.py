import asyncio
from aiopg.sa import create_engine
import sqlalchemy as sa


metadata = sa.MetaData()

tbl = sa.Table('users', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255),
		sa.Column('pass', sa.String(255))

async def go():
    async with create_engine(user='aiopg',
                             database='aiopg',
                             host='127.0.0.1',
                             password='passwd') as engine:
        async with engine.acquire() as conn:
            await conn.execute(tbl.insert().values(val='abc'))

            async for row in conn.execute(tbl.select().where(tbl.c.val=='abc')):
                print(row.id, row.val)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())

