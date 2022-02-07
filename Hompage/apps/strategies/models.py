# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps import db

class Strategies(db.Model):
    
    __tablename__ = 'Strategies'
    
    id = db.Column(db.Integer, primary_key=True)
    