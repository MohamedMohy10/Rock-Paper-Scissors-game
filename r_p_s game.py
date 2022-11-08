import random

print(''' 
*******************************************
====> Rock: ✊
====> Paper: ✋
====> Scissors: ✌️
*******************************************
''')
rock = '✊'
paper = '✋'
scissors = '✌'

user_score = 0
cpu_score = 0
turn = 0
choice = 'y'

while choice.lower() == 'y' :
	turn += 1
	print(f"\n              ###### Turn {turn} ######\n")
	player_choice = int(input("Enter the number corrisponding to your choice:\n(1)Rock\n(2)Paper\n(3)Scissors\n\n= \n"))
	computer_choice = random.randint(1,3)

	#decision: 

	if player_choice == 1 :
		print(f"you played: {rock}")
		if computer_choice == 1:
			print(f"CPU played: {rock}")
			print("\nDraw 🤝")
		if computer_choice == 2:
			print(f"CPU played: {paper}")
			print("\nYou Lose 👎")
			cpu_score += 1
		if computer_choice == 3:
			print(f"CPU played: {scissors}")	
			print("\nYou Win 👍")
			user_score += 1

	elif player_choice == 2 :
		print(f"you played: {paper}")
		if computer_choice == 1:
			print(f"CPU played: {rock}")
			print("\nYou Win 👍")
			user_score += 1
		if computer_choice == 2:
			print(f"CPU played: {paper}")
			print("\nDraw 🤝")
		if computer_choice == 3:
			print(f"CPU played: {scissors}")	
			print("\nYou Lose 👎")
			cpu_score += 1

	elif player_choice == 3 :
		print(f"you played: {scissors}")
		if computer_choice == 1:
			print(f"CPU played: {rock}")
			print("\nYou Lose 👎")
			cpu_score += 1
		if computer_choice == 2:
			print(f"CPU played: {paper}")
			print("\nYou Win 👍")
			user_score += 1
		if computer_choice == 3:
			print(f"CPU played: {scissors}")	
			print("\nDraw 🤝")

	else:
		print("\nInvalid input .. You Lose 😕 👎")
		cpu_score += 1
	
	choice = input("\nplay again ? [y/n]\n") #expecting only 'y' or 'n' as an input 

if user_score > cpu_score :
	result = "YOU WIN !! 🥳 👍"
if user_score < cpu_score :
	result = "YOU LOSE !! ☹️ 👎"
if user_score == cpu_score :
	result = "DRAW !! 🙂 🤝 💻"

print(f'''\n\n***********************************************
                ~ FINAL SCORE ~

Total turns : {turn}

You: {user_score}
CPU: {cpu_score}

Match result : {result} 

**********************************************\n
''')