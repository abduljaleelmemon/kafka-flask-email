from datetime import datetime
from app import *

class email_db(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    sender = db.Column(db.String)
    website = db.Column(db.String)
    recipient = db.Column(db.String)
    status = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, sender=None, website=None, recipient=None, status=None, time= datetime.utcnow):
        self.sender = sender
        self.website = website
        self.recipient = recipient
        self.status = status
        self.time = time