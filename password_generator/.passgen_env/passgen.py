from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.form.get('length', type=int)
    if not length or length < 8 or length > 16:
        flash('Password length must be between 8 and 16 characters.', 'error')
        return redirect(url_for('index'))
    
    charachters = string.ascii_letters + string.digits
    passwd = ''.join(random.choice(charachters) for _ in range(length))
    flash(f'Generated Password: {passwd}', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)