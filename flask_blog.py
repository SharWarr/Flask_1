from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY




posts = [
    {
        'author':'Jane Doe',
         'title':'Blog post',
         'content':'In the 2010s, the majority are interactive Web 2.0 websites, allowing visitors to leave online comments, and it is this interactivity that distinguishes them from other static websites. In that sense, blogging can be seen as a form of social networking service. Indeed, bloggers not only produce content to post on their blogs but also often build social relations with their readers and other bloggers.',
         'date_posted':'April 20 2021'
    },
    {
        'author':'Jane Warrier',
         'title':'MY blog post ',
         'content':'The emergence and growth of blogs in the late 1990s coincided with the advent of web publishing tools that facilitated the posting of content by non-technical users who did not have much experience with HTML or computer programming. Previously, a knowledge of such technologies as HTML and File Transfer Protocol had been required to publish content on the Web, and early Web users therefore tended to be hackers and computer enthusiasts.',
         'date_posted':'April 22 2021'
    },
    {
        'author':'Jane2 Warrier',
         'title':'MY blog post ',
         'content':'The emergence and growth of blogs in the late 1990s coincided with the advent of web publishing tools that facilitated the posting of content by non-technical users who did not have much experience with HTML or computer programming. Previously, a knowledge of such technologies as HTML and File Transfer Protocol had been required to publish content on the Web, and early Web users therefore tended to be hackers and computer enthusiasts.',
         'date_posted':'April 22 2021'
    }
]

@app.route("/")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/registration")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='login',form=form)
if __name__ == '__main__':
    app.run(debug=True)


