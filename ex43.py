#-*- coding:utf-8 -*-
#
from sys import exit
from random import randint
#场景基类
class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
#引擎类
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene();
        last_scene = self.scene_map.next_scene("finished")

        while current_scene !=  last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene.enter();
#死亡场景
class Death(Scene):
    quips = ["You died. You kinda suck at this.",
            "Your mom would be proud...if she were smarter.",
            "Such a luser."
            "I have a small puppy that's better at this."]
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet #25 have invaded your ship and destroyed"
        print "your entier crew. You are the last sruviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge,and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central central corridor to the Weapons Armory when"
        print "a Gothon jumps out,red scaly skin,dark grimy teeth,and evil clown costume"
        print "flowing around his hate filled body,He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."

        action = raw_input(">")
        if action == "shoot":
            print "shoot...."
            return 'death'
        elif action == "dodge":
            print "action dodge"
            return 'death'
        elif action == "tell a joke":
            print "action joke....."
            return "laser_weapon_armory"
        else:
            print "Does not compute"
            return 'central_corridor'
class LaserWeaponArmory(Scene):
    def enter(self):
        print "LaserWeaponArmory enter..."
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        print "code = " + code
        guess = raw_input("[keypad]>")
        guesses = 0
        while guess != code and guesses < 10:
            print "BZZZZZZEDDDDD!!"
            guesses += 1
            guess = raw_input("[keypad]")
        if guess == code:
            print "guess == code"
            return 'the_bridge'
        else:
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print "TheBridge enter..."
        action = raw_input(">")
        if action == "throw the bomb":
            print "throw the bomb boom!!!!"
            return 'death'
        elif action == "slowly place the bomb":
            print "get off this tin can"
            return 'escaped_pod'
        else:
            return 'the_bridge'

class EscapedPod(Scene):
    def enter(self):
        print "EscapedPod enter...."
        good_pod = randint(1,5)
        guess = raw_input("[pos #]>")
        if int(guess) != good_pod:
            print "into jam jelly."
            return 'death'
        else:
            print "time. You won!"
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "You won! Good job."
        return 'finished'
class Map(object):
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escaped_pod':EscapedPod(),
        'death':Death(),
        'finished':Finished(),
    }
    def __init__(self,start_scene):
        print "create a Map"
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        print "scene_name = ",scene_name
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
