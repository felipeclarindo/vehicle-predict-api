🌍 [Leia em Português](README.pt-BR.md)

# Vehicle Predict Api

Api Rest developed in `flask` to make predictions based on a Machine Learning model.

## Technologies Used

- `scikit-learn` - Main library for predictive model creation and training, including data preprocessing and performance evaluation.
- `pandas` - Used for data manipulation and analysis, facilitating the processing of input and output data of the model.
- `flask` - Development of the project API, allowing communication between the prediction model and users.
- `joblib` - Save and load the Machine Learning model efficiently, ensuring fast inference.
- `flask-cors` - API CORS configuration.
- `Python` - Language used for developer.

## Objectives

This Machine Learning model was developed to predict the number of vehicles in different contexts, based on the available data. The API allows you to send new information and receive accurate forecasts that can be applied to improve traffic, logistics and infrastructure planning and management. Below are some of the insights this model offers:

1.  Vehicle Volume Forecast: With the data provided, the model estimates the number of vehicles for a given scenario, providing a useful reference base for traffic analysis.

2.  Pattern Identification: The model captures trends and seasonality in the flow of vehicles, which is useful for identifying times and periods of greater and lesser movement.

3.  Impact of Specific Variables: When using a Random Forest model, it is possible to determine which variables have the greatest influence on the number of vehicles, such as days of the week, weather conditions or special events.

4.  Model Accuracy Assessment: Metrics such as Mean Squared Error (MSE) and R2 Score are calculated to understand the accuracy of predictions:
    - The MSE quantifies the mean squared difference between the predicted and actual values, providing a measure of the mean forecast error.
    - The R2 Score indicates the proportion of variation in the data explained by the model, helping to assess how well it represents reality.

These results can be applied to improve decision-making in traffic management, urban planning and logistics optimization, providing practical forecasts that support informed decisions.

## Steps to install and run

1. Clone the Repository:

```bash
git clone https://github.com/felipeclarindo/vehicle-predict-api.git
```

2. Enter directory:

```bash
cd vehicle-predict-api
```

3. Create `Virtual Environment`:

```bash
python -m venv .venv
```

4. Enable `Virtual Environment` by running the `.bat` file in `.venv/Scripts/activate.bat`.

5. Install dependencies :

```bash
pip install - r ./requirements.txt
```

6. Run the jupyter cell phone from the file [model_training.ipynb](./src/model_training.ipynb).

7. Run the api:

```bash
python ./src/api/api.py
```

8. After run access api in:

- `http://localhost:3000/api`

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
