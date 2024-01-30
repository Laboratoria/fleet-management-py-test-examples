from typing import Optional
from flask import Flask, jsonify, request
from .config import Config
from .models.taxis import TaxiModel
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
            taxis = TaxiModel.get_taxis(page, per_page)
            response = {"taxis": taxis, "count": len(taxis)}
            return jsonify(response)
        # pylint: disable=broad-except
        except Exception as ex:
            # pylint: disable=raise-missing-from
            return jsonify({"message": str(ex)}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
