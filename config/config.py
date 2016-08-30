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
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
        self.PROJ_DIR = base_path
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

    # media

    @property
    def media_root(self):
        return self._data["media"]["MEDIA_ROOT"]

    @property
    def media_url_prefix(self):
        return self._data["media"]["MEDIA_URL_PREFIX"]

    def get_full_path(self, path_name):
        return os.path.join(self.PROJ_DIR, path_name)

    def get_media_abs_path(self, media_name):
        return os.path.join(self.PROJ_DIR, self.media_root, media_name)

    def get_media_url(self, media_name):
        return os.path.join(self.media_url_prefix, media_name)
