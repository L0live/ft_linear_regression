

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
        theta0 = 8499.59964993269
        theta1 = -2144.8963591698
        normalization = 100000

        return theta0 + (theta1 * (mileage / normalization))

    print(f"Estimated price: {estimatePrice(mileage)} for {mileage} km")


if __name__ == "__main__":
    main()