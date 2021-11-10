import os

from waitress import serve

from src import api
from routes import configure_routes

configure_routes(api)

if __name__ == '__main__':
    serve(api, host=os.environ.get("API_HOST", "0.0.0.0"), port=os.environ.get("API_PORT", "8080"))
