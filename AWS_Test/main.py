from waitress import serve

from src import api
from src.routes import configure_routes

configure_routes(api)

if __name__ == '__main__':
    print("Starting API...")
    serve(api, host="0.0.0.0", port=8080)
