import pandas as pd

def main():
    data = pd.read_csv("data.csv")

    km_data = data['km'] / 10000
    price_data = data['price']

    learningRate = 0.01
    # learningRate = 0.00000001

    theta0 = 0
    theta1 = 0

    size = km_data.size

    def estimatePrice(mileage, t0, t1):
        return t0 + (t1 * mileage)
    
    def errorFunc(t0, t1, isTheta1=False):
        errorSomme = 0
        for i in range(size):
            error = estimatePrice(km_data.loc[i], t0, t1) - price_data.loc[i]
            if isTheta1:
                error *= km_data.loc[i]
            errorSomme += error
        # print(f"ErrorSomme: {errorSomme}")
        return errorSomme

    for i in range(10000):
        tmp0 = learningRate * (errorFunc(theta0, theta1) / size)
        tmp1 = learningRate * (errorFunc(theta0, theta1, True) / size)
        theta0 -= tmp0
        theta1 -= tmp1
        if not i % 100:
            print(f"Iteration: {i} , Theta0: {theta0} , Theta1: {theta1}")

    print(f"Finaly:  Theta0: {theta0} , Theta1: {theta1}")

if __name__ == "__main__":
    main()