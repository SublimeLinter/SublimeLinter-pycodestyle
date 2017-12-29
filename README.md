SublimeLinter-pycodestyle
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pycodestyle.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pycodestyle)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [pycodestyle](https://github.com/PyCQA/pycodestyle). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `pycodestyle` (1.4.6 or later) is installed on your system. To install `pycodestyle`, do the following:

1. For best performance, install [Python 3](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `pycodestyle` by typing the following in a terminal, replacing '3.x' with the available version of pip:
   ```
   [sudo] pip-3.x install pycodestyle
   ```

In order for `pycodestyle` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
