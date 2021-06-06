# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:05:57 2021

@author: Administrator
"""

from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import SearchForm

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('search.html', title='Sign In', form=form)

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)