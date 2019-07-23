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
        logging.info('Program Good')
        # Step 3 Use the jinja Environment to get our file
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class StudentPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'name': 'Mayra',
        }
        template = jinja_env.get_template('templates/students.html')
        logging.info('StudentPage')
        # Step 3 Use the jinja Environment to get our file
        self.response.write(template.render(template_vars))
#
# class SecretPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('This is the secret entrance to the page')
#
# class AboutPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Isaac Anastasoff, 2019')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/students', StudentPage),
    # ('/aboutpage', AboutPage),
    # ('/FamBam', FamBam)
], debug = True)
