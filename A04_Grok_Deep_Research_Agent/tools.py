import os, re

from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()
firecrawl = Firecrawl(api_key=os.getenv("FIRECRAWL_API_KEY"))

def clean_text(text: str) -> str:
    # 링크, URL, 역슬래시, 개행, non-breaking space를 모두 " "로 치환
    text = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://\S+|\\+|\n+|\xa0", " ", text)
    # 2개 이상 공백 → 하나로 압축
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

def web_search_tool(query: str):
    """
    Web search tool,
    Args:
        query:str
            The query to search the web for.

    Returns:
        A list of search results with the website content in Markdown format.
    """
    cleaned_chunks = []

    results = firecrawl.search(
        query=query,
        limit=5,
        scrape_options={"formats": ["markdown"]},
    )

    for result in results.web:
        if hasattr(result, "markdown"):
            cleaned_chunks.append({
                "title": result.metadata.title,
                "url": result.metadata.url,
                "markdown": clean_text(result.markdown),
            })

    return cleaned_chunks