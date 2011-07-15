from google.appengine.ext import db
from app.modelsl.word import Word, WordMember, WordList

class StudyingList(db.Model):
    user = db.StringProperty()
    list = db.ReferenceProperty()
    active = db.BooleanProperty()

class Box(db.Model):
    user = db.StringProperty()
    time = db.DateTimeProperty()
    step = db.IntegerProperty()
    word = db.ReferenceProperty(Word)
    list = db.ReferenceProperty(WordList)
    active = db.BooleanProperty()
