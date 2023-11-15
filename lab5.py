# from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn=psycopg2.connect(host="127.0.0.1", 
                          database="knowledge_base_for_kapinos_daniil", 
                          user="kapinos_daniil_knowledge_base",
                          password="4441")
    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route ("/lab5")
def main():
    visibleUser="Anon"
    conn = dbConnect()
    cur = conn.cursor()

    # Пишем запрос, который psycog2 должен выполнить
    cur.execute ("SELECT * FROM users;")
    
    # fetchall получить все строки, которые получились результате
    # выполнения SOL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()
    # Закрываем соединение с БД
    print(result)
    
    dbClose(cur, conn)
    return render_template('lab5.html', username=visibleUser)
    # return "go to console"


@lab5.route('/lab5/users')
def user():
    conn = dbConnect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users;")
    result=cur.fetchall()
    
    dbClose(cur, conn)

    return render_template('users.html', users=result)


# Роут регистрации пользователя
@lab5.route('/lab5/register', methods=['GET','POST'])
def registerPage():
    errors=[]

    # Если это метод GET, то верни шаблон и заверши выполнение
    if request.method=='GET':
        return render_template('register.html',errors=errors)

    # Если мы попали сюда, значит это метод POST, так как GET мы уже обработали и сделали return.
    # После return функция немедленно завершается
    username=request.form.get('username')
    password=request.form.get('password')

    # Проверяем username и password на пустоту
    # Если любой из них пустой, то добавляем ошибку и рендерим шаблон
    if username =='' or password == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('register.html',errors=errors)

    # Если мы попали сюда, значит username и password заполнены
    # Подключаемся к БД
    conn = dbConnect()
    cur = conn.cursor()

    # Проверяем наличие клиента в базе. У нас не может быть два пользователя с одинаковыми логинами
    # WARNING: мы используем f-строки, что не рекомендуется делать 
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    # fetchone, в отличие от fetchall, получает только одну строку
    # мы задали свойство UNIQUE для пользователя, значитбольше одной строки мы не можем получить 
    # Только один пользователь с таким именем может быть в БД
    if cur.fetchone() is not None:
        errors='Пользователь с данным именем уже существует'

        dbClose(cur,conn)
        return render_template('register.html',errors=errors)

    # Если мы попали сюда, то значит в cur.fetchone нет ни одной строки
    # Значит пользователя с таким же логином не существует
    cur.execute(f"INSERT INTO users (username,password) VALUES ('{username}','{password}');")

    # Делаем commit - фиксируем изменения
    conn.commit()
    dbClose(cur,conn)

    return redirect('/lab5/login')