from pandas import read_csv
from json import dump

def linearRegression(data, learningRate):
	
	km_data = data['km']
	price_data = data['price']

	size = km_data.size

	theta0 = 0
	theta1 = 0
	j = 0
	stopWhenReached = 2
	while True:
		errorSum0 = 0
		errorSum1 = 0
		for i in range(size):
			error = theta0 + (theta1 * km_data.loc[i]) - price_data.loc[i]
			errorSum0 += error
			errorSum1 += error * km_data.loc[i]
		tmp0 = (errorSum0 / size) * learningRate
		tmp1 = (errorSum1 / size) * learningRate
		if theta0 == theta0 - tmp0 and theta1 == theta1 - tmp1:
			if not stopWhenReached:
				print("\nConvergence reached.")
				break
			stopWhenReached -= 1
		elif not j % 100:
			print("\r" + f"Error Step: {tmp0}", end="", flush=True)
		theta0 -= tmp0
		theta1 -= tmp1
		
		if not j % 10000 or stopWhenReached < 2:
			print("\r" + f"Iteration {j}    Theta0: {theta0} 	Theta1: {theta1}", flush=True)
		j += 1
	return theta0, theta1

def main():
	data = read_csv("data.csv")

	normalization = 100000
	data['km'] /= normalization
	learningRate = 0.001

	theta0, theta1 = linearRegression(data, learningRate)
	thetas = {
		"theta0": theta0,
		"theta1": theta1,
		"normalization": normalization,
		"learningRate": learningRate
	}
	print(thetas)

	with open("thetas.json", "w") as f:
		dump(thetas, f)

if __name__ == "__main__":
	main()