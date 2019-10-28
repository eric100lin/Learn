'''
Python MRO(Method Resolution Order: C3 Method)
https://www.youtube.com/watch?v=EiOglTERPEo
https://www.python.org/download/releases/2.3/mro/

super() doesn't mean call your parents
super() means it should have been called 
the next one in the line

linearization:
Children get called before their parents
Parents get called in the order listed
'''

'''
Level 3         | Root |
            /      |      \
Level 2  | Cx |  | Cy |  | Cz |
              \  /    \  /
Level 1      | C1 |  | C2 |
                \     /
Level 0        | Child |
'''
print("1. Classic MRO example")
class RootAtLevel3: pass
class ClazzXAtLevel2(RootAtLevel3): pass
class ClazzYAtLevel2(RootAtLevel3): pass
class ClazzZAtLevel2(RootAtLevel3): pass
class Clazz1AtLevel1(ClazzXAtLevel2, ClazzYAtLevel2): pass
class Clazz2AtLevel1(ClazzYAtLevel2, ClazzZAtLevel2): pass
class ChildAtLevel0(Clazz1AtLevel1, Clazz2AtLevel1): pass

help(ChildAtLevel0)
print("======================")

'''
Level 2        | DoughFactory |
               /              \
Level 1 | PizzaStore |  | OrganicDoughFactory |
               \              /
Level 0        | OrganicStore |
'''
print("2. Dough and Pizza")
class DoughFactory:

    def getDough(self):
        return "from DoughFactory"

class PizzaStore(DoughFactory):

    def orderPizza(self):
        print("Getting Dough from super()...")
        #           Super considered super! ↓↓
        print("Made pizza with dough " + super().getDough())

PizzaStore().orderPizza()

class OrganicDoughFactory(DoughFactory):

    def getDough(self):
        return "from OrganicDoughFactory"

class OrganicStore(PizzaStore, OrganicDoughFactory): pass

OrganicStore().orderPizza()
print("======================")

print("3. Mock in Unit testing")
class Robot:

    def move_forward(self):
        print("Physical Movement! Moving forward")
    def move_backward(self):
        print("Physical Movement! Moving backward")

class CleaningRobot(Robot):

    def clean(self, times=5):
        for i in range(times):
            super().move_forward()
            super().move_backward()

#CleaningRobot().clean()

class MockBot(Robot):

    def __init__(self):
        self.tasks = []
    def move_forward(self):
        self.tasks.append("forward")
    def move_backward(self):
        self.tasks.append("backward")

class MockCleaningRobot(CleaningRobot, MockBot): pass

import unittest

class TestCleaningRobot(unittest.TestCase):

    def testClean(self):
        times = 10
        mockedBot = MockCleaningRobot()
        mockedBot.clean(times)
        # Amazing list with times !!
        expected = ["forward", "backward"] * times
        self.assertEqual(mockedBot.tasks, expected)

unittest.main()
#help(MockCleaningRobot)
print("======================")
