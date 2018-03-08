#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015-2016 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
#
# License: MIT
#

"""This module exports the PYCODESTYLE plugin linter class."""


from SublimeLinter.lint import PythonLinter


class PYCODESTYLE(PythonLinter):
    """Provides an interface to the pep8 python module/script."""

    syntax = 'python'
    cmd = ('pycodestyle', '*', '-')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.6'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>E\d+)|(?P<warning>W\d+)) (?P<message>.+)'
    multiline = True
    defaults = {
        '--select=,': '',
        '--ignore=,': '',
        '--max-line-length=': None
    }
