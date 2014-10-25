
actions = [];

def set_environment():
	add_predator();
	add_victim();


def generate_next_bit():
	bit = 1;
	#TODO - generate bits function
	return bit

def asses_object():
	stork = check_if_stork()
	fly = check_if_fly()

	if ( fly == 1 ):
		eat()
	if ( stork == 1):
		run()

def make_decision():
	run = 0;
	eat = 0;
	for action in actions:
		if action == "RUN":
			act("RUN");
		else:
			if action == "EAT":
				act("EAT")
