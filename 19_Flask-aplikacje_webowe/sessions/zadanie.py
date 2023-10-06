# flask --app app run
#wypisanie wlasnego imienia - to jest kopia pliku zadanie_app5.py
from flask import Flask, render_template, request,session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = 'sessions'
app.config.from_object(__name__)
Session(app)


@app.route('/params')
def hello():
    name = ""
    args = request.args
    print(args)
    params = [{"key": k, "value": v} for k, v in args.items()]
    if "name" in args.keys():
        name=args["name"]
        #session['key'] = 'value'
        session['name'] = args["name"] # to powoduje ze imie nie znika
    print(params)
    #print(type(session.get('name', 'name not set')))

    if name != "":
        name = session.get('name', 'name not set')
        print("podstawiam zmienna sesyjna")

    return render_template('params5.html', params=params, name=name)
params5 to u mnie:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FlaskApp</title>
</head>
<body>
    <h1>Hello World {{ name }}!</h1>

<ul>
{% for item in params  %}
   <li>{{ item["key"] }}: {{ item.value }}</li>
{% else %}
   no items
{% endfor %}
</ul>

</body>
</html>