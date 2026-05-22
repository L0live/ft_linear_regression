import pandas as pd

def main():
	data = pd.read_csv("data.csv")

	normalization = 100000

	km_data = data['km'] / normalization
	price_data = data['price']

	learningRate = 0.01

	theta0 = 0
	theta1 = 0

	size = km_data.size

	# iterations = 2636 # for lr = 0.1
	iterations = 24625 # for lr = 0.01
	# iterations = 227639 # for lr = 0.001

	for j in range(iterations):
		tmp0 = 0
		tmp1 = 0
		for i in range(size):
			error = theta0 + (theta1 * km_data.loc[i]) - price_data.loc[i]
			tmp0 += error
			tmp1 += error * km_data.loc[i]
		theta0 -= learningRate * (tmp0 / size)
		theta1 -= learningRate * (tmp1 / size)
		if not j % 1000 or j >= iterations - 2:
			print(f"Iteration[{j}]    	Theta0: {theta0} 	| Theta1: {theta1}")

	print(f"\n Theta0: {theta0} , Theta1: {theta1}")

if __name__ == "__main__":
	main()