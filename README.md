# ChatGPT in Python (What i like to call the DuranGPT)

ChatGPT in Python (or should I say DuranGPT) is a simple Python command line program that is design to my prefernece and my needs. 

The main purpose of this project is just for me to learn more about the OpenAI ChatGPT API.

## Installation
First, install the OpenAI library:
```bash
pip install openai
```
For me, i use Anaconda (Miniconda) to set up an enviroment in order to contain the library and also set the API key. Can check out reference for more info.
<br>
<br>After that, you can set the ```OpenAI.api_key``` by copying your api key at the ```openai_api_key.txt``` 
<br>
<br>Command line for setting the API key in an enviroment: 
```bash
setx OPENAI_API_KEY "your_api_key_here"
```
Command line for checking your API key:
```bash
echo %OPENAI_API_KEY%
```
After all the setup you can just run the code from ```main.py```

## Feature
- Currently, the code is able to continue conversation with the user but only with the maximum of 6 past coversation (To save token)
- Able to view past conversation in ```GPT Log``` (Each log will be saved by date and time)
- Able to change between GPT 3.5 Turbo to GPT 4 easily from the menu

## Future Feature
- Will add more GPT version
- Able to get image and audio from ChatGPT

# Reference
- OpenAI Official Documentation https://platform.openai.com/docs/overview
- OpenAI Cookbook https://cookbook.openai.com
- Miniconda docummentation https://docs.conda.io/projects/miniconda/en/latest/
- Miniconda cheat sheet https://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf

# DuranDurannn Note
I know the code is spaghetti but this is my first program I created. Feel free to give any suggestion for the program. Thank you :D
