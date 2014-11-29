import pprint

data = [
	{"AURA":0, "HUMIDITY":1, "WIND":0, "WILL_RAIN":0},
	{"AURA":0, "HUMIDITY":1, "WIND":1, "WILL_RAIN":0},
	{"AURA":1, "HUMIDITY":1, "WIND":0, "WILL_RAIN":1},
	{"AURA":2, "HUMIDITY":1, "WIND":0, "WILL_RAIN":1},
	{"AURA":2, "HUMIDITY":0, "WIND":1, "WILL_RAIN":0},
	{"AURA":1, "HUMIDITY":0, "WIND":1, "WILL_RAIN":1},
	{"AURA":0, "HUMIDITY":1, "WIND":0, "WILL_RAIN":0},
	{"AURA":0, "HUMIDITY":0, "WIND":0, "WILL_RAIN":1},
	{"AURA":2, "HUMIDITY":0, "WIND":0, "WILL_RAIN":1},
	{"AURA":0, "HUMIDITY":0, "WIND":1, "WILL_RAIN":1},
	{"AURA":1, "HUMIDITY":1, "WIND":1, "WILL_RAIN":1},
]

def main():
	printer = pprint.PrettyPrinter(indent=4)
	printer.pprint(data)


if __name__ == "__main__":
	main()