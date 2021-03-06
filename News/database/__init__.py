# coding: utf-8

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from News.settings import POSTGRES

Base = automap_base()
engine = create_engine(POSTGRES)
Base.prepare(engine, reflect=True)
Monitor = Base.classes.monitor
session = Session(engine)

