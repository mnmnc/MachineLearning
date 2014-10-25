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
		#print("VIEW:", view)
		#print("STORK:", stork_bits)
		match = 0
		for i in range(len(stork_bits)):
			if stork_bits[i] == view[i]:
				match = match + 1
		#print("MATCHING IN:", match)
		#print(" ")
		if match == len(stork_bits):
			return 1
		else:
			current_index = current_index + 1
	return 0

def check_if_fly(probe):
	global fly_bits
	current_index = 0
	for i in range(0, len(probe)-len(fly_bits)):
		view = probe[current_index:current_index+len(fly_bits)]
		#print("VIEW:", view)
		#print("FLY:", fly_bits)
		match = 0
		for i in range(len(fly_bits)):
			if fly_bits[i] == view[i]:
				match = match + 1
		#print("MATCHING IN:", match)
		#print(" ")
		if match == len(fly_bits):
			return 1
		else:
			current_index = current_index + 1
	return 0


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
	environment_size = 10000
	probe_size = 50
	generate_bits(environment_size)
	#display_bits()
	print(" ");

	set_environment()

	times_eaten = 0
	times_run = 0

	for i in range(round(environment_size/probe_size)):
		p = probe_environment(probe_size);
		#print(p)
		stork = (check_if_stork(p))
		fly = (check_if_fly(p))
		print("\t",stork, fly, end="\t")
		if stork == 1:
			print("FROG JUMPING AWAY", end="")
			times_run = times_run + 1
		else:
			if fly == 1:
				print("FROG'S DINNER IS SERVED.", end="")
				times_eaten = times_eaten +1
			else:
				print("-", end="")

	print(" ")
	print("\nSTATS:\n", "\tTIMES EATEN: ", times_eaten, "\n\tTIMES RUN: ", times_run )

if __name__ == "__main__":
    main();

