import requests

count = 0
starts = list(x for x in range(1,100,10))
for start in starts :
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "<Your API Key>"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "018212539862037696382:-xa61bkyvao"
    query = "corona"
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    # url = 'https://cse.google.com/cse?cx=018212539862037696382:-xa61bkyvao'
    params = {'num': 10, 'start': start}

    res = requests.get(url, params=params).json()
    # print(res)
    items = res['items']
    for item in items:
        count +=1
        title = item['title']
        link = item['link'].replace('https://','').replace('www.','').strip()
        judul = item['pagemap']['metatags'][0]['twitter:title'].strip()
        image_scr = item['pagemap']['cse_image'][0]['src'].replace('https://','').strip()

        print(judul)
        print('Link         : ', link)
        print('Image Source : ', image_scr,'\n', count)