# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:32:41 2020

@author: kriti
"""

from flask_wtf import Form
from wtforms import StringField,PasswordField,TextAreaField
from wtforms.validators import (DataRequired,Regexp, ValidationError,Email,Length,EqualTo)
from models import User

def name_exists(form,field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('This username  already exists.')
 
def email_exists(form,field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('This email already exists.')
  

    
class RegisterForm(Form):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Regexp(
                r'^[A-za-z0-9_]+$',
                   message=("Username should be one word,"
                   " letters, numbers and underscores only.")
                   ),
            name_exists 
            ])
    
    email = StringField(
        'Email',
        validators=[DataRequired(),
                    Email(),
                    email_exists
                    ])
    password = PasswordField(
        'Password',
        validators =[
            DataRequired(),
            Length(min=3),
            EqualTo('password2',message='Passwords must match')
            ]
        )
    password2 = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired()]
    
        )
    
class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(),Email() ])
    password = PasswordField('Password',validators =[DataRequired()])
    
class PostForm(Form):
    content = TextAreaField("Whats up?",validators=[DataRequired()])
    