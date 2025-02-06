from flask import Flask, jsonify, request
from modules.load_model import load_model
from utils.utils import check_folder
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

check_folder("models")

model = load_model("./models/vehicle_regression_model.joblib")
label_encoders = load_model("./models/label_encoders.joblib")


@app.route("/api/", methods=["GET"])
def index():
    """
    Returns API information.
    ---
    tags:
      - API Info
    responses:
      200:
        description: API status and details
        schema:
          type: object
          properties:
            status:
              type: string
              example: "API is running"
            description:
              type: string
              example: "Vehicle prediction API using a machine learning model"
            version:
              type: string
              example: "1.0.0"
            creation_date:
              type: string
              example: "2024-10-25"
            technologies:
              type: array
              items:
                type: string
              example: ["Python 3.x", "Flask"]
            endpoints:
              type: object
              properties:
                /api/:
                  type: string
                  example: "API information (GET)"
                /api/predict/:
                  type: string
                  example: "Vehicle prediction (POST)"
    """
    return jsonify(
        {
            "status": "API is running",
            "description": "Vehicle prediction API using a machine learning model",
            "version": "1.0.0",
            "creation_date": "2024-10-25",
            "technologies": ["Python 3.x", "Flask"],
            "endpoints": {
                "/api/": "API information (GET)",
                "/api/predict/": "Vehicle prediction (POST)",
            },
        }
    )


@app.route("/api/predict", methods=["POST"])
def predict():
    """
    Predicts the number of vehicles based on input parameters.
    ---
    tags:
      - Prediction
    parameters:
      - name: zip_code
        in: query
        type: string
        required: true
        description: Postal code of the region
      - name: model_year
        in: query
        type: integer
        required: true
        description: Vehicle model year
      - name: fuel
        in: query
        type: string
        required: true
        description: Type of fuel used
      - name: make
        in: query
        type: string
        required: true
        description: Vehicle manufacturer
      - name: duty
        in: query
        type: string
        required: true
        description: Type of vehicle duty
    responses:
      200:
        description: Prediction result
        schema:
          type: object
          properties:
            status:
              type: string
              example: "success"
            predict:
              type: float
              example: 1234.56
      400:
        description: Invalid input parameters
        schema:
          type: object
          properties:
            error:
              type: string
              example: "All parameters (zip_code, model_year, fuel, make, duty) are required."
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Error while making the prediction."
    """
    zip_code = request.args.get("zip_code")
    model_year = request.args.get("model_year")
    fuel = request.args.get("fuel")
    make = request.args.get("make")
    duty = request.args.get("duty")

    if not all([zip_code, model_year, fuel, make, duty]):
        return (
            jsonify(
                {
                    "error": "All parameters (zip_code, model_year, fuel, make, duty) are required."
                }
            ),
            400,
        )

    try:
        args = [
            int(model_year),
            label_encoders["ZIP Code"].transform([zip_code])[0],
            label_encoders["Fuel"].transform([fuel])[0],
            label_encoders["Make"].transform([make])[0],
            label_encoders["Duty"].transform([duty])[0],
        ]
    except KeyError as e:
        return jsonify({"error": f"Invalid parameter: {str(e)}"}), 400
    except Exception as e:
        return (
            jsonify({"error": f"Error while processing input parameters: {str(e)}"}),
            500,
        )

    try:
        prediction = model.predict([args])[0]
        return jsonify({"status": "success", "predict": prediction}), 200
    except Exception as e:
        return jsonify({"error": f"Error while making the prediction: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=3000, debug=True)
