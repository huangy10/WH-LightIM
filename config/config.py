import yaml
import os


class Singleton(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__()
        return cls._instance


class GlobalConfig(object):

    __metaclass__ = Singleton

    def __init__(self, file_path=None):
        if file_path is None:
            file_path = os.path.join(__file__.dir, "config.yaml")
        self._data = yaml.load(open(file_path))

        self._configure_check()

    def _configure_check(self):
        pass

    # database configurations

    @property
    def database_url(self):
        return self._data["database"]["URL"]

    @property
    def database_port(self):
        return self._data["database"]["PORT"]

    @property
    def database_name(self):
        return self._data["database"]["NAME"]

    @property
    def database_passwd(self):
        return self._data["database"]["PASSWORD"]
