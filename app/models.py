from . import db

class PropertyProfile(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    ptitle = db.Column(db.String(255))
    pdescription = db.Column(db.String(255))
    rooms = db.Column(db.String(255))
    bathrooms = db.Column(db.String(255))
    price = db.Column(db.String(255))
    ptype = db.Column(db.String(255))
    location = db.Column(db.String(255))
    filename = db.Column(db.String(500))

    def __init__(self,ptitle,pdescription,rooms,bathrooms,price,ptype,location,filename):
        self.ptitle = ptitle
        self.pdescription = pdescription
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.ptype = ptype
        self.location = location
        self.filename = filename

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)