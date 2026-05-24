from json import load
from os import path

def main():
    print("Your mileage to estimate the price: ")
    try:
        mileage = input()
        assert mileage.isdigit()
        mileage = float(mileage)
    except EOFError:
        print("Nothing... ok, bye")
    except AssertionError:
        print("The mileage must be a full digit entry")
        exit(1)

    theta0 = 0
    theta1 = 0
    normalization = 1
    if path.exists("thetas.json"):
        with open("thetas.json", "r") as f:
            thetas = load(f)
        theta0 = thetas["theta0"]
        theta1 = thetas["theta1"]
        normalization = thetas["normalization"]

    estimatePrice = theta0 + (theta1 * (mileage / normalization))

    print(f"Estimated price: {estimatePrice} for {mileage} km")

if __name__ == "__main__":
    main()