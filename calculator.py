import time

print("ā" * 15)
print("š ļø Created by The Young Programmer [TYP šØāš»] š ļø")
print("āļø      Version 2.4.1     āļø")
print("ā" * 15)

def main():
    
  num1 = float(input("š Enter first num: "))
  op = input("š Enter an operator: ")
  num2 = float(input("š Enter second num: "))

  if op == "+":
    print("ā" * 15)
    print("ā Result:",num1, op, num2, "=" ,num1+num2,"ā")
    print("ā" * 15)
  elif op == "-":
    print("ā" * 15)
    print("ā Result:",num1, op, num2, "=" ,num1-num2,"ā")
    print("ā" * 15)
  elif op == "*":
    print("ā" * 15)
    print("ā Result:" ,num1, op, num2, "=" ,num1*num2,"ā")
    print("ā" * 15)
  elif op == "/":
    print("ā" * 15)
    print("ā Result:" ,num1, op, num2, "=" ,num1/num2,"ā")
    print("ā" * 15)
  else:
    print("ā" * 15)
    print("ā Incorrect operator! ā\nā³  Please try again   ā³")
    print("ā" * 15)

#restart

main()
while True:
  restart = input("š Try again? [y/n]")
  if restart == "y":
    print("ā" * 15)
    print("ā" * 15)
    main()
  elif restart == "n":
    print("ā" * 15)
    print("š„ Thanks for using! š„\nā­ Give a star if you like it ā­")
    print("ā­ for more programing contact >> ")
    print("The Young Programmer Nemonet on github ā­")
    time.sleep(0.5)
    break
  else:
     continue
