from myproject import db

class Restaurants(db.Model):

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    stars = db.Column(db.Integer, index=True)
    review_count = db.Column(db.Integer, index=True)
    new_cat = db.Column(db.String(128), index=True)
    address = db.Column(db.String(128), index=True)
    cuisine = db.Column(db.String(32), index=True)
    new_postal = db.Column(db.String(32), index=True)
    new_time = db.Column(db.String(32), index=True)

    def __init__(self, id, name, stars, review_count, new_cat, address, cuisine, new_postal, new_time):
        self.id = id
        self.name = name
        self.stars = stars
        self.review_count = review_count
        self.new_cat = new_cat
        self.address = address
        self.cuisine = cuisine
        self.new_postal = new_postal
        self.new_time = new_time
