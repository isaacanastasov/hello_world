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
            'name': self.request.get('student_name'),
            'university': self.request.get('university')
        }
        template = jinja_env.get_template('templates/students.html')
        logging.info('StudentPage')
        # Step 3 Use the jinja Environment to get our file
        self.response.write(template.render(template_vars))


class AllStudents(webapp2.RequestHandler):
    def get(self):
        cssi = [
        {"name":"Asia", "university":"SDSU"},
        {"name":"Taylor", "university":"Stanford"},
        ]
        template_vars = {
            'cssi': cssi,
        }
        template = jinja_env.get_template('templates/all_students.html')
        logging.info('all students')
        self.response.write(template.render(template_vars))

# class AboutPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Isaac Anastasoff, 2019')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/student', StudentPage),
    ('/all_students', AllStudents),
    # ('/FamBam', FamBam)
], debug = True)
