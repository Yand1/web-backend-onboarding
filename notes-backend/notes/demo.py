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

# Route: /demo/sql
# Objective: Execute a sql command on the database'
@notes.app.route('/demo/sql')
def sql():
    return 'Hello, World!'

# Route: /demo/param
# Objective: Take in a query parameter id, and use 
#            it to modify the corresponding note
@notes.app.route('/demo/param/')
def param():
    note = flask.request.args.get('note')

    return "You sent the note: " + str(note)

# Route: /demo/path
# Objective: Take in a path parameter, and use it to
#            modify the corresponding note
@notes.app.route('/demo/path/<note>')
def path(note):
    return "You sent the note: " + str(note)

# Route: /demo/body
# Objective: Take in a json body, and use it to
#            modify the corresponding note
@notes.app.route('/demo/body')
def body():
    body = flask.request.get_json()
    return body["text"] + "\nP.S." + body["additional"]

# Route: /demo/names
# Objective: Take in a file, and perform the demo operations
@notes.app.route('/demo/names')
def names():
    names = []
    with open(os.getcwd() + "/names.txt", "r") as f:
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
        output_str += "<li>" + firstnames_sorted_list[i][0] + ", count = " + str(firstnames_sorted_list[i][1]) + "<\li>"
        
    output_str += "</ul>"

    lastnames_sorted_list = sorted(lastnames.items(), key=lambda x: x[1], reverse=True)
    output_str += "Lastnames:<ul>"
    for i in range(5):
        output_str += "<li>" +lastnames_sorted_list[i][0] + ", count = " + str(lastnames_sorted_list[i][1]) + "<\li>"

    output_str += """
        </ul>
        </body>
    </html>
    """
    return output_str
    