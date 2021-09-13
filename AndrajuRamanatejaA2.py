import random

# lists declared for storage of the round values to display at the end .
round_value = []
par_message = []


def main():
    # input of the user name
    name_of_player = input("What is your name? ")

    # condition to check whether the entered input is correct or incorrect
    while not name_of_player.isalpha():
        # checking with blank or in-correct format
        if name_of_player == "":
            print("Name cannot be blank!!!")
        else:
            print("There might be a mistype in  please check it and enter your name")
        name_of_player = input("What is your name? ")
    print("\nWelcome ", name_of_player, "\nLet's play golf, CP1401 style! \n")
    par = input("Choose a par for this course (between 3-5 inclusive): ")
    # input of the par value  and condition error handling
    while not par.isnumeric():
        numeric(par)
        # called numeric function to handle the error
        par = input("Choose a par for this course (between 3-5 inclusive): ")
    par = int(par)
    while not (2 < par < 6):
        print("I’m sorry, you must choose a number between 3-5 inclusive. Please enter again.\n")
        par = int(input("Choose a par for this course (between 3-5 inclusive): "))
    hole_distance = input("How many meters to the hole (between 195 – 250 inclusive:)")
    # input of the hole distance value  and condition error handling
    while not hole_distance.isnumeric():
        numeric(hole_distance)
        # called numeric function to handle the error
        hole_distance = input("Choose a par for this course (between 3-5 inclusive): ")
    hole_distance = int(hole_distance)
    while not (194 < hole_distance < 251):
        print("I’m sorry, you must choose distance between 195 -250 inclusive. Please enter again.")
        hole_distance = int(input("\nHow many meters to the hole (between 195 – 250 inclusive: )"))
    print("\nSelect the option with its first letter or the letter from the below ()")

    # main game logic

    game_menu = input("Golf! \n (I) Instructions \n (P) Play round \n (Q) Quit\n Your Choice: ").upper()
    # if choice is not Q then loop executes
    while game_menu != "Q":
        if game_menu == "P":
            # initializing the values to zero before each round starts!
            ball_hit_count = 0
            travel_distance_of_ball = 0
            print("\nPlay round :)")
            print("\nThis hole is a " + str(hole_distance) + " par " + str(par) + ".")
            # calling the game function once the chooses to play the game
            play_game(travel_distance_of_ball, hole_distance, ball_hit_count, par)
        elif game_menu == "I":
            # calling the instructions function to display the instructions!
            instructions(hole_distance, par)
        else:
            # displaying error message to select the correct option
            print("\n\tInvalid Menu Choice")
        game_menu = input("\n\nGolf! \n (I) Instructions \n (P) Play round \n (Q) Quit\nYour Choice: ").upper()
    print("\nThanks for playing golf CP1401 style! ", name_of_player, "\U0001f607")  # \U0001f607 used for emoji symbol
    # Final Result of the game once the user chooses to quit!
    for game in range(len(round_value)):
        print("Round ", game + 1, ":", round_value[game], " shots ", par_message[game])


def instructions(hole_distance_value, par_value):
    # function to display the instructions
    print("This is a simple golf game in which each hole is ", hole_distance_value, " game away with par ", par_value,
          ". You are able to choose from"
          "\n3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around 30m and the Putter"
          "\nround 10m. The putter is best used very close to the hole. \n\nFor each shot, you may use a driver, iron "
          "or a putter – each shot will vary in distance. \nThe average distance each club can hit is:"
          "\n \tDriver = 100m \n \tIron = 30m \n \tPutter = 10m")


def play_game(travel_distance_of_ball_value, hole_distance_value, ball_hit_count_value, par_value):
    # function to organise the game
    while travel_distance_of_ball_value != hole_distance_value:
        # loop to make the program run until the ball reaches the hole distance
        remaining_distance = abs(hole_distance_value - travel_distance_of_ball_value)
        # used for calculation of the ball if it is less than 10meters and to display the output
        print("\nYou are " + str(remaining_distance) + "m from the hole, after " + str(
            ball_hit_count_value) + " shot/s.")
        print("\nClub selection: press D for driver, I for Iron, P for Putter.")
        club_choice = input("Choose club: ").upper()
        if travel_distance_of_ball_value < hole_distance_value:
            # condition to check whether the distance travelled by the  ball is less than the hole distance
            shot_distance = ball_distance_calculator(club_choice,
                                                     remaining_distance)  # function to generate the shot distance
            travel_distance_of_ball_value += shot_distance  # adding the generated values to the distance travelled by the
            # ball
        else:
            # condition to check whether the distance travelled by the  ball is more than the hole distance
            shot_distance = ball_distance_calculator(club_choice,
                                                     remaining_distance)  # function to generate the shot distance
            travel_distance_of_ball_value -= shot_distance  # subtracting the generated values to the distance travelled by
            # the ball
        print("\nYour shot went " + str(shot_distance) + "m")
        ball_hit_count_value += 1  # incrementing the ball count

    round_value.append(ball_hit_count_value)  # storing the score of the round into list
    par_result(ball_hit_count_value, par_value)  # calling the function to display the result after each round.


def par_result(ball_hit_count_value, par_value):
    # function to display the result after each round
    print("\nClunk… After", ball_hit_count_value, " hits your ball is in the hole!")
    if ball_hit_count_value < par_value:
        print("\nCongratulations. You are ", par_value - ball_hit_count_value, " under par for this hole.")
        print("Your overall score is ", sum(round_value), " and you are ", par_value - ball_hit_count_value,
              " under par.")
        message = str(par_value - ball_hit_count_value) + "under par."
    elif ball_hit_count_value == par_value:
        print("\nCongratulations. You are  exactly on the  par for this hole.")
        print("Your overall score is ", sum(round_value), " and you are ", par_value - ball_hit_count_value,
              " on par.")
        message = str(par_value - ball_hit_count_value) + "on par."
    else:
        print("\nDisappointing. You are", ball_hit_count_value - par_value, "over par for this hole.")
        print("Your overall score is ", sum(round_value), " and you are ", ball_hit_count_value - par_value,
              " over par.")
        message = str(ball_hit_count_value - par_value) + "over par."
    par_message.append(message)  # storing the message value for the round result of the par value


def ball_distance_calculator(club_choice, distance):
    # generating a random  number for the distance of the ball travelled when the user selected a club
    if club_choice == "D":
        shot_distance = random.randint(80, 120)
    elif club_choice == "I":
        shot_distance = random.randint(24, 36)
    elif club_choice == "P" and (0 < distance < 10):
        # if the distance to the hole is less than 10 meters to the hole and the user choose option as Putter this
        # condition executes
        shot_distance = random.randint(round(((distance / 100) * 80)),
                                       round(((distance / 100) * 120)))
    elif club_choice == "P":
        shot_distance = random.randint(8, 12)
    else:
        print("\nInvalid club selection – air swing :( ")
        shot_distance = 0
    return shot_distance
    # returns the value of the shot travelled.


def numeric(value):
    # exception cases to check the number is valid or not
    try:
        value
    except ValueError:
        print("please enter a number")


main()
