from flask import Flask, render_template, request
from model import movies_recommend
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/result',methods = ["GET","POST"])
def result_page():
    if request.method == "POST":
        movie_name = request.form["movie_name"]
        res=movies_recommend(movie_name)
        return res




@app.route('/about_us')
def abus():
    
    return 'This is About Page'



app.run(debug=True)