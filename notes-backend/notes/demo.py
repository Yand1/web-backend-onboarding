import flask
import os
import notes

# Route: /demo/
# Objective: Print 'Hello, World!'
@notes.app.route('/demo/hello')
def hello():
    return 'Hello, World!'

# Route: /demo/html
# Objective: Print some HTML
@notes.app.route('/demo/html')
def html():
    ret = """
    <!DOCTYPE html>
    <html>
        <body>
            <ul>
    """

    for i in range(3):
        ret += "<li>element " + str(i) + "</li>"

    ret += """
            </ul>
        </body>
    </html>
    """
    
    return ret

# Route: /demo/json
# Objective: Return some JSON
@notes.app.route('/demo/json')
def json_endpt():
    count_dict = {}
    
    for i in range(3):
        count_dict["element" + str(i)] = i

    return count_dict, 200

# Route: /demo/param
# Objective: Take in a query parameter, and use 
#            it to print a note
@notes.app.route('/demo/param/')
def param():
    note = flask.request.args.get('note')

    return "You sent the note: " + str(note)

# Route: /demo/path
# Objective: Take in a path parameter, and use it to
#            print the  note
@notes.app.route('/demo/path/<note>')
def path(note):
    return "You sent the note: " + str(note)

# Route: /demo/body
# Objective: Take in a json body, and use it to
#            modify the corresponding note
@notes.app.route('/demo/body')
def body():
    body = flask.request.get_json()
    return body["text"] + "\nP.S. " + body["additional"]

# Route: /demo/names
# Objective: Take in a file, and run the example program on that file
@notes.app.route('/demo/names/<filename>')
def names(filename):
    names = []
    with open(os.getcwd() + "/" + filename, "r") as f:
        for line in f:
            names.append(line)

    firstnames = {}
    lastnames = {}
    
    for name in names:
        name_arr = name.split()

        if name_arr[0] not in firstnames:
            firstnames[name_arr[0]] = 0

        firstnames[name_arr[0]] += 1

        if name_arr[1] not in lastnames:
            lastnames[name_arr[1]] = 0

        lastnames[name_arr[1]] += 1

    output_str = """
    <!DOCTYPE html>
    <html>
        <body>
    """

    firstnames_sorted_list = sorted(firstnames.items(), key=lambda x: x[1], reverse=True)
    output_str += "Firstnames:<ul>"
    for i in range(5):
        output_str += "<li>" + firstnames_sorted_list[i][0] + ", count = " + str(firstnames_sorted_list[i][1]) + "</li>"
        
    output_str += "</ul>"

    lastnames_sorted_list = sorted(lastnames.items(), key=lambda x: x[1], reverse=True)
    output_str += "Lastnames:<ul>"
    for i in range(5):
        output_str += "<li>" +lastnames_sorted_list[i][0] + ", count = " + str(lastnames_sorted_list[i][1]) + "</li>"

    output_str += """
        </ul>
        </body>
    </html>
    """
    return output_str

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
    firstnames = flask.request.get_json()["firstnames"]
    firstnames_count = {}
    for name in firstnames:
        if name not in firstnames_count:
            firstnames_count[name] = 0

        firstnames_count[name] += 1
    
    max_name = max(firstnames_count.items(), key=lambda k: k[1])

    return {
        "name": max_name[0],
        "count": max_name[1]
    }

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
        storage.pop(key, None)

        return '', 204
    elif flask.request.method == "GET":
        if key not in storage:
            return {"message": "key doesn't exist"}, 400

        return {
            "key": key,
            "value": storage[key]
        }

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
    original_json = flask.request.get_json()
    key = original_json["key"]
    value = original_json["value"]

    if flask.request.method == "POST" and key in storage:
        return {"message": "key already exists"}, 400
    elif flask.request.method == "PUT" and key not in storage:
        return {"message": "key doesn't exist"}, 400

    storage[key] = value

    return original_json, 201
