import bcrypt
from flask import Flask, render_template, request, url_for, redirect, session, jsonify, make_response
import os
from db_connection import *
from PASS.PASS import PASSWORD
import random
from PASS.EMAIL_PASS import Email, Email_password
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = PASSWORD

app.config['MAIL_SERVER'] = 'smtp.ukr.net'
app.config["MAIL_PORT"] = 465
app.config['MAIL_USERNAME'] = Email
app.config['MAIL_DEFAULT_SENDER'] = Email
app.config['MAIL_PASSWORD'] = Email_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.app_context().push()
def send_email(*args):
    print('email send minus')
    msg = Message('Event reminder', recipients=[args[4]])
    msg.body = 'Your daily weather'
    msg.html = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            padding: 20px;
        }}
        h1 {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        .label {{
            font-weight: bold;
        }}
    </style>
</head>
"""
    msg.html = f"""
<body>
    <h1>Котячий документ</h1>
    <ul>
        <li><span class="label">Імʼя:</span> {args[0]}</li>
        <li><span class="label">Порода:</span> {args[1]}</li>
        <li><span class="label">Стать:</span> {args[2]}</li>
        <li><span class="label">Вік:</span> {args[3]} років</li>
        <li><span class="label">Email:</span> {args[4]}</li>
        <li><span class="label">ID паспорту:</span> {args[5]}</li>
    </ul>
    <p>Дякуємо за звернення до нас!</p>
</body>
</html>
"""
    mail.send(msg)
    print('email send plus')

def send_email_answer(email):
    print('email send minus')
    msg = Message('Event reminder', recipients=[email])
    msg.body = 'Your daily weather'
    msg.html = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            padding: 20px;
        }}
        h1 {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        .label {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Ваше замовлення оформлено!</h1>
    <ul>
        <li><span class="label">Найближчим часом з вами звʼяжуться та підтвердять ваше замовлення!</li>
    </ul>
    <p>Дякуємо за звернення до нас!</p>
</body>
</html>
"""
    mail.send(msg)
    print('email send plus')
def file_counter():
    path = 'static/uploads'
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return len(files)

@app.route('/', methods=['GET','POST'])
@app.route('/home/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        query = data.get('query', '')
        result = search(words=query)
        return render_template('search.html', position=result)
    return render_template('home.html')

@app.route('/home/search/', methods=['GET'])
def searching():
    data = request.get_json()
    query = data.get('query', '')
    result = search(words=query)
    print(result)
    return render_template('search.html', position=result)

@app.route('/home/marriage-registration/')
def marriage_registration():
    email = request.cookies.get('email')
    if email:
        return render_template('/marriage_reg/marriage_reg.html', error = request.args.get('error'))
    else:
        return redirect(url_for('profile'))

@app.route('/home/marriage-registration/document/', methods=['POST'])
def marriage_registration_document():
    email = request.cookies.get('email')
    passport_id1 = request.form['pass1']
    passport_id2 = request.form['pass2']
    id1id2 = read_profile_email(email)

    print(id1id2)
    if read_profile(passport_id1):
        if read_profile(passport_id2):
            if id1id2[7] == passport_id1 or id1id2 == passport_id2:
                if passport_id1 == passport_id2:
                    return redirect(url_for('marriage_registration', error="Error are required"))
                else:
                    if not search_ragistration(passport_id1, passport_id2):
                        add_registration(passport_id1, passport_id2)
                        return redirect(url_for('profile'))
                    else:
                        return redirect(url_for('marriage_registration', error="Error are required"))
            else:
                return redirect(url_for('marriage_registration', error="Error are required"))
        else:
            return redirect(url_for('marriage_registration', error="Error are required"))
    else:
        return redirect(url_for('marriage_registration', error="Error are required"))

@app.route('/home/<string:title>/')
def position(title):
    pos = ['veterinary_clinic', 'wedding', 'photograph', 'restaurant', 'ceremony', 'honeymoon']
    if title == pos[0]:
        result = read_position('Veterinary')
    elif title == pos[1]:
        return render_template('wedding.html')
    elif title == pos[2]:
        result = read_position('Photograph')
    elif title == pos[3]:
        result = read_position('Restaurant')
    elif title == pos[4]:
        result = read_position('Ceremony')
    else:
        result = read_position('Honeymoon')
    return render_template('position.html', position=result, email=request.cookies.get('email'))

@app.route('/home/wedding_bag/<wedding>/')
def wedding_bag(wedding):
    email = request.cookies.get('email')
    if not email:
        return redirect(url_for('sign_in'))
    if wedding:
        add_my_bag(email, 'Вінчання', 'Послуги вінчання чарівної котячої пари.', '2500', '/static/wedding.jpg')
        return redirect(url_for('bag'))
    else:
        return redirect(url_for('home'))

@app.route('/home/make-document/')
def make_document():
    return render_template('/profile/make_document.html', email=request.cookies.get('email'))

@app.route('/home/make-document/document/', methods=['POST'])
def document():
    global file_counter
    name = request.form['name']
    type = request.form['type']
    stat = request.form['stat']
    age = request.form['age']
    email = request.form['email']
    password = request.form['password']
    passport_id = request.form['passport_id']
    file = request.files['photo']
    id_file = file_counter() + 1
    if file:
        unique_filename = f"{id_file}.jpg"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
    if not passport_id:
        while True:
            passport_id = random.randint(100000, 999999)
            if not any(passport_id in pass_id for pass_id in read_profile_passport_id()):
                break
    add_profile(name, type, stat, float(age), email, password, int(passport_id), str(id_file))

    send_email(name, type, stat, float(age), email, int(passport_id), str(id_file))
    if not request.cookies.get('email'):
        res = make_response(redirect(url_for('profile', passport_id=passport_id)))
        res.set_cookie('email', email, max_age=60 * 60 * 24)
        return res
    return redirect(url_for('profile'))

@app.route('/home/sign-in/')
def sign_in():
    return render_template('/profile/sign_in.html', error = request.args.get('error'))

@app.route('/home/profile/', methods=['GET', 'POST'])
def profile():
    if request.cookies.get('email'):
        profile = read_profile_email(request.cookies.get('email'))
        if profile:
            registration = read_registration_id(profile[7])
            if registration[1] == profile[7]:
                profile_cat2 = read_profile(registration[2])
                return render_template('/profile/profile.html', profile=profile, cat2=profile_cat2)
            else:
                profile_cat2 = read_profile(registration[1])
                return render_template('/profile/profile.html', profile=profile, cat2=profile_cat2)
        else:
            return 'Not Found'
    if request.method == 'GET':
        return redirect(url_for('sign_in'))

@app.route('/home/profile/out/', methods=['POST'])
def out():
    response = make_response(redirect(url_for('home')))
    response.set_cookie('email', 'None', expires=60*60*24)
    return response

@app.route('/home/sign-in/answer/', methods=['POST'])
def sign_in_post():
    email = request.form['email']
    password = request.form['password']
    passport_id = int(request.form['passport_id'])
    profile = read_profile(passport_id)
    if profile[0][5] == email:
        if password == profile[0][6]:
            if not request.cookies.get('email'):
                res = make_response(redirect(url_for('profile', passport_id=passport_id)))
                res.set_cookie('email', email, max_age=60 * 60 * 24)
                return res
            return redirect(url_for('profile'))
        else:
            return redirect(url_for("sign_in", error = "Error are required"))
    else:
        return redirect(url_for("/profile/sign_in", error = "Error are required"))

@app.route('/home/bag/')
def bag():
    email = request.cookies.get('email')
    if not email:
        return redirect(url_for('sign_in'))
    else:
        result = read_my_bag(email)
        price = sum(int(pos[4]) for pos in result)
        return render_template('my_bag.html', position=result, sum=price)

@app.route('/home/bag/<name>/', methods=['GET', 'POST'])
def my_bag(name):
    if request.method == 'GET':
        result = search(name)
        email = request.cookies.get('email')
        if not email:
            return redirect(url_for('sign_in'))
        for position in result:
            add_my_bag(email, position[1], position[2], position[3], position[4])
        return redirect(url_for('bag'))
    else:
        return "Not Found"

@app.route('/home/bag/answer/', methods=['GET', 'POST'])
def answer():
    if request.cookies.get('email'):
        if request.method == 'POST':
            email = request.cookies.get('email')
            number_phone = request.form['phone']
            data = request.form['data']
            add_answer(email, number_phone, data)

            send_email_answer(email)
            return render_template('answer.html', post=True)
        else:
            return render_template('answer.html')
    else:
        return redirect(url_for('home'))



@app.route('/home/bag/delete/<int:id>/', methods=['POST'])
def delete(id):
    delete_my_bag(id)
    return redirect(url_for('bag'))

# @app.route("/login/", methods=["GET", "POST"])
# def login():
#     if not request.cookies.get('email') and request.method == "POST":
#         res = make_response("Setting a cookie")
#         res.set_cookie('email', request.form.get("Email"), max_age=60 * 60 * 24)
#         return res
#     return render_template("/make_document/make_document.html")

if __name__ == '__main__':
    app.run(debug=True, port=1203)