from flask import Blueprint, render_template

main=Blueprint('main',__name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/view')
def view():
    return render_template('view.html')