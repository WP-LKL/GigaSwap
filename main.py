from server import app
from func import utils
import sys

baseConfig = {
    "verbose"       : True,
    
    "runserver"     : False,
    "getPrice"      : False,
    "getBalance"    : True,

    "exchange"      : "cdc",
    "c1"            : "cro",
    "c2"            : "usdc",

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

    if args["runserver"]:
        app.app.run()
    