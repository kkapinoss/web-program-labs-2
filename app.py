from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)

# Лабораторная работа №2

@app.route('/lab2/example')
def example():
		name = 'Даниил Капинос'
		number = '2'
		groupe = 'ФБИ-12'
		course = '3 курс'
		fruits = [
				{'name':'яблоки','price':'99₽'},
				{'name':'груши','price':'139₽'},
				{'name':'апельсины','price':'79₽'},
				{'name':'мандарины','price':'259₽'},
				{'name':'манго','price':'199₽'}
				]
		books = [
				{'name': 'Волчья стая', 'name_author': 'Василь Быков', 'zanr': 'Повесть', 'kol_stranits': '381'},
				{'name': 'Четыре сезона', 'name_author': 'Стивен Кинг', 'zanr': 'Повесть', 'kol_stranits': '542'},
				{'name': 'КлаТбище домашних животных', 'name_author': 'Стивен Кинг', 'zanr': 'Роман', 'kol_stranits': '476'},
				{'name': 'Великий Гэтсби', 'name_author': 'Фрэнсис Скотт Фицджеральд', 'zanr': 'Роман', 'kol_stranits': '253'},
				{'name': 'Призрак дома на холме', 'name_author': 'Ширли Джексон', 'zanr': 'Роман', 'kol_stranits': '285'},
				{'name': 'Война и мир', 'name_author': 'Лев Толстой', 'zanr': 'Роман', 'kol_stranits': '1225'},
				{'name': 'Мастер и Маргарита', 'name_author': 'Михаил Булгаков', 'zanr': 'Роман', 'kol_stranits': '448'},
				{'name': 'Преступление и наказание', 'name_author': 'Федор Достоевский', 'zanr': 'Роман', 'kol_stranits': '592'},
				{'name': 'Капитанская дочка', 'name_author': 'Александр Пушкин', 'zanr': 'Роман', 'kol_stranits': '320'},
				{'name': 'Мой добрый папа', 'name_author': 'Виктор Голявкин', 'zanr': 'Повесть', 'kol_stranits': '200'}
    ]
		return render_template('example.html', name=name, number=number, groupe=groupe, course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/musics')
def musics():
    return render_template('musics.html')

@app.route('/lab2/zash')
def zash():
	A = 2
	B = 3
	C = 4

	# A = float(input("Введите значение переменной A: "))
	# B = float(input("Введите значение переменной B: "))
	# C = float(input("Введите значение переменной C: "))

	if A < B < C:
			A *= 2
			B *= 2
			C *= 2
			# A = A *= 2
			# B = B *= 2
			# C = C *= 2

	# print("A =", A)
	# print("B =", B)
	# print("C =", C)
	# return render_template('lab2.html', A=A, B=B, C=C)
	return f"A = {A}, B = {B}, C = {C}"

@app.route('/lab2/zash2')
def print_number():
    N = 6
    K = 3
    result = str(N) * K
    return f"result = {result}"

@app.route('/lab2/zash3')
def lala_la():
	# result = 0
	# N = 2
	# K = 4
	# for i in range(N, K+1):
	# 	result += i
	# 	return f"The sum from {N} to {K} is {result}"
	
	N = 2
	K = 4
	result = 0
	for i in range(1, N+1):
		result += i**K
	return f"Сумма {N} и {K} будет равна {result}"