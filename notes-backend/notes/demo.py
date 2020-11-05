import flask
import notes

# Route: /demo/
# Objective: Print 'Hello, World!'
@notes.app.route('/demo/hello')
def hello():
    pass

# Route: /demo/html
# Objective: Print some HTML
@notes.app.route('/demo/html')
def html():
    pass

# Route: /demo/jinja
# Objective: Print some HTML with jinja templating
@notes.app.route('/demo/jinja')
def jinja():
    pass

# Route: /demo/sql
# Objective: Execute a sql command on the database'
@notes.app.route('/demo/sql')
def sql():
    pass

# Route: /demo/param
# Objective: Take in a query parameter id, and use 
#            it to modify the corresponding note
@notes.app.route('/demo/param/')
def param():
    pass

# Route: /demo/path
# Objective: Take in a path parameter, and use it to
#            modify the corresponding note
@notes.app.route('/demo/path')
def path():
    pass

# Route: /demo/body
# Objective: Take in a json body, and use it to
#            modify the corresponding note
@notes.app.route('/demo/body')
def body():
    pass

# Route: /demo/hello2
# Objective: Take in a path parameter, and use it to
#            return the corresponding note
@notes.app.route('/demo/hello2')
def hello2():
    pass

# Route: /demo/return
# Objective: Take in a path parameter, and use it to
#            return the corresponding note
@notes.app.route('/demo/return')
def ret():
    pass
