<ins>English</ins> // [Русский](README-ru.md)
<hr>

![GitHub](https://img.shields.io/github/license/f1refa11/shootbox?style=for-the-badge)<br>

![GitHub all releases](https://img.shields.io/github/downloads/f1refa11/shootbox/total?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/f1refa11/shootbox?style=for-the-badge)

![GitHub issues](https://img.shields.io/github/issues/f1refa11/shootbox?color=1fc482&style=for-the-badge)
![GitHub closed issues](https://img.shields.io/github/issues-closed/f1refa11/ShootBox?style=for-the-badge&color=533bb8)


[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=for-the-badge)](https://github.com/astral-sh/ruff)
# ShootBox
ShootBox is a 2D Top-down sandbox game, written in Python using Pygame library which is used to make other multimedia apps. This game is a complete rewrite of ALPHA version, which is now outdated: https://github.com/f1refa11/shootbox-alpha

## Comparison between [ALPHA](https://github.com/f1refa11/shootbox-alpha) version
TODO

# Screenshots
TODO

# Running
## GitHub Releases
We provide prebuilt binaries at Releases page: https://github.com/f1refa11/ShootBox/releases; but if you encountered some problems, you can always use other ways below to launch the game.

## Running from Source
To run the game using the source and existing Python instance, you would need the following **dependencies**:
- Python 3.8+(older versions may work, untested) with **pip installed**
    - Pygame-ce(*recommended*) or Pygame 2.3.0+ - `pip3 install pygame-ce` or `pip3 install pygame`;
    - pypresence 4.3.0+ - `pip3 install pypresence`;
    - orjson 3.9.2+ - `pip3 install orjson`;

Then, just clone the repo, go the downloaded directory, and launch the `main.py` script:
```sh
git clone https://github.com/f1refa11/ShootBox
cd ShootBox
python3 main.py
```

# Building
- Check [here](#running-from-source) if you have the needed dependencies to build the game
- Clone the repo: `git clone https://github.com/f1refa11/ShootBox`
- Move to downloaded folder: `cd ShootBox`
## Using PyInstaller:
`pyinstaller ... main.py` :
- `-F` to make one-file build(UNTESTED);
- `-w` to disable appearing console.

See more options at: https://pyinstaller.org/en/stable/usage.html#options
## Using Nuitka(recommended):
`python -m nuitka ... main.py` :
- `--standalone` if you plan to run your build on systems which don't have Python installed;
- `--onefile` to make one-file build(UNTESTED);
- `--follow-imports`- only if `--standalone` wasn't specified; use to include used modules in your build;
- `--include-data-dir=assets=assets --include-data-files=config.json=config.json` to automatically add necessary game files;
- `--run` to immediately run the game after its build;
- `--disable-console` to disable appearing console;

See more options by running: `python -m nuitka --help`

# Contributing<hr>
*useful info for new contributors to help them get oriented*

## Project Structure
- assets/ - customizable(can be changed even in built game) assets;
    - font.ttf - Fira Sans font(available on Google Font); can be changed to any font(even non-unicode, which may cause problems when rendering unicode text);
    - lang/ - Localizations folder(translations to other languages);
    - textures/ - Game textures(in good resolution);
- widgets/ - UI elements(widgets) modules
- pages/ - Game scenes(main menu, settings, game, etc.);
- utils/ - Useful functions and other utilities separated for better code readability.

