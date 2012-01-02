from google.appengine.ext import webapp
from google.appengine.api import users
from app.models.word import WordList

def getWordList(user,id):
    query = WordList.all()
    query = query.filter('key =', id)
    query = query.filter('user =', user)

    return query.get()

# FIXME: should extract out API request handler class from handlers below

class MakeWordList(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()

        wordlist = WordList(owner=user)
        wordlist.put()

        self.response.headers['Content-Type'] = 'application/json'
        # FIXME: should use JSON printer
        self.response.out.write('{"ListId": "%s"}' % wordlist.key())

class EditList(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        listid = self.request.get('ListId')
        listname = self.request.get('ListName')

        wordlist = getWordList(user, listid)
        if wordlist:
            wordlist.name = listname
            wordlist.put()
        else:
            pass                # FIXME: error should be reported

class DeleteList(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        listid = self.request.get('ListId')

        wordlist = getWordList(user, listid)
        if wordlist:
            wordlist.delete()
        else:
            pass                # FIXME: error should be reported

class AddWord(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        listid = self.request.get('ListId')
        wordid = self.request.get('WordId')

        wordlist = getWordList(user, listid)
        if not wordlist:
            pass                # FIXME: error should be reported

        query = Word.all()
        query = query.filter('key =', wordid)
        word = query.get()

        if word:
            wm = WordMember(wordlist=wordlist, word=word)
            wm.put()
        else:
            pass                # FIXME: error should be reported

class DeleteWord(webapp.RequestHandler):
    def post(self):
        pass

class SearchWords(webapp.RequestHandler):
    # the spec says that it must return [{Word: word, Id: id, Meaning: meaning}]
    # where `id' is a Word key, but probably a WordMember key seems to be
    # more useful.
    def get(self):
        pass
