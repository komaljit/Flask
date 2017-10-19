from flask import Flask, url_for, request, render_template
import random
import json
import redis

app = Flask(__name__)
wsgi_app = app.wsgi_app
r = redis.StrictRedis(decode_responses=True)
p = open("C:/Users/Komal Raju/flask3/templates/question.json.txt","r")
s = json.loads(p.read())
p.close()
f = open("C:/Users/Komal Raju/flask3/templates/option.json.txt","r")
opt = json.loads(f.read())
f.close()
  
@app.route('/')
def hello():
    createlink = url_for('create')
    return render_template("index.html",createlink=createlink)
@app.route('/quiz',methods=['GET','POST'])
def create():

    if request.method == 'GET':
        num = random.randint(1,9)
        question = s[str(num)]["question"]
        options = opt[str(num)]
        answer = s[str(num)]["answer"]
        r.set("answer",answer) 
        return render_template('quiz.html',options=options,question=question)

    elif request.method == 'POST':
        submittedanswer = request.form['first']
        answer = r.get("answer")
        nextquestion = url_for('create')
        if submittedanswer == answer:
            return render_template('Correct.html',nextquestion=nextquestion)       
        else:
            return render_template('Incorrect.html',submittedanswer=submittedanswer,answer=answer,nextquestion=nextquestion)     
    else:
        return "<h2>Invalid request</h2>"

if __name__ == "__main__":
    app.run(debug=True)
