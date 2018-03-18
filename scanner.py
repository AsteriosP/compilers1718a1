teams = {
	"team1" : ["0", "1"],
	"team2" : ["2"],
	"team3" : ["3"],
	"team4" : ["4", "5"],
	"team5" : ["6", "7", "8", "9"],
	"divider" : [":", "."]
}

def getchar(words,pos):
	if pos<0 or pos>=len(words):
		return None
	else:
		char = words[pos]
		for key in teams.keys():
			if char in teams[key]:
				# print(char, key)
				return key
	return None


def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state
	pos = 0
	state = 'q0'

	while True:

		c = getchar(text,pos)	# get next char

		if state in transition_table and c in transition_table[state]:

			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char

		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos


# the transition table, as a dictionary

td = {
	'q0':{ 'team1':'q6', 'team2':'q1', 'team3':'q2', 'team4':'q2', 'team5':'q2' },
    'q1':{ 'team1':'q2', 'team2':'q2', 'team3':'q2', 'divider':'q3' },
    'q2':{ 'divider':'q3' },
    'q3':{ 'team1':'q4', 'team2':'q4', 'team3':'q4', 'team4':'q4' },
    'q4':{ 'team1':'q5', 'team2':'q5', 'team3':'q5', 'team4':'q5', 'team5':'q5' },
    'q6':{ 'team1':'q2', 'team2':'q2', 'team3':'q2', 'team4':'q2', 'team5':'q2', 'divider':'q3' }
}

# the dictionary of accepting states and their
# corresponding token


ad = {'q5':'TIME_TOKEN'}


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0

	# get next token and position after last char recognized
	token,position = scan(text,td,ad)

	if token=='ERROR_TOKEN':
		print('ERROR_TOKEN at pos',position+1,'of',text)
		break

	print("token:",token,"string:",text[:position])

	# remaining text for next scan
	text = text[position:]
