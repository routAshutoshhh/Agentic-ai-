from dotenv import load_dotenv , find_dotenv
import os
from pathlib import Path
#defining the path of the .env file 


#option1 - here to find the .env file we are basiscally using pathlib with parent 
# BASE_DIR_PATH = Path(__file__).resolve().parent.parent
# DOTENV_PATH = BASE_DIR_PATH/".env"


#for dynamically finding 

# # Start at current file, search parents for `.env`
for parent in Path(__file__).resolve().parents:
    candidate = parent / ".env"
    if candidate.exists():
        load_dotenv(dotenv_path=candidate)
        break

#option2 using find_dotenv
dotenv_path_using_find_dotenv = find_dotenv()

#in the path we are loading from the path 
#load_dotenv(dotenv_path = DOTENV_PATH)
load_dotenv(dotenv_path = dotenv_path_using_find_dotenv)

# OPEN_AI_KEY: str = os.getenv("OPENAI_API_KEY","")
OLLAMA_API_KEY:str = os.getenv("OLLAMA_API_KEY","")