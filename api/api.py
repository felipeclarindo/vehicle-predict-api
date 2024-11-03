from flask import Flask, jsonify, request
from modules.load_model import load_model
from utils.utils import check_folder
import os

app = Flask("__main__")

check_folder("models")
model = load_model('./models/vehicle_regression_model.joblib')
label_encoders = load_model('./models/label_encoders.joblib')


@app.route("/api/", methods=["GET"])
def index():
    return jsonify({
        "status": "API is running",
        "description": "API de previsões de veículos por um modelo de machine learning",
        "version": "1.0.0",
        "creation_date": "2024-10-25",
        "technologies": [
            "Python 3.x",
            "Flask"
        ],
        "endpoints": {
            "/api/": "Informações sobre a API (GET)",
            "/api/predict/": "Predição de veículos (POST)"
        }
    })


@app.route("/api/predict", methods=["POST"])
def predict():
    zip_code = request.args.get("zip_code")
    model_year = request.args.get("model_year")
    fuel = request.args.get("fuel")
    make = request.args.get("make")
    duty = request.args.get("duty")

    if not all([zip_code, model_year, fuel, make, duty]):
        return jsonify({"error": "Todos os parâmetros (zip_code, model_year, fuel, make, duty) são necessários."}), 400

    try:
        args = [
            int(model_year),
            label_encoders["ZIP Code"].transform([zip_code])[0],
            label_encoders["Fuel"].transform([fuel])[0],
            label_encoders["Make"].transform([make])[0],
            label_encoders["Duty"].transform([duty])[0]
        ]
    except KeyError as e:
        return jsonify({"error": f"Parâmetro inválido: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erro durante a transformação dos parâmetros: {str(e)}"}), 500

    try:
        prediction = model.predict([args])[0]
        return jsonify({
            "status": "success",
            "predict": prediction
            }
        ), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao realizar a predição: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=3000, debug=True)