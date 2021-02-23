# ADD MORE CUSTOM CONFIGS HERE
configs = {
    "cautios" : {
        "desc" : "cautios: Fewer, but safer trades.",
        "thrAlpha" : 0.01,  # Tolerance
    },

    "balanced" : {
        "desc" : "balanced: .",
        "thrAlpha" : 0.005,  # Tolerance
    },

    "risky" : {
        "desc" : "risky: .",
        "thrAlpha" : 0.001,  # Tolerance
    }

    # "myConf" :{}

}

def selectConfig(mode, lastConf=None, curConfig=None):
    return configs[mode]
