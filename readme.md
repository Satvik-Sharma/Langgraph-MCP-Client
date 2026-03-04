# 🚀 Crypto AI Agent (LangGraph + MCP + Gemini)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Framework-purple)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Framework-green)
![Gemini](https://img.shields.io/badge/LLM-Google_Gemini-orange)
![MCP](https://img.shields.io/badge/MCP-Model_Context_Protocol-black)
![Status](https://img.shields.io/badge/Project-Working-success)

An **AI-powered cryptocurrency assistant** that uses **LangGraph agents + MCP tools** to fetch **real-time crypto market data from CoinGecko**.

The agent can intelligently decide when to **call tools** and when to **answer directly**, making it a **true LLM agent system**.

Example query:

> **"Which crypto has gone up the most in the last 24 hours?"**

The AI automatically calls the **CoinGecko MCP server**, fetches data, and generates the answer.

---

# 🧠 What This Project Demonstrates

This project demonstrates modern **AI agent architecture** using:

* **LangGraph agent workflows**
* **Tool calling**
* **MCP (Model Context Protocol)**
* **Google Gemini LLM**
* **Async AI pipelines**

This is the **same architecture used in production AI systems**.

---

# ⚡ Key Features

✅ AI Agent using **LangGraph**
✅ Real-time crypto data using **CoinGecko MCP Server**
✅ Automatic **tool selection by the LLM**
✅ **Gemini 2.5 Flash** for reasoning
✅ Fully **asynchronous architecture**
✅ Modular and production-ready design

---

# 🏗️ System Architecture

```
User Query
    │
    ▼
LangGraph Agent
(StateGraph)
    │
    ▼
Chat Node (Gemini LLM)
    │
    ├── Needs Tool?
    │
    ├── NO → Generate Response → END
    │
    └── YES
          │
          ▼
     Tool Node
  (CoinGecko MCP)
          │
          ▼
   Return Tool Result
          │
          ▼
     Chat Node
          │
          ▼
         END
```

---

# 📊 Agent Workflow

```
START
  │
  ▼
Chat Node (LLM reasoning)
  │
  ▼
Tool Condition
  │
  ├── END (if no tool needed)
  │
  └── Tool Node
          │
          ▼
      Chat Node
          │
          ▼
          END
```

---

# 🧰 Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core language                   |
| LangGraph     | Agent workflow framework        |
| LangChain     | LLM abstraction                 |
| Google Gemini | Large Language Model            |
| MCP           | Tool communication protocol     |
| CoinGecko API | Crypto market data              |
| AsyncIO       | Asynchronous execution          |
| dotenv        | Environment variable management |

---

# 📁 Project Structure

```
crypto-ai-agent/
│
├── main.py
├── .env
├── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/crypto-ai-agent.git
cd crypto-ai-agent
```

---

## 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Linux / Mac

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## 3️⃣ Install dependencies

```
pip install langgraph
pip install langchain
pip install langchain-google-genai
pip install langchain-mcp-adapters
pip install python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=your_google_api_key
```

Get your key from **Google AI Studio**.

---

# ▶️ Running the Agent

Run the script:

```
python main.py
```

Example query:

```
Which crypto has gone up the most in last 24 hours
```

Example output:

```
HumanMessage: Which crypto has gone up the most in last 24 hours

Tool Called

AIMessage: The cryptocurrency with the highest increase in the last 24 hours is...
```

---

# 🧩 Code Overview

## Load MCP Tools

The agent connects to the **CoinGecko MCP server**.

```python
client = MultiServerMCPClient(
    {
        "coingecko": {
            "transport": "http",
            "url": "https://mcp.api.coingecko.com/mcp",
        }
    }
)
```

---

## Define Agent State

The agent keeps conversation history using a **TypedDict state**.

```python
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
```

---

## Bind Tools to the LLM

```python
llm_with_tools = llm.bind_tools(tools=tools)
```

Now Gemini can automatically decide when to call tools.

---

## LangGraph Agent Workflow

```python
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)
```

Conditional routing:

```python
graph.add_conditional_edges(
    'chat_node',
    tools_condition,
    {"tools": "tools", END: END}
)
```

---

# 📈 Example Queries

The agent can answer questions like:

• Which crypto increased the most today?
• What is the price of Bitcoin?
• Top trending cryptocurrencies
• Market cap rankings
• 24-hour crypto performance

---

# 🔮 Future Improvements

Possible upgrades:

• Web UI (Next.js / Streamlit)
• Crypto portfolio tracker
• Multi-agent system
• Memory for long conversations
• Add more MCP servers
• Deploy as an API

---

# 📚 References

LangGraph Documentation
LangChain Documentation
Google Gemini API
CoinGecko API
Model Context Protocol (MCP)

---

# 👨‍💻 Author

**Satvik Sharma**

AI Developer | Full Stack Developer

Interested in:

* AI Agents
* LLM Applications
* LangGraph
* Real-time AI systems
