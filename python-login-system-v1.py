attempt = 3

while True:
  print("====================================")
  print("       ACCOUNT REGISTRATION         ")
  print("====================================")

  create_acc = input("Create Username: ")
  create_pin = input("Create 4-digit PIN: ")

  if not len(create_pin) == 4:
    print("\n[!] Error: PIN must be exactly 4 digits.")
  else:
    print("\n[✓] Account created successfully!")
    break

while attempt > 0:
  print("====================================")
  print("           SYSTEM LOGIN             ")
  print("====================================")

  official_acc = input("\nUsername: ")
  official_pin = input("Enter PIN: ")

  if not official_acc.isalpha() or not official_pin.isdigit():
    attempt -= 1
    print("[!] Error: Invalid character types used.")
    print(f"[i] {attempt} attempt(s) remaining.")

  elif official_acc == create_acc and official_pin == create_pin:
    print(f"\n[✓] Access Granted! Welcome, {official_acc.upper()}.")
    break
          
  else:
    attempt -= 1
    print("[!] Error: Invalid username or PIN.")
    print(f"[i] {attempt} attempt(s) remaining.")

if attempt == 0:
  print("\n[!!!] SECURITY ALERT [!!!]")
  print("Maximum login attempts reached.")
  print("SYSTEM LOCKED.")
  print("====================================")
