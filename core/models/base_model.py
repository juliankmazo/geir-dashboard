from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    # We extend all the models from this one because they all
    # have the same structure
    name = ndb.StringProperty()
    code = ndb.StringProperty()
    column = ndb.IntegerProperty()
    value = ndb.FloatProperty()
    updated = ndb.StringProperty()
    dayVariation = ndb.FloatProperty()
    monthVariation = ndb.FloatProperty()
    yearVariation = ndb.FloatProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    timeStamp = ndb.DateTimeProperty(auto_now=True)
