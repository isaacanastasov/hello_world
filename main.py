import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('In Main Page')
        self.response.write('hello_world')

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is the secret entrance to the page')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Isaac Anastasoff, 2019')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secretentrance', SecretPage),
    ('/aboutpage', AboutPage),
], debug = True)
