import web
import random
import serialsend

urls = (
        '/', 'index',
        )
render = web.template.render('templates/', base='layout')

'''
used to display a simple form using HTML5 
x-webkit-speech to. post data is then sent
to serialsend.py which acts as a middleman between
python and the micro-controller.
'''
class index():
    def GET(self):
        return render.index('hey')
    
    def POST(self):
        p = web.input()
        serialsend.input(p.talk)
        
if __name__ == "__main__":
   app = web.application(urls, globals())
   app.internalerror = web.debugerror
   app.run() 


