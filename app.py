from flask import Flask
app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return "starting a machine learning program"

if __name__=="__main__":
    app.run(debug=True)