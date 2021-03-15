from datetime import datetime

from sqlalchemy import CheckConstraint, func

from audio import db
from audio.models import Base


class Song(Base):
    __tablename__ = 'songs'

    name = db.Column(db.String(100), index=True, nullable=False, unique=True)
    duration = db.Column(db.INTEGER, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (CheckConstraint(duration >= 0, name='duration_non_negative'),
                      CheckConstraint(func.length(name) <= 100, name='not_more_than_100'),
                      CheckConstraint(upload_time >= func.current_date(), name='in_the_present')
                      )


class Podcast(Base):
    __tablename__ = 'podcasts'

    name = db.Column(db.String(100), index=True, nullable=False, unique=True)
    duration = db.Column(db.INTEGER, nullable=False)
    host = db.Column(db.String(100), index=True, nullable=False)
    participants = db.Column(db.JSON)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (CheckConstraint(duration >= 0, name='duration_non_negative'),
                      CheckConstraint(func.length(name) <= 100, name='name_not_more_than_100'),
                      CheckConstraint(func.length(host) <= 100, name='host_not_more_than_100'),
                      CheckConstraint(upload_time >= func.current_date(), name='in_the_present')
                      )


class Audiobook(Base):
    __tablename__ = 'audiobooks'

    title = db.Column(db.String(100), index=True, nullable=False)
    author = db.Column(db.String(100), index=True, nullable=False)
    narrator = db.Column(db.String(100), index=True, nullable=False)
    duration = db.Column(db.INTEGER, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (CheckConstraint(duration >= 0, name='duration_non_negative'),
                      CheckConstraint(func.length(title) <= 100, name='title_not_more_than_100'),
                      CheckConstraint(func.length(author) <= 100, name='author_not_more_than_100'),
                      CheckConstraint(func.length(narrator) <= 100, name='narrator_not_more_than_100'),
                      CheckConstraint(upload_time >= func.current_date(), name='in_the_present')
                      )
