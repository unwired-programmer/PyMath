print("\nPyMath")
print("__________")
tgb = input("help yes/no: ")
if tgb == "yes":
    print("HELP:")
    print("yes = select")
    print("no = next")
    print("n.1 = number 1")
    print("n.2 = number 2")
    print(" ")
    print(" ")
    qwe = input("+: ")
    if qwe == "yes":
        n1 = float(input("n.1: "))
        n2 = float(input("n.2: "))
        print("+: ")
        print(n1 + n2)
        input(" ")
    if qwe == "no":
        wer = input("-: ")
        if wer == "yes":
            nu1 = float(input("n.1: "))
            nu2 = float(input("n.2: "))
            print("-: ")
            print(nu1 - nu2)
            input(" ")
        if wer == "no":
            ert = input("/: ")
            if ert == "yes":
                num1 = float(input("n.1: "))
                num2 = float(input("n.2: "))
                print("/: ")
                print(num1 / num2)
                input(" ")
            if ert == "no":
                rty = input("x: ")
                if rty == "yes":
                    numt1 = float(input("n.1: "))
                    numt2 = float(input("n.2: "))
                    print("x: ")
                    print(numt1 * numt2)
                    input(" ")
                if rty == "nu":
                    input("Press enter to exit")
if tgb == "no":
    qwe = input("+: ")
    if qwe == "yes":
        n1 = float(input("n.1: "))
        n2 = float(input("n.2: "))
        print("+: ")
        print(n1 + n2)
        input(" ")
    if qwe == "no":
        wer = input("-: ")
        if wer == "yes":
            nu1 = float(input("n.1: "))
            nu2 = float(input("n.2: "))
            print("-: ")
            print(nu1 - nu2)
            input(" ")
        if wer == "no":
            ert = input("/: ")
            if ert == "yes":
                num1 = float(input("n.1: "))
                num2 = float(input("n.2: "))
                print("/: ")
                print(num1 / num2)
                input(" ")
            if ert == "no":
                rty = input("x: ")
                if rty == "yes":
                    numt1 = float(input("n.1: "))
                    numt2 = float(input("n.2: "))
                    print("x: ")
                    print(numt1 * numt2)
                    input(" ")
                if rty == "no":
                    input("Press enter to exit")