# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:22:52 2020

@author: braud
"""

import sqlalchemy
import uuid

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.interfaces import PoolListener

class ForeignKeysListener(PoolListener):
    def connect(self, dbapi_con, con_record):
        db_cursor = dbapi_con.execute('pragma foreign_keys=ON')
  

#Nom des tables
        
ACTIVITE        = 'activite'
EQUIPEMENT      = 'equipement'
INSTALLATION    = 'installation'
PRATIQUE        = 'pratique'
CONTIENT        = 'contient'

#Nom de la BD

DBNAME          = 'ProjetPython'

DB_ENGINE = 'sqlite:///{}'

engine_url = DB_ENGINE.format(DBNAME)

db_engine = create_engine(engine_url, listeners=[ForeignKeysListener()])


metadata = MetaData()

activite        =Table(ACTIVITE, metadata,
                   Column('ActCode', String, primary_key=True),
                   Column('ActLib', String, nullable=False),
                   )
equipement      =Table(EQUIPEMENT, metadata,
                   Column('EquipementID', String, primary_key=True),
                   Column('EquNom', String, nullable=False)
                   )
installation    =Table(INSTALLATION, metadata,
                       Column('InsNumeroInstall', String, primary_key=True),
                       Column('InsNom', String, nullable=False),
                       Column('InsAdresse', String, nullable=True),
                       Column('InsLatitude', String, nullable=True),
                       Column('InsLongitude', String, nullable=True)
                       )

pratique        =Table(PRATIQUE, metadata,
                       Column('ActCode', String, ForeignKey(ACTIVITE+".ActCode"), nullable=False),
                       Column('EquipementID', String, ForeignKey(EQUIPEMENT+".EquipementID"), nullable=False),
                       Column('ActNivLib', String, nullable=False)
                       )

contient        =Table(CONTIENT, metadata,
                       Column('EquipementID', String, ForeignKey(EQUIPEMENT+".idEquipement"), nullable=False),
                       Column('InsNumeroInstall', String, ForeignKey(INSTALLATION+".InsNumeroInstall"), nullable=False)
                       )


