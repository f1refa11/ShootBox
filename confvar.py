from funcs import openJSON
config = openJSON("config.json")

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