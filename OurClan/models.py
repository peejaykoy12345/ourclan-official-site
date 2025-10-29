from OurClan import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    townhall_level = db.Column(db.Integer, nullable=False)
    trophies = db.Column(db.Integer, nullable=False)
    donations = db.Column(db.Integer, nullable=False)
    is_leader = db.Column(db.Boolean, default=False)
    is_coleader = db.Column(db.Boolean, default=False)
    is_elder = db.Column(db.Boolean, default=False)
