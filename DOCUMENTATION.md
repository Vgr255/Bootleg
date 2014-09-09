## Bootleg 041 Documentation

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