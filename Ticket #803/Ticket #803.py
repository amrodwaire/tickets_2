from flask import Flask
import requests
import jsonify
app = Flask(__name__)
@app.route("/weather")
def weather():

    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"error": "City name cannot be empty"}),404
    elif not city.isalpha():
        return jsonify({"error": "City name must contain letters only"}),404
    else:
     return jsonify ({"message": f"Sunny in {city}"})
if __name__ == "__main__":
    app.run(debug=True)