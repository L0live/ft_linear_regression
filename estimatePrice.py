

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

    def estimatePrice(mileage):
        theta0 = 8499.599639859707
        theta1 = -214.48963512490795

        return theta0 + (theta1 * mileage)

    print(f"Estimated price: {estimatePrice(mileage)}")


if __name__ == "__main__":
    main()