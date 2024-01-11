from flask import Flask, jsonify, request
from models.TaxiModel import TaxiModel

app = Flask(__name__)
ROWS_PER_PAGE=20
    
@app.get('/api/taxis/')
def get_taxis():
  try:     
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", ROWS_PER_PAGE, type=int)
    taxis = TaxiModel.get_taxis(page, per_page)
    response = {
        'taxis': taxis,
        'count': len(taxis)
    }   
    return jsonify(response)
  except Exception as ex:
        return jsonify({'message': str(ex)}), 500