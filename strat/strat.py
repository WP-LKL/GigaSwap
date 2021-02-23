def validStrategy(strat, **kwargs):
    if strat == "canyon":
        if ['p1', 'p2'] in kwargs:
            return True
        else:
            print(f"Missing args in {kwargs}")
            return False
    else:
        print(f"invalid strat {strat}")
        return False


def initStrategy():
    return None

if __name__ == '__main__':
    None