## Bootleg 041 Documentation

Hello and welcome to the Bootleg 041 code. Please note that, while the code currently runs, it cannot currently install anything and is unsupported.

See [CONTRIBUTING.md][0] if you want to contribute to this repository.

Release date: None yet. Aiming towards a 2014 release.

### Running the code yourself

1. You need Python 3.2 or higher
2. Copy or rename `config.py.example` to `config.py`
3. If using the User Interface, that's all you need to do
4. Else, edit `config.py` to fit your settings

### Presets

The User Interface can add, edit or remove any presets. If you wish to do so yourself, you can open a *.bp file with any text editor and change settings. If you forked the repository, the Bootleg Presets files are ignored, should you make any commit.

### Using the User Interface by Insight

You can use the Bootleg Configurator UI to pick your settings without needing to touch the code.

### Choosing your own default settings

You may pick your own settings in the `config.py` file (You need to rename it from `config.py.example` before). Those settings will get overridden by any preset setting you're loading.

### Adding temporary config (for debugging)

You can make a temporary `cfg.py` file, with any setting present in `tools/variables.py` and/or `config.py`. The settings present in `cfg.py` will override any other.

### Adding new translations

Bootleg is designed to be used completely in English. However, there is a built-in translation feature to translate any full or partial line. Due to the extremely large amount of text involved in Bootleg, translating every single line is a long and tedious work. If you are fluent in English as well as another language (preferably native), you can help translating Bootleg. You will need to fork the repository and then clone it. You can then edit the [translations.xml][1] file to add your own language, following the same syntax as what's already in there. Since I natively speak French, I translated a few lines, however I do not have the time to translate every single line, or I would not have time left to do actual code. I will however make sure every English line is present.

[0]: https://github.com/Vgr255/Bootleg/blob/master/CONTRIBUTING.md
[1]: https://github.com/Vgr255/Bootleg/blob/master/translations.xml