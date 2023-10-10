print(""""
      ****************
      User Login Program
      ***************** 
      """)


sys_username = "kadir"
sys_password = "12345"
right_of_acces = 3

while True:
    username = input("Username: ")
    password = input("Password: ")
    if (sys_username != username and password == sys_password):
        print("Wrong Username...")
        right_of_acces -=1
    elif ( password != sys_password and sys_username == username ):
        print("Wrong Password...")
        right_of_acces -=1
    elif (sys_username != username and sys_password != password):
        print("wrong Username and wrong Password")
        right_of_acces -=1
    else:
        (print("Succesfully Login...") )
        break
    if (right_of_acces == 0):
        print("you've run out of access...")


