import webapp2
import os
import jinja2
from core.helpers import BaseHelper
# Configuring the jinja2 template enviroment
template_dir = os.path.join(os.path.dirname("geir-dashboard"), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)
# Function used in the template to change a float to the percentage form
jinja_env.filters['percentage'] = BaseHelper.float2percentage
# Function used in the template to format the currency values
jinja_env.filters['currency'] = BaseHelper.format_currency


def render_str(template, **params):
    # Function to get the template and render it
    j = jinja_env.get_template(template)
    return j.render(params)


class BaseController(webapp2.RequestHandler):
    # We extend all the controllers from here. This functions are used to
    # render the templates
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
