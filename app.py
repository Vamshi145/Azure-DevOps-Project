from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Azure DevOps Pipeline for App Service : Vamshi krishna </h2>'

if __name__ == "__main__":
    app.run(debug=True)
