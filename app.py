from flask import Flask, request, render_template, redirect
#from googlesearch import google

app = Flask(__name__)

@app.get("/")
def index():
    # TODO: Render the home page provided under templates/index.html in the repository
    # return "TODO"
      return render_template("index.html")

@app.get("/search")
def search():
	# TODO:
	# 1. Capture the word that is being searched
	# 2. Seach for the word on Google and display results
    # return "TODO"
    args = request.args.get("q")
    return redirect("https://www.google.com/search?q={args}".format(args=args))

@app.get("/firstlink")
def firstlink():
    args = request.args.get("f")
    return redirect("https://www.google.com/search?btnI=I&q={args}".format(args=args))

if __name__ == "__main__":
    app.run()