import enum
from datetime import datetime

from pydantic import BaseModel, Field

from app.app_ctx import AppCtx
from app.settings import settings


class DataNotReady(Exception):
    ...


class AppInfo(BaseModel):
    name: str = "test-sma"
    version: str = "0.0.1"


class ErrorResponse(BaseModel):
    success: bool = False
    message: str


class SMAWindow(enum.IntEnum):
    seven = 7
    twenty_five = 25
    ninenty_nine = 99


class SMAResult(BaseModel):
    symbol: str = settings.SYMBOL
    periods: SMAWindow
    sma_value: float


class ClosePrice(BaseModel):
    value: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def save(self) -> None:
        sql = 'INSERT INTO close_prices (value, created_at) VALUES (?, ?)'
        with AppCtx.db as conn:
            conn.cursor().execute(sql, (self.value, self.created_at))

    def get_sma(periods: SMAWindow) -> float:
        sql = 'SELECT value FROM close_prices ORDER BY created_at DESC LIMIT ?'
        items = AppCtx.db.cursor().execute(sql, (periods,)).fetchall()
        if items:
            return sum([i['value'] for i in items]) / min(periods, len(items))

        raise DataNotReady("No data available yet, please, try again later")
