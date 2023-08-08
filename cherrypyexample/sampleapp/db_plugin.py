from cherrypy.process import plugins, wspbus
import cherrypy

class DatabasePlugin(plugins.SimplePlugin):
    def __init__(self, bus, db_klass):
        plugins.SimplePlugin.__init__(self, bus)
        self.db= db_klass

    def start(self):
        self.bus.log('Starting up DB process')
        self.bus.subscribe("db-save", self.saveit)
    
    def stop(self):
        self.bus.log('Stopping DB process')
        self.bus.unsubscribe("db-save", self.saveit)
    
    def saveit(self, entity):
        cherrypy.log('saved successfully')
        self.db.save(entity.cart_data)