import time

a = input("Enter your name: ")
print("Welcome to the Hot seat","MR.",a,"Its me Amitabh Bachchan and You are watching KBC.Let's Begin")
print()
time.sleep(6)

questions = ["Which club won the champions league 2015?","Which club won the FA cup 2024?"," Manchester is....?","What is the first name of The Professor in money heist?","In what year was the first iPhone released?","What is the capital city of Spain?","Where is Billie Eilish from?","How many goals Messi scored for Barcelona","Who's the smartest person you know"]

correctAnswers = ["Barcelona","Manchester United","Blue","Sergio","2007","Madrid","Los Angeles","672","Rhythm"]

print("1.The first question on your computer screen is,",questions[0])
print()
time.sleep(2)
 
b = input("Enter your answer: ")
print("Heart beats")
print()
time.sleep(3)

if(b == correctAnswers[0]):
    print("You are absolutely correct")
    print()
    time.sleep(2)

    print("2.With that said next question on your computer screen is,",questions[1])
    print()
    time.sleep(2)

    b = input("Enter your answer: ")
    print("Heart beats")
    print()
    time.sleep(3)

    if(b == correctAnswers[1]):
        print("Your Answer is....")
        time.sleep(2)
        print("Correct")
        print()
        time.sleep(2)

        print("3.Moving on to your next question on your computer screen,",questions[2])
        print()
        time.sleep(2)

        b = input("Enter your answer: ")
        print("Heart beats")
        print()
        time.sleep(3)

        if(b == correctAnswers[2]):
            print("Adhbut")
            print()
            time.sleep(2)

            print("4.Next we have a tricky question,",questions[3])
            print()
            time.sleep(2)

            b = input("Enter your answer: ")
            print("Heart beats")
            print()
            time.sleep(3)

            if(b == correctAnswers[3]):
                print("Absolutely correct")
                print()
                time.sleep(2)

                print("5.Moving on to your next question,",questions[4])
                print()
                time.sleep(2)

                b = input("Enter your answer: ")
                print("Heart beats")
                print()
                time.sleep(3)

                if(b == correctAnswers[4]):
                    print("Bohot hard Bhohot kya?")
                    print()
                    time.sleep(2)

                    print("6.Agla sawal,",questions[5])
                    print()
                    time.sleep(2)

                    b = input("Enter your answer: ")
                    print("Heart beats")
                    print()
                    time.sleep(3)

                    if(b == correctAnswers[5]):
                        print("OP")
                        print()
                        time.sleep(2)

                        print("7.Next question on your computer screen ,",questions[6])
                        print()
                        time.sleep(2)

                        b = input("Enter your answer: ")
                        print("Heart beats")
                        print()
                        time.sleep(3)

                        if(b == correctAnswers[6]):
                            print("Avisvasniye")
                            print()
                            time.sleep(2)

                            print("8.Agla sawal 1 crore k liye apki screen par ye raha,",questions[7])
                            print()
                            time.sleep(2)

                            b = input("Enter your answer: ")
                            print("Heart beats")
                            print()
                            time.sleep(3)

                            if(b == correctAnswers[7]):
                                print("Avisvasniye Adbhut Saandar ")
                                print()
                                time.sleep(2)

                                print("Mr.",a,"If you'll answer this last question, You'll win Rs.7 crore")
                                print("9.THe last question on computer screen is,",questions[8])
                                print()
                                time.sleep(2)

                                b = input("Enter your answer: ")
                                print("Heart beats")
                                print()
                                time.sleep(3)

                                if(b == correctAnswers[8]):
                                    print("Mr.",a,"What made u think your answer is",b)
                                    time.sleep(3)
                                    print("Cause its absolutely right")
                                    print("7 croreee")
                                    print()
                                    time.sleep(2)

                                else:
                                    print("Its me bro Rhythm")
                                    time.sleep(2)
                                    print("Mr.",a,"The answer is incorrect")
                                    time.sleep(2)
                                    print("Dont worry because Still you won Rs.1,00,00,000")

 
                            else:
                                print("I think you got no ball knowledge")
                                time.sleep(2)
                                print("Mr.",a,"The answer is incorrect")
                                time.sleep(2)
                                print("Dont worry because Still you won Rs.25,00,000")

    
                        else:
                            print("Black top big tshirt got you fail")
                            time.sleep(2)
                            print("Mr.",a,"The answer is incorrect")
                            time.sleep(2)
                            print("Dont worry because Still you won Rs.16,00,000")


    
                    else:
                        print("Mr.",a,"The answer is incorrect")
                        time.sleep(1)
                        print("Dont worry because Still you won Rs.8,00,000")


                else:
                    print("Everyone got an iphone nowdays")
                    time.sleep(2)
                    print("Mr.",a,"The answer is incorrect")
                    time.sleep(2)
                    print("Dont worry because Still you won Rs.4,00,000")



            else:
                print("I guess you haven't watched Money heist")
                time.sleep(2)
                print("Mr.",a,"The answer is incorrect")
                time.sleep(2)
                print("Dont worry because Still you won Rs.2,00,000")


        else:
            print("You'r a United fan?")
            time.sleep(2)
            print("Mr.",a,"The answer is incorrect")
            time.sleep(2)
            print("Dont worry because Still you won Rs.1,00,000")

    
    else:
        print("I think you got no ball knowledge")
        time.sleep(2)
        print("Mr.",a,"The answer is incorrect")
        time.sleep(2)
        print("Dont worry because Still you won Rs.50,000")

    

else:
    print("I think you got no ball knowledge")
    time.sleep(2)
    print("Mr.",a,"The answer is incorrect")
    time.sleep(2)
    print("Sorry to say but you won nothing")

time.sleep(3)
print()
print()
