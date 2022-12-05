from flask import Flask
from flask_restful import Resource, Api
from flask_caching import Cache
import time

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_TYPE": 'redis',
    "CACHE_REDIS_HOST": 'RedisCache',
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": 'redis://localhost:6379',
    "CACHE_DEFAULT_TIMEOUT": 500,
}

app = Flask(__name__)
api = Api(app)
app.config.from_mapping(config)
cache = Cache(app)


class HelloWorld(Resource):

    @cache.memoize(timeout=30)
    def get(self, id):
        time.sleep(5)
        if id == 1:
            return {'hello': 'world'}
        else:
            return {'hello': 'no'}


api.add_resource(HelloWorld, '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
