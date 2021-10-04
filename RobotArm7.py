from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for a in range (1,6):
    for a in range(1,7):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()