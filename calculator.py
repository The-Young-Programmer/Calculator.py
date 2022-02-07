import time

print("➖" * 15)
print("🛠️ Created by The Young Programmer [TYP 👨‍💻] 🛠️")
print("⚙️      Version 2.4.1     ⚙️")
print("➖" * 15)

def main():
    
  num1 = float(input("👉 Enter first num: "))
  op = input("👉 Enter an operator: ")
  num2 = float(input("👉 Enter second num: "))

  if op == "+":
    print("➖" * 15)
    print("✅ Result:",num1, op, num2, "=" ,num1+num2,"✅")
    print("➖" * 15)
  elif op == "-":
    print("➖" * 15)
    print("✅ Result:",num1, op, num2, "=" ,num1-num2,"✅")
    print("➖" * 15)
  elif op == "*":
    print("➖" * 15)
    print("✅ Result:" ,num1, op, num2, "=" ,num1*num2,"✅")
    print("➖" * 15)
  elif op == "/":
    print("➖" * 15)
    print("✅ Result:" ,num1, op, num2, "=" ,num1/num2,"✅")
    print("➖" * 15)
  else:
    print("➖" * 15)
    print("❌ Incorrect operator! ❌\n⏳  Please try again   ⏳")
    print("➖" * 15)

#restart

main()
while True:
  restart = input("🔄 Try again? [y/n]")
  if restart == "y":
    print("➖" * 15)
    print("➖" * 15)
    main()
  elif restart == "n":
    print("➖" * 15)
    print("🔥 Thanks for using! 🔥\n⭐ Give a star if you like it ⭐")
    print("⭐ for more programing contact >> ")
    print("The Young Programmer Nemonet on github ⭐")
    time.sleep(0.5)
    break
  else:
     continue
