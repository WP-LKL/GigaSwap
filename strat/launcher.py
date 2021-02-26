from multiprocessing import Process
from strat import canyon

def validStrategy(strat, **kwargs):
    if strat == "canyon":
        if ['c1', 'c2'] in kwargs:
            return True
        else:
            print(f"Missing args in {kwargs}")
            return False
    else:
        print(f"invalid strat {strat}")
        return False

def launchStrategy(**kwargs):
    if kwargs["strat"] == "canyon":
        pass
        #p = Process(target=canyon.canyonStrat, args=(**kwargs))
    return None #p

if __name__ == '__main__':
    None