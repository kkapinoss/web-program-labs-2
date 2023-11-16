from flask import Blueprint, render_template, request, make_response
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login_4.html")
    
    #Получение введенных значений 
    username = request.form.get('username')
    password = request.form.get('password')

    # Проверка на пустой логин и пароль
    if not username:
        error = 'Не введен логин'
        return render_template('login_4.html', error=error)
    elif not password:
        error = 'Не введен пароль'
        return render_template('login_4.html', error=error)

    #Если данные введены корректно 
    if username == 'alex' and password == '123':
        return render_template('success_4.html', username=username)
    #Если данные введены некорректно 
    else:
        error = 'Неверный логин или пароль'
        return render_template('login_4.html', error=error, username=username, password=password)


#Роут ввода температуры для холодильника
@lab4.route('/lab4/fridge_4',methods = ['GET','POST'])
def fridge():
    return render_template('fridge_4.html')

#Роут вывода холодильника
@lab4.route('/lab4/success_fridge_4',methods = ['GET','POST'])
def fridge1():
    temperature = request.form.get('temperature') 
    temperature = int(temperature)
    if not temperature:
        message = 'Ошибка: не задана температура'
        return render_template('success_fridge_4.html', message=message)

    if temperature < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
        return render_template('success_fridge_4.html', message=message)
    elif temperature > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
        return render_template('success_fridge_4.html', message=message)
    elif -12 <= temperature <= -9:
        snowflakes = 'три синих снежинки'
    elif -8 <= temperature <= -5:
        snowflakes = 'две синих снежинки'
    elif -4 <= temperature <= -1:
        snowflakes = 'одна синяя снежинка'
    else:
        snowflakes = ''
    message = f'Установлена температура: {temperature}°С'
    return render_template('success_fridge_4.html', message=message, snowflakes=snowflakes)


#Роут заказа зерна
@lab4.route('/lab4/corn_4', methods = ['GET','POST'])
def corn():
    return render_template('corn_4.html')


#Роут успешного оформления заказа зерна
@lab4.route('/lab4/success_corn_4',methods = ['GET','POST'])
def corn1():
    corn = request.form.get('corn') 
    weight = request.form.get('weight') 
    weight = int(weight)
    
    if weight > 500:
        error = 'Такого объёма сейчас нет в наличии'
        return render_template('corn_4.html', weight=weight, error=error)
    if weight <=0:
        error = 'Неверное значение веса'
        return render_template('corn_4.html', weight=weight, error=error)
    
    if corn == 'Ячмень':
        corn = 'Ячмень'
        money = 12000 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn_4.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Овёс':
        corn = 'Овёс'
        money = 8500 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn_4.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Пшеница':
        corn = 'Пшеница'
        money = 8700 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn_4.html', weight=weight, money=money, discount=discount,corn=corn)
    
    if corn == 'Рожь':
        corn = 'Рожь'
        money = 14000 * weight
        discount = ''
        if weight >50:
            discount = 'Применена скидка за большой объём'
            money = money * 0.9
        return render_template('success_corn_4.html', weight=weight, money=money, discount=discount,corn=corn)
    return render_template('success_corn_4.html', corn=corn, weight=weight)


@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    mes=''
    resp = make_response(render_template('cookies.html'))
    color = request.form.get('color')
    b_color = request.form.get('background-color')
    f_size = request.form.get('font-size')

    if color and b_color and f_size:
        if color == b_color:
            mes='поменяйте цвета'
            return make_response(render_template('cookies.html', mes=mes))

        resp.set_cookie('color', color)
        resp.set_cookie('background-color', b_color)
        resp.set_cookie('font-size', f"{f_size}px")
    return resp
    
    return 'waiting for parameters'


# @lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
# def cookies():
#     if request.method == 'GET':
#         return render_template('cookies.html')
    
#     color = request.form.get('color')
#     background = request.form.get('background')
#     font_size = request.form.get('font-size')
#     headers = {
#         'Set-Cookie': 'color=' + color + '; path=/',
#         'Location': '/lab4/cookies'
#     }
#     headers = {
#         'Set-Cookie': 'background=' + background + '; path=/',
#         'Location': '/lab4/cookies'
#     }
#     headers = {
#         'Set-Cookie': 'font-size=' + font_size + '; path=/',
#         'Location': '/lab4/cookies'
#     }
#     return '', 303, headers
    