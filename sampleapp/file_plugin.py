import inspect
from bottle import HTTPError, PluginError

class FileConnector:
    def __init__(self) -> None:
        pass

    def upload(self, data, path):
        '''
        Upload the file to the adls
        '''
        print(f'uploading file to the {data} to the path {path}') 

class FilePlugin(object):
    ''' This plugin passes an sqlite3 database handle to route callbacks
    that accept a `db` keyword argument. If a callback does not expect
    such a parameter, no connection is made. You can override the database
    settings on a per-route basis. '''

    name = 'file'
    api = 2

    def __init__(self, keyword='df'):
         self.keyword = keyword

    def setup(self, app):
        ''' Make sure that other installed plugins don't affect the same
            keyword argument.'''
        for other in app.plugins:
            if not isinstance(other, FilePlugin): continue
            if other.keyword == self.keyword:
                raise PluginError("Found another Adls plugin with "\
                "conflicting settings (non-unique keyword).")

    def apply(self, callback, context):
        # Override global configuration with route-specific values.
        conf = context.config.get('file') or {}
        config = context.config()
        keyword = conf.get('keyword', self.keyword)
        file_type = config.get('connect_type','')


        # Test if the original callback accepts a 'db' keyword.
        # Ignore it if it does not need a database handle.
        args = inspect.getargspec(context.callback)[0]
        if keyword not in args:
            return callback
        
        if file_type and file_type != 'FILE':
            return callback

        def wrapper(*args, **kwargs):
            # Connect to the adls
            df = FileConnector()
            print('File connector connected')
            # Add the connection handle as a keyword argument.
            kwargs[keyword] = df
            kwargs['file'] = df

            try:
                rv = callback(*args, **kwargs)

            except Exception as e:
                raise HTTPError(' Error occurred in adls plugin')
            return rv

        # Replace the route callback with the wrapped one.
        return wrapper