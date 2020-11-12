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

# Route: /demo/json
# Objective: Return some JSON
@notes.app.route('/demo/json')
def json_endpt():
    pass

# Route: /demo/param
# Objective: Take in a query parameter, and use 
#            it to print a note
@notes.app.route('/demo/param/')
def param():
    pass

# Route: /demo/path
# Objective: Take in a path parameter, and use it to
#            print the note
@notes.app.route('/demo/path/<note>')
def path(note):
    pass

# Route: /demo/body
# Objective: Take in a json body, and use it to
#            modify the corresponding note
@notes.app.route('/demo/body')
def body():
    pass

# Route: /demo/names
# Objective: Take in a file, and run the example program on that file
@notes.app.route('/demo/names/<filename>')
def names(filename):
    pass

# Route: /demo/names/body
# Objective: Take in a json body of first names, and return the most common name
# Input: Json as such:
# {
#     "firstnames": ["name1", "name2, "name3"]
# }
# Output: Json as such:
# {
#     "name": "most_common_name"
#     "count": "number_of_appearances"
# }
@notes.app.route('/demo/names/body')
def names_body():
    pass

storage = {
}

# Route: /demo/storage
# GET:
# Objective: Take in a key, and return that element from storage
#            return an error message and 400 bad request if key does not exist
# Output:
# {
#     "key": "key",
#     "value": "val"
# }
#
# DELETE:
# Objective: Take in a key, and delete that element from storage
@notes.app.route('/demo/storage/<key>', methods=["GET", "DELETE"])
def get_or_delete(key):
    if flask.request.method == "DELETE":
        pass
    elif flask.request.method == "GET":
        pass

# Route: /demo/storage
# POST:
# Objective: Take in a json body of key and value, and store it in storage
# Input:
# {
#     "key": "x",
#     "value": 1
# }
# Output: return the input json, and 201 Created on success,
#         return an error message and 400 bad request if key already exists
#
# PUT: 
# Objective: Take in a json body of key and value, and modify the key in storage
# Input:
# {
#     "key": "x",
#     "value": 1
# }
# Output: return the input json, and 201 Created on success,
#         return an error message and 400 bad request if key does not exist
@notes.app.route('/demo/storage', methods=["POST", "PUT"])
def post_or_put():
    pass
