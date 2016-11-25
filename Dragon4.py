#!/usr/bin/python -tt
# Dragon game v2
# 03/22/16
import sys
import random
# from calculator import dragon_attack
# from calculator import dragon_initiative
# from calculator import dragon_hp
# from calculator import elf_attack  # Random number from 1 - 50
# from calculator import elf_defense
# from calculator import elf_initiative
# from calculator import stay_hidden
# from calculator import you_die  # List of creative ways to kill a character

class Nums():
    def __init__(self):
        self.stay_hidden = random.randrange(0, 1001)
        # dragon_things:
        self.dragon_initiative = random.randrange(
            1, 21)  # fix all the dragon things
        self.dragon_defense = random.randrange(1, 30)
        self.dragon_hp = random.randrange(101)
        # elf things
        self.elf_initiative = random.randrange(1, 51)
        self.elf_attack = random.randrange(1, 51)
        self.a_million_ways_to_die = ["A chicken fell on you.", "Your sword bounced off the dragon and hit you instead.",
                                      "A D20 crushed you.", "You stubbed your toe.", "You were burninated.", "You took an arrow to the knee.",
                                      "The sky fell on you.", "The dragon stepped on you"]
        self.you_die = random.choice(self.a_million_ways_to_die)

def again():
    start_over = raw_input("Would you like to play again? (Y or N) ")
    if start_over.lower() != "y" and start_over.lower() != "n":
        print "Please choose yes or no"
    elif start_over.lower() == "n":
        sys.exit()
    else:
        beginning()

def hide(a):
    if a.stay_hidden == 777:
        print "A Holy Knight appeared and slayed the dragon! You're saved!"
        again()
    elif a.stay_hidden == 666:
        print "You made a deal with the devil, you're safe... for now."
        again()
    elif a.stay_hidden == 42:
        print "You hitch a ride with aliens and get away. Don't forget your towel!"
        again()
    elif a.stay_hidden == 911:
        print "Turns out it's a dragon 'of color', the cops show up and shoot it"
        again()
    else:
        print "Fine, the dragon burninated everything. You died because", a.you_die
        again()


def attack(a):
    score = 0
    if a.dragon_initiative > a.elf_initiative:
        print "The dragon saw you before you could attack, you're dead,", a.you_die
        again()
    else:
        attack = raw_input("You're sure you want to attack? (Y or N) ")
        if attack.lower() == "y":
            hit_points = a.dragon_hp
            print "The dragon's defense is ", a.dragon_defense
            print "Your attack strength is ", a.elf_attack
            if a.dragon_defense > a.elf_attack:
                print "bad choice, you have died.", a.you_die
                again()
            elif a.dragon_defense < a.elf_attack:
                hit_points = hit_points - (a.elf_attack - a.dragon_defense)
                while hit_points > 0:
                    print "The dragon's hit points are now ", hit_points
                    continue_attack = raw_input("Attack again? (Y or N) ")
                    if continue_attack.lower() == "y":
                        elf_attack = random.randrange(1, 50)
                        dragon_defense = random.randrange(1, 20)
                        print "Your attack is ", elf_attack
                        print "dragon defense is ", dragon_defense
                        if elf_attack > dragon_defense:
                            hit_points = hit_points - \
                                (elf_attack - dragon_defense)
                        if hit_points > 0 and elf_attack < dragon_defense:
                            print "The dragon attacked you, you died.", a.you_die
                            again()
                        elif hit_points <= 0:
                            print "You killed the dragon! You're everyone's hero."
                            score += 2
                            print "Your score is ", score
                            # done = True
                            again()
                    elif continue_attack.lower() == "n":
                        print "Bravely run away!"
                        break
                        again()
                if hit_points <= 0:
                    print "You killed the dragon! You're everyone's hero."
                    score += 2
                    print "Your score is ", score
                    again()
            else:
                # need to find something to do in a tie
                print "The dragon seems confused, Throw the Holy Hand Grenade!"
        if attack.lower() == "n":
            print "Good choice, bravely run away!"
            score += 1
            print "Your score is ", score
            again()


def beginning():
    a = Nums()
    print "A dragon is attacking your village!"
    player_choice = raw_input("Do you want to attack (a), or hide (h)? ")
    if player_choice.lower() != "h" and player_choice.lower() != "a":
        print "This is serious! Attack or hide."
        beginning()
    elif player_choice.lower() == "h":
        hide(a)
    else:
        attack(a)
if __name__ == '__main__':
    while True:
        play_game = raw_input("Do you want to play a game? (Y/N) ")
        if play_game.lower() != "y" and play_game.lower() != "n":
            print "Please make a valid choice"
            play_game
        elif play_game.lower() != "n":
            beginning()
            sys.exit()
        else:
            sys.exit()