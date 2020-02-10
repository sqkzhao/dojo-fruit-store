from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html", strawberry=int(request.form['strawberry']), raspberry=int(request.form['raspberry']), apple=int(request.form['apple']), blackberry=int(request.form['blackberry']),
    first=request.form['first_name'], last=request.form['last_name'], id=request.form.get('student_id'), now=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    