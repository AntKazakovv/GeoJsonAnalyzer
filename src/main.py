from flask import Flask, jsonify, request
import geo_tools

app = Flask(__name__)

@app.route("/geo/analyze", methods=["POST"])
def hello():
    input_json_dict = request.get_json(force=True)
    string_geo_json = str(input_json_dict).replace("'", '"')
    return geo_tools.getNumberObjects(geo_tools.toGeoJson(string_geo_json))

if __name__ == "__main__":
    app.run()