from flask import Flask
from flask import session
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab5 import lab5

# Секретный ключ, который обеспечит безопасность генерируемого JWT-токена
app = Flask(__name__)
app.secret_key = '321'

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab5)
