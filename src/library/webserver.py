# This is initial learnings of the flask websever framework
# This will then later be used to wrap around the CRUD database commands

from flask import Flask

app = Flask(__name__)

# this decorator will pass the function into it and therefore set it as the function to be called on the route /
@app.route('/create') # This is a decorator, it will mutate the below somehow. allows us to use the same code without needing to modify it.
def create():
    return '<h1>Hello, World!</h1>'