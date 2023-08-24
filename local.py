# ShootBox Core module - Localization
# Manages game localization
from funcs import openJSON
loc = {}
def reload():
    from confmgr import lang
    global loc
    if lang != "en":
        loc = openJSON("assets/lang/%s.json"%lang)
    else:
        loc = {}
reload()