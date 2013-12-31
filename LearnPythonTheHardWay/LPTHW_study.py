# This program was created by me (Joshua Diamond) to help study the keywords and operators in
# exercise 37 of Zed Shaw's Learn Python the hard Way.
from sys import exit
import os
from random import randrange

clear = True

def clear_screen():
	if clear:
		os.system('cls')
	else: 
		print "and..."

all_keywords = ['and','del','from','not','while','as','elif','global','or','with','assert','else','if','pass','yield','break',
	'except','import','print','class','exec','in','raise','continue','finally','is','return','def','for','lambda','try',
	'%d', '%i','%o','%u','%x','%X','%e','%E','%f','%F','%g','%G','%c','%r','%s','%%','+','-','*','**','/','//','%','<','>','<=',
	'>=','==','!=','<>','( )','[ ]','{ }','@',',',':','.','=',';','+=','-=','*=','/=','//=','%=','**='
	]

useful_keywords = {
	'and': "An operator. If both the opperands are true then the condition is true.",
	'del': "A way to remove an item from a list given an index.",
	'from': "Specifies a module in which to import a specific attribute.",
	'not': "Reverses the logical state of its operands.",
	'while': "Repeatedly executes a target statement as long as the condition is True.",
	'as': "Attributes an alias to a function.",
	'elif': "Else if. Used in an If/else block to define another condition upon which the statement does something",
	'global': "A declaration statement whih holds true for an entire code block.",
	'or': "Declares that if any of the two operands are true, then the condition is true.",
	'with': "Used to wrap the execution of a block with methods defined by a context manager.",
	'assert': "Tests a condition and aborts as a fatal error if condition is false.",
	'else': "Defines what to do if no condition is met in an if/elif statement.",
	'if': "Checks to see whether a condition is true.",
	'pass': "A null operatior. Used to do nothing.",
	'yield':"Only used when defining a generator function. Returns the generator.",
	'break': "Terminates a loop",
	'except': "Raises an exception when an error in the code is hit.",
	'import': "Inputs a specific module or attribute to be used in a script.",
	'print': "Returns to the screen a statement.",
	'class': "Defines a group of functions.",
	'exec': "supports a dynamic execution of python code.",
	'in': "Evaluates to true if it finds a variable in a specified sequence and false otehrwise.",
	'raise': "Calls a user defined error.",
	'continue': "resumes the iteration of a loop (after a break statement).",
	'finally': "ends a try statement by defining a closing action.",
	'is': "Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.",
	'return': "Exits a functions and optionally passes back an expression to the caller.",
	'def': "Begins a function and defines the function name.",
	'for': "Begins a loop by defining what to do for each item in a sequence",
	'lambda': "Creates an anomyous function.",
	'try': "Tests a statement for errors.",
	'%d': "Signed integer decimal.",
	'%i': "Signed integer decimal.",
	'%o': "Unsigned octal.",
	'%u': "Unsigned decimal.",
	'%x': "Unsigned hexadecimal (lowercase).",
	'%X': "Unsigned hexadecimal (uppercase).",
	'%e': "Floating point exponential format (lowercase).",
	'%E': "Floating point exponential format (uppercase).",
	'%f': "Floating point decimal format.",
	'%F': "Floating point decimal format.",
	'%g': "Floating point format. Uses exponential format if exponent is greater than -4 or less than precision,\ndecimal format otherwise.",
	'%F': "Floating point format. Uses exponential format if exponent is greater than -4 or less than precision,\ndecmial format otherwise.",
	'%c': "Single character (accepts integer or single character string).",
	'%r': "String (converts any python object using repr()).",
	'%s': "String (converts any python object using str()).",
	'%%': "No argument is converted, results in a '%' character in the result.",
	'+': "Addition - Adds values on either side of the operator",
	'-': "Subtraction - Subtracts right hand operand from left hand operand,",
	'*': "Multiplication - Multiplies values on either side of the operator.",
	'**': "Exponet- Performs exponential (power) calculation on operators.",
	'/': "Division - Divides left hand operand by right hand operand.",
	'//': "Floor division - The division of operands where the result is the quotient in which the digits after\ndecimal point are moved.",
	'%': "Modulus - Divides left hand operand by right hand operand.",
	'<': "Checks if the value of left operand is less than the value of right operand.\nIf yes,then condition becomes true.",
	'>': "Checks if the value of the left operand is greater than the value of the right operand.\nIf yes, then condition becomes true.",
	'<=': "Checks if the value of the left operand is less than or equal to the value of the right operand.\nIf yes then condition becomes true.",
	'>=': "checks if the value fo the left operand is greater than or equal to teh value of the right operand.\n If yes then condition becomes true.",
	'==': "Checks if the value of two operands are equal or not.\nIf yes then condition becomes true.",
	'!=': "Checks if the value of two operands are equal or not.\nIf values are not equal tehn condition ebcomes true.",
	'<>': "Checks if the value of two operands are equal or not.\nIf values are not equal, tehn condition becoems true.",
	'( )': "Parentheses -  used to define a function and any variables\nto pass to the function.",
	'[ ]': "Brackets -  used to enclose the contents of a list.",
	'{ }': "Curley Braces -  used to enclose the contents of a dictionary.",
	'@': "At Symbol - a class function and method decorator.",
	',': "Comma - separates the contents of a list or dictionary.\nAt the end of a print statements, a comma tells the print command to\nprint both print statements on the same line.",
	':': "Colon -  used to begin a block of code statements such\nas a for statement, def statement or while statement.\nAlso assigns a left operator key to a right value in a dictionary.",
	'.': "Dot  - assigns attributes or methods to objects - such as [list].append().",
	'=': "Simle assignment operator. Assigns values from right side operands to left side operand.",
	';':  "Semicolon - an optional symbol that can be used to put multiple object on the same line.",
	'+=': "Add AND asignment operator. It adds right operand to the left operand\nand assign the result to left oeprand.",
	'-=': "Subtract AND assignment operator. It subtracts right operand from the left operand\nand assign the result to the left oeprand.",
	'*=': "Multiply AND assignment operator. It multiplies right operand with the left operand\nand assign the result to the left operand.",
	'/=': "Divide AND assignment operator. It divides left operand with teh right operand\nand assign the result to left operand.",
	'//=': "Floor Division and assigns a value. Performs floor division on operators and\nassign value to the left operand.",
	'%=': "Modulus AND assignment operator. It takes modulus using two operands\nand assign the result to the left operand.",
	'**=': "Exponent AND assignment operator. Performs exponential (power) calculation\non operators and assign value to the left operand."
}

def get_dictionary():
	def list_keywords():
		clear_screen()
		print '-' * 50
	
		print "Here is a lit of useful Keywords and Operators:\n"

		def fmtpairs(mylist):
				pairs = zip(mylist[::2],mylist[1::2])
				return '\n'.join('\t\t\t'.join(i) for i in pairs)

		print fmtpairs(all_keywords)
		
		print "\n"	
		print '-' * 50

	def studying():
		list_keywords()
	
		def keyword_input():
			next = raw_input("Which do you want defined? ")
			if next in useful_keywords:
				clear_screen()
				print "'%s' - %s" % (next, useful_keywords[next])
				print '-' * 50
			elif next.lower() == 'quit':
				exit(0)
			elif next.lower() == 'exit':
				start()
			else:
				print "Please type an above listed keyword or operand: "
				keyword_input()

		keyword_input()

		move_on = raw_input("Press enter to continue ")
		if move_on.lower() == 'exit':
			start()
		elif move_on.lower() == 'quit':
			exit(0)
		elif move_on == move_on:
			clear_screen()
			studying()
		else:
			pass

	studying()

def start_game():
	instructions = """
	This game is very simple. A keyword or Symbol will be 
	flashed on the screen. Once you are sure that you 
	know the answer, hit enter and the answer will appear. 
	You can go back to the begining at anytime by typing 'RETURN'.
	If you want to do a flashcard again, type 'AGAIN' after recieving the answer.
	Got it? Good. let's being.
	"""
	print instructions
	next = raw_input("\tReady to proceed? Hit ENTER to contine. > ")
	if next.lower() == 'exit':
		start()
	elif next.lower() == 'quit':
		exit()
	elif next == next:
		randomizer()
	else: 
		pass

def randomizer():
	clear_screen()
	newkey = all_keywords[randrange(len(all_keywords))]
	def return_to():
		print "\n"
		for keyword, definition in useful_keywords.items():
			print "\t\t\t\t%r" % (newkey) 
			break
		print "\n"
		print '-' * 50
	
		next = raw_input("Think you got it? Hit Enter to find out\n> ")
		if next.lower() == 'exit':
			start()
		elif next.lower() == 'quit':
			exit(0)
		elif next == next:
			clear_screen()
			print "\n"
			print "'%s' - %s" % (newkey, useful_keywords[newkey])
			print "\n"
			print '-' * 50
		else: 
			pass

	return_to()

	def onward():
		move_on = raw_input("Ready to continue? Hit Enter.\n(OR Type 'AGAIN' to do this flash card again)\n> ")
		if move_on.lower() == 'again':
			clear_screen()
			return_to()
			onward()
		elif move_on.lower() == 'exit':
			start()
		elif move_on == move_on:
			randomizer()
		else: 
			pass

	onward()


intro = """
	Welcome to my Study program.
	I hope this helps us both learn python.\n
	---------VERY IMPORTANT--------------
	If at anytime you want to return to this welcome screen type 'EXIT'.
	If at anytime you want to leave the program, type 'QUIT'.
	-------------------------------------\n

	HAVE FUN!
	"""

def start():
	clear_screen()
	print intro
	print "\t",
	print "-" * 50
	next = raw_input("\tDo you want to Play Flashcards or Get Dictionary?\n\t[Type 'Play Flashcards' or 'Get Dictionary']\n> ")

	if next[0].lower() == 'p' or next[0].lower() == 'f':
		clear_screen()
		start_game()
	elif next[0].lower() == 'g' or next[0].lower() == 'd':
		clear_screen()
		get_dictionary()
	elif next.lower() == 'quit':
		exit(0)
	elif next.lower() == 'exit':
		start()
	else:
		print "Invalid Entry"
		start()

start()