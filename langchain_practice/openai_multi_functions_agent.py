# Do this so we can see exactly what's going on under the hood
import langchain
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from util import ddg_search_api_wrapper, initialize

langchain.debug = True

initialize()

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

tools = [
    Tool(
        name="Search",
        func=ddg_search_api_wrapper().run,
        description="Useful when you need to answer questions about current events. You should ask targeted questions.",
    ),
]

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
)

res = agent.run("What is the weather in LA and SF?")
print(res)
