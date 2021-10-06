from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
for a in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for b in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(1,10):
            robotArm.moveLeft()
    else: 
        break



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()