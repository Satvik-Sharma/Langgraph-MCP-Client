from dotenv import load_dotenv
import asyncio
load_dotenv()
from langgraph.graph import StateGraph, START, END, add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage

client = MultiServerMCPClient(
    {
        "coingecko": {
            "transport": "http",
            "url": "https://mcp.api.coingecko.com/mcp",
        }
    }
)

async def load_tools():
  return await client.get_tools()

class ChatState(TypedDict):
  messages: Annotated[list[BaseMessage], add_messages]

async def build_graph():
  tools = await load_tools()

  llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash'
  )
  llm_with_tools = llm.bind_tools(tools=tools)

  async def chat_node(state: ChatState) -> ChatState:
    messages = state['messages']
    ai_message = await llm_with_tools.ainvoke(messages)
    return {'messages': ai_message}

  tool_node = ToolNode(tools=tools)
  graph = StateGraph(ChatState)

  graph.add_node('chat_node', chat_node)
  graph.add_node('tools', tool_node)

  graph.add_edge(START, 'chat_node')
  graph.add_conditional_edges('chat_node', tools_condition, {"tools": "tools", END: END})
  graph.add_edge('tools', 'chat_node')
  return graph

async def main():
  graph = await build_graph()
  chatbot = graph.compile()

  initial_state = {'messages': [HumanMessage(content='Which crypto has gone up the most in last 24 hours')]}
  final_state = await chatbot.ainvoke(initial_state)
  
  for m in final_state["messages"]:
        if m.content:
            print(f"{m.__class__.__name__}: {m.content}\n")
        else:
           print('Tool Called\n')

if __name__ == '__main__':
  asyncio.run(main())
