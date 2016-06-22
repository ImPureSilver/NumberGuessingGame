# My First Python Program on a MacBook Pro 
#(I'm switching from Command Prompt on Windows 10)
# Alison Stuart
# March 10, 2016

#Import statement(s)
import random

#Game introduction:
print
print
print "Welcome to my number-guessing game!"
print "I am thinking of a number between 1 and 100..."
print
#Decide what the magic number will be that must be guessed
secret_num = random.randrange(1,100)

#Make the answer a string so it will concatenate into an English sentence
secret_num = str(secret_num)

#Temporary check to see if it picked a number in the desired range (working)
#print "The answer is " + secret_num

#Change the correct answer's variable type back into a number from a string
#to make the program work right
secret_num = int(secret_num)

#Set the value of the variable "guess" to something outside the
#bounds set in the game, so that no errors occur when the first guess is made
guess = -1

#Set the number-of-tries counter to 0
attempt_num = 0

#Keep count of the number of tries (working)
while attempt_num < 10: 
	attempt_num = attempt_num + 1
	
	#Keep informing the player of the number of tries they have left (working)
	remaining = 11 - attempt_num
	remaining = str(remaining)
	print "You have " + remaining + " guesses left..."
	
	#Continue to provide opportunities to guess while they're wrong (working)
	if secret_num != guess:
		print "Guess: "
		guess = raw_input()
	
	#Temporary check to see if the value of guess has been updated after input 
	#print guess
	
	#Make Python able to concatenate the variable values into English sentences
	guess = str(guess)
	secret_num = str(secret_num)
	
	#Tell the player the relationship between their guess and the answer 
	if (guess < secret_num):
		print "Your guess is too low!"
		#Optional debugging or "practice round" output:
		#print "You guessed " + guess + " but the answer is " + secret_num + "."
		print
	if (guess > secret_num):
		print "Your guess is too high!"
		#Optional debugging or "practice round" output:
		#print "You guessed " + guess + " but the answer is " + secret_num + "."
		print
	
	#Tell the player if they won or lost
	if (guess == secret_num):
		print "Correct, you won!"
		break
	if (attempt_num == 10):
		print "You are out of guesses! You lose!"

		
#end of while loop for the 10 attempts given 
