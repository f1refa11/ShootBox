![GitHub](https://img.shields.io/github/license/f1refa11/shootbox?style=for-the-badge)<br>

![GitHub all releases](https://img.shields.io/github/downloads/f1refa11/shootbox/total?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/f1refa11/shootbox?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/f1refa11/shootbox?color=%2357F287&style=for-the-badge)</br>

![Discord](https://img.shields.io/discord/973540399706677279?color=%235865F2&label=Discord%20&style=for-the-badge)
![GitHub Sponsors](https://img.shields.io/github/sponsors/f1refa11?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/f1refa11/shootbox?color=%23FEE75C&style=for-the-badge)
# ShootBox
ShootBox is a 2D Top-down sandbox game, written in Python using Pygame library which is used to make other multimedia apps. This is the up-to-date version; to see the ALPHA version go to: https://github.com/f1refa11/shootbox-alpha

## Comparison between [ALPHA](https://github.com/f1refa11/shootbox-alpha) version
TODO

# Screenshots
TODO

# Running
We provide prebuilt binaries at Releases page: https://github.com/f1refa11/ShootBox/releases; but if you encountered some problems, you can always build the game by using instructions below.

# Building & Contributing
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
- `--onefile` to make one-file build;
- `--follow-imports`- only if `--standalone` wasn't specified; use to include used modules in your build;
- `--include-data-dir=assets=assets --include-data-files=config.json=config.json` to automatically add necessary game files;
- `--run` to immediately run the game after its build;
- `--disable-console` to disable appearing console;

See more options by running: `python -m nuitka --help`