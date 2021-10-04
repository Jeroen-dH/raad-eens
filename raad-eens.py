import random 

score = 0
ronden = 1 
while ronden <= 20:
    print("\ndit is ronden", ronden)
    randomgetal = random.randint(1,1000)
    ronden = ronden + 1    
    a = 1
    print("je hebt nu", score, "punten")
    while randomgetal >= 0:
        getal = input("Raad het getal tussen 1-1000. als je de ronden wilt skippen type dan 'skip' \nJou keuze: ")
        print(randomgetal)
        if getal == 'skip':
            print("skipping....")
            break
        hoeveel_eraf = randomgetal - int(getal)
        if hoeveel_eraf <= 20 and hoeveel_eraf >= -20:
            print('poging', a)
            a = a + 1
            print("\nje zit heel warm\n")
        if a > 10:
            print("Je hebt geen pogingen meer!")
            print("Het getal was", randomgetal)
            break
        elif hoeveel_eraf <= 50 and hoeveel_eraf >= -50:
            print('poging', a)
            a = a + 1
            print("\nje zit warm\n")
        if a > 10:
            print("Je hebt geen pogingen meer!")
            print("Het getal was", randomgetal)
            break    
        elif int(getal) < randomgetal:
            print('poging', a)
            a = a + 1
            print("\nhoger\n")
            if a > 10:
                print("Je hebt geen pogingen meer!")
                print("Het getal was", randomgetal)
                break
        elif int(getal) > randomgetal:
            print("\nlager\n")
            print('poging', a)
            a = a + 1
            if a > 10:
                print("Je hebt geen pogingen meer!")
                print("Het getal was", randomgetal)
                break            
        else:
            print("---------------------------------\nJe hebt het getal geraden!\nHet getal was", randomgetal)
            score = score + 1
            break
print("Je bent klaar!")
print("Je hebt", score, "punten gehaald")

            