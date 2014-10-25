import random


actions = [];
bits_array = []
stork_bits = []
fly_bits = []
environment_index = 0;

def set_environment():
	global stork_bits, fly_bits
	stork_bits = [1,0,0,1,0,1]
	fly_bits = [1,1,1,1,0,0]


def generate_bits(n):
	global bits_array
	for i in range(n):
		r = random.randint(0,1)
		bits_array.append(r)

def display_bits():
	global bits_array
	index = 0
	for i in bits_array:
		if (index % 50) == 0:
			print(" ")
		print(i, end="")
		index = index + 1


def check_if_stork(probe):
	global stork_bits
	current_index = 0
	for i in range(0, len(probe)-len(stork_bits)):
		view = probe[current_index:current_index+len(stork_bits)]
		print("VIEW:", view)
		print("STORK:", stork_bits)
		match = 0
		for i in range(len(stork_bits)):
			if stork_bits[i] == view[i]:
				match = match + 1
		print("MATCHING IN:", match)
		print(" ")
		if match == len(stork_bits):
			return 1
		else:
			current_index = current_index + 1
	return 0



def asses_object( probe ):
	stork = check_if_stork( probe )
	fly = check_if_fly( probe )

	if ( fly == 1 ):
		eat()
	if ( stork == 1):
		run()

def probe_environment(n):
	print(" ")
	global environment_index
	probe = bits_array[environment_index:environment_index+n]
	for i in probe:
		print(i, end="")
	environment_index = environment_index + n;
	return probe

def make_decision():
	run = 0;
	eat = 0;
	for action in actions:
		if action == "RUN":
			act("RUN");
		else:
			if action == "EAT":
				act("EAT")


def main():
	generate_bits(1000)
	display_bits()
	print(" ");
	set_environment()
	p = probe_environment(50);
	print("\n");
	print(check_if_stork(p))

if __name__ == "__main__":
    main();
