import flask
import notes

#   We will need to accept GET, POST, PUT, and DELETE
#   from the notes frontend. Create endpoints to serve the
#   frontend by filling in these functions!

# Route: /notes/
# GET:
#    Input: None
#    Objective: Return a list of all notes in the database, in this json format:
#    {
#        "notes": [
#            {
#                "id": 1,
#                "note": "note string",
#                "completed": true
#            }
#            {
#                "id": 2,
#                "note": "note string 2",
#                "completed": false
#            }
#        ]
#    }
#
# POST:
#    Input: Json body with a note to add in the following format:
#    {
#        "note:" "note string",
#        "completed": false
#    }
#    Objective: Add that note to the database, return the note added
@notes.app.route('/notes/', methods=["GET", "POST"])
def get_or_post_notes():
    connection = notes.db.get_db()

    if flask.request.method == "GET":
        pass
    elif flask.request.method == "POST":
        pass

# Route: /notes/<int:note_id>/
# PUT:
#    Input: Path parameter note_id and json body in the following format
#    {
#        "completed": false
#    }
#    Objective: Modify the note with the given note id to be completed or not
#               completed based on the input json, return status code 200
#
# DELETE:
#    Input: Path parameter note_id
#    Objective: Delete the note with the given note id from the database, return 204 no content
@notes.app.route('/notes/<int:note_id>/', methods=["PUT", "DELETE"])
def edit_or_delete_note(note_id):
    connection = notes.db.get_db()

    if flask.request.method == "PUT":
        pass
    elif flask.request.method == "DELETE":
        pass