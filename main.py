password = "salom1234"
son = input("Password: ")


while son != password:
   son = input("try again: ")
   if son == password:
        print("You are welcome!")
        break
