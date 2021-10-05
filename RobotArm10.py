from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for a in range(9,0,-2):
    robotArm.grab()
    for b in range(0,a):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(0,a - 1):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()