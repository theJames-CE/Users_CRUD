from user import User
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    context = {
        "users": User.get_all()
    }
    return render_template("read_all.html", **context)

# Show link will render the Users Read (One) page
# Read (One) page will display the User's information
@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return render_template("show.html", user=user)
    else:
        return redirect('/users')

@app.route('/users/new')
def new():
    return render_template("create.html")

# After successful creation of a new User, redirect to Read (One) page
@app.route('/users/create', methods=['POST'])
def create():
    user_id = User.save(request.form)
    if user_id:
        return redirect(f'/users/{user_id}')
    else:
        return redirect('/users')

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    user = User.get_by_id(user_id)
    if user:
        return render_template("edit.html", user=user)
    else:
        return redirect('/users')

# After successful update of user, redirect to the Read (One) page and display the updated information
@app.route('/users/<int:user_id>/update', methods=['POST'])
def update(user_id):
    user = User.get_by_id(user_id)
    if user:
        user.first_name = request.form.get('fname')
        user.last_name = request.form.get('lname')
        user.email = request.form.get('email')
        user.update()
    return redirect(f'/users/{user_id}')

# Delete link will delete the User from the database, and redirect to the Read (All) page
@app.route('/users/<int:user_id>/delete', methods=['GET'])
def delete(user_id):
    user = User.get_by_id(user_id)
    if user:
        user.delete()
    return redirect('/users')

# All Home links should redirect to the Read (All) page
@app.route('/home')
def home():
    return redirect('/users')  # Redirect to the Read (All) page

if __name__ == '__main__':
    app.run(debug=True)
