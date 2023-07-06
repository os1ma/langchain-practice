import langchain
import openai
from dotenv import load_dotenv


def initialize():
    load_dotenv()
    langchain.verbose = True
    openai.log = "debug"


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )
