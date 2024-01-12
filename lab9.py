from flask import Blueprint, render_template, request

lab9=Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method =='GET':
        return render_template('lab9/index.html')
    if request.method == 'POST':
        user = request.form.get('user')
        gender = request.form.get('gender')
        user2 = request.form.get('user2')
        return render_template('lab9/otkrytka.html', gender=gender, user=user, user2=user2)

@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/error.html'), 404


@lab9.route('/lab9/500')
def server_error():
    raise Exception("Произошла ошибка")


@lab9.app_errorhandler(Exception)
def er500(e):
   return render_template('lab9/500.html'), 500