from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE: str = 'data.db'
    TICKER_URI: str = 'wss://stream.binance.com:9443/ws'
    SYMBOL: str = 'BTCUSDT'

    class Config:
        env_prefix = 'TS_'


settings = Settings()
