userConfigs = {
    "cautios" :         {
        "desc" : "cautios: Fewer, but safer trades.",
        "thrAlpha"  : 0.01,
    },

    "balanced" :        {
        "desc"      : "balanced: .",
        "thrAlpha"  : 0.005,
    },

    "risky" :           {
        "desc"      : "risky: .",
        "thrAlpha"  : 0.001,
    }
    # ADD MORE CUSTOM CONFIGS HERE
    # "myConf" :{}

}

def selectConfig(mode, lastConf=None, curConfig=None):
    return userConfigs[mode]

exchangeCredentials = {
    "CDC" :         {
        "api_key"       : "",
        "api_secret"    : "",
    },  
}

def selectCredentials(exchange : str) -> dict:
    return exchangeCredentials[exchange]