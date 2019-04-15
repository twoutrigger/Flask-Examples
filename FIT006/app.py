from myproject import app, db
from flask import render_template, redirect, request, url_for, session
from hashlib import md5, sha1, sha256, sha512
from myproject.models import Restaurants
from myproject.forms import EntryForm, HashForm

@app.route('/', methods=['GET', 'POST'])
def data_entry():

    form = EntryForm()

    if form.validate_on_submit():

        session['area'] = form.area.data
        session['cuisine'] = form.cuisine.data
        session['diningtime'] = form.diningtime.data

        return redirect(url_for('result'))

    return render_template('data_entry.html', form=form)

@app.route('/result')
def result():

    restaurant_1 = Restaurants.query.filter(Restaurants.new_time.like(session['diningtime']),
                                            Restaurants.new_postal.like(session['area']),
                                            Restaurants.cuisine.like(session['cuisine']))[0]

    session['r1name'] = str(restaurant_1.name)
    session['r1cuisine'] = str(restaurant_1.cuisine).capitalize()
    session['r1stars'] = str(restaurant_1.stars)
    session['r1address'] = str(restaurant_1.address)

    restaurant_2 = Restaurants.query.filter(Restaurants.new_time.like(session['diningtime']),
                                            Restaurants.new_postal.like(session['area']),
                                            Restaurants.cuisine.like(session['cuisine']))[1]

    session['r2name'] = str(restaurant_2.name)
    session['r2cuisine'] = str(restaurant_2.cuisine).capitalize()
    session['r2stars'] = str(restaurant_2.stars)
    session['r2address'] = str(restaurant_2.address)

    restaurant_3 = Restaurants.query.filter(Restaurants.new_time.like(session['diningtime']),
                                            Restaurants.new_postal.like(session['area']),
                                            Restaurants.cuisine.like(session['cuisine']))[2]

    session['r3name'] = str(restaurant_3.name)
    session['r3cuisine'] = str(restaurant_3.cuisine).capitalize()
    session['r3stars'] = str(restaurant_3.stars)
    session['r3address'] = str(restaurant_3.address)

    restaurant_4 = Restaurants.query.filter(Restaurants.new_time.like(session['diningtime']),
                                            Restaurants.new_postal.like(session['area']),
                                            Restaurants.cuisine.like(session['cuisine']))[3]

    session['r4name'] = str(restaurant_4.name)
    session['r4cuisine'] = str(restaurant_4.cuisine).capitalize()
    session['r4stars'] = str(restaurant_4.stars)
    session['r4address'] = str(restaurant_4.address)

    return render_template('result.html')

@app.route('/hash', methods=['GET', 'POST'])
def hash_entry():

    form = HashForm()

    if form.validate_on_submit():

        session['password_input'] = form.password_input.data
        session['hash_type'] = form.hash_type.data
        session['hash_label'] = form.hash_type.data

        return redirect(url_for('hash_result'))

    return render_template('hash_entry.html', form=form)

@app.route('/hash_result')
def hash_result():

    if session['hash_type'] == 'MD5':

        hash_returned = md5(session['password_input'].encode())
        session['secure_text'] = 'Weak'
        session['secure_color'] = 'red'

    elif session['hash_type'] == 'SHA-1':

        hash_returned = sha1(session['password_input'].encode())
        session['secure_text'] = 'Weak'
        session['secure_color'] = 'red'

    elif session['hash_type'] == 'SHA-256':

        hash_returned = sha256(session['password_input'].encode())
        session['secure_text'] = 'Strong'
        session['secure_color'] = 'green'

    elif session['hash_type'] == 'SHA-512':

        hash_returned = sha512(session['password_input'].encode())
        session['secure_text'] = 'Strong'
        session['secure_color'] = 'green'

    session['hash_in_bytes'] = str(hash_returned.digest())
    session['hash_in_hex'] = str(hash_returned.hexdigest())
    session['hash_digest_size'] = str(hash_returned.digest_size)

    return render_template('hash_result.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=80)
