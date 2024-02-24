import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.
Author - Madhukar Kumar"""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.oppo_last_move = ""
        self.my_last_move = ""
        print(f"Player's name is {self.name}")

    # This is the default method and gets overridden in the sub classes.
    def move(self):
        return 'rock'

    def get_name(self):
        return self.name

    def learn(self, my_move, their_move):
        self.oppo_last_move = their_move
        self.my_last_move = my_move

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors'])
        # return a random move each time this is called


class HumanPlayer(Player):
    human_input = ""

    def move(self):
        while True:
            self.human_input = input(f"What's your move "
                                     f"- rock, paper or scissors: ")
            if self.human_input.lower() not in ['rock', 'paper', 'scissors']:
                print("\033[92m {}\033[00m".format(f"*** Sorry, "
                                                   f"I don't understand."
                                                   f" Please try again ***"))
            else:
                break
        return self.human_input.lower()


class ReflectPlayer(Player):
    def move(self):
        if self.oppo_last_move:  # Not Empty variable
            return self.oppo_last_move
        else:
            # The string is empty so first move
            return random.choice(['rock', 'paper', 'scissors'])


class CyclePlayer(Player):
    def move(self):
        if self.my_last_move:  # Not Empty variable
            if self.my_last_move == 'rock':
                return 'paper'
            elif self.my_last_move == 'paper':
                return 'scissors'
            else:
                return 'rock'
        else:
            # The string is empty so first move is rock
            return 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # Compare the two moves to see if they are identical and a tie
    def is_a_tie(self, one, two):
        return one == two

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"{self.p1.get_name()}'s move: {move1} "
              f" {self.p2.get_name()}'s move: {move2}")
        if self.is_a_tie(move1, move2):
            print('\033[96m The round was a tie \033[00m')
        else:
            if self.beats(move1, move2):  # If true then move 1 won)
                print(f"{self.p1.get_name()} won")
                self.p1.increment_score()  # set Player 1 score to + 1
            else:
                print("\033[94m {}\033[00m".
                      format(f"{self.p2.get_name()} won"))
                self.p2.increment_score()  # set Player 2 score to + 1
        print(f"{self.p1.get_name()} score = {self.p1.get_score()}")
        print(f"{self.p2.get_name()} score = {self.p2.get_score()}")
        # set player 2 score to +1

    def play_game(self):
        print("Game will  have total of",rounds, "rounds, first one to reach the best out of",rounds," score wins!")
        print("Game start!")
        for r in range(rounds):
            print("\033[93m {}\033[00m".format(f"Round {r + 1}:"))
            self.play_round()
        p1_final_score = self.p1.get_score()
        p2_final_score = self.p2.get_score()
        print("\033[92m {}\033[00m".format(f"{self.p1.get_name()} final score = {p1_final_score}"))
        print("\033[92m {}\033[00m".format(f"{self.p2.get_name()} final score = {p2_final_score}"))
        if p1_final_score == p2_final_score:
            print("\033[95m The Game was a tie !! \033[00m ")
        else:
            if p1_final_score > p2_final_score:
                print("\033[95m {}\033[00m".
                      format(f"{self.p1.get_name()} is the winner"))
            else:
                print("\033[95m {}\033[00m".
                      format(f"{self.p2.get_name()} is the winner"))
        print("Game over!")


if __name__ == '__main__':
    human_player_name = input("\033[91m {}\033[00m".
                              format(f"Welcome to Rock, "
                                     f"Paper and Scissors. "
                                     f"What's your name: "))
    cycle_player_name = input("\033[91m {}\033[00m".format(f"Enter computer's name: "))
    rounds=int(input("\033[91m Enter the number of total rounds to be played: \033[00m"))
    # Play first with CyclePlayer
    game = Game(CyclePlayer(cycle_player_name), HumanPlayer(human_player_name))
    game.play_game()
    while True:
        user_choice = input("Do you want to play again? "
                            "Type Yes or No ")
        if user_choice.lower() in ['yes', 'no']:
            if user_choice.lower() == 'yes':  #Here in the user_choice.lower, () was missing from the syntax thus leading to an error when prompted the yes at the end of the game.
                game2 = Game(RandomPlayer(cycle_player_name),
                             HumanPlayer(human_player_name))
                game2.play_game()
            else:
                print("\033[96m Goodbye \033[00m")
                break
        else:
            print("\033[92m {}\033[00m".format(f"*** Sorry, "
                                               f"I don't understand."
                                               f" Please try again ***"))
