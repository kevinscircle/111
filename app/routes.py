from flask import Flask             # import flask class


app = Flask(__name__)               # create instance of flask class (app is now an object)

@app.route('/')                     # flask decorator to map routes to view functions 
def get_home():                      # flask view function 
    me = {                           # python dictionary (key value pairs)
        "first_name": "Kevin",
        "last_name": "Reyes",
        "hobbies": "jogging, time with pet at trails or parks",
        "is_online": True
        
    }
    return me                           # when you return a dict in Flask it is converted to JSON!
