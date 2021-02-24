import cryptocom.exchange as cdc
from utils import db
from conf import exchangeCredentials

EXCHANGE = cdc.Exchange()
ACCOUNT = cdc.Account(**exchangeCredentials["CDC"])

def createPair(c1, c2):
    return cdc.structs.Pair(name=f"{c1}_{c2}", price_precision=16, quantity_precision=16)

async def getPrice(**kwargs) -> float:
    """ Get price """
    price = await EXCHANGE.get_price(createPair(kwargs["c1"], kwargs["c2"]))
    return price

async def marketOrder(**kwargs):
    if kwargs["marketOrder"] == "buy":
        order_id = await ACCOUNT.buy_market(createPair(kwargs["c1"], kwargs["c2"]), spend=kwargs["qty"])
        db.insert_db(table="order", rows=[(order_id, "cdc", "buy", kwargs["c1"], kwargs["c2"], kwargs["qty"])])
        return order_id
    elif kwargs["marketOrder"] == "sell":
        order_id = await ACCOUNT.sell_market(createPair(kwargs["c1"], kwargs["c2"]), quantity=kwargs["qty"])
        db.insert_db(table="order", rows=[(order_id, "cdc", "sell", kwargs["c1"], kwargs["c2"], kwargs["qty"])])
        return order_id

async def getBalance(**kwargs):
    return await ACCOUNT.get_balance()