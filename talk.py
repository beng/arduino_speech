import web
import random

urls = (
        '/', 'index',
        )
render = web.template.render('templates/', base='layout')

class index():
    def GET(self):
        return render.index('hey')
    
    def POST(self):
        p = web.input()
        print p.talk
        
if __name__ == "__main__":
   app = web.application(urls, globals())
   app.internalerror = web.debugerror
   app.run() 


