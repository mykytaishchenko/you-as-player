from flask import Flask, render_template, redirect, request

import auth
from auth import is_logged_in, get_user

from models import DataBase, Answer

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.secret_key = "something_secret"
app.register_blueprint(auth.app)


@app.route('/')
def home():
    return render_template("home.html", log=is_logged_in())


@app.route('/me')
def me():
    if is_logged_in():
        return render_template("me.html", graded=len(get_user().form.answers), user=get_user())
    return redirect('login')


@app.route('/form/<_id>')
def show(_id):
    if not is_logged_in():
        return redirect('/login')
    if DataBase.get_user_by_id(_id) is not None:
        return render_template("user.html", graded=len(DataBase.get_user_by_id(_id).form.answers), cur=get_user(), user=DataBase.get_user_by_id(_id),
                               mails=[answer.mail for answer in DataBase.get_user_by_id(_id).form.answers])
    return redirect('/')


@app.route('/grade/<_id>', methods=["POST", "GET"])
def grade(_id):
    if not is_logged_in():
        return redirect('/login')
    if request.method == 'POST':
        new_answer = Answer(get_user().mail)
        new_answer.force = int(request.form.get("radio-1"))
        new_answer.agility = int(request.form.get("radio-2"))
        new_answer.speed = int(request.form.get("radio-3"))
        new_answer.beauty = int(request.form.get("radio-4"))
        new_answer.physique = int(request.form.get("radio-5"))
        new_answer.intelligence = int(request.form.get("radio-6"))
        new_answer.wisdom = int(request.form.get("radio-7"))
        new_answer.stress_tolerance = int(request.form.get("radio-8"))
        new_answer.creativity = int(request.form.get("radio-9"))
        new_answer.charisma = int(request.form.get("radio-10"))
        new_answer.sociability = int(request.form.get("radio-11"))
        new_answer.reliability = int(request.form.get("radio-12"))
        new_answer.leadership_skills = int(request.form.get("radio-13"))
        new_answer.special_skills = int(request.form.get("radio-14"))

        DataBase.add_answer(new_answer, _id)

        return redirect(f'/form/{_id}')

    if DataBase.get_user_by_id(_id) is not None:
        return render_template("grade.html", cur=get_user(), user=DataBase.get_user_by_id(_id),
                                topics=["Сила", "Cпритність", "Швидкість", "Краса", "Статура",
                                        "Інтелект", "Мудрість", "Стресостійкість", "Креативність",
                                        "Харизма", "Социалізація", "Надійність", "Лідерські навички",
                                        "Особливі навички"])
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
