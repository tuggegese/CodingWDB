from flask import Response


def configure_routes(api):
    @api.route('/', methods=['GET'])
    @api.route('/home', methods=['GET'])
    def home() -> Response:
        response: str = "Hello there, API is up"
        return Response(response, status=200, mimetype="text/html")
