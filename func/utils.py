import asyncio
from sockets import cdcExchange as cdc

def getPrice(**kwargs) -> float:
    """ Get price """
    if kwargs["exchange"] == "cdc":
        return asyncio.run(cdc.getPrice(**kwargs))

def getBalance(**kwargs):
    if kwargs["exchange"] == "cdc":
        return asyncio.run(cdc.getBalance(**kwargs))

def marketOrder(**kwargs):
    if kwargs["exchange"] == "cdc":
        return asyncio.run(cdc.marketOrder(**kwargs))

def closeOrder(**kwargs):
    pass

def closeAll(**kwargs):
    pass

# TODO: Express conditionals (if) as hash-mapped structs