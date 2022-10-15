print("                                                                                                        ")

print("==== Hello! This is a calculator that was fully made by All3xx (Discord: All3xx#5198) using Python ====")
print("==== This is a basic program that can only add, subtract, multiply or divide up to 5 different numbers ====")
print("==== Decimal numbers are also supported =====")

print("                                                                        ")
print("                                                                        ")

print("======== !!! PLEASE READ THE INSTRUCTIONS !!! ========")

print("                                                                        ")
print("                                                                        ")

print("==== What do the numbers you're gonna be asked to input mean? ====")
print("Number 1 is for addition.")
print("Number 2 is for subtraction.")
print("Number 3 is for multiplication.")
print("Number 4 is for division.")
print("------------------------------------------------------------------------")
print("If you don't input a number from 1-4 the program will automatically end.")
print("------------------------------------------------------------------------")
print("                                                                        ")
maths_symbols = input("Input a number from 1-4: ")

if maths_symbols == "1":
    print("=== So you chose addition ===")
    print("=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
    print("                                                                                                               ")
    addn_1 = input("What would you like your first number to be? ")
    if addn_1.isdigit():
        print("Ok, so your first number is", str(addn_1))

        addn_2 = input("What would you like you second number to be? ")
        if addn_2.isdigit():
            print("Ok, so your second number is", str(addn_2))
            result1_add = float(addn_1) + float(addn_2)
            print("Your answer is", str(result1_add))


            third_1 = input("Would you like a third number? ")
            if third_1.lower() == "yes":
                    addn_3 = input("What would you like your third number to be? " )
                    if addn_3.isdigit():
                        print("Ok, so your third number is", str(addn_3))
                        result2_add = float(addn_1) + float(addn_2) + float(addn_3)
                        print("Your answer is", str(result2_add))


            if third_1.lower() != "yes":
                quit()
            fourth_1 = input("Would you like a fourth number? ")
            if fourth_1.lower() == "yes":
                    addn_4 = input("What would you like your fourth number to be? ")
                    if addn_4.isdigit():
                        print("Ok, so your fourth number is", str(addn_4))
                        result4_add = float(addn_1) + float(addn_2) + float(addn_3) + float(addn_4)
                        print("Your answer is", str(result4_add))

            if third_1.lower() and fourth_1.lower() != "yes":
                quit()
            fifth_1 = input("Would you like a fifth number? ")
            if fifth_1.lower() == "yes":
                    addn_5 = input("What would you like your fifth number to be? ")
                    if addn_5.isdigit():
                        print("Ok, so your third number is", str(addn_5))
                        result5_add = float(addn_1) + float(addn_2) + float(addn_3) + float(addn_4) + float(addn_5)
                        print("Your answer is", str(result5_add))



if maths_symbols == "2":
    print("=== So you chose subtraction ===")
    print("=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
    print("                                                                                                               ")
    subn_1 = input("What would you like your first number to be? ")
    if subn_1.isdigit():
        print("Ok, so your first number is", str(subn_1))

        subn_2 = input("What would you like you second number to be? ")
        if subn_2.isdigit():
            print("Ok, so your second number is", str(subn_2))
            result1_add = float(subn_1) - float(subn_2)
            print("Your answer is", str(result1_add))

            third_1 = input("Would you like a third number? ")
            if third_1.lower() == "yes":
                subn_3 = input("What would you like your third number to be? ")
                if subn_3.isdigit():
                    print("Ok, so your third number is", str(subn_3))
                    result2_add = float(subn_1) -float(subn_2) - float(subn_3)
                    print("Your answer is", str(result2_add))

            if third_1.lower() != "yes":
                quit()
            fourth_1 = input("Would you like a fourth number? ")
            if fourth_1.lower() == "yes":
                subn_4 = input("What would you like your fourth number to be? ")
                if subn_4.isdigit():
                    print("Ok, so your third number is", str(subn_4))
                    result4_add = float(subn_1) - float(subn_2) - float(subn_3) - float(subn_4)
                    print("Your answer is", str(result4_add))

            if third_1.lower() and fourth_1.lower() != "yes":
                quit()
            fifth_1 = input("Would you like a fifth number? ")
            if fifth_1.lower() == "yes":
                subn_5 = input("What would you like your fifth number to be? ")
                if subn_5.isdigit():
                    print("Ok, so your third number is", str(subn_5))
                    result5_add = float(subn_1) - float(subn_2) - float(subn_3) - float(subn_4) - float(subn_5)
                    print("Your answer is", str(result5_add))

# ---- CREDIT TO All3xx (Discord: All3xx#5198) ----

if maths_symbols == "3":
    print("=== So you chose multiplication ===")
    print("=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
    print("                                                                                                               ")
    muln_1 = input("What would you like your first number to be? ")
    if muln_1.isdigit():
        print("Ok, so your first number is", str(muln_1))

        muln_2 = input("What would you like you second number to be? ")
        if muln_2.isdigit():
            print("Ok, so your second number is", str(muln_2))
            result1_add = float(muln_1) * float(muln_2)
            print("Your answer is", str(result1_add))

            third_1 = input("Would you like a third number? ")
            if third_1.lower() == "yes":
                muln_3 = input("What would you like your third number to be? ")
                if muln_3.isdigit():
                    print("Ok, so your third number is", str(muln_3))
                    result2_add = float(muln_1)  * float(muln_2) * float(muln_3)
                    print("Your answer is", str(result2_add))

            if third_1.lower() != "yes":
                quit()
            fourth_1 = input("Would you like a fourth number? ")
            if fourth_1.lower() == "yes":
                muln_4 = input("What would you like your fourth number to be? ")
                if muln_4.isdigit():
                    print("Ok, so your third number is", str(muln_4))
                    result4_add = float(muln_1) * float(muln_2) * float(muln_3) * float(muln_4)
                    print("Your answer is", str(result4_add))

            if third_1.lower() and fourth_1.lower() != "yes":
                quit()
            fifth_1 = input("Would you like a fifth number? ")
            if fifth_1.lower() == "yes":
                muln_5 = input("What would you like your fifth number to be? ")
                if muln_5.isdigit():
                    print("Ok, so your third number is", str(muln_5))
                    result5_add = float(muln_1) * float(muln_2) * float(muln_3) * float(muln_4) * float(muln_5)
                    print("Your answer is", str(result5_add))

# ---- CREDIT TO Alex ----

if maths_symbols == "4":
    print("=== So you chose division ===")
    print("=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
    print("                                                                                                               ")
    muln_1 = input("What would you like your first number to be? ")
    if muln_1.isdigit():
        print("Ok, so your first number is", str(muln_1))

        muln_2 = input("What would you like you second number to be? ")
        if muln_2.isdigit():
            print("Ok, so your second number is", str(muln_2))
            result1_add = float(muln_1) / float(muln_2)
            print("Your answer is", str(result1_add))

            third_1 = input("Would you like a third number? ")
            if third_1.lower() == "yes":
                muln_3 = input("What would you like your third number to be? ")
                if muln_3.isdigit():
                    print("Ok, so your third number is", str(muln_3))
                    result2_add = float(muln_1)  / float(muln_2) / float(muln_3)
                    print("Your answer is", str(result2_add))

            if third_1.lower() != "yes":
                quit()
            fourth_1 = input("Would you like a fourth number? ")
            if fourth_1.lower() == "yes":
                muln_4 = input("What would you like your fourth number to be? ")
                if muln_4.isdigit():
                    print("Ok, so your fourth number is", str(muln_4))
                    result4_add = float(muln_1) / float(muln_2) / float(muln_3) / float(muln_4)
                    print("Your answer is", str(result4_add))

            if third_1.lower() and fourth_1.lower() != "yes":
                quit()
            fifth_1 = input("Would you like a fifth number? ")
            if fifth_1.lower() == "yes":
                muln_5 = input("What would you like your fifth number to be? ")
                if muln_5.isdigit():
                    print("Ok, so your fifth number is", str(muln_5))
                    result5_add = float(muln_1) / float(muln_2) / float(muln_3) / float(muln_4) / float(muln_5)
                    print("Your answer is", str(result5_add))

# ---- CREDIT TO All3xx (Discord: All3xx#5198) ----

print("==== If you answer anything but 'yes' to the question below the program will end ====")
calculator_repeat = input("Would you like to continue using this calculator? ")
while calculator_repeat.lower() == "yes":
                        print("                                                                                                        ")

                        print("==== Hello! This is a calculator that was fully made by All3xx (Discord: All3xx#5198) using Python ====")
                        print(
                            "==== This is a basic program that can only add, subtract, multiply or divide up to 5 different numbers ====")
                        print("==== Decimal numbers are also supported =====")

                        print("                                                                        ")
                        print("                                                                        ")

                        print("======== !!! PLEASE READ THE INSTRUCTIONS !!! ========")

                        print("                                                                        ")
                        print("                                                                        ")

                        print("==== What do the numbers you're gonna be asked to input mean? ====")
                        print("Number 1 is for addition.")
                        print("Number 2 is for subtraction.")
                        print("Number 3 is for multiplication.")
                        print("Number 4 is for division.")
                        print("------------------------------------------------------------------------")
                        print("If you don't input a number from 1-4 the program will automatically end.")
                        print("------------------------------------------------------------------------")
                        print("                                                                        ")
                        maths_symbols = input("Input a number from 1-4: ")

                        if maths_symbols == "1":
                            print("=== So you chose addition ===")
                            print(
                                "=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
                            print(
                                "                                                                                                               ")
                            addn_1 = input("What would you like your first number to be? ")
                            if addn_1.isdigit():
                                print("Ok, so your first number is", str(addn_1))

                                addn_2 = input("What would you like you second number to be? ")
                                if addn_2.isdigit():
                                    print("Ok, so your second number is", str(addn_2))
                                    result1_add = float(addn_1) + float(addn_2)
                                    print("Your answer is", str(result1_add))


                                    third_1 = input("Would you like a third number? ")
                                    if third_1.lower() == "yes":
                                        addn_3 = input("What would you like your third number to be? ")
                                        if addn_3.isdigit():
                                            print("Ok, so your third number is", str(addn_3))
                                            result2_add = float(addn_1) + float(addn_2) + float(addn_3)
                                            print("Your answer is", str(result2_add))

                                    if third_1.lower() != "yes":
                                        quit()
                                    fourth_1 = input("Would you like a fourth number? ")
                                    if fourth_1.lower() == "yes":
                                        addn_4 = input("What would you like your fourth number to be? ")
                                        if addn_4.isdigit():
                                            print("Ok, so your fourth number is", str(addn_4))
                                            result4_add = float(addn_1) + float(addn_2) + float(addn_3) + float(addn_4)
                                            print("Your answer is", str(result4_add))

                                    if third_1.lower() and fourth_1.lower() != "yes":
                                        quit()
                                    fifth_1 = input("Would you like a fifth number? ")
                                    if fifth_1.lower() == "yes":
                                        addn_5 = input("What would you like your fifth number to be? ")
                                        if addn_5.isdigit():
                                            print("Ok, so your fourth    number is", str(addn_5))
                                            result5_add = float(addn_1) + float(addn_2) + float(addn_3) + float(
                                                addn_4) + float(addn_5)
                                            print("Your answer is", str(result5_add))

                        if maths_symbols == "2":
                            print("=== So you chose subtraction ===")
                            print(
                                "=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
                            print(
                                "                                                                                                               ")
                            subn_1 = input("What would you like your first number to be? ")
                            if subn_1.isdigit():
                                print("Ok, so your first number is", str(subn_1))

                                subn_2 = input("What would you like you second number to be? ")
                                if subn_2.isdigit():
                                    print("Ok, so your second number is", str(subn_2))
                                    result1_add = float(subn_1) - float(subn_2)
                                    print("Your answer is", str(result1_add))

                                    third_1 = input("Would you like a third number? ")
                                    if third_1.lower() == "yes":
                                        subn_3 = input("What would you like your third number to be? ")
                                        if subn_3.isdigit():
                                            print("Ok, so your third number is", str(addn_3))
                                            result2_add = float(subn_1) - float(subn_2) - float(subn_3)
                                            print("Your answer is", str(result2_add))

                                    if third_1.lower() != "yes":
                                        quit()
                                    fourth_1 = input("Would you like a fourth number? ")
                                    if fourth_1.lower() == "yes":
                                        subn_4 = input("What would you like your fourth number to be? ")
                                        if subn_4.isdigit():
                                            print("Ok, so your third number is", str(addn_4))
                                            result4_add = float(subn_1) - float(subn_2) - float(subn_3) - float(subn_4)
                                            print("Your answer is", str(result4_add))

                                    if third_1.lower() and fourth_1.lower() != "yes":
                                        quit()
                                    fifth_1 = input("Would you like a fifth number? ")
                                    if fifth_1.lower() == "yes":
                                        subn_5 = input("What would you like your fifth number to be? ")
                                        if subn_5.isdigit():
                                            print("Ok, so your third number is", str(addn_5))
                                            result5_add = float(subn_1) - float(subn_2) - float(subn_3) - float(
                                                subn_4) - float(subn_5)
                                            print("Your answer is", str(result5_add))

# ---- CREDIT TO All3xx ----

                        if maths_symbols == "3":
                            print("=== So you chose multiplication ===")
                            print(
                                "=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
                            print(
                                "                                                                                                               ")
                            muln_1 = input("What would you like your first number to be? ")
                            if muln_1.isdigit():
                                print("Ok, so your first number is", str(muln_1))

                                muln_2 = input("What would you like you second number to be? ")
                                if muln_2.isdigit():
                                    print("Ok, so your second number is", str(muln_2))
                                    result1_add = float(muln_1) * float(muln_2)
                                    print("Your answer is", str(result1_add))

                                    third_1 = input("Would you like a third number? ")
                                    if third_1.lower() == "yes":
                                        muln_3 = input("What would you like your third number to be? ")
                                        if muln_3.isdigit():
                                            print("Ok, so your third number is", str(muln_3))
                                            result2_add = float(muln_1) * float(muln_2) * float(muln_3)
                                            print("Your answer is", str(result2_add))

                                    if third_1.lower() != "yes":
                                        quit()
                                    fourth_1 = input("Would you like a fourth number? ")
                                    if fourth_1.lower() == "yes":
                                        muln_4 = input("What would you like your fourth number to be? ")
                                        if muln_4.isdigit():
                                            print("Ok, so your third number is", str(muln_4))
                                            result4_add = float(muln_1) * float(muln_2) * float(muln_3) * float(muln_4)
                                            print("Your answer is", str(result4_add))

                                    if third_1.lower() and fourth_1.lower() != "yes":
                                        quit()
                                    fifth_1 = input("Would you like a fifth number? ")
                                    if fifth_1.lower() == "yes":
                                        muln_5 = input("What would you like your fifth number to be? ")
                                        if muln_5.isdigit():
                                            print("Ok, so your third number is", str(muln_5))
                                            result5_add = float(muln_1) * float(muln_2) * float(muln_3) * float(
                                                muln_4) * float(muln_5)
                                            print("Your answer is", str(result5_add))

                        if maths_symbols == "4":
                            print("=== So you chose division ===")
                            print(
                                "=== If you answer anything but numbers in this it will automatically ask you if you want to close it or not ===")
                            print(
                                "                                                                                                               ")
                            muln_1 = input("What would you like your first number to be? ")
                            if muln_1.isdigit():
                                print("Ok, so your first number is", str(muln_1))

                                muln_2 = input("What would you like you second number to be? ")
                                if muln_2.isdigit():
                                    print("Ok, so your second number is", str(muln_2))
                                    result1_add = float(muln_1) / float(muln_2)
                                    print("Your answer is", str(result1_add))

                                    third_1 = input("Would you like a third number? ")
                                    if third_1.lower() == "yes":
                                        muln_3 = input("What would you like your third number to be? ")
                                        if muln_3.isdigit():
                                            print("Ok, so your third number is", str(muln_3))
                                            result2_add = float(muln_1) / float(muln_2) / float(muln_3)
                                            print("Your answer is", str(result2_add))

                                    if third_1.lower() != "yes":
                                        quit()
                                    fourth_1 = input("Would you like a fourth number? ")
                                    if fourth_1.lower() == "yes":
                                        muln_4 = input("What would you like your fourth number to be? ")
                                        if muln_4.isdigit():
                                            print("Ok, so your third number is", str(muln_4))
                                            result4_add = float(muln_1) / float(muln_2) / float(muln_3) / float(muln_4)
                                            print("Your answer is", str(result4_add))

                                    if third_1.lower() and fourth_1.lower() != "yes":
                                        quit()
                                    fifth_1 = input("Would you like a fifth number? ")
                                    if fifth_1.lower() == "yes":
                                        muln_5 = input("What would you like your fifth number to be? ")
                                        if muln_5.isdigit():
                                            print("Ok, so your third number is", str(muln_5))
                                            result5_add = float(muln_1) / float(muln_2) / float(muln_3) / float(
                                                muln_4) / float(muln_5)
                                            print("Your answer is", str(result5_add))
                                            break


