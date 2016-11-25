import random

'''#testing calculator for mpg

miles_driven = raw_input("How many miles did you drive? ")
gallons_of_gas = raw_input("How many gallons of gas did you use? ")

m = int(miles_driven)
g = int(gallons_of_gas)
mpg = m / g

print "You got %d miles per gallon" % (mpg)'''

'''x = raw_input("please enter several numbers, separated by a comma ")
y = x.split(",")
y = [int(x) for x in y]
print y
z = sum(y)
print z
average = z / len(y)
print "The average of your list is %d.2" % average'''

#hide chances
stay_hidden = random.randrange(1001)

#dragon_things:
dragon_initiative = random.randrange(1, 21) #fix all the dragon things
dragon_attack = random.randrange(1,51)
dragon_defense = random.randrange(1, 30)
dragon_hp = random.randrange(101)

#elf things
elf_initiative = random.randrange(1, 51)
elf_attack = random.randrange(1, 51)
elf_defense = random.randrange(1,51)

#death things
a_million_ways_to_die = ["A chicken fell on you.", "Your sword bounced off the dragon and hit you instead.",
                         "A D20 crushed you.", "You stubbed your toe.", "You were burninated.", "You took an arrow to the knee.",
                         "The sky fell on you.", "The dragon stepped on you"]
you_die = random.choice(a_million_ways_to_die)
