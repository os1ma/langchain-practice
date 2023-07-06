import langchain
import openai
from dotenv import load_dotenv


def initialize():
    load_dotenv()
    langchain.verbose = True
    openai.log = "debug"
