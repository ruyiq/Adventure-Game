import time
import random


def input_question() -> any:
    time.sleep(2)
    return input("What would you like to do?  (Please enter 1 or 2). :")


def invalid_answer() -> any:
    return input("Your previous answer is not valid. Please enter 1 or 2 :")


def ans_matching(ans: str, response1: str, response2: str, option11: str,
                 option12: str, option21: str, option22: str) -> any:
    if ans is '1':
        print(response1)
        time.sleep(2)
        print(f"enter 1 to {option11}")
        time.sleep(2)
        print(f"enter 2 to {option12}")
    elif ans is '2':
        print(response2)
        time.sleep(2)
        print(f"enter 1 to {option21}")
        time.sleep(2)
        print(f"enter 2 to {option22}")
    else:
        answer = error_message(ans)
        ans_matching(answer, response1, response2, option11, option12,
                     option21, option22)


def error_message(ans: str) -> any:
    while ans not in ['1', '2']:
        ans = invalid_answer()
    return ans


def matching(answer, response1, response2) -> any:
    time.sleep(2)
    if answer is '1':
        print(response1)
    elif answer is '2':
        print(response2)
    else:
        answer = error_message(ans)
        matching(answer, response1, response2)


def transportation(type_of_message) -> any:
    print("There 2 two options.")
    time.sleep(2)
    print(f"enter 1 to {walk_option}")
    time.sleep(2)
    print(f"enter 2 to {bus_option}")
    matching(input_question(), robbed_response, type_of_message)


#  Here are some important variables
robbed_response = "You are so unlucky today! You were almost home but went " \
                  "across the Queens Park and got robbed. Poor you. Let me" \
                  " call 911 for you. [GAME OVER] "

pity_message = "Congratulations! You arrived home safely! Its a pity that" \
               " you didnt get to visit the park but its OK! GOOD NIGHT! " \
               "[GAME OVER]"

congratulation_message = "Congratulations! You are correct! Your trip home will"
"be covered by the shop! Good night!"
walk_option = 'go back home walking'
bus_option = 'go back home by bus'
safe_message = 'Congratulations! You arrived home safely! [GAME OVER]'
sorry_message = "Sorry, you guessed wrong. Its already late at night you " \
                "should go home now"

# This is the introduction part. No action need to be taken from the client.
print("You find yourself standing in an open field, filled with grass and "
      "yellow wildflowers.")
time.sleep(2)
print("Rumor has it that a wicked fairie is somewhere around here, and has "
      "been terrifying the nearby village.")
time.sleep(2)
print("In front of you is a theme park.")
time.sleep(2)
print("To your right is a second-hand shop.")
time.sleep(2)
print("In your hand you hold your trusty (but not very effective) dagger.")
time.sleep(2)
print("Enter 1 to buy a ticket to the park ")
time.sleep(2)
print("Enter 2 to go to the shop to sell the dagger. ")
time.sleep(2)
ans = input_question()  # choose park or shop

# first move
response1 = "The clerk says that the ticket is $50 but if you would like to " \
            "post sth related to the park on instagram then you can get it " \
            "for $10. "
response2 = "They don't really want one and they offered a price of $2. DO " \
            "YOU WANT TO SELL IT OR YOU WANT TO BRING IT BACK TO HOME?"

option11 = 'buy it at original price'
option12 = 'buy it at lower price by advertising the park'
option21 = 'sell it'
option22 = 'go back home. '
ans_matching(ans, response1, response2, option11, option12, option21, option22)
your_choice = input_question()  # whether you choose option1 or option2

# IF CHOOSE TO GO TO PARK
if ans is '1':
    response1 = "Oops! You didnt bring enough cash with you! I'm afraid you " \
                "have to go back home now. You have 2 transportation options. "
    response2 = "Congratulations! You only brought 12 dollars to the park and"\
                " normally you would not be able to get in the park! " \
                "Now, there are 2 options in front of you. You can " \
                "either choose to go take roller coasters or go to the shops "
    roller_coaster = 'take roller coaster'
    shops = 'go to the shops'
    ans_matching(your_choice, response1, response2, walk_option, bus_option,
                 roller_coaster, shops)
    another_choice = input_question()
    if your_choice is '1':  # you have to go back home
        matching(another_choice, robbed_response, safe_message)
    else:
        message1 = "You spend 2 hours waiting for your turn. After the ride, " \
                   "its already 8pm and you are asked to leave. "
        message2 = "There is a activity going on. The clerk will randomly " \
                   "come up with a number. He/she will write it down without " \
                   "showing it to you and your job is to guess whether it is " \
                   "odd or even "
        while another_choice not in ['1', '2']:
            another_choice = error_message(another_choice)
        if another_choice is '1':  # need to go home
            print(message1)
            time.sleep(2)
            transportation(safe_message)
        elif another_choice is '2':  # play the number game
            print(message2)
            print("Enter 1 if you think it is odd. Enter 2 otherwise.")
            your_ans = int(input("Please enter 1 or 2). :"))
            random_num = random.randint(1, 10000)
            if random_num % 2 == 1:
                if your_ans == 1:
                    print(congratulation_message)
                else:
                    print(sorry_message)
                    time.sleep(2)
                    transportation(safe_message)
            else:
                if your_ans == 2:
                    print(congratulation_message)
                else:
                    print(sorry_message)
                    time.sleep(2)
                    transportation(safe_message)
# IF CHOOSE TO GO TO SHOP
else:
    if your_choice == '1':
        print("Congratulations! You've earned 2 dollars today. However, is "
              "too late and you are refused from going into the park. "
              "You have to go home now. ")
        time.sleep(2)
        transportation(pity_message)
    else:
        transportation(pity_message)
