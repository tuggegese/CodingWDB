# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms import StringField
from wtforms.validators import DataRequired

# login and registration

class StrategyForm(FlaskForm):
    strategy_name = StringField('StrategyName',id='strategy_create',validators=[DataRequired()])
    #code_mirror = CodeMirrorField(language='python', config={'lineNumbers': 'true'},validators=[DataRequired()])
    #source_code = CodeMirrorField(language='python',config={'lineNumbers' : 'true'})    


   

