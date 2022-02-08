'''
FrameWork --

A framework in programming is a tool that provides 
ready-made components or solutions that are customized 
in order to speed up development.

*A framework is a structure that you can build software on. 
It serves as a foundation,
so you're not starting entirely from scratch.

Django and Flask are two different web 
frameworks built on top of the Python programming language.

'''

'''
setting venv --> python3.8 -m venv <projectname>

or

python3.8 -m venv venv
or 
python3 -m venv venv
'''

'''
activation -->
mac--> source projectName/bin/activate

windows -->

.\venv\Scripts\activate

'''
'''
pip list (to check item inside folder venv)

'''

from flask import Flask,jsonify, request
 
app = Flask(__name__)

tasks = [
     {
        'id' : 1,
        'title' : u'Buy groceries',
        'description'  : u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done' : False
     },
     {
         'id' : 2,
        'title' : u'Learn Python',
        'description'  : u'Need to find a good python tutorial on the web',
        'done' : False
     }

]
@app.route("/")
def hello_world():
    return "Hello chotu"

@app.route('/add_data', methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    
    
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['Name'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/receive_data")
def get_task():
    return jsonify({
        "data" : tasks
    })    

if (__name__ == "__main__"):
    app.run(debug=True,port = 8080)    