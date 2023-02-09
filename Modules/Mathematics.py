import math
import random

class Mathematics:

    def GetRandomInteger(max): 
        return math.floor(random.random() * max)

    def GetRandomBoolean(): 
        return math.floor(random.random() * 2)