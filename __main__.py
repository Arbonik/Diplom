from Facult import Facult, HolderBuilder
from Command import CommandHolder, Command
from database import *

fst = HolderBuilder\
 .addHungler(HolderBuilder.addHungler()) ([CommandHolder(), CommandHolder()])




fst.directs[0] = (Command(FSTKEY[0], FSTANSWER[0]),
 Command(FSTKEY[1], FSTANSWER[1]),
 Command(FSTKEY[2], FSTANSWER[2]),
 Command(FSTKEY[3], FSTANSWER[3]),
 Command(FSTKEY[4], FSTANSWER[4]))

# (Command(BUILDKEY[0], BUILDANSWER[0]),
#             Command(BUILDKEY[1], BUILDANSWER[1]),
#             Command(BUILDKEY[2], BUILDANSWER[2]),
#             Command(BUILDKEY[3], BUILDANSWER[3]))
print(fst.delegate("инноватика").answer)
