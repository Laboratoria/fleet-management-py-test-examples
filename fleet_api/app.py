from typing import Optional
import json
import yaml
from flask import Flask, jsonify, request

from .config import Config
from .models import taxis
from .models.locations import get_locations
from .spec import spec

ROWS_PER_PAGE = 20

def create_app(cfg: Optional[Config] = None) -> Flask:
    if cfg is None:
        cfg = Config()
    # pylint: disable=redefined-outer-name
    app = Flask(__name__)
    app.config.from_object(cfg)

    @app.route("/api/taxis/", methods=["GET"])
    def get_taxis():
        """Endpoint to get list of taxis
        ---
        get:
          description: Get taxi list
          responses:
            200:
              description: Returns the list of taxis
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      taxis:
                        type: array
                        items:
                          $ref: '#/components/schemas/TaxiModel'
                      count:
                        type: integer
        """
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
        """Endpoint to get list of locations for a specific taxi
        ---
        get:
          description: Get locations list
          responses:
            200:
              description: Return locations list for a specific taxi
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      locations:
                        type: array
                        items:
                          $ref: '#/components/schemas/LocationsModel'
        """
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

    # Register the path and the entities within it
    # Since path inspects the view and its route,
    # we need to be in a Flask request context
    with app.test_request_context():
        spec.path(view=get_taxis)
        spec.path(view=get_locations_by__taxi_id)
    # Both .yaml & .json files are being generated but we
    # are aware we just need one of them
    with open("swagger.yaml", "w", encoding="utf-8") as file:
        yaml.dump(spec.to_yaml(), file, line_break="\n", indent=4)
    with open("swagger.json", "w", encoding="utf-8") as file:
        json.dump(spec.to_dict(), file)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
