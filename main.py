import GPT
import os
from time import sleep

def main_menu():
  while True:
    print("\nWelcome to DuranGPT!!!\n")

    print("(1) Launch GPT\n(2) Select model\n(3) Exit")

    try:
      option = int(input("\nPlease selct an option: "))

      if (option == 1):
        GPT.launch()
      elif (option == 2):
        option_menu()
      elif (option == 3):
        exit()
    except ValueError:
      print("\nInvalid option")

    sleep(1)
    os.system("cls")

def option_menu():
  os.system("cls")
  print("\nPlease choose an option")

  print("\n(1) GPT-3.5-Turbo \n(2) GPT-4 \n(3)Back")

  option = int(input("\nPlease selct an option: "))
  GPT.GPT_option(option)

if __name__ == "__main__":
  os.system("cls")
  main_menu()
