# Construct URL for search because the url are dynamic
def construct_url_for_search(search_content, search_engine, page):
    search_content = search_content.replace(' ', '+')
    base_urls = {
        'Google': f'https://news.google.com/search?q={search_content}&tbm=nws&start={page * 10}',
        'Yahoo': f'https://news.search.yahoo.com/search?q={search_content}&b={page * 10}+1',
        'Bing': f'https://www.bing.com/news/search?q={search_content}&first={page-1}+1'
    }
    return base_urls.get(search_engine, '')