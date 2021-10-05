from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

for aantal in range(1,5):
    for a in range(0,aantal):
        robotArm.grab()
        for b in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(0,5,):
            robotArm.moveLeft()
    robotArm.moveRight()
        
 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()