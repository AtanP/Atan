from google.appengine.ext import db

class Word(db.Model):
    spelling = db.StringProperty()
    meaning = db.StringProperty()
