from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello puppy</h1>"

@app.route('/information')
def info():
	return "<h1>puppies are cute and awesome</h1>"

@app.route('/information/<name>')
def individual(name):
    if name.endswith('y'):
        name = name.replace("y","iful")
    else:
        if name.endswith('y') == False:
            name[:-1] = 'y'
    return "<h1>This page belongs to:{}</h1>".format(name)
    
if __name__=="__main__":
    app.run(debug=True)
