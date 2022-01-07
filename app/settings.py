from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_HOST: str = '127.0.0.1'
    APP_PORT: int = 8000
    DATABASE: str = 'data.db'
    TICKER_URI: str = 'wss://stream.binance.com:9443'
    SYMBOL: str = 'BTCUSDT'

    class Config:
        env_prefix = 'TS_'


settings = Settings()
