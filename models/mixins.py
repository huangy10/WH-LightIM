import datetime

from sqlalchemy import Column, DateTime, BigInteger


class CreatedAtMixin(object):

    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False, index=True)


class UpdateAtMixin(object):

    update_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False,
                       index=True, onupdate=datetime.datetime.utcnow)


class HasExternalIDMixin(object):

    external_id = Column(BigInteger, nullable=True, index=True, unique=True)
