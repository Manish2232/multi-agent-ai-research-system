from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import streamlit as st
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()


def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key)


TAVILY_API_KEY = get_secret("TAVILY_API_KEY")

tavily = TavilyClient(api_key=TAVILY_API_KEY)

@tool
def web_search(query: str):
    """
    Search the web for recent and reliable information.     
    Returns the top 5 search results.
    """

    results = tavily.search(query = query, max_results = 5)
    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL:{r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n----\n".join(out)

# print(web_search.invoke("what is the recent news war ?"))

@tool # I want to make a tool
def scrape_url(url: str) -> str:
    """
    Scrap and return clean text contents from a given URL for deeper reading.
    """

    try:
        resp = requests.get(url, timeout = 8, headers = {"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator =" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrap URL: {str(e)}"


# print(scrape_url.invoke("https://edition.cnn.com/2026/07/11/world/live-news/iran-war-trump"))