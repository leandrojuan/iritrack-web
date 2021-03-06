#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, Sequence, String
from server import Base

class Driver(Base):
    __tablename__ = 'drivers'
    gid = Column(Integer, Sequence('id_seq'), primary_key=True, autoincrement=True)
    id = Column(Integer)
    name = Column(String(50))
    country = Column(String(50))
    driver_id = Column(String(50))
    stage_id = Column(Integer)
    def __repr__(self):
        return "<Driver: '%s' (name:'%s', driver_id:'%s')>" % (self.id, self.name, self.driver_id)
