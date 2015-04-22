from core.controllers import MainPageController
from core.controllers import TaskUpdateInformationController
import webapp2


app = webapp2.WSGIApplication([
    ('/', MainPageController),
    ('/tasks/update-info', TaskUpdateInformationController)

], debug=True)
