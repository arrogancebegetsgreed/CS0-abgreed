import random

contestant1 = []
contestant2 = []
contestant3 = []
contestant4 = []
contestant5 = []

contestant1 = random.sample(range(1, 6), 4)
OnePoints = sum(contestant1)
One = 1
print(contestant1)
print(OnePoints)
contestant2 = random.sample(range(1, 6), 4)
TwoPoints = sum(contestant2)
Two = 2
print(contestant2)
print(TwoPoints)
contestant3 = random.sample(range(1, 6), 4)
ThreePoints = sum(contestant3)
Three = 3
print(contestant3)
print(ThreePoints)
contestant4 = random.sample(range(1, 6), 4)
FourPoints = sum(contestant4)
Four = 4
print(contestant4)
print(FourPoints)
contestant5 = random.sample(range(1, 6), 4)
FivePoints = sum(contestant5)
Five = 5
print(contestant5)
print(FivePoints)
highestscore = max(OnePoints, TwoPoints,ThreePoints , FourPoints, FivePoints)

if highestscore == OnePoints:
    print("The winner is contestant...", + One, OnePoints)
if highestscore == TwoPoints:
    print("The winner is contestant...", + Two, TwoPoints)
if highestscore == ThreePoints:
    print("The winner is contestant...", + Three, ThreePoints)
if highestscore == FourPoints:
    print("The winner is contestant...", + Four, FourPoints)
if highestscore == FivePoints:
    print("The winner is contestant...", + Five, FivePoints)
else:
    print("It's a Tie!")

print(highestscore)
