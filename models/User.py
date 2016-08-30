from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql.expression import false, true

from models.base import BaseModel
from models.mixins import UpdateAtMixin, HasExternalIDMixin

from config import GlobalConfig


config = GlobalConfig()


class User(BaseModel, UpdateAtMixin, HasExternalIDMixin):

    # Login name defined by external service
    username = Column(String(256), nullable=False, unique=True, index=True)

    # Human-readable name for this user
    name = Column(String(256), nullable=False, server_default="")

    # whether the user is a superuser
    is_superuser = Column(Boolean, server_default=false())

    # whether the account is active. Messages sent to the inactive user will be revoked
    active = Column(Boolean, server_default=true())

    # whether the user is online. Message sent to an off-line user will be cached
    online = Column(Boolean, server_default=false())

    # the time of the last login
    last_login_at = Column(DateTime, nullable=True)

    # name of the avatar image, also the relative path against media root
    avatar = Column(String(256), server_default="")

    @property
    def avatar_url(self):
        return config.get_media_url(self.avatar)

    @property
    def avatar_path(self):
        return config.get_full_path(self.avatar)
