from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5
for a in range(1,8):
    robotArm.moveRight()
    for a in range(1,2):
        robotArm.grab()
        for a in range(1,9):
            robotArm.moveRight()
        robotArm.drop() 
        for a in range(1,10):
            robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()