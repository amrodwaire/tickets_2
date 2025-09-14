from flask import Flask
import requests
import jsonify
app = Flask(__name__)
@app.route("/weather")
def weather_1():
    city = request.args["city"]
    if not city:
        return jsonify({"error": "Please enter a city"}),404
    data={city:"city","weather":weather}
    return jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)