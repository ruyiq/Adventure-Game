import time
import random
import os
import sys


def print_pause(message: str, pause=2) -> any:
    """
    Create a function to give pauses automatically.
    """
    print(message)
    time.sleep(pause)


def valid_input(prompt, options=None):
    """
    Create a function that helps to detect invalid ans and help the user to
    reenter.
    """
    if options is None:
        options = ['1', '2']
    choice = input(prompt)
    if choice in options:
        return choice
    else:
        print_pause("Your previous answer is not valid. Please enter 1 or 2"
                    "next time.")
        return valid_input(prompt, options)


def matching(answer: str, response1: str, response2: str) -> any:
    if answer is '1':
        print_pause(response1)
    elif answer is '2':
        print_pause(response2)


def transportation(message: str) -> any:
    """
    This is a function to help user select transportation option. Created for
    readability.
    """
    print("There 2 two options.")
    print_pause(f"enter 1 to {walk_option}")
    print_pause(f"enter 2 to {bus_option}")
    matching(valid_input('Please enter 1 or 2'), robbed_response, message)
    restart_or_not()


def check_result(guess, random_num) -> any:
    """
    To check whether the user win in the game.
    :return: return 'win' or 'lose'
    """
    if random_num % 2 == 1:
        if guess == 1:
            return 'win'
        else:
            return 'lose'
    else:
        if guess == 2:
            return 'win'
        else:
            return 'lose'


def restart_or_not():
    option = valid_input("DO you want to restart the game? Enter"
                         "1 for yes and 2 for no", options=None)
    if option is '1':
        restart()
    else:
        sys.exit(0)


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


#  Here are some important variables
robbed_response = "You are so unlucky today! You were almost home " \
                  "but went across the Queens Park and got robbed. " \
                  "Poor you. Let me call 911 for you. [GAME OVER] "

pity_message = "Congratulations! You arrived home safely! Its a " \
               "pity that you didnt get to visit the park but " \
               "its OK! GOOD NIGHT! [GAME OVER]"

congratulation_message = "Congratulations! You are correct! Your " \
                         "trip home will be covered by the shop! " \
                         "Good night!"
walk_option = 'go back home walking'
bus_option = 'go back home by bus'
safe_message = 'Congratulations! You arrived home safely! [GAME OVER]'
sorry_message = "Sorry, you guessed wrong. Its already late " \
                "at night you should go home now"


# This is the introduction part. No action need to be taken from the client.
print_pause(
    "Rumor has it that a wicked fairie is somewhere around here, and "
    "has been terrifying the nearby village.")
print_pause("In front of you is a theme park.")
print_pause("To your right is a second-hand shop.")
print_pause(
    "In your hand you hold your trusty (but not very effective) dagger.")
print_pause("Enter 1 to buy a ticket to the park ")
print_pause("Enter 2 to go to the shop to sell the dagger. ")
# park or shop
ans = valid_input("What would you like to do?  (Please enter 1 or 2). :")

# park
if ans == '1':
    print_pause("The clerk says that the ticket is $50 but if "
                "you would like to post sth related to the park"
                "on instagram then you can "
                "get it for $10. ")
    answer = valid_input("Enter 1 to do the ad. Enter 2 otherwise.")
    response1 = "Oops! You didnt bring enough cashn with you! I'm " \
                "afraid you have to go back home now. You have" \
                " 2 transportation options. "
    response2 = "Congratulations! You only brought 12 dollars to " \
                "the park and normally you would not be able to " \
                "get in the park! Now, there are 2 options in " \
                "front of you. You can either choose to go " \
                "take roller coasters or go to the shops "
    matching(answer, response1, response2)
    # transportation
    if answer == '1':
        transportation(safe_message)
    else:
        answer = valid_input(
            "What would you like to do?  (Please enter 1 or 2). :")
        message1 = "You spend 2 hours waiting for your turn. After " \
                   "the ride, its already 8pm and you are asked to leave. "
        message2 = "There is a activity going on. The clerk will " \
                   "randomly come up with a number. He/she will write" \
                   "it down without showing it to you and your job is" \
                   "to guess whether it is odd or even "
        matching(answer, message1, message2)
        if answer == '1':
            transportation(safe_message)
        else:
            your_ans = valid_input("Enter 1 if you think it is odd. "
                                   "Enter 2 otherwise.")
            random_num = random.randint(1, 10000)
            result = check_result(your_ans, random_num)
            if result is 'win':
                print_pause(congratulation_message)
                restart_or_not()
            else:
                print_pause(sorry_message)
                transportation(safe_message)
# shop
if ans == '2':
    print_pause("They don't really want one and they offered a price of $2. "
                "DO YOU WANT TO SELL IT OR YOU WANT TO BRING IT BACK"
                "TO HOME?")
    ans = valid_input('enter 1 to sell. 2 otherwise.')

    if ans == '1':
        print_pause("Congratulations! You've earned 2 dollars today. "
                    "However, is too late and you are refused "
                    "from going into the park."
                    "You have to go home now. ")
        transportation(pity_message)
    else:
        transportation(pity_message)
