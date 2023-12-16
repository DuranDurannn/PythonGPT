from openai import OpenAI
import time
import os

client = OpenAI()

def print_text_animation(text):
  print("\nChat GPT: ")

  for char in text:
    print(char, end = "", flush = True)
    time.sleep(0.01)
  
  print("\n")

def GPT_option(option):
  gpt_versions = option

  with open ("version.txt", "rt") as file_versions:
    versions = file_versions.readline().split("=")

  if (gpt_versions == 1):
    versions[1] = 1
    versions[2] = "GPT 3.5 Turbo"
    print("\nSuccessfully change to GPT 3.5 Turbo")
  elif (gpt_versions == 2):
    versions[1] = 2
    versions[2] = "GPT 4"
    print("\nSuccessfully change to GPT 4")
  elif (gpt_versions == 3):
    pass
  
  with open ("version.txt", "wt") as file_versions:
    line = "{}={}={}".format(versions[0], versions[1], versions[2])
    file_versions.write(line)

class all_gpt:
  with open ("version.txt", "rt") as file_versions:
    versions = file_versions.readline().split("=")

  def GPT_4(cls):
    os.system("cls")
    print("\nGPT 4\n")

    while True:
      user_input = input("Prompt: ")

      if (user_input == "exit"):
        break

      completion = client.chat.completions.create(
        model = "gpt-4",
        messages = [
          {"role": "assistant", "content": "Hi, how can i assist you"},
          {"role" : "user", "content" : user_input},
        ],
        temperature = 0.5,
        n = 1,
        stop = None,
        max_tokens = 500
      ) 

      chat_reply = ""
      for choice in completion.choices:
        chat_reply += choice.message.content

      print_text_animation(chat_reply)

  def GPT_3p5_turbo(cls):
    os.system("cls")
    print("\nGPT 3.5 Turbo")

    while True:

      user_input = input("\nPrompt: \n")

      if (user_input == "exit"):
        break

      completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
          {"role": "assistant", "content": "Hi, how chat_reply i assist you"},
          {"role" : "user", "content" : user_input}
        ],
        temperature = 0.5,
        n = 1,
        stop = None,
        max_tokens = 500
      )

      chat_reply = ""
      for choice in completion.choices:
        chat_reply += choice.message.content

      print_text_animation(chat_reply)

def launch():
  with open ("version.txt", "rt") as file_versions:
    versions = file_versions.readline().split("=")

  if (int(versions[1]) == 1):
    all_gpt.GPT_3p5_turbo = classmethod(all_gpt.GPT_3p5_turbo)
    all_gpt.GPT_3p5_turbo()
  elif (int(versions[1]) == 2):
    all_gpt.GPT_4 = classmethod(all_gpt.GPT_4)
    all_gpt.GPT_4()