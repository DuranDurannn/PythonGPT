from openai import OpenAI
import time
import os

client = OpenAI()

def print_text_animation(text):
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

  def GPT_4(prompt):
    completion = client.chat.completions.create(
      model = "gpt-4",
      messages = [
        {"role" : "assistant", "content" : "Hi, how chat_reply i assist you"},
        {"role" : "user", "content" : prompt}
      ],
      temperature = 0.5,
      n = 1,
      stop = None,
      max_tokens = 200
    )

    return completion.choices[0].message.content.strip()
    #return completion

  def GPT_3p5_turbo(prompt):
    completion = client.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages = [
        {"role": "assistant", "content": "Hi, how chat_reply i assist you"},
        {"role" : "user", "content" : prompt}
      ],
      temperature = 0.5,
      n = 1,
      stop = None,
      max_tokens = 200
    )

    return completion.choices[0].message.content.strip()
    #return completion

def create_log(dateTime):
  with open ("GPT Log/" + dateTime + ".txt", "x") as log_file:
    header_line = "Date and time: {}\n".format(dateTime)
    log_file.write(header_line)

def output():
  with open ("version.txt", "rt") as file_versions:
    versions = file_versions.readline().split("=")
  
  os.system("cls")

  file_name = time.strftime("%Y,%m,%d-%H,%M,%S")

  create_log(file_name)

  conversation_history = []
  user_input = ""

  print(versions[2] + "\n")
  
  while (user_input.lower != "exit"):
    user_input = input("You: \n")
    if (user_input == "exit"):
      break
      
    conversation_history.append({"role" : "user", "content" : user_input})

    prompt = "\n".join(message["content"] for message in conversation_history)

    if (int(versions[1]) == 1):
      response = all_gpt.GPT_3p5_turbo(prompt)
    if (int(versions[1]) == 2):
      response = all_gpt.GPT_4(prompt)

    print_text_animation(f"\nChatGPT: \n{response}")

    conversation_history.append({"role" : "assistant", "content" : response})

    with open("GPT Log/" + file_name + ".txt", "at") as write_file:
      log = "\n{}\n{}\n".format({"role" : "user", "content" : user_input}, {"role" : "assistant", "content" : response})
      write_file.write(log)

    while len(conversation_history) > 6:
      conversation_history.pop(0)
      conversation_history.pop(1)