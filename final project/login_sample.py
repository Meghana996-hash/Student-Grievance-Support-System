from bottle import route, run, get, post, request, template, static_file
from datastore import *
import os


@get("/")
def login():
	return template("login1")


@get('/upload')
def upload():
       return template("upload")

@get('/about')
def about():
	return template("about")

@get('/help')
def help():
	return template("help")


      
@get('/upvote/<id>/<username>')
def upvote(id, username):
	gr = get_griv(id)
	update_upvote(gr)
	grs = get_grs()
	return template("upload",user=username, grs=grs)


@post('/uploadsucc')
def do_upload():
        username = request.forms.get("username")
        name = request.forms.get("name")
        comment = request.forms.get("comment")
        add_griv(name, username, comment)
        grs = get_grs()
        return template("upload",user=username, grs=grs)

@route('/lists')
def lists():
	grs = get_grs()
	return template("list_g", grs=grs)

 
@get('/homepage')
def do_homepage():
    return template("homepage")
      
@get('/register')
def do_register():
    return template("register")

@post('/regsucc')
def reg_succ():
	username = request.forms.get("username")
	password = request.forms.get("password")
	name = request.forms.get("name")	
	add_user(name,username,password)
	return "Success"

@route("/listusers")
def list_users():
	users = get_users()
	return template("list",users=users)
  


@get("/login")
def login1():
     return template("login1")


@post("/login1")
def do_login():
	username = request.forms.get("username")
	password = request.forms.get("password")
	myuser = get_user(username, password)
	if myuser:
		grs = get_grs()
		return template("upload",user=username, grs=grs)
	else:
		return template("login_failed",user=username)



@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route("/<name>/profile")
def profile(name):
	return template("profile",user=name)


run(host="localhost",reloader="True",port=8000)
