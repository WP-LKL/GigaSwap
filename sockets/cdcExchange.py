import cryptocom.exchange as cdc

from conf import exchangeCredentials

async def getPrice(**kwargs) -> float:
    """ Get price """
    exchange = cdc.Exchange()
    price = await exchange.get_price(cdc.pairs.CRO_USDT)
    return f'{price}'

async def marketOrder(**kwargs):
    exchange = cdc.Exchange()
    price = await exchange.buy_market(cdc.pairs.CRO_USDT)
    return f'{price}'

async def getBalance(**kwargs):
    account = cdc.Account(**exchangeCredentials["CDC"])
    data = await account.get_balance()
    print(data)
    return (f'Account balance {data}')