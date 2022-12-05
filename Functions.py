from flask import (
  Flask, 
  jsonify,
  abort,
  make_response,
  request
)

from Globals import Global

@Global.app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#register 
@Global.app.route('/notebook', methods=['GET', 'POST'])
def create_user():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        #
        print(login, password, type(login))
        if login in Global.users:
            return '''<h2> This login exits</h2>
                      <h2> Try again</h2>'''
        Global.users[login] = password
        Global.notebook[login]  = dict()
        return first_get_notes(login)
    return '''<form method="POST">
              <div><label>Login: <input type="text" name="login"></label></div>
              <div><label>Password: <input type="text" name="password"></textarea></label></div>
              <input type="submit" value="Sign Up">
            </form>'''


#new list of notes 
@Global.app.route('/notebook/<user>', methods=['GET'])
def first_get_notes(user):
    return ''' <h1> Notes </h1> <h1>Welcome {} </h1> {} 
        <h3> <a href = "http://127.0.0.1:5000//notebook/note/create/{}"> click here </a>  to create note </h3>
        <h3> follow by  http://127.0.0.1:5000//notebook/note/&ltuser&gt/&ltnote_id&gt  to edit created note </h3>
        <h3> follow by http://127.0.0.1:5000//notebook/note/delete/&ltuser&gt/&ltnote_id&gt   to delete created note </h3>
     '''.format(user, Global.notebook[user], user)

#list of notes with authorization
@Global.app.route('/notebook/notes', methods=['GET', 'POST'])
def get_notes():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')
        #
        print(login in Global.users)
        if not login in Global.users:
            return '''<h2>This user doesn't exist</h2>'''
        if (Global.users[login] != password):
            return '''<h2>Password is incorrect</h2>'''
        return ''' <h1>Notes {} </h1> {} 
            <h3> <a href = "http://127.0.0.1:5000//notebook/note/create/{}"> click here </a>  to create note </h3>
            <h3> follow by http://127.0.0.1:5000//notebook/note/&ltuser&gt/&ltnote_id&gt  to edit created note </h3>
            <h3> follow by http://127.0.0.1:5000//notebook/note/delete/&ltuser&gt/&ltnote_id&gt  to delete created note </h3>
        '''.format(login, Global.notebook[login], login)
    return '''<form method="POST">
              <div><label>Login: <input type="text" name="login"></label></div>
              <div><label>Password: <input type="text" name="password"></textarea></label></div>
              <input type="submit" value="Sign Up">
            </form>'''

#create note
@Global.app.route('/notebook/note/create/<user>', methods=['GET', 'POST'])
def create_note(user):
    if request.method == 'POST':
        password = request.form.get('password')
        if user in Global.users and Global.users[user] == password:
            note = {'title': request.form.get('title'),
                'description': request.form.get('description')
            }
            num = str(len(Global.notebook[user]) + 1)
            Global.notebook[user][num] = note
            return'''
                <h1> Note {}</h1>
                <h2> Title: {}<h2>
                <h3>{}<h3>
                <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>'''.format(num, note['title'], note['description'], user)
        if not user in Global.users:
            return '''<h2>This login doesn't exist</h2>'''
        return '''<h2>Password is incorrect</h2>'''
    return  '''<form method="POST">
              <div><label>Title: <input type="text" name="title"></label></div>
              <div><label>Note: <textarea type="text" name="description"></textarea></label></div>
              <div><label>Password: <input type = 'text' name = 'password'></label></div>
              <input type="submit" value="Save">
            </form>'''

#get and change note
@Global.app.route('/notebook/note/<user>/<note_id>', methods=['GET', 'POST'])
def get_note(user, note_id):
    if request.method == 'POST':
        password = request.form.get('password')
        if user in Global.users and Global.users[user] == password:
            note = Global.notebook[user][note_id]
            if len(note) == 0:
                abort(404)
            note['title'] = request.form.get('title')
            note['description'] = request.form.get('description')
            Global.notebook[user][note_id] = note
            return '''
                    <h1> Note {}</h1>
                    <h2> Title: {}<h2>
                    <h3>{}<h3>
                    <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>'''.format(note_id, note['title'], note['description'],user) 
        if not user in Global.users:
            return '''<h2>This login doesn't exist</h2>'''
        return '''<h2>Password is incorrect</h2>'''
    return '''<form method = "POST">
            <h1>Note {}</h1>
            <h2> Title: <textarea type = "text" name = "title">{}</textarea><h2>
            <h3>Text: <textarea type = "text" name = "description">{}</textarea> <h3>
            <div><label>Password: <input type = 'text' name = 'password'></label></div>
            <input type = "submit" value = "Save Changes"> </input>
            </form>'''.format(note_id, Global.notebook[user][note_id]['title'], Global.notebook[user][note_id]['description'])


#delete note
@Global.app.route('/notebook/note/delete/<user>/<note_id>', methods=['POST', 'GET'])
def delete_note(user, note_id):
    if request.method == 'POST':
        password = request.form.get('password')
        if user in Global.users and Global.users[user] == password:
            note = Global.notebook[user][note_id]
            if len(note) == 0:
                abort(404)
            Global.notebook[user].pop(note_id)
            return'''
                <h1> Note {} was deleted</h1>
                <a href = "http://127.0.0.1:5000//notebook/{}"> list of notes </a>
                '''.format(note_id, user)
        if not user in Global.users:
            return '''<h2>This login doesn't exist</h2>'''
        return '''<h2>Password is incorrect</h2>'''        
    return  '''<form method = "POST">
            <h1> Note {}</h1>
            <h2> Title: {}<h2>
            <h3>Text: {}<h3>
            <div><label>Password: <input type = 'text' name = 'password'></label></div>
            <input type = "submit" value = "Delete note"> </input>
            </form>'''.format(note_id, note['title'], note['description'])
