"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, redirect, render_template, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake
from forms import AddCupcakeForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ECHO'] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SECRET_KEY'] = "SECRET!"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def show_cupcakes():
    return render_template('index.html')


@app.route("/add-cupcake", methods= ['GET', 'POST'])
def new_cupcake_form():
    form = AddCupcakeForm()
    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating= form.rating.data
        image = form.image.data

        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

        db.session.add(cupcake)
        db.session.commit()

        flash (f"Added {flavor} to menu.")

        return redirect ("/")
    else:
        return render_template('new-cupcake-form.html', form=form)

    return render_template('index.html')
    


@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return JSON {'cupcakes': [{id, flavor, size, rating, image}]}"""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(all_cupcakes)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Returns JSON of ONE user specified cupcake"""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake = cupcake.serialize())


@app.route("/api/cupcakes", methods=['POST'])
def create_cupcake():
    """Creates a new cupcake and returns JSON of that created cupcake"""

    new_cupcake = Cupcake(flavor = request.json['flavor'], size = request.json['size'], rating = request.json['rating'], image=request.json['image'])

    print('******************************')
    print(new_cupcake)
    print('******************************')

    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)


@app.route("/api/cupcakes/<int:id>", methods=['PATCH'])
def update_cupcake(id):
    """updates a cupcake and returns JSON of that updated cupcake"""

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=['DELETE'])
def delete_cupcake(id):
    """updates a cupcake and returns JSON of that updated cupcake"""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='deleted')
