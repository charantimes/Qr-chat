#from distutils import debug
from tkinter import Image
from flask import Flask, request, render_template
from text import Generate


app=Flask(__name__)

@app.route("/")
@app.route("/index", methods =("GET", "POST"))
def Gene():
    if request.method=="POST":
         message = request.form.get('text')
         Generate(
            message
        )
       
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)


