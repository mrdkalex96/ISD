bit = True
attempts = 0
while bit:
    if attempts ==5:
        print("Access denied, please press enter to exit \
and contact security to reset your password")
        break
    userpassword = input("Insert the password: ")
    if userpassword ==  "changeme":
        bit = False
        attempts+=1
        print("You have been authenticated, with" ,attempts,"attempts")
    else: 
        attempts+=1
    


