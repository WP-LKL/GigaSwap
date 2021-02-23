import asyncio
import cryptocom.exchange as cro
from sockets import cdcExchange as cdc

def getPrice(**kwargs) -> float:
    """ Get price """
    if kwargs["exchange"] == "cdc":
        return asyncio.run(cdc.getPrice(**kwargs))
