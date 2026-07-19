from ddgs import DDGS

# Search latest sports news from internet
def get_live_news_context(sport):
    search_query=(f"{sport} latest tournament news")
    
    
    with DDGS() as ddgs:
        results=ddgs.text(
            search_query,
            max_results=3 
        )
        context=""
        for result in results:
            context+= f"""
                    Title: {result["title"]}
                    Body: {result["body"]}


                    -------------------------
                    """
        return context
if __name__ == "__main__":
    get_live_news_context("Football")