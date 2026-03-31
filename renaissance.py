import artifact as art
from random import randint
#We know date of the renaissance. from the 14th century to the 16th#
#Then, let's take a number between 1300 and 1700, it will be the date of the object#

paint = art.Painting("The guy who's thinking", randint(1300, 1700), "An Anonymous guy", "colors")

sculpture = art.Sculpture("The mona Lisa but in 3D", randint(1300, 1700), "marble", 12)

building = art.Building("Versaille Palace but in Romania", randint(1300, 1700), "An Armee of builder", "Romania", "Bucarest")
