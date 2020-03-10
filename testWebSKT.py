# -*- coding: utf-8 -*-
import asyncio #异步
import base64
import gzip
import json
import logging # 日志

import chardet
from datetime import datetime #时间
from aiowebsocket.converses import AioWebSocket #aiowebsocket需要安装，异步websocket

async def startup(uri): # anync 异步语法
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        # 客户端给服务端发送消息
        #await converse.send('{"action":"subscribe","args":["QuoteBin5m:14"]}') # await 也是异步语法
        await converse.send('{"event": "req", "params": {"channel": "review"}')
        #await converse.send('{"event":"sub","params":{"channel":"market_vdsusdt_ticker","cb_id":"vdsusdt"}}')
        await converse.send('{"event": "req", "params": {"channel": "market_btcusdt_trade_ticker", "cb_id": "btcusdt", "top": 100}}')
        await converse.send('{"event": "sub", "params": {"channel": "market_btcusdt_trade_ticker", "cb_id": "btcusdt", "top": 100}}')
        while True:
            mes = await converse.receive()
            mesUnPack = gzip.decompress(mes)
            mesJSON = json.loads(str(mesUnPack)[2:-1])
            #print(mesJSON)
            print('{time}-Client receive: {rec}'
             .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mesUnPack))
            if('ping' in mesJSON):
                await converse.send('{"pong":'+str(mesJSON['ping'])+'}')
            else:
                if('tick' in mesJSON):
                    tickJSON = mesJSON['tick']
                    if(tickJSON is not None):
                        if('data' in tickJSON):
                            dataJSONArray = tickJSON['data']
                            for c in range(0, len(dataJSONArray)):
                                price = dataJSONArray[c]['price']
                                ds = dataJSONArray[c]['ds']
                                print("price:"+str(price)+";data:"+ds)

if __name__ == '__main__':

    remote = 'wss://wspool.mpuuss.top/kline-api/ws'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
