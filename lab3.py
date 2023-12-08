from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)

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


# Железнодорожный билет
@lab3.route('/lab3/ticket')
def ticket():
    #Переменная "Ошибки"
    errors = {}
    #Перкменная "ФИО"
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    #Переменна "Тип билета"
    type = request.args.get('type')  
    #Переменна "Полка"  
    shelf = request.args.get('shelf') 
    #Переменна "Багаж" 
    bag = request.args.get('bag')
    #Переменная "Возраст"
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    #Переменная "Пункт отправления"
    departure = request.args.get('departure')
    if departure == '':
        errors['departure'] = 'Заполните поле!'
    #Переменная "Пункт прибытия"
    entry = request.args.get('entry')
    if  entry == '':
        errors['entry'] = 'Заполните поле!'
    #Переменная "Дата"
    date = request.args.get('date')
    if  date == '':
        errors['date'] = 'Заполните поле!'
    return render_template('ticket.html', user=user, errors=errors, type=type, shelf=shelf, bag=bag, age=age, departure=departure,entry=entry, date=date)


# Защита 3 лабораторной работы 

from math import factorial
@lab3.route('/lab3/zashita')
def zashita2():
    N = request.args.get('N')
    X = request.args.get('X')

    result2 = 0
    if N and X:
        N = int(N)
        X = float(X)

        result2 = X

        for i in range(N):
            result2 += (((-1**i)*(X**(2*i+1)))/(factorial(2*i+1)))
    else:
        result2 = -1
    print(f"xxxxxx {result2}") 
    return render_template('/zac_3.html', result2 = result2, N=N, X=X)


@lab3.route('/lab3/zashita1')
def zashita():
    ##Второе задание##
    A = request.args.get('A'),
    B = request.args.get('B'),
    C = request.args.get('C'),
    D = request.args.get('D')

    if A == B and A == C and A == D:
        result = 'Все числа равны'
    elif A == B and A == C:
        result = 4
    elif A == B and A == D:
        result = 3
    elif B == C and B == D:
        result = 2
    else:
        result = 1
    return render_template('/zac_3.html', result = result, A=A, B=B, C=C, D=D)