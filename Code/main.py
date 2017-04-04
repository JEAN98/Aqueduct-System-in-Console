from Menu import *
from LogInSystem import *
from InspectorWorks import *
personID = ""
def menuAdmin():

    menu.menuAdministradores()

    option = input("Select one option: ")

    if option == "1":

        print("option#1")


    elif option == "2":

        print("option#2")


    elif option == "3":

        print("option#3")


    elif option == "4":

        print("option#4")


    elif option == "5":

        print("option#5")

    elif option == "6":

        print("Good Bye")
        return

    else:

        print("The option is incorrect\n")

def menuInspector():

    menu.menuInspectores()

    option = input("Select one option: ")


    if option == "1":
       # ownerID = listSolicutedes
        #Serch if is in the list
        waterMeterCode = input("Enter the water meter ID: ")
        amount = float(input("Enter the amount the water meter have: "))



    elif option == "2":
        waterMeterID = input("Enter the water meter ID: ")
        cubicsMeter = float(input("Enter the get cubic meter: "))
        print("option#2")


    elif option == "3":

        return


    else:
        print("Invalid option")

def menuApp():
    'Application main menu'

    menu.menuPrincipal()

    option = input("Enter an option: ")

    print("")

    if option == "1":
        'Access system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")

        log, admin = logIn.logIn(id, password)

        if  log and admin:

            menuAdmin()

        elif  log and admin != True:

            menuInspector()

        else:

            print("\nCheck the ID and password or Sign up\n")

    elif option == "2":
        'Register system by ID and password'

        id = input("Enter your ID:\n")
        password = input("Enter you pasword:\n")
        admin = input("You are Administrator(y/n):\n")
        fullName = input("Enter your full name:\n")
        age = input("Enter your age:\n")
        email = input("Enter your email:\n")

        logIn.signUp(id , password, admin, fullName, age, email)

        print("Welcome {} to Aqueduct System Console\n".format(fullName))

    elif option == "3":

        print("Good Bye")
        return

    else:

        print("The option is incorrect\n")

    menuApp()

menu = Menu()
logIn = LogInSystem()

menuApp()
