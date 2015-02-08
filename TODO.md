# To-Do List for Bootleg

## What is done

* File architecture
* Config file (Redone!)
* Parsable settings easy modification
* Most functions are done
* Preset file parsing (To re-do - see below)
* Git integration, automatic updates
* Creating of a clone instance if it wasn't (first-time setup)
* Full translatability in any language

## What is left to do

* Main function
* Some functions and the parser for each parameter
* Game loader in python instead of batch
* Much more that I can't remember right now

## To Re-Do List

* Shrink the number of modules
* Shrink parser finder in a single variable used directly (instead of indirectly)
* Move parser installers in a different package (or, at least, improve it)
* Split modules over multiple packages
* Re-Do presets like config
* Reduce cluster in tools/__init__.py
* Get rid of tools/get.py
* Possibly move translate in another package
* Overhaul of a lot of things basically

Most of what I did isn't as good and could be redone in an object-oriented way.
However, the main goal is to get it in a working state for release.
Once that's done, then improving can be considered.
