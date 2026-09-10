from __future__ import annotations

import argparse
from pathlib import Path

from src.data_generator import generate_house_dataset
from src.house_price_model import HousePriceModel


def print_report(model: HousePriceModel, input_features: dict | None = None) -> None:
    metrics = model.metrics
    print("\n" + "=" * 58)
    print("HOUSE PRICE PREDICTION REPORT")
    print("=" * 58)
    print(f"Model Type: {type(model.model).__name__}")
    print(f"Training Samples: {len(model._train_X)}")
    print(f"Testing Samples: {len(model._test_X)}")
    print(f"R² Score: {metrics['r2']:.4f}")
    print(f"Mean Absolute Error (MAE): ${metrics['mae']:,.2f}")
    print(f"Root Mean Squared Error (RMSE): ${metrics['rmse']:,.2f}")

    if input_features:
        pred = model.predict_price(input_features)
        print(f"\nPredicted House Price: ${pred:,.2f}")

    print("\nFEATURE SUMMARY")
    print("-" * 58)
    if input_features:
        for key, value in input_features.items():
            print(f"{key:<18}: {value}")
    else:
        print("No custom input provided. Showing a demo prediction.")

    print("=" * 58)


def main() -> None:
    parser = argparse.ArgumentParser(description="House Price Prediction Showcase Project")
    parser.add_argument("--demo", action="store_true", help="Run demo prediction")
    parser.add_argument("--dataset", default="data/house_prices.csv", help="Dataset file path")
    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    dataset_path.parent.mkdir(parents=True, exist_ok=True)

    if not dataset_path.exists():
        generate_house_dataset(dataset_path)

    model = HousePriceModel(dataset_path)
    model.train()

    if args.demo:
        sample = model.get_sample_prediction()
        print_report(model, sample["features"])
    else:
        custom_features = {
            "area_sqft": 2500,
            "bedrooms": 4,
            "bathrooms": 3,
            "age": 7,
            "distance_to_city": 10,
            "location_score": 88,
            "garage": 2,
            "garden": 1,
        }
        print_report(model, custom_features)


if __name__ == "__main__":
    main()
