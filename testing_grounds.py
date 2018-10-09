import obiektowosc as ob
from obiektowosc import Axis

od1 = ob.Odcinek((0,2),(2,0))

print(od1.index)
print(od1.isVertical)
print(od1.isHorizontal)

print(od1.dlugosc())

print(od1.odleglosc((3,4)))

od2 = ob.Odcinek((0,2),(100,0))

print(od2.index)

print(od2.dlugosc())

print(od1.dluzszy(od2))

print(od1.rzut(Axis.x).dlugosc())
print(od1.rzut(Axis.y).dlugosc())

print(str(od1))
print(str(od2))