# ShootBox - Core Module - Config Manager
# Validates config.json file, fixes it's errors and defines variables to config's ones
# Notice: ShootBox Core modules 
from funcs import openJSON
validConfig = {
    "graphics": {
        "antialias": { "font": True, "ui": True, "game": True },
        "showGrass": False,
        "smartRender": True,
        "renderDistance": 5,
        "blockSelection": True,
        "animations": { "ui": True, "game": True },
        "fullscreen": False,
        "gpu": False,
        "fps": 60
    },
    "rpc": False,
    "sound": { "sfx": 100, "music": 100 },
    "lang": "en"
}
# opening config.json, or creating it if FileNotFoundError
try:
    config = openJSON("config.json")
except FileNotFoundError:
    from funcs import saveJSON
    saveJSON(validConfig, "config.json")
    config = validConfig

# validating function
keys = []
def validate(dictionary: dict):
    global keys
    for key in list(dictionary.keys()):
        if type(dictionary[key]) == dict:
            keys.append(key)
            validate(dictionary[key])
        else:
            tmpData = validConfig
            for k in keys:
                tmpData = tmpData[k]
            if type(dictionary[key]) != type(tmpData[key]):
                pass
    keys.pop() if keys else False

validate(config)

#defining config values as Python variables for better readability
sfxVolume = config["sound"]["sfx"]
musicVolume = config["sound"]["music"]

enableRPC = config["rpc"]
lang = config["lang"]

fontAntialias = config["graphics"]["antialias"]["font"]
uiAntialias = config["graphics"]["antialias"]["ui"]
gameAntialias = config["graphics"]["antialias"]["game"]

showGrass = config["graphics"]["showGrass"]
smartRender = config["graphics"]["smartRender"]
renderDistance = config["graphics"]["renderDistance"]
blockSelection = config["graphics"]["blockSelection"]

uiAnimations = config["graphics"]["animations"]["ui"]
gameAnimations = config["graphics"]["animations"]["game"]

isFullscreen = config["graphics"]["fullscreen"]
GPUAcceleration = config["graphics"]["gpu"]

fpsLimit = config["graphics"]["fps"]