# ShootBox Core module - Localization
# Manages game localization
# TODO: use gettext
# TODO: make this as a separate deactivatable module with updates
from funcs import openJSON
import gettext
loc = {}
def reload():
    from confmgr import lang
    global loc
    if lang != "en":
        loc = openJSON("assets/lang/%s.json"%lang)
    else:
        loc = {}
reload()