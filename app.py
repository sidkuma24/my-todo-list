from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route("/")
def main():
	return render_template('index.html')

if __name__=="__main__":
	app.run()