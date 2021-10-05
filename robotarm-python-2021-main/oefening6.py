from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for a in range(1,8):
    robotArm.moveRight()
for b in range (1,9):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()