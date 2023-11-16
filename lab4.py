from flask import Blueprint, render_template, request, session
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