from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient(
    "mongodb+srv://naamameypen:kJlFQ6jtZj8zK1eZ@cluster0.nh5hxwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['companyDatabase']



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['POST'])
def login():
    identity_number = request.form['identity_number']
    user = db.users.find_one({"_id": ObjectId(identity_number)})
    if user:
        if user['type'] == 'employee':
            return redirect(url_for('employee_dashboard', user_id=user['_id']))
        elif user['type'] == 'manager':
            return redirect(url_for('manager_dashboard', user_id=user['_id']))
    return 'User not found', 404


@app.route('/employee/<user_id>')
def employee_dashboard(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    projects = db.projects.find({"group_id": user['group_id']})
    return render_template('employee_dashboard.html', user=user, projects=projects)


@app.route('/request_permission', methods=['POST'])
def request_permission():
    user_id = request.form['user_id']
    project_id = request.form['project_id']
    access_type = request.form['access_type']
    request_data = {
        "user_id": ObjectId(user_id),
        "project_id": ObjectId(project_id),
        "access_type": access_type,
        "status": "pending"
    }
    db.requests.insert_one(request_data)
    return redirect(url_for('employee_dashboard', user_id=user_id))


@app.route('/manager/<user_id>')
def manager_dashboard(user_id):
    requests = db.requests.find({"status": "pending"})
    return render_template('manager_dashboard.html', requests=requests)


@app.route('/approve_request/<request_id>')
def approve_request(request_id):
    db.requests.update_one({"_id": ObjectId(request_id)}, {"$set": {"status": "approved"}})
    return redirect(url_for('manager_dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
