from SublimeLinter.lint import PythonLinter


class PYCODESTYLE(PythonLinter):
    cmd = ('pycodestyle', '${args}', '-')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>E\d+)|(?P<warning>W\d+)) (?P<message>.+)'
    multiline = True
    defaults = {
        'selector': 'source.python'
    }
