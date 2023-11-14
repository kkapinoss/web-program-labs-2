from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn=psycopg2.connect(host="127.0.0.1", 
                          user="nikoleta_knowledge_base",
                          database="knowledge_base_for_nickoleta", 
                          password="111",
                          port=5432)
    return conn;

def dbClose(cursor,connection):
    cursor.close()
    connection.close()

@lab5.route ("/lab5")
def main():
    visibleUser='anon'
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_kapinos_daniil",
        user="kapinos_daniil_knowledge_base",
        password="4441")

    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()

    # Пишем запрос, который psycog2 должен выполнить
    cur.execute ("SELECT * FROM users;")
    # fetchall получить все строки, которые получились результате
    # выполнения SOL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall ()
    # Закрываем соединение с БД
    cur.close ()
    conn.close ()
    print(result)
    return render_template('lab5.html', username=visibleUser)
    # return "go to console"
    # return render_template("lab5.html", username=visibleUser)

@lab5.route('/lab5/users')
def user():
    conn=psycopg2.connect(host="127.0.0.1", 
                          user="kapinos_daniil_knowledge_base",
                          database="knowledge_base_for_kapinos_daniil", 
                          password="4441",
                          port=5432)
    cur = conn.cursor()
    cur.execute("SELECT * From users;")
    result=cur.fetchall()
    return render_template('users.html', users=result)


# Роут регистрации пользователя
@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors=""

    if request.method=='GET':
        return render_template('register.html', errors=errors)

    username=request.form.get('username')
    password=request.form.get('password')

    if not (username and password):
        errors=[]
        errors='please, fill the fields'
        print(errors)
        return render_template('register.html', errors=errors)

    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT username From users where username='{username}';")

    if cur.fetchone() is not None:
        errors.append('the user already exists')
        dbClose(cur,conn)
        return render_template('register.html', errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")

    conn.commit
    dbClose(cur,conn)

    return redirect ('/lab5/login')