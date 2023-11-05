from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

#Роут "Лабораторная работа№3"
@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


# Формы
@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


#Заказ напитка
@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
		price = 0
		drink = request.args.get('drink')
		if drink == 'cofee':
				price = 120
		elif drink == 'black-tea':
				price = 80
		else:
				price = 70
                                
		# Добавка молока и сахара
		if request.args.get('milk') == 'on':
				price += 30
		if request.args.get('sugar') == 'on':
				price += 10

		return render_template('pay.html', price = price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')