from server import app
from func import utils
import sys

baseConfig = {
    "verbose"       : True,
    
    "runserver"     : False,
    "getPrice"      : True,
    "getBalance"    : False,
    "marketOrder"   : False,  # sell, buy

    "exchange"      : "cdc",
    "c1"            : "CRO",
    "c2"            : "USDC",
    "currencies"    : [("CRO", "USDC")],
    "qty"           : 2.0,

}

if __name__ == "__main__":
    args = dict([arg.split('=', maxsplit=1) for arg in sys.argv[1:]])
    args = {**baseConfig, **args}

    if args["getPrice"]:
        if args["verbose"] : print(f"Getting price of {args['c1']} in {args['c2']} from {args['exchange']}")
        print(utils.getPrice(**args))
    
    if args["getBalance"]:
        if args["verbose"] : print(f"Getting balance from {args['exchange']}")
        print(utils.getBalance(**args))
    
    if args["marketOrder"]:
        if args["verbose"] : print(f"Getting balance from {args['exchange']}")
        print(utils.marketOrder(**args))

    if args["runserver"]:
        app.app.run()
    