import os
from formspj import AddForm, OwnerForm, ToyForm, DelForm
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    toys = db.relationship('Toys', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):


        ### Toy section ###
        if self.owner and self.toys:
            return f"Puppy name is {self.name} and the owner is {self.owner.name}. It has a toy {self.toys.item_name}"
        elif self.owner and not self.toys:
            return f"Puppy name is {self.name} and the owner is {self.owner.name}. It has no toys."
        elif self.toys and not self.owner:
            return f"Puppy name is {self.name} and has no owner yet. It has a toy {self.toys.item_name}"
        else:
            return f"Puppy name is {self.name} and has no owner and no toys."

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

### Toy section ###
class Toys(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

@app.route('/')
def index():
    return render_template('homepj.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)

        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('addpj.html', form=form)

@app.route('/owner', methods=['GET','POST'])
def add_owner():

    form = OwnerForm()

    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.id.data

        new_owner = Owner(name, puppy_id)

        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('ownerpj.html', form=form)

### Toy section ###
@app.route('/toys', methods=['GET', 'POST'])
def add_toys():

    form = ToyForm()

    if form.validate_on_submit():

        item_name = form.item_name.data.lower()
        puppy_id = form.id.data

        new_toy = Toys(item_name, puppy_id)

        db.session.add(new_toy)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('toypj.html', form=form)

@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('listpj.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data

        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('deletepj.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
