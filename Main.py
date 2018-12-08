#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from datetime import datetime
import hashlib

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='pricosha',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
    return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/add_comment')
def add_comment():
    return render_template('create_comment.html')

@app.route('/tag_someone')
def tag_someone():
    return render_template('tag_content.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/new_friend')
def newMember():
    return render_template('new_user.html')

@app.route('/old_friend')
def oldMember():
    return render_template('old_user.html')


@app.route('/create_group')
def newGroup():
    return render_template('new_group.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    #grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    password = password.encode('utf-8')
    password = hashlib.sha256(password).hexdigest()
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM person WHERE email = %s and password = %s'
    cursor.execute(query, (email, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['email'] = email
        return redirect(url_for('home'))
    else:
        #returns an error message to the html page
        error = 'Invalid password or email'
        return render_template('login.html', error=error)

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    #grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    password = request.form['password']
    password = password.encode('utf-8')
    password = hashlib.sha256(password).hexdigest()
    fname = request.form['fname']
    lname = request.form['lname']
    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM person WHERE email = %s'
    cursor.execute(query, (email))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        ins = 'INSERT INTO person VALUES(%s, %s, %s, %s)'
        cursor.execute(ins, (email, password, fname, lname))
        conn.commit()
        cursor.close()
        return render_template('index.html')


@app.route('/home')
def home():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM contentitem WHERE is_pub = 1 AND post_time > DATE_SUB(CURDATE(), INTERVAL 1 DAY) ORDER BY post_time DESC'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('home.html', email=email, posts=data)

#creates a new post
@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    email = session['email']
    cursor = conn.cursor();
    title = request.form['title']
    file_path = request.form['file_path']
    post_time = datetime.now()
    is_pub = int(request.form['is_pub'])
    fgroup = request.form['fgroup']
    query = 'INSERT INTO contentitem (item_name, file_path, email_post, post_time, is_pub) VALUES(%s, %s, %s, %s, %s)'
    cursor.execute(query, (title, file_path, email, post_time, is_pub))
    if(fgroup != "" and is_pub == 0):
        query = 'SELECT item_id FROM contentitem WHERE item_name = %s AND email_post = %s'
        cursor.execute(query, (title, email))
        data = cursor.fetchone()
        data = data.get('item_id')
        query = 'INSERT INTO share (owner_email, fg_name, item_id) VALUES(%s, %s, %s)'
        cursor.execute(query, (email, fgroup, data))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))

#adds new user to group
@app.route('/new_user', methods=['GET', 'POST'])
def new_person():
    email = session['email']
    cursor = conn.cursor();
    groupName  = request.form['fg_name']
    ownerEmail  = request.form['owner_email']
    userEmail   = request.form['user_email']
    if ownerEmail != email:
        return redirect(url_for('error'))
    query = 'INSERT INTO belong (email,owner_email,fg_name) VALUES(%s,%s,%s)'
    cursor.execute(query, (userEmail,ownerEmail,groupName))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))

#removes a user from a group
@app.route('/old_user', methods=['GET', 'POST'])
def delete_person():
    
    cursor = conn.cursor();
    groupName  = request.form['fg_name']
    ownerEmail  = request.form['owner_email']
    userEmail   = request.form['user_email']
    query = 'DELETE FROM belong WHERE email = %s AND owner_email = %s AND fg_name = %s'
    cursor.execute(query, (userEmail,ownerEmail,groupName))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))

#creates a new group
@app.route('/create_new_group', methods=['GET', 'POST'])
def create_new_group():  
    email = session['email']
    cursor = conn.cursor();
    groupName  = request.form['fg_name']
    query = 'INSERT INTO friendgroup (owner_email,fg_name) VALUES(%s,%s)'
    cursor.execute(query, (email,groupName))
    return redirect(url_for('home'))  


@app.route('/my_posts', methods=["GET", "POST"])
def my_posts():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s) ORDER BY post_time DESC'
    cursor.execute(query, (email, email))
    data = cursor.fetchall()
    cursor.close()
    return render_template('my_posts.html', posts=data)

@app.route('/tags', methods=["GET", "POST"])
def tags():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM tag NATURAL JOIN person WHERE tag.email_tagged = person.email and tag.status = "True" AND item_id IN (SELECT item_id FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s))'
    cursor.execute(query, (email, email))
    data = cursor.fetchall()
    cursor.close()
    return render_template('tags.html', posts=data)

@app.route('/ratings', methods=["GET", "POST"])
def ratings():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM rate NATURAL JOIN contentitem WHERE item_id IN (SELECT item_id FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s))'
    cursor.execute(query, (email, email))
    data = cursor.fetchall()
    cursor.close()
    return render_template('ratings.html', posts=data)

@app.route('/my_groups', methods=["GET", "POST"])
def groups():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM friendgroup WHERE owner_email = %s'
    cursor.execute(query, (email))
    data = cursor.fetchall()
    cursor.close()
    return render_template('groups.html', posts=data)

@app.route('/manage_tags', methods=["GET", "POST"])
def manage_tags():
    email = session['email']
    cursor = conn.cursor();
    query = 'SELECT * FROM tag WHERE email_tagged = %s AND status = "False"'
    cursor.execute(query, email)
    data = cursor.fetchall()
    idtoapprove = int(request.args.get('idtoapprove', default=-1))
    idtodelete = int(request.args.get('idtodelete', default=-1))
    print(idtoapprove)
    print(idtodelete)
    if(idtoapprove > 0):
        query = 'UPDATE tag SET status = "True" WHERE item_id = %s'
        cursor.execute(query, idtoapprove)
    if(idtodelete > 0):
        query = 'DELETE FROM tag WHERE item_id = %s AND email_tagged = %s'
        cursor.execute(query, (idtodelete, email))
    cursor.close()
    return render_template('manage_tags.html', posts = data)

@app.route('/tag_content', methods=["GET","POST"])
def tag_content():
    email = session['email']
    cursor = conn.cursor();
    item_id = int(request.args.get('id_post'))
    email_tagged = request.args.get('email_tagged')
    post_time = datetime.now()
    query = 'SELECT item_id FROM contentitem WHERE item_id IN (SELECT item_id FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s))'
    cursor.execute(query, (email_tagged, email_tagged))
    data = cursor.fetchone()
    if(data):
        if (email_tagged == email):
            query = 'INSERT INTO tag VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(query, (email, email, item_id, 'True', post_time))
        else:
            query = 'INSERT INTO tag VALUES (%s, %s, %s, %s, %s)'
            cursor.execute(query, (email_tagged, email, item_id, 'False', post_time))
    else:
        redirect(url_for('error'))
    cursor.close()
    return redirect(url_for('home'))


@app.route('/create_comment', methods=["GET","POST"])
def create_comment():
    email = session['email']
    cursor = conn.cursor();
    item_id = int(request.args.get('id_post'))
    comment = request.args.get('comment')
    commenttime = datetime.now()
    query = 'SELECT item_id FROM contentitem WHERE item_id IN (SELECT item_id FROM contentitem NATURAL LEFT JOIN share WHERE email_post = %s OR item_id IN (SELECT item_id FROM share NATURAL JOIN belong WHERE email = %s))'
    cursor.execute(query, (email, email))
    data = cursor.fetchone()
    if(data):
        query = 'INSERT INTO comments(commentor,comment,item_id,commenttime) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (email, comment, item_id, commenttime))
    else:
        redirect(url_for('error'))
    cursor.close()
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('email')
    return redirect('/')
        
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
