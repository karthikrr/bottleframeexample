from typing import Any
import cherrypy
from db_plugin import DatabasePlugin

class Cart:
    def __init__(self, cart_data):
        self.cart_data = cart_data

class SampleDB:
    data =[]
    def __init__(self) -> None:
        pass

    def list(self):
        print(self.data)
        return ','.join(self.data)

    def save(self, cart_data):
        self.data.append(cart_data) 


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World !!!!'
    
class Ecommerce(object):
    @cherrypy.expose
    def save_kart(self, cart_data):
        cart = Cart(cart_data)
        cherrypy.engine.publish('db-save', cart)
        return 'Saved successfully!!!'
    
    @cherrypy.expose
    def list_kart(self):
        db = SampleDB()
        print(db.list())
        return db.list()



if __name__ == '__main__':
    cherrypy.tree.mount(HelloWorld(),'/hello')
    cherrypy.tree.mount(Ecommerce(),'/com/')
    #cherrypy.quickstart(HelloWorld(),'/')
    DatabasePlugin(cherrypy.engine, SampleDB()).subscribe()
    #cherrypy.quickstart(Ecommerce(),'/save')
    cherrypy.engine.start()
    cherrypy.engine.block()
    DatabasePlugin(cherrypy.engine, SampleDB()).unsubscribe()