# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.strategies import blueprint
from apps.strategies.forms import StrategyForm

#@blueprint.route('/')
#def route_default():
#    return redirect(url_for('strategies_blueprint.login'))

# Login & Registration

#@blueprint.route('/strategies', methods=['GET', 'POST'])
#def strategies():
#    # check if button is pressed
#    if request.form.get("submit_a"):
#        return redirect(url_for('strategies_blueprint.createstrategy'))
#    
#    # redirect
#    
#    #return render_template('home/createstrategy.html')

@blueprint.route('/createstrategy', methods=['GET', 'POST'])
def createstrategy():
    # create form
    strat_form = StrategyForm(request.form)
    
   # print(request.form['strategy_name'])
    if 'save' in request.form:
        # if request form is saved add strategy to database
        
        print(request.form)
    if 'discard' in request.form:
        return redirect(url_for('strategies_blueprint.strategies'))
    
    #return render_template('home/strategies.html')
    return render_template('home/createstrategy.html',form=strat_form)
    #return redirect(url_for('strategies_blueprint.createstrategy'))

@blueprint.route('/strategies', methods=['GET', 'POST'])
def strategies():
       
    return render_template('home/strategies.html')



    



# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
