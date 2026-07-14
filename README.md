# 🚀 Multi-Agent AI Research System

A professional AI-powered research assistant built using **LangChain**, **LangGraph**, **LCEL**, **Mistral AI**, **Tavily Search**, **BeautifulSoup**, and **Streamlit**.

The system follows a four-stage autonomous research pipeline:

> **Search Agent → Reader Agent → Writer Chain → Critic Chain**

It automatically searches the web, scrapes relevant information, generates a structured research report, and critiques the final output.

---

# 📌 Features

- 🔍 AI Search Agent using Tavily Search API
- 🌐 Web Scraping using BeautifulSoup
- 🤖 Multi-Agent Architecture
- 🧠 Mistral AI Integration
- 🔗 LCEL (LangChain Expression Language)
- ⚡ LangGraph Agents
- 📝 Automated Research Report Generation
- ✅ AI Critic for Report Evaluation
- 🎨 Professional Streamlit Dashboard
- 🔒 Secure API Key Management using .env

---

# 🏗️ System Architecture

```
                User Query
                     │
                     ▼
             Search Agent
          (Tavily Web Search)
                     │
                     ▼
             Reader Agent
        (BeautifulSoup Scraper)
                     │
                     ▼
             Writer Chain
       (Generates Research Report)
                     │
                     ▼
             Critic Chain
      (Reviews & Scores the Report)
                     │
                     ▼
             Final Output
```

---

# 📂 Project Structure

```
multi-agent-ai-research-system/
│
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Framework
- LangChain
- LangGraph
- LCEL

### LLM
- Mistral AI

### Search
- Tavily Search API

### Web Scraping
- BeautifulSoup

### Environment
- Python Dotenv

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/multi-agent-ai-research-system.git

cd multi-agent-ai-research-system
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=YOUR_MISTRAL_KEY

TAVILY_API_KEY=YOUR_TAVILY_KEY
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

# 🔄 Workflow

### Step 1

Search Agent searches recent information using Tavily.

↓

### Step 2

Reader Agent scrapes the selected webpage.

↓

### Step 3

Writer Chain generates a professional research report.

↓

### Step 4

Critic Chain reviews the report and provides feedback.

---

# 📸 Dashboard

The Streamlit dashboard includes

- Research Input
- Live Pipeline Status
- Search Results
- Scraped Content
- Final Report
- Critic Feedback
- Dark Professional UI

---

# Future Improvements

- PDF Report Export
- Citation Generator
- Multi-LLM Support
- Agent Memory
- Vector Database Integration
- RAG Pipeline
- Voice Research Assistant
- Docker Deployment
- Authentication
- Chat History

---

# Skills Demonstrated

- Multi-Agent Systems
- Agentic AI
- LangChain
- LangGraph
- LCEL
- Prompt Engineering
- Web Scraping
- REST API Integration
- Streamlit
- Python
- LLM Applications

---

# Author

**Manish Kumar**

B.Tech (Computer Science & Engineering)

AI Engineer | Python Developer | LangChain | Agentic AI | Machine Learning

GitHub:
https://github.com/yourusername

LinkedIn:
https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project useful, consider giving it a Star.