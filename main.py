import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        # logging.info('In helllo handler')
        self.response.write('<b> hello </b> world <br> This is a great program')
        self.response.write('<ul> <li> this is a bullet <li> We the best <li> rock paper scisors')
        self.response.write('</ul>')

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
