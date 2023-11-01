from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

#Роут "Лабораторная работа№3"
@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')
