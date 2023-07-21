[English][[Russian](README-ru.md)]

![GitHub](https://img.shields.io/github/license/f1refa11/shootbox?style=for-the-badge)<br>

![GitHub all releases](https://img.shields.io/github/downloads/f1refa11/shootbox/total?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/f1refa11/shootbox?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/f1refa11/shootbox?color=%2357F287&style=for-the-badge)</br>

![Discord](https://img.shields.io/discord/973540399706677279?color=%235865F2&label=Discord%20&style=for-the-badge)
![GitHub Sponsors](https://img.shields.io/github/sponsors/f1refa11?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/f1refa11/shootbox?color=%23FEE75C&style=for-the-badge)
# ShootBox
ShootBox is a 2D Top-down sandbox game, written in Python using Pygame library which is used to make other multimedia apps. This game is a complete rewrite of ALPHA version, which is now outdated: https://github.com/f1refa11/shootbox-alpha

## Comparison between [ALPHA](https://github.com/f1refa11/shootbox-alpha) version
TODO

# Screenshots
TODO

# Running
We provide prebuilt binaries at Releases page: https://github.com/f1refa11/ShootBox/releases; but if you encountered some problems, you can always build the game by yourself by using instructions below.

# Building
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

