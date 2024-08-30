"""conf.py"""
from configparser import ConfigParser, NoOptionError

from rpyutils import Level, printd


class ConfigHeader(object):
    def __init__(self, fp):
        self.fp = fp
        self.first_line = True
        self.dummy_section = "[fakeap]\n"

    def readline(self):
        if self.first_line:
            self.first_line = False
            return self.dummy_section
        else:
            return self.fp.readline()


class Conf(ConfigParser):
    def __init__(self, path):
        ConfigParser.__init__(
            self
        )  # ConfigParser is an old-style class... Can't user 'super'
        self.path = path
        with open(path, encoding="latin1") as file_handle:
            self.read_file(ConfigHeader(file_handle))

    def get(self, key, default=None):
        """get"""
        value = None
        try:
            value = ConfigParser.get(self, "fakeap", key)
        except NoOptionError as e:
            value = default
            printd(
                f"Option '{e.option}' not specified in config file. Using default.",
                Level.WARNING,
            )

        printd(f"{key} -> {value}", Level.INFO)

        return value
