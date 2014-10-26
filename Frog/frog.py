import random

environment = []
stork_genom = []
fly_genom 	= []
environment_state = 0

def initiate_environment():
	global stork_genom, fly_genom
	stork_genom = [1,0,0,1,0,1]
	fly_genom 	= [1,1,1,1,0,0]

def generate_environment(n):
	global environment
	for i in range(n):
		r = random.randint(0,1)
		environment.append(r)

def display_environment():
	global environment
	index = 0
	for i in environment:
		if (index%50) == 0:
			print(" ")
		print(i, end="")
		index = index + 1


def check_if_stork(probe):
	global stork_genom
	current_index = 0
	for i in range(0, len(probe)-len(stork_genom)):
		view = probe[current_index:current_index+len(stork_genom)]
		match = 0
		for i in range(len(stork_genom)):
			if stork_genom[i] == view[i]:
				match = match + 1
		if match == len(stork_genom):
			return 1
		else:
			current_index = current_index + 1
	return 0

def check_if_fly(probe):
	global fly_genom
	current_index = 0
	for i in range(0, len(probe)-len(fly_genom)):
		view = probe[current_index:current_index+len(fly_genom)]
		match = 0
		for i in range(len(fly_genom)):
			if fly_genom[i] == view[i]:
				match = match + 1
		if match == len(fly_genom):
			return 1
		else:
			current_index = current_index + 1
	return 0


def probe_environment(n):
	print(" ")
	global environment_state
	probe = environment[environment_state:environment_state+n]
	for i in probe:
		print(i, end="")
	environment_state = environment_state + n;
	return probe

def main():
	environment_size = 10000
	probe_size = 50
	generate_environment(environment_size)

	print(" ");

	initiate_environment()
	times_eaten = 0
	times_run = 0

	for i in range(round(environment_size/probe_size)):
		p = probe_environment(probe_size);
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

