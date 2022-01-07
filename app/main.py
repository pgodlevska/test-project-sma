import asyncio
import json
import logging

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.app_ctx import AppCtx
from app.models import AppInfo, ClosePrice, DataNotReady, ErrorResponse, SMAResult, SMAWindow
from app.settings import settings

app = FastAPI()

responses = {
    status.HTTP_503_SERVICE_UNAVAILABLE: {'description': 'Service not ready', 'model': ErrorResponse},
}

@app.get('/', response_model=AppInfo)
def root() -> dict:
    """Root endpoint, app info"""
    return {}


@app.get('/sma', response_model=SMAResult, responses=responses, tags=['SMA'])
def get_sma(periods: SMAWindow) -> dict:
    """Get SMA value for specified number of periods"""
    return {'periods': periods, 'sma_value': ClosePrice.get_sma(periods)}


@app.exception_handler(DataNotReady)
async def not_ready_handler(request: Request, ex: DataNotReady) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={'success': False, 'message': str(ex)},
    )


async def receive_close_prices() -> None:
    async for message in AppCtx.ws:
        try:
            ClosePrice(value=json.loads(message)['c']).save()
        except (json.JSONDecodeError, KeyError) as ex:
            logging.error(f'Failed to save close price: {ex}')


@app.on_event('startup')
async def start() -> None:
    await AppCtx.start()
    asyncio.create_task(receive_close_prices())


@app.on_event('shutdown')
async def stop() -> None:
    await AppCtx.stop()


if __name__ == '__main__':
    uvicorn.run(app=app, host=settings.APP_HOST, port=settings.APP_PORT)
