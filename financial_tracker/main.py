from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Finansial tracker app"

@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return f"Login page with username: {request.form['username']} and password: {request.form['password']}"

@app.route('/register', methods=['GET','POST'])
def register_page():
        if request.method =='POST':
            return f"Register page with name: {request.form['name']}\nemail: {request.form['email']}\n username: {request.form['username']}\n and password: {request.form['password']}"
        elif request.method == 'GET':
            return render_template('register.html')

@app.route("/user", methods=['GET', 'DELETE'])
def user_page():
    if request.method == 'DELETE':
        return "Delete user"
    elif request.method == 'GET':
        return "Get user"


@app.route('/category', methods=['POST', 'GET'])
def get_all_category():
    if request.method == 'DELETE':
        return "Delete category"
    elif request.method == 'GET':
        return "Get category"

@app.route('/category/<int:category_id>', methods=['GET', 'POST'])
def get_category(category_id):
    if request.method == 'GET':
        return render_template('category.html')
    else:
        method_from_request = request.form['method']
        if method_from_request == 'DELETE':
            return f"Delete category with ID: {category_id}"
        elif method_from_request == 'PATCH':
            return f"Update category with ID: {category_id}"
        else:
            return "Invalid method"

@app.route('/income', methods=['POST', 'GET'])
def get_all_income():
    if request.method == 'DELETE':
        return "post income"
    elif request.method == 'GET':
        return "Get income"

@app.route('/income/<int:income_id>', methods=['Get', 'DELETE', 'PATCH'])
def get_income_id(income_id):
    if request.method == 'GET':
        return f"Income page for ID: {income_id}"
    elif request.method == 'DELETE':
        return f"Delete income with ID: {income_id}"
    elif request.method == 'PATCH':
        return f"Update income with ID: {income_id}"
    
    
@app.route('/expense', methods=['POST', 'GET'])
def get_all_expense():
    if request.method == 'DELETE':
        return "post expense"
    elif request.method == 'GET':
        return "Get expense"
    
@app.route('/expense/<int:expense_id>', methods=['Get', 'DELETE', 'PATCH'])
def get_expense_id(expense_id):
    if request.method == 'GET':
        return f"Income page for ID: {expense_id}"
    elif request.method == 'DELETE':
        return f"Delete income with ID: {expense_id}"
    elif request.method == 'PATCH':
        return f"Update income with ID: {expense_id}"


 



if __name__ == '__main__':
    app.run(debug=True)