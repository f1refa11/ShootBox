[[English](README.md)][Russian]

![GitHub](https://img.shields.io/github/license/f1refa11/shootbox?style=for-the-badge)<br>

![GitHub all releases](https://img.shields.io/github/downloads/f1refa11/shootbox/total?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/f1refa11/shootbox?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/f1refa11/shootbox?color=%2357F287&style=for-the-badge)</br>

![Discord](https://img.shields.io/discord/973540399706677279?color=%235865F2&label=Discord%20&style=for-the-badge)
![GitHub Sponsors](https://img.shields.io/github/sponsors/f1refa11?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/f1refa11/shootbox?color=%23FEE75C&style=for-the-badge)
# ShootBox
ShootBox это 2D Песочница с видом сверху, написанная на Python при помощи библиотеки Pygame, которая используется для создания прочих мультимедиа приложений. Данная игра является полной переписью кода АЛЬФА версии, которая теперь является устаревшей: https://github.com/f1refa11/shootbox-alpha

## Разница между [ALPHA](https://github.com/f1refa11/shootbox-alpha) версией
TODO

# Скриншоты
TODO

# Запуск
## Релизы GitHub
Мы всегда предоставляем собранные исполняемые файлы на странице Релизов: https://github.com/f1refa11/ShootBox/releases; но если вы столкнулись с проблемами при запуске, вы всегда можете воспользоваться другими способами, расположенными ниже.

## Запуск из исходного кода
Чтобы запустить игру из исходного кода, используя установленный Python, вам понадобятся следующие зависимости:
- Python 3.8+(версии постарше могут заработать, но не факт) с **установленным pip**
    - Pygame-ce(*рекомендуется*) или Pygame 2.3.0+ - `pip3 install pygame-ce` or `pip3 install pygame`;
    - pypresence 4.3.0+ - `pip3 install pypresence`;
    - orjson 3.9.2+ - `pip3 install orjson`;

Затем, просто склонируйте репозиторий на ваш компьютер, перейдите в скачанную директорию, и запустите скрипт `main.py`:
```sh
git clone https://github.com/f1refa11/ShootBox
cd ShootBox
python3 main.py
```

# Сборка
- Склонируйте репозиторий: `git clone https://github.com/f1refa11/ShootBox`
- Перейдите в скачанную папку: `cd ShootBox`
## Используя PyInstaller:
`pyinstaller ... main.py` :
- `-F` чтобы собрать в один файл(НЕ ПРОТЕСТИРОВАНО);
- `-w` чтобы отключить появляющуюся консоль.

Посмотрите больше опций здесь: https://pyinstaller.org/en/stable/usage.html#options
## Используя Nuitka(рекомендуется):
`python -m nuitka ... main.py` :
- `--standalone` если вы планируете запускать вашу сборку на системах без установленного Python;
- `--onefile` чтобы собрать в один файл(НЕ ПРОТЕСТИРОВАНО);
- `--follow-imports`- только если `--standalone` не был указан; используйте чтобы включить используемые модули в вашей сборке;
- `--include-data-dir=assets=assets --include-data-files=config.json=config.json` чтобы автоматически добавить необходимые файлы игры;
- `--run` чтобы сразу запустить игру после её сборки;
- `--disable-console` чтобы отключить появляющуюся консоль.

Посмотрите больше опции, запустив: `python -m nuitka --help`

# Вклад в проект<br>
*полезная информация для новых вкладчиков чтобы помочь им сориентироваться*

## Project Structure
- assets/ - кастомизируемые(can be changed even in built game) наборы ресурсов;
    - font.ttf - Шрифт Fira Sans(доступен на Google Font); может быть заменён на любой шрифт(даже без поддержки Unicode, что может вызвать проблемы с отрисовкой текста Unicode);
    - lang/ - Папка с локализациями(переводами на другие языки);
    - textures/ - Игровые текстуры(в хорошем разрешении)
- widgets/ - Модули-элементы(виджеты) интерфейса
- pages/ - Игровые сцены(главное меню, настроки, игра и т.д.);
- utils/ - Полезные функции и другие утилиты, разделённые для лучшей читаемости кода.