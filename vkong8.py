#Vicky Kong
#Lab 8


print("You are going to a K-Pop concert soon. Let's see how prepared you are to go the concert!")

name=input("What is your name super fan?")

x="yes"

while(x=="yes"):
    #part 1
    print("Hello",name,"! before we start heading out, you need to choose an outfit!")
    print("1. Comfy outfit")
    print("2. Silly Costume")
    print("3. Nice outfit")
    y=int(input("Enter the number to choose your outfit!"))

    if(y==1):
        print("Nice choice! Being confortable is important to having fun at a concert!")
    if(y==2):
        print("All the fans around you will love your fit and take pictures with you! Everyone is having a good laugh.")
    if(y==3):
        print("You look really nice! Slayyyy!")

    #part 2
    print("Now that you have an outfit, let's pack your concert bag!")
    print("Oh no! Your concert bag is full! You will need to take an item out.")
    print("1. Lightstick")
    print("2. Polaroid")
    print("3. Freebies")
    z=int(input("Enter the number to take out that item:"))

    if(z==1):
        print("You can't go to a K-Pop concert without a lightstick! You are not able to go to the concert anymore.")
        x=input("Would you like to play again?")

    if(z==2):
        print("Good choice! You are not able to take a polaroid into the venue anyways. It is best to not bring it.")

    if(z==3):
        print("You must bring your freebies! It is K-pop culture to give out freebies to other fans.")
        x=input("Would you like to play again?")

    #part 3
    if(x=="yes"):
        print("Now that you are ready, let's plan out on when you should arrive to the venue!")
        print("1. 12pm")
        print("2. 5pm")
        print("3. 8pm")
        a=int(input("Enter the number for the time you plan to arrive at the venue:"))

        if(a==1):
            print("That is a bit early, but you got to exchange a lot of freebies with other fans!")

        if(a==2):
            print("5pm is a good time! You have enough time to find parking and line up to get inside the venue!")

        if(a==3):
            print("You are late! The concert has already started! You did not make it to the concert.")
            x=input("Would you like to play again?")

    #part 4
    if(x=="yes"):
        print("Let's decide how you would get to the venue.")
        print("1. Driving")
        print("2. Public Transportation")
        print("3. Walking")
        b=int(input("Enter the number for your means of transportation:"))

        if(b==1):
            print("Not the best option in my opinion. Hope you are okay with paying for parking!")

        if(b==2):
            print("Public transportation is the best!")

        if(b==3):
            print("Walking is not a good option especially if you live far from the venue. You did not make it to the concert.")
            x=input("Would you like to pay again?")

    #part 5
    if(x=="yes"):
        print("You have made it to the venue! Let's decide what you should do before going inside!")
        print("1. Use the restroom")
        print("2. Get food! Yum!")
        print("3. Buy merch!")
        c=int(input("Enter the number for the activity you want to do:"))

        if(c==1):
            print("Use the restroom inside the venue! The portable restrooms are so dirty!")
            x=input("Would you like to play again?")

        if(c==2):
            print("Yes! Eat before going in! The food inside the venue is overpriced.")
            print("Have fun at the concert!")
            x=input("Would you like to play again?")

        if(c==3):
            print("Yes! Buy some merch to commemorate tonight!")
            print("Have fun at the concert!")
            x=input("Would you like to play again?")

if(x!="yes"):
    print("Thank you for playing!")
