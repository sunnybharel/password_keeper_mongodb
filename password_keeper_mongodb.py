from mongoengine import *
import datetime

connect('password_db', host='localhost', port=27017)

class Post(Document):
    url = StringField(required=False, max_length=200)
    user = StringField(required=True)
    password = StringField(required=False)
    published = DateTimeField(default=datetime.datetime.now)

def create():
    post = Post()
    post.url = input("Enter URL: ")
    post.user = input("Enter Username: ")
    post.password = input("Enter Password: ")
    post.save()
    pretty_print(post)

def pretty_print(post):
    print("---\n{}\t\t{}\n{}\t\t{}\n{}\t{}\n{}\t{}".format("URL",post.url, "User", post.user, "Password", post.password, "Published", post.published))

def view():
    for rec in Post.objects:
        pretty_print(rec)

def view_by_domain():
    filter = input("Enter partial or complete domain name to search for: ")
    for rec in Post.objects(url__contains=filter):
        pretty_print(rec)

while True:
    response = input("'c' to create a record \n'v' to view all records \n'w' to filter by domain \nAny other key to quit: ")
    if response[0].lower() == 'c':
        create()
    elif response[0].lower() == 'v':
        view()
    elif response[0].lower() == 'w':
        view_by_domain()
    else:
        break
