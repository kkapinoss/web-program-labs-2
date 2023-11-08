from flask import Blueprint, render_template, request, session
import psycopg2

lab5 = Blueprint('lab5', __name__)

@lab5.route ("/lab5")
def main():
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
    return "go to console"