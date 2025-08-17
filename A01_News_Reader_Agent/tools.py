

from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

def scrape_tool(url:str):
    """
    Return the content of a website.
    Input should be a 'url' string.
    """