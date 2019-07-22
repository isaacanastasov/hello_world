#Step one is to import Jinja2
import webapp2
import jinja2
import logging
import os
# Step 2 setup the jinja Environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('Program Ran')
        # Step 3 Use the jinja Environment to get our file
        template = jinja_env.get_template('hello.html')
        self.response.write(template.render())
        
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
