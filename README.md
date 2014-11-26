## Bootleg 041 Documentation

Hello and welcome to the Bootleg 041 code. Please note that, while the code currently runs, it cannot currently install anything and is unsupported.

See [CONTRIBUTING.md][0] if you want to contribute to this repository.

Release date: None. This being a one-man job, it takes a long time to do.

### Running the code yourself

You need python 3.2 or higher. Bootleg will copy over the example config file if it doesn't exist. You can do so yourself and edit the settings to your liking. You can use Insight's User Interface to configure your settings, but Bootleg can run perfectly fine by itself.

### Presets

The User Interface can add, edit or remove any presets. If you wish to do so yourself, you can open a *.bp file with any text editor and change settings. If you forked the repository, the Bootleg Presets files are ignored, should you make any commit.

### Using the User Interface by Insight

You can use the Bootleg Configurator UI to pick your settings without needing to touch the code.

### Choosing your own default settings

You may pick your own settings in the `config.py` file (You need to rename it from `config.py.example` before). Those settings will get overridden by any preset setting you're loading.

### Adding temporary config (for debugging)

You can make a temporary `cfg.py` file, with any setting present in `tools/variables.py` and/or `config.py`. The settings present in `cfg.py` will override any other.

### Automatic updating

If Auto-Update is enabled in the config, Bootleg will attempt, everytime it's ran, to check for updates and prompt the user to download it. On every run, it also checks if it's a clone of a repository or a fork. This is only useful the first time it's launched, as if it's not a clone, it will clone the repository in a temporary folder, copy over the .git folder and all files, overwriting everything already present in the folder by those files. This allows to keep one download, that will probably become obsolete soon enough, but still be able to give updates to everyone.

### Reading documentation

The documentation can be accessed directly from within the documentation folder, but it can also be viewed with the 'read' command, directly from within Bootleg. See 'help read' to get more information on that command.

### Adding new translations

Bootleg's programming is done with translating in mind. As such, no line is hardcoded in the code, and everything is in the [translate.py][1] file.

If you are fluent in English as well as another language (preferably native), you can help translating Bootleg.

You need to edit the [translate.py][1] file to add your own language, following the same syntax as what's already in there. Add a constant at the top (such as German: "German") and use that constant at all times.

Since I natively speak French, I translated a few lines, however I do not have the time to translate every single line, or I would not have time left to do actual code. I will however make sure every English line is present, for future people to translate accordingly.

[0]: https://github.com/Vgr255/Bootleg/blob/master/CONTRIBUTING.md
[1]: https://github.com/Vgr255/Bootleg/blob/master/tools/translate.py
