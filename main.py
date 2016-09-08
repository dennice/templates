import os
import webapp2



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write.out(*a, **kw)

class MainPage(Handler):
    def get(self):
        self.write("Hello, Owlrd")

        
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
