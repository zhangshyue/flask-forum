import os
import secrets
from PIL import Image
#this is from package Pillow, used for treating images
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db,bcrypt, mail
#directly import from __init__.py
from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
	PostForm, RequestResetForm, ResetPasswordForm)
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message



