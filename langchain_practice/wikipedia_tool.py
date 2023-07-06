from langchain.utilities import WikipediaAPIWrapper

wikipedia = WikipediaAPIWrapper()
res = wikipedia.run("HUNTER X HUNTER")
print(res)
