# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:03:17 2022

@author: vicgu
"""

import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

# Création de la base de données


def create_base():
    base = declarative_base()

    class Videos_Insight(base):

        __tablename__ = "Videos_Insight"
        create_at = sqla.Column(sqla.DateTime)
        id = sqla.Column(sqla.Integer, primary_key=True)
        video_id = sqla.Column(sqla.Integer, sqla.ForeignKey("Videos.id",
                                                             ondelete='CASCADE'))
        likes = sqla.Column(sqla.Integer)
        views = sqla.Column(sqla.Integer)
        video = relationship("Video", backref=backref(
            "Videos_Insight", passive_deletes=True))

    class Videos(base):

        __tablename__ = "Videos"
        create_at = sqla.Column(sqla.DateTime)
        id = sqla.Column(sqla.Integer, primary_key=True, )
        title = sqla.Column(sqla.String)
        page_id = sqla.Column(sqla.Integer, sqla.ForeignKey("Pages.id",
                                                            ondelete='CASCADE'))
        insight = relationship("Pages", backref=backref(
            "Videos", passive_deletes=True))

    class Pages(base):

        __tablename__ = "Pages"
        id = sqla.Column(sqla.Integer, primary_key=True)
        create_at = sqla.Column(sqla.DateTime)
        name = sqla.Column(sqla.String)
        page = relationship("Videos")

    engine = sqla.create_engine("sqlite:///Brut.db", echo=True)
    base.metadata.create_all(engine)
