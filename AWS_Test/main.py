from src import api
from src.routes import configure_routes

configure_routes(api)

if __name__ == '__main__':
    print("Starting API...")
    api.run(host="0.0.0.0", port=8080, debug=True)
