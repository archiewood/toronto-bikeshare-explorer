from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def home():
    return render_template( '<H1> Hello World!</H1>' )
