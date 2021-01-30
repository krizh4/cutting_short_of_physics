from functions import E_k
import string
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹", "-": u"\u207B"}

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))
#Working on liquid pressure
    

print("Please enter quit to quit")
#When adding a new equation remember to add a spaced and a not spaced one to solvable problems
solvable_problems = ["kinetic energy", "potential energy", "mass pressure","liquid pressure"]
print(solvable_problems)
count = 0
limit1 = 3
limit = False
while not limit and count <= 10:
    today_problem1 = (input("What do you want to solve today(Please enter one of the above?)"))
    today_problem = today_problem1.lower()
    if today_problem == "kinetic energy"  and today_problem != "quit":
        #added error comment
        try:
            m = int(input("Please Enter MASS [From Kilograms]: "))
            v = int(input("Please enter VELOCITY: "))
            f = E_k(m, v)
            f.answer_kinetic()
            count += 1
        except ValueError:
            print("<<<Error: input should be number>>>")
            break
        
    elif today_problem == "mass pressure" and today_problem != "quit":
            print("Please answer with \"yes\" or \"no\"")
            print("Please use kilo grams and Meters")
            pq_1 = input("Do you know the FORCE?")
            pq_2 = input("Do you know the AREA?")
            pq_F = pq_1.lower()
            pq_A = pq_2.lower()
            if pq_F == "yes" and pq_A == "yes":
                F = int(input("Please enter FORCE:"))
                A = int(input("Please enter AREA:"))
                P_m = float(F)/float(A)
                str(P_m)
                print(P_m + "Pa")
                count += 1
            elif pq_F == "no" and pq_A == "yes":
                A = int(input("Please enter AREA:"))
                m = int(input("please enter MASS:"))
                F = m*10
                P_m = float(F)/float(A)
                print(str(P_m) +"Pa")
                count += 1
            elif pq_F == "yes" and pq_A == "no":
                F = int(input("Please enter FORCE:"))
                L = int(input("Please enter LENGTH:"))
                W = int(input("please enter WIDTH:"))
                A = int(L*W)
                P_m = float(F)/float(A)
                print(str(P_m) + "Pa")
                count += 1
            else:
                m = int(input("please enter MASS:"))
                F = m * 10
                L = int(input("Please enter LENGTH:"))
                W = int(input("please enter WIDTH:"))
                A = int(L * W)
                P_m = float(F)/float(A)
                print(str(P_m) + "Pa")
    elif today_problem == "potential energy" and today_problem != "quit":
            m = int(input("Please Enter MASS: "))
            h = int(input("Please enter Height: "))
            g = int((input("Please enter GRAVITATION: ")))
            E_p = float(m) * float(h) * float(g)
            print(str(E_p) + "J")
            count += 1
    elif today_problem == "quit":
        quit("You Entered quit")
    else:
        quit("Don't mess with my system...")
        count += 1
if limit is True and count == 3:
            quit("You have reached the limit of guesses. Don't be lazy go study yourself...")













