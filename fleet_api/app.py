from flask import Flask, jsonify, request
from typing import Optional
from .config import Config
from .models.Taxis import TaxiModel
# import pdb

ROWS_PER_PAGE = 20


def create_app(cfg: Optional[Config] = None) -> Flask:
    if cfg is None:
        cfg = Config()
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
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
