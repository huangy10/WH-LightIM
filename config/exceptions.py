
class ImproperConfiguredException(Exception):

    def __init__(self, key_path):
        self.key_path = key_path
        super(ImproperConfiguredException, self).__init__()

    def __repr__(self):
        return "<ImproperConfiguredException: %s>" % self.key_path

    def __str__(self):
        return "ImproperConfiguredException: %s" % self.key_path
