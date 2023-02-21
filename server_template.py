from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route("/") #root directory.
def landing_page():
    return render_template('./index.html')


# @app.route("/index.html") #home re-direct
# def home_page():
#     return render_template('./index.html')

# @app.route("/work.html") #inspect why we have 'work' and 'works'
# def work_page():
#     return render_template('./work.html')

# @app.route("/works.html")
# def works_page():
#     return render_template('./works.html')

# @app.route("/about.html") 
# def about_page():
#     return render_template('./about.html')

# @app.route("/contact.html")
# def contact_page():
#     return render_template('./contact.html')

#if no valid enpoint
# @app.route("/<username>")
# def imvalid_endpoint(username):
#     return 'Please input a valid URL'

@app.route('/<string:page_name>') 
def html_page(page_name):
    return render_template(page_name)


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    return redirect('./thankyou.html')





