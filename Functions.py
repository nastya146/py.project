from flask import Flask, jsonify, abort, make_response, request, send_file

from Globals import Global


@Global.app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

  

#log in
@Global.app.route("/notebook", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        print(login in Global.users)
        if login in Global.users:
            if Global.users[login] == password:
                return first_get_notes(login)
        return """<h2> Incorrect login or password</h2>
                    <h2> <a href = "http://127.0.0.1:5000//notebook"> Try again </a>  </h2>"""
    return  """  <style>
                body {
                background-color: blanchedalmond;
                }
                h1 {
                line-height: 70%;
                }
                div {
                line-height: 2;
                }
            </style><body>
            <form method="POST"> 
            <center>
                <h1> Welcome to your beautiful notebook </h1>
                <div><label>Login: <input type="text" name="login"></label></div>
                <div><label>Password: <input type="text" name="password"></textarea></label></div>
                <div> <input type="submit" value="Sign in"> </div>
                <h2> <a href = "http://127.0.0.1:5000//notebook/sign"> Sign up </a>  </h2></center>
                </form> 
            </body>"""
    


# register
@Global.app.route("/notebook/sign", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if login in Global.users:
            return """<h2> This login exits</h2>
                      <h2> Try again</h2>"""
        Global.users[login] = password
        Global.notebook[login] = dict()
        return first_get_notes(login)
    return """    <style>
                body {
                background-color: blanchedalmond;
                }
                    h1 {
                line-height: 70%;
                }
                div {
                line-height: 2;
                }
            </style> <body>
            <form method="POST"> <center>
            <h1> Your new beautiful noteboook </h1>
            <div><label>Login: <input type="text" name="login"></label></div>
            <div><label>Password: <input type="text" name="password"></textarea></label></div>
            <h3> <input type="submit" value="Sign Up"> </h3> </center>
            </form></body>"""


#list of notes
@Global.app.route("/notebook/<user>", methods=["GET"])
def first_get_notes(user):
    dictionary = [Global.notebook[user]]
    result = '; '.join([f'{key}: {value["title"]}' for key, value in dictionary[0].items()])    
    return """ 
        <body bgcolor = azure>
        <form method="POST"> <font size = "5"> 
        <h1> Notebook </h1>
        <h1>{} </h1> 
        <h3>{} </h3> 
        <h3> <a href = "http://127.0.0.1:5000//notebook/note/create/{}"> create new note </a>  </h3>
        <h3> <a href = "http://127.0.0.1:5000//notebook/note/{}"> edit note </a>  </h3>
        <h3> <a href = "http://127.0.0.1:5000//notebook/note/delete/{}"> delete note </a>  </h3>
        <h4> <a href = "http://127.0.0.1:5000//notebook"> log out </a>  </h4>
    """.format(
        user, result, user, user, user, user, user, user
    )




# create note
@Global.app.route("/notebook/note/create/<user>", methods=["GET", "POST"])
def create_note(user):
    if request.method == "POST":
        password = request.form.get("password")
        if user in Global.users and Global.users[user] == password:
            note = {
                "title": request.form.get("title"),
                "description": request.form.get("description"),
            }
            num = str(len(Global.notebook[user]) + 1)
            Global.notebook[user][num] = note
            return """
                <h1> Note {}</h1>
                <h2> Title: {}<h2>
                <h3>{}<h3>
                <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>""".format(
                num, note["title"], note["description"], user
            )
        if not user in Global.users:
            return """<h2>This login doesn't exist</h2>
                    <h2> <a href = "http://127.0.0.1:5000//notebook"> Try again </a>  </h2>"""
        return """<h2>Password is incorrect
                <h2> <a href = "http://127.0.0.1:5000//notebook"> Try again </a>  </h2></h2>"""
    return """
            <font size = "5"> 
            <form method="POST">
              <h1><label>Title: <input type="text" name="title"></label></h1>
              <h1><label>Note: <textarea type="text" rows = '4' name="description"></textarea></label></h1>
              <h3><label>Password:   <input type = 'text' name = 'password' size = '19'></label></h3>
              <input type="submit" value="Save">
            </form>"""


# get and change note
@Global.app.route("/notebook/note/<user>/<note_id>", methods=["GET", "POST"])
def get_note(user, note_id):
    print("get", request.method)
    if request.method == "POST":
        password = request.form.get("password")
        if user in Global.users and Global.users[user] == password:
            note = Global.notebook[user][note_id]
            if len(note) == 0:
                abort(404)
            note["title"] = request.form.get("title")
            note["description"] = request.form.get("description")
            Global.notebook[user][note_id] = note
            return """
                    <h1> Note {}</h1>
                    <h2> Title: {}<h2>
                    <h3>{}<h3>
                    <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>""".format(
                note_id, note["title"], note["description"], user
            )
        if not user in Global.users:
            return """<h2>This login doesn't exist</h2>
                    <h2> <a href = "http://127.0.0.1:5000//notebook"> Try again </a>  </h2>"""
        return """<h2>Password is incorrect</h2>"""
    return """<form method = "POST"> <center>
            <h1>Note {}</h1>
            <h2> Title: <textarea type = "text" name = "title">{}</textarea><h2>
            <h3>Text: <textarea type = "text" name = "description">{}</textarea> <h3>
            <div><label>Password: <input type = 'text' name = 'password'></label></div>
            <input type = "submit" value = "Save Changes"> </input>
            </center></form>""".format(
        note_id,
        Global.notebook[user][note_id]["title"],
        Global.notebook[user][note_id]["description"],
    )


#edit note by click
@Global.app.route("/notebook/note/<user>", methods=["POST", "GET"])
def edit_clicked_note(user):
    if not user in Global.users:
        return abort(404)
    if request.method == "POST":
        password = request.form.get("password")
        id = request.form.get("id")
        title = request.form.get("title")
        if Global.users[user] == password:
            if title != None:
                note = Global.notebook[user][id]
                if len(note) == 0:
                        abort(404)
                note["title"] = request.form.get("title")
                note["description"] = request.form.get("description")
                Global.notebook[user][id] = note
                return """
                <h1> Note {}</h1>
                <h2> Title: {}<h2>
                <h3>{}<h3>
                <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>""".format(
                id, note["title"], note["description"], user
                )
            note = Global.notebook[user][id]
            if len(note) == 0:
                abort(404)
            return """<form method = "POST">
        <h1>Note <textarea type = "text" name = "id" rows = '1' cols = '22'>{}</textarea></h1>
        <h2> Title: <textarea type = "text" name = "title" rows = '1' cols = '24'>{}</textarea><h2>
        <h2>Text: <textarea type = "text" name = "description"rows = '5' cols = '24'>{}</textarea> <h2>
        <h3><label>Password: <input type = 'text' name = 'password'></label></h3>
        <input type = "submit" value = "Save Changes"> </input> <print("llooolll)>
        </form>""".format(
        id,
        Global.notebook[user][id]["title"],
        Global.notebook[user][id]["description"],
            )
        if not user in Global.users:
            return """<h2>This login doesn't exist</h2>
                    <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>""".format(user)
        return """<h2>Password is incorrect</h2> <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>""".format(user)

    return """<form method = "POST">
            <h2> Enter note id that you want to look and edit</h2>
            <h3> Note: <input type = 'text' name = 'id'> </h3>
            <h3><label>Password: <input type = 'text' name = 'password'></label></h3>
            <input type = "submit" value = "Choose note"> </input>
            </form>"""


#delete note by click
@Global.app.route("/notebook/note/delete/<user>", methods=["POST", "GET"])
def delete_clicked_note(user):
    if not user in Global.users:
        return abort(404)
    if request.method == "POST":
        password = request.form.get("password")
        id = request.form.get("id")
        if Global.users[user] == password:
            note = Global.notebook[user][id]
            if len(note) == 0:
                abort(404)
            lengh = str(len(Global.notebook[user]))
            if id != lengh:
                Global.notebook[user][id] = Global.notebook[user][lengh]
            Global.notebook[user].pop(lengh)
            return """
                <h1> Note {} was deleted</h1>
                <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>
                """.format(
                id, user
            )
        if not user in Global.users:
            return """<h2>This login doesn't exist</h2>
                        <a href = "http://127.0.0.1:5000//notebook"> try again </a>"""
        return """<h2>Password is incorrect</h2>
                <a href = "http://127.0.0.1:5000//notebook"> try again </a>"""
    return """<form method = "POST">
            <h2> Enter note id that you want to delete</h2>
            <h3> Note id: <input type = 'text' name = 'id'> </h3>
            <div><label>Password: <input type = 'text' name = 'password'></label></div>
            <h3> <input type = "submit" value = "Delete note"> </input> </h3>
            </form>"""
