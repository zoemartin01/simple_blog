from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base


class PasswordResetToken(Base):
    __tablename__ = 'pw_reset_tokens'
    id = Column(Integer, primary_key=True)
    token = Column(Text, unique=True, nullable=False)

    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref='pw_reset_token')