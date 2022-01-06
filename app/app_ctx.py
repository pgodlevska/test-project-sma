import json
import sqlite3
from contextlib import contextmanager

from websockets.client import WebSocketClientProtocol, connect as ws_connect

from app.settings import settings


class AppCtx:
    db: sqlite3.Connection
    ws: WebSocketClientProtocol

    @classmethod
    async def start(cls) -> None:
        # connect to database and init fresh schema
        cls.db = sqlite3.connect(
            settings.DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES,
            check_same_thread=False,
        )
        cls.db.row_factory = sqlite3.Row
        with open('app/db/schema.sql') as f:
            cls.db.executescript(f.read())

        # subscribe to binance Ticker
        cls.ws = await ws_connect(f'{settings.TICKER_URI}/ws/{settings.SYMBOL.lower()}@miniTicker')

    @classmethod
    async def stop(cls) -> None:
        await cls.ws.close()
        cls.db.close()
