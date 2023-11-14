from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
	return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
	return """
<!doctype html>
<html>
	<head>
		<title>НГТУ, ФБ, Лабораторные работы</title>
	</head>
	<body>
		<header>
			НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
		</header>

		<main>
			<ol>
				<li>
					<a href="/lab1" target="_self">Лабораторная работа №1</a>
				</li>
				<li>
					<a href="/lab2" target="_self">Лабораторная работа №2</a>
				</li>
				<li>
					<a href="/lab3" target="_self">Лабораторная работа №3</a>
				</li>
				<li>
					<a href="/lab5" target="_self">Лабораторная работа №5</a>
				</li>
			</ol>
		</main>
		
		<footer>
			&cope; Даниил Дмитриевич, ФБИ-12, 3 курс, 2023
		</footer>
	</body>
</html>
"""


@lab1.route("/lab1")
def lab():
	return """
<!doctype html>
<html>
	<head>
		<title></title>
	</head>
	<body>
		<header>
			НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных работ
		</header>

		<h1>web-сервер на flask</h1>

		<p>
			Flask — фреймворк для создания веб-приложений на языке
			программирования Python, использующий набор инструментов
			Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
			называемых микрофреймворков — минималистичных каркасов
			веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
		</p>

		<a href="/menu" target="_blank">меню</a>

		<h1>Реализованные роуты</h1>

		<main>
			<ul>
				<li>
					<a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a>
				</li>
			</ul>
			<ul>
				<li>
					<a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a>
				</li>
			</ul>
			<ul>
				<li>
					<a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a>
				</li>
			</ul>
			<ul>
				<li>
					<a href="http://127.0.0.1:5000/lab1/dagestan" target="_blank">Дагестан</a>
				</li>
			</ul>
		</main>

		<footer>
			&cope; Даниил Дмитриевич, ФБИ-12, 3 курс, 2023
		</footer>
	</body>
</html>
"""


@lab1.route("/lab1/oak")
def oak():
	return '''
<!doctype html>
<html>
	<link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
	<body>
		<h1 class='header_1'>Дуб</h1>
		<img class='img' src="''' + url_for('static', filename='oak.jpg') + '''">
	</body>
</html>
'''


@lab1.route("/lab1/student")
def student():
	return '''
<!doctype html>
<html>
	<link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
	<body>
		<h1 class='header_1'>Капинос Даниил Дмитриевич</h1>
		<img class='img' src="''' + url_for('static', filename='nstu.jpg') + '''">
	</body>
</html>
'''


@lab1.route("/lab1/python")
def python():
	return '''
<!doctype html>
<html>
	<link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
	<body>
		<h1 class='header_1'>
			Что такое Python?
		</h1>

		<p class='paragraph'>
			Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки.
		</p>

		<h2 class='header_2'>
			В чем заключаются преимущества языка Python?
		</h2>

		<p class='paragraph'>
			Язык Python имеет следующие преимущества:

			Разработчики могут легко читать и понимать программы на Python, поскольку язык имеет базовый синтаксис, похожий на синтаксис английского. 
			Python помогает разработчикам быть более продуктивными, поскольку они могут писать программы на Python, используя меньше строк кода, чем в других языках.
			Python имеет большую стандартную библиотеку, содержащую многократно используемые коды практически для любой задачи. В результате разработчикам не требуется писать код с нуля.
			Разработчики могут легко сочетать Python с другими популярными языками программирования: Java, C и C++.
			Активное сообщество Python состоит из миллионов поддерживающих разработчиков со всего мира. При возникновении проблем сообщество поможет в их решении.
			Кроме того, в Интернете доступно множество полезных ресурсов для изучения Python. Например, вы можете легко найти видеоролики, учебные пособия, документацию и руководства для разработчиков.
			Python можно переносить на различные операционные системы: Windows, macOS, Linux и Unix.
		</p>

		<img class='img' src="''' + url_for('static', filename='python.jpg') + '''">
	</body>
</html>
'''


@lab1.route("/lab1/dagestan")
def dagestan():
	return '''
<!doctype html>
<html>
	<link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
	<body>
		<h1 class='header_1'>Дагестан</h1>

		<p class='paragraph'>
			Субъект Российской Федерации, республика в её составе. Входит в Северо-Кавказский федеральный округ и является частью Северо-Кавказского экономического района. Самый многонациональный регион в Российской Федерации.
			Образована 19 января 1921 года как автономная республика в составе РСФСР. Столица — город Махачкала.
		</p>

		<p class='paragraph'>
			Граничит с Азербайджанской Республикой на юге, с Грузией на юго-западе, а также с Чеченской Республикой на западе, со Ставропольским краем на северо-западе и с Республикой Калмыкия (последние три являются субъектами России) на севере.
		</p>

		<p class='paragraph'>
			Согласно Конституции Республики Дагестан, государственными языками являются русский и языки всех народов, населяющих республику.
		</p>



		<img class='img' src="''' + url_for('static', filename='dagestan.jpg') + '''">
	</body>
</html>
'''