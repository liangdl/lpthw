# -*- coding: utf-8 -*-

# ex35: Branches and Functions

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input(">")
	if "0" in choice or "1" in choice: # 这个太诡异了，不能输入不含0或1的数字，有空改过来，这是个bug
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved: # 调戏熊把它驱赶出去然后改变bear_moved变量,然后再open door就可以了。
			print "The bear has move from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved: #改变完变量再调戏熊就是找死
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty")
	else:
		cthulhu_room()


def dead(why):
	print why,"good job!"
	exit(0)

def start():
	# print "You are in a dark room."
	print "你在一个黑暗的房间里"
	print "这里左右各有一个门" #"There is a door to your right and left."
	print "打算走哪边？"#"Which one dou you take?"

	choice = raw_input("输入left或者right > ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()
