try:
    from flask import Flask,render_template,redirect,url_for
    from forms import AddForms, DelForms
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
    import os
    print("All libraries imported")
except ImportError as e:
    print(e)

###initiating the app
app = Flask(__name__)

##for forms, importing the secret key 
app.config['SECRET_KEY'] = 'mysecretkey'

####################################
######### DB part ##################
####################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


####setting up the database and migration class

db = SQLAlchemy(app)
Migrate(app,db)




#########################################
##### Creating the model ################
#########################################


## we will just have one model for this project

class Puppy(db.Model):

    __tablename__='pups'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name is {self.name}"

###########################################
########### VIEW FUNCTIONS: FORMS #########
###########################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():
    forms=AddForms()
    if forms.validate_on_submit():
        name = forms.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('add.html',forms=forms)

@app.route('/list')
def list_pup():
    list_pup=Puppy.query.all()
    return render_template('list.html',list_pup=list_pup)

@app.route('/delete',methods=['POST'])
def del_pup():
    forms=DelForms()
    if forms.validate_on_submit():
        id=forms.id.data
        puppies=Puppy.query.get(id)
        db.session.delete(puppies)

        return redirect(url_for('list_pup'))
    return render_template('delete.html',forms=forms)

if __name__=="__main__":
    app.run(debug=True)

