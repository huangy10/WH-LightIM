from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.sql.expression import false, true

from models.base import BaseModel
from models.mixins import UpdateAtMixin, CreatedAtMixin

from utils.sqlalchemy_ext import JSON

from config import GlobalConfig


config = GlobalConfig()


class Message(BaseModel, UpdateAtMixin, CreatedAtMixin):

    #
    message_type = Column(Enum('chat', 'present', 'notification'))

    is_read = Column(Boolean, server_default=false())

    is_sent = Column(Boolean, server_default=false())

    extra_message_body = Column(JSON, nullable=False)