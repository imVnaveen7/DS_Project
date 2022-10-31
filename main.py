# registration and login system using python,file handling
def uservalid(username):
    x = username
    spcl = ('[@_!#$%^&*()<>?/\|}{~:]')
    if ("@" in x) and (x.count("@") != len(x)) and (x[0] != "@") and (((x.index(".")) - (x.index("@"))) >1) and (
            x[0] not in spcl):
        if x[0].isnumeric():
            return False
        else:
            return True
    else:
        return False


def passvalid(password):
    y = password
    spcl = ('[@_!#$%^&*()<>?/\|}{~:]')
    if len(y) > 5 and len(y) < 16:
        for i in y:
            if i in spcl:
                spclchar=("yes")
            elif i.isdigit():
                number= ("yes")
            elif i.isupper():
                upp= ("yes")
            elif i.islower():
                loww= ("yes")
        if (spclchar==number) and (upp==loww):
            return True
        else:
            return False
    else:
        return False


def Register():
    ps1='''*you must enter valid details,otherwise you got error!
     *username contains one special character'''
    ps2 = ''' *Length of password is more than 5 and not exceed 15
  *must have one special character
  *atleast minimum of one digit/number
  *one uppercase and one lower case'''
    print(ps1)
    username = input("Enter New Username:")
    print(ps2)
    password = input("Enter the Password:")
    file=open("user_details.txt","r")
    f=file.readlines()
    file.close()
    for i in f:
        a,b = i.split(",")
        b = b.strip()
        if a!=username:
            if passvalid(password) and uservalid(username):
                file = open("user_details.txt", "a")
                file.write("\n" + username + "," + password)
                file.close()
                print("Your registration is successfully!")

            else:
                print("Sorry,You given invalid username/password details,please try again!")

        else:
            print("Sorry this username is already exists!")
            Register()



def forgot_pass():
    username = input("Enter your username:")
    file = open('user_details.txt', "r")
    if username in file:
        for i in file:
            a, b = i.split(",")
            b = b.strip()
            count = 1
            if username == a:
                new_password = input("Enter the new password :")
                if (passvalid(new_password)):

                    fle = open("user_details.txt", "r")
                    flelines = fle.readlines()
                    fle.close()
                    flelines[count] = username + "," + new_password
                    fle = open("user_details.txt", "w")
                    fle.writelines(flelines)
                    fle.close()
                else:
                    ps = ''' *Length of password is more than 5 and not exceed 15
        *must have one special character
        *atleast minimum of one digit/number
        *one uppercase and one lower case'''
                    print(ps)
                    forgot_pass()
            else:
                count += 1
        else:
            print("sorry!,you didn't have account")
    file.close()


def Log_in():
    file = open("user_details.txt", "r")
    # file1=file.read()
    username = input("Enter your username:")
    password = input("Enter the password:")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == username and b == password):
            print("Hello" + username + ", login successfully!")

        else:
            print("Your account doesn't exists,")

            def res():
                response = input("Go for Registration or Forgot password(reg,forgotpass):")
                if (response != "reg") and (response != "forgotpass"):
                    print("Enter a valid details")
                    res()
                else:
                    if (response == "reg"):
                        Register()
                    else:
                        forgot_pass()
            res()
    file.close()
    """if (success):
      print("Hello"+username+", login successfully!")
    else:
      print("Your account doesn't exists,")
      def res():
        response=input("Go for Registration or Forgot password(reg,forgotpass):")
        if (response!="reg") and (response!="forgotpass"):
          print("Enter a valid details")
          res()
        else:
          if (response=="reg"):
            Register()
          else:
            forgot_pass()
      res()"""


def access(option):
    if (option == "login"):
        Log_in()
    else:
        Register()


def begin():
    global option
    print("Hello, Welcome To My New Portal")

    option = input("Select Login Or Register(login,reg):")
    if (option != "login") and (option != "reg"):
        print("Please Enter Valid Details")
        begin()
    elif (option == "login"):
        Log_in()
    elif (option=="reg"):
        Register()


begin()
