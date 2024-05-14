from typing import Optional
from datetime import datetime
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException, BadRequest # NotFound, InternalServerError
from .models import taxis
from .models import locations
from .config import Config

DEFAULT_PAGE = 1
ROWS_PER_PAGE = 20

def create_app(cfg: Optional[Config] = None) -> Flask:
    if cfg is None:
        cfg = Config()

    app = Flask(__name__)
    app.config.from_object(cfg)

    @app.route("/api/taxis/", methods=["GET"])
    def get_taxis():
        """Endpoint to get list of taxis
        """
        page = request.args.get("page", DEFAULT_PAGE, type=int)
        per_page = request.args.get("per_page", ROWS_PER_PAGE, type=int)
        taxis_response = taxis.get(page, per_page)
        response = taxis_response
        return jsonify(response)

    @app.route("/api/taxis/<int:taxi_id>/locations/", methods=["GET"])
    def get_locations_by_taxi_id(taxi_id):
        """Endpoint to get list of locations for a specific taxi
        """
        # how do we require taxi_id?
        # pdb.set_trace()
        date = request.args.get("date", None, type=str) # date format yyyy-MM-dd
        if date is None:
            return handle_exception(BadRequest("Missing date parameter"))
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return handle_exception(BadRequest("Invalid date format, use yyyy-MM-dd"))

        page = request.args.get("page", DEFAULT_PAGE, type=int)
        per_page = request.args.get("per_page", ROWS_PER_PAGE, type=int)
        results = locations.get_locations_by_taxi_id(taxi_id, page, per_page, date)
        return jsonify(results)

    # https://code-maven.com/python-flask-catch-exception
    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            return jsonify({ 'message': e.description }), e.code
        return jsonify({ 'message': str(e) }), 500

    return app

if __name__ == "__main__":
    taxi_app = create_app()
    taxi_app.run()
