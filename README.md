SublimeLinter-pycodestyle
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pycodestyle.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pycodestyle)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [pycodestyle](https://github.com/PyCQA/pycodestyle). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `pycodestyle` is installed on your system. To install `pycodestyle`, do the following:

1. For best performance, install [Python 3](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `pycodestyle` by typing the following in a terminal, replacing '3.x' with the available version of pip:
   ```
   [sudo] pip-3.x install pycodestyle
   ```

**Note:** This plugin requires `pycodestyle` 1.4.6 or later.

### Linter configuration
In order for `pycodestyle` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `pycodestyle` is installed and configured, you can proceed to install the SublimeLinter-pycodestyle plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `pycodestyle`. Among the entries you should see `SublimeLinter-pycodestyle`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-pycodestyle provides its own settings. 
