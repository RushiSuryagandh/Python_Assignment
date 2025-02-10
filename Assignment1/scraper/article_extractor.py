
# Extract articles from the soup object when each search engine having different HTML structure
def extract_articles(soup, engine):
    article_lst = []
    if not soup:
        return article_lst
    if engine == "Google":
        articles = soup.find_all('article', {"class": "IFHyqb DeXSAc"})
        for article in articles[:10]:
            link_of_news = article.find('a', {'class': 'WwrzSb'})['href']
            title = article.find('a', {'class': 'JtKRv'}).text
            timestamp = article.find('time')
            data_time_value = timestamp['datetime']
            media_name = article.find('div', {'class': 'vr1PYe'}).text
            article_lst.append((link_of_news, title, data_time_value.split("T")[0], media_name))
        
    elif engine == "Yahoo":
        articles = soup.find_all('div', {"class": "dd NewsArticle"})
        for article in articles[:10]:
            title_ = article.find('h4', {'class': 's-title fz-20 lh-m fw-500 ls-027 mt-8 mb-2'})
            link_of_news = title_.find('a')['href']
            title = title_.find('a').text
            data_time_value = article.find('span', {'class': 's-time fz-14 lh-18 fc-dustygray fl-l mr-4'}).text
            media_name = article.find('span', {'class': 's-source fw-l'}).text
            article_lst.append((link_of_news, title, data_time_value, media_name))
        
    elif engine == 'Bing':
        articles = soup.find_all('div', {"class": "news-card newsitem cardcommon"})
        for article in articles[:10]:
            link_of_news = article.find('a', {'class': 'title'})['href']
            title = article.find('a', {'class': 'title'}).text
            data_time_value = article.find('span', {'aria-label': True}).text
            media_name_ = article.find('div', {'class': 'source set_top'})
            if media_name_:
                img_tag = media_name_.find('img')
                if img_tag and img_tag.has_attr('title'):
                    media_name = img_tag['title']
                else:
                    media_name = media_name_.text.strip()
            else:
                media_name = 'Unknown'
            article_lst.append((link_of_news, title, data_time_value, media_name))
       

    return article_lst