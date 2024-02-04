from typing import Optional
from flask import Flask, jsonify, request
from .config import Config
from .models import taxis
from .models.locations import get_locations

# import pdb

ROWS_PER_PAGE = 20


def create_app(cfg: Optional[Config] = None) -> Flask:
    if cfg is None:
        cfg = Config()
    # pylint: disable=redefined-outer-name
    app = Flask(__name__)
    app.config.from_object(cfg)

    @app.route("/api/taxis/", methods=["GET"])
    def get_taxis():
        try:
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", ROWS_PER_PAGE, type=int)
            taxis_response = taxis.get(page, per_page)
            response = {"taxis": taxis_response, "count": len(taxis_response)}
            return jsonify(response)
        # pylint: disable=broad-except
        except Exception as ex:
            # pylint: disable=raise-missing-from
            return jsonify({"message": str(ex)}), 500

    @app.route("/api/locations/", methods=["GET"])
    def get_locations_by__taxi_id():
        try:
            taxi_id = request.args.get("taxi_id", 1, type=int)
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", ROWS_PER_PAGE, type=int)
            locations = get_locations(taxi_id, page, per_page)
            return jsonify(locations)
        # pylint: disable=broad-except
        except Exception as ex:
            # pylint: disable=raise-missing-from
            return jsonify({"message": str(ex)}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
