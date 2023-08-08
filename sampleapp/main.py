from bottle import Bottle, run, route,install,template, HTTPError,request
from timer_plugin import stopwatch
from sqlite_plugin import SQLitePlugin
from adls_plugin import AdlsPlugin
from file_plugin import FilePlugin
import settings



# Create the main Bottle application instance
app = Bottle()

sqlite = SQLitePlugin(dbfile='D:/test.db')
adls = AdlsPlugin()
fileplug  = FilePlugin()

# install(stopwatch)
app.install(stopwatch)
app.install(sqlite)
app.install(adls)
app.install(fileplug)

@app.route('/config', method='POST')
def set_app_config():
    data = request.json
    print(data)
    app.config.update(data)
    return data

@app.route('/hello')
def start_hello():
    return {"a":'Hello world!'}

@app.route('/connect/adls')
def connect_ad(adls):
    adls.upload('file.txt', 'D://1212')
    return {'a':'adls connected'}

@app.route('/connect/filesystem', connect_type=settings.FILE_TYPE)
def connect_ad(df):
    df.upload('file.txt', 'D://1212')
    return {'a':'adls connected'}

@app.route('/connect/file')
def connect_ad(file):
    file.upload('file.txt', 'D://1212')
    return {'a':'file connected'}

@app.route('/show/<page>')
def show(page, db):
    row = db.execute('SELECT * from pages where name=?', page).fetchone()
    if row:
        return template('showpage', page=row)
    return HTTPError(404, "Page not found")

@app.route('/start')
def start_app():
    run(app=app)



@app.route('/close')
def close_application():
    app.close()
    return {'a':'application closed'}

#app.run()
run(app=app, reloader=True)
