from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcode the available organizations
ORGANIZATIONS = ['Club A', 'Club B', 'Club C', 'Club D', 'Club E']

# Dictionary to store the registered users
registered_users = {}

@app.route('/')
def index():
    return render_template('index.html', organizations=ORGANIZATIONS)

@app.route('/register', methods=['POST'])
def register():
    # Get the user's name and organization from the form data
    name = request.form.get('name')
    organization = request.form.get('organization')

    # Validate the form data
    errors = []
    if not name:
        errors.append('Please enter your name.')
    if not organization:
        errors.append('Please select an organization.')
    elif organization not in ORGANIZATIONS:
        errors.append('Please select a valid organization.')
    if errors:
        return render_template('index.html', organizations=ORGANIZATIONS, errors=errors)

    # Add the user to the registered_users dictionary
    registered_users[name] = organization

    # Redirect to the list of registered users
    return redirect(url_for('list_users'))

@app.route('/list')
def list_users():
    return render_template('list.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run()
