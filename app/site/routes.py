from flask import Blueprint, render_template, request

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/about')
def about():
    return render_template('about.html')

@site.route('/cats')
def cats():
    return render_template('cats.html')

@site.route('/submit_form', methods=['GET'])
def contact():
    return render_template('contact.html')

@site.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    
    return "Form submitted successfully!"
