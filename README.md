# House Price Prediction Project

A final-year showcase project for predicting residential property prices using machine learning and a clean, presentation-friendly output dashboard.

## Project Title
House Price Prediction Using Machine Learning

## Objective
To build an intelligent system that estimates the price of a house based on key property attributes such as area, number of bedrooms, bathrooms, age of the property, and location score.

## Key Features
- Predicts estimated house price using a trained machine learning model
- Uses real-world-inspired housing attributes
- Produces structured, readable console reports for presentation
- Evaluates model performance using standard metrics
- Includes demo predictions for showcase purposes
- Easy to extend with a larger dataset or a web interface

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- CSV-based dataset management

## Machine Learning Algorithm
This project uses a Random Forest Regressor because it performs well on tabular data, handles non-linearity effectively, and provides strong predictive accuracy for real estate estimation.

## Project Structure
```text
house-price-prediction/
├── README.md
├── requirements.txt
├── data/
│   └── house_prices.csv
├── docs/
│   └── project_documentation.md
├── src/
│   ├── __init__.py
│   ├── data_generator.py
│   ├── house_price_model.py
│   └── __init__.py
├── main.py
└── .gitignore
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Command-line demo
```bash
python main.py
```

### Showcase demo
```bash
python main.py --demo
```

### Interactive Streamlit app
```bash
streamlit run app.py
```

## Example Output
```text
====================================
HOUSE PRICE PREDICTION REPORT
====================================
Model: RandomForestRegressor
Training Rows: 180
Test Rows: 45
R² Score: 0.92
MAE: 18000.00
RMSE: 24000.00

Predicted Price: $420,500
```

## Future Enhancements
- Add more advanced visual analytics in the Streamlit dashboard
- Use a larger real estate dataset
- Compare multiple algorithms such as XGBoost, Linear Regression, and Gradient Boosting
- Add map-based location features and price trend analysis

## Author
Final Year Student Showcase Project
