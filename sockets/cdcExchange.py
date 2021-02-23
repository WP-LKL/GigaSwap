import cryptocom.exchange as cro

async def getPrice(**kwargs) -> float:
    """ Get price """
    exchange = cro.Exchange()
    price = await exchange.get_price(cro.pairs.CRO_USDT)
    return f'{price}'