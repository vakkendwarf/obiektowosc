import math
from enum import Enum

class Axis(Enum):
    x = 1
    y = 2

class TypOdcinka(Enum):
    Zwykly = 1
    Odleglosc = 2
    Rzut = 3

class Odcinek(object):

    index = 0

    def __init__(self,coordsStart,coordsEnd,type:TypOdcinka=1):

        Odcinek.index += 1

        if type is not None:
            self.type = type
        else:
            self.type = 1
        self.coordsStart = coordsStart
        self.coordsEnd = coordsEnd
        self.length = 0
        self.isVertical = False
        self.isHorizontal = False
        self.index = Odcinek.index

        if self.coordsStart[1] == self.coordsEnd[1]:
            self.isHorizontal = True
        elif self.coordsStart[0] == self.coordsEnd[0]:
            self.isVertical = True



    def __str__(self):

        print("Informacje o odcinku nr. " + str(self.index))
        print("Jest to odcinek: " + str(TypOdcinka(self.type).name))
        print("Koordynaty początkowe: " + str(self.coordsStart))
        print("Koordynaty końcowe: " + str(self.coordsEnd))
        print("Długość odcinka: " + str(self.dlugosc()))
        if self.isVertical or self.isHorizontal:
            if self.isVertical:
                print("Odcinek jest pionowy.")
            elif self.isHorizontal:
                print("Odcinek jest poziomy.")
        elif not self.isHorizontal and not self.isVertical:
            print("Odcinek nie jest ani pionowy, ani poziomy, oraz nie jest punktem (posiada dlugosc).")


        return ""

    def dlugosc(self):

        if self.isHorizontal or self.isVertical:
            if self.isHorizontal:
                return abs(self.coordsEnd[0] - self.coordsStart[0])
            elif self.isVertical:
                return abs(self.coordsEnd[1] - self.coordsStart[1])
        elif self.isHorizontal and self.isVertical:
            return 0
        else:
            thirdpoint = (self.coordsStart[0],self.coordsEnd[1])
            alength = self.coordsStart[1] - thirdpoint[1]
            blength = self.coordsEnd[0] - thirdpoint[0]
            result = abs(math.sqrt(blength**2+alength**2))
            if result == int(result):
                return result
            else:
                resultstr = str(result) + " (√" + str(int(result**2)) + ")"
                return resultstr

    def odleglosc(self, target):

        middle = (self.coordsStart[1]/2,self.coordsEnd[0]/2)
        tempod = Odcinek(middle, target, 2)
        return tempod.dlugosc()

    def dluzszy(self, target2):
        if self.dlugosc() < target2.dlugosc():
            return True
        else:
            return False

    def rzut(self, axis:Axis):

        if axis == Axis(1):
            return Odcinek((self.coordsStart[0],0),(self.coordsEnd[0],0),3)
        elif axis == Axis(2):
            return Odcinek((0,self.coordsStart[1]),(0,self.coordsEnd[1]),3)


