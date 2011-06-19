from os.path import dirname, join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from app.models.word import Word

class Words(webapp.RequestHandler):
    def get(self):
        words_query = Word.all()
        words = words_query.fetch(1000)

        template_values = {'words': words}

        path = join(dirname(dirname(dirname(__file__))), 'template', 'words.html')
        self.response.out.write(template.render(path,template_values))

    def post(self):
        content = self.request.get('content')
        for line in content.split('\n'):
            spelling, meaning = line.split(',')

            word = Word()
            word.spelling = spelling
            word.meaning = meaning

            word.put()

        self.redirect('/words')
