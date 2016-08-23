from sqlalchemy import Column, BigInteger
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from models.mixins import CreatedAtMixin


@as_declarative()
class BaseModel(CreatedAtMixin):

    """
     Root Object of all models, provides id field and created_at timestamp.
    """

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @declared_attr
    def __table_args__(self):
        return {'extend_existing': True}

    def __repr__(self):
        return "<{} (id: {})>".format(self.__module__ + "." + self.__class__.__name__, self.id)


