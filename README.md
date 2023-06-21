# News Scraper and Summarizer
The News Scraper and Summarizer is a Python application that allows you to scrape news articles from various sources 
and summarize them using Natural Language Processing (NLP) APIs. This tool helps you stay updated with the latest news by providing concise summaries of news articles.

# Features
Scrapes news articles from sources.
Utilizes OpenAI's APIs for text summarization.
Provides concise summaries of news articles.

# Requirements
Python 3.x
Libraries: requests, BeautifulSoup 
# API 
OpenAI API

# Sample Output
```
{
    "title": "Epsom College deaths: Teacher and daughter shot by husband, police believe",
    "link": "https://www.bbc.co.uk/news/uk-england-surrey-64544884?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 14:08:37 GMT",
    "content": ": Head teacher of Epsom College is shot dead by her husband, before he kills their daughter and takes his own life with the same gun. Police believe the family was targeted."
  },
  {
    "title": "Nicola Bulley search expert says case is most unusual",
    "link": "https://www.bbc.co.uk/news/uk-england-lancashire-64549298?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 10:22:38 GMT",
    "content": ": A search expert says he has not seen such an unusual case in 20 years of his work.The police are focusing their efforts on the river path which leads from the fields back to Garstang Road - for that they need drivers and cyclists who travelled that way on the morning of 27 January to make contact."
  },
  {
    "title": "Harry Styles' Grammys routine went in wrong direction, dancers reveal",
    "link": "https://www.bbc.co.uk/news/entertainment-arts-64552569?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 09:44:02 GMT",
    "content": ": Two of Harry Styles' dancers say they had to quickly adapt their Grammy Awards routine after the stage started spinning in the wrong direction."
  },
  {
    "title": "Ukraine war: Russians seen reinforcing east ahead of offensive",
    "link": "https://www.bbc.co.uk/news/world-europe-64551937?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:18:55 GMT",
    "content": "- The Ukrainian governor of Luhansk region says tens of thousands of Russians are being sent to eastern Ukraine as part of an offensive planned after 15 February. There is widespread scepticism of significant Russian success."
  },
  {
    "title": "What three luxury homes reveal about who owns UK property",
    "link": "https://www.bbc.co.uk/news/uk-64536926?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 00:04:34 GMT",
    "content": ": Half of companies required to declare who is behind them failed to do so, and the government has yet to equip Companies House with the teeth and resources to apply these in practice."
  },
  {
    "title": "Mark Cavendish robbery: Two men jailed for raid at cyclist's home",
    "link": "https://www.bbc.co.uk/news/uk-england-essex-64541757?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:34:25 GMT",
    "content": ": Two men have been jailed for a knifepoint robbery at the family home of elite cyclist Mark Cavendish."
  },
  {
    "title": "Richard Sharp: BBC chairman denies arranging loan for Boris Johnson",
    "link": "https://www.bbc.co.uk/news/entertainment-arts-64552571?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:38:50 GMT",
    "content": ": Richard Sharp denies helping arrange a loan for Boris Johnson when he was prime minister."
  },
  {
    "title": "Turkey earthquake: The survivors' choice - danger inside or freezing outside",
    "link": "https://www.bbc.co.uk/news/world-europe-64555959?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 12:44:11 GMT",
    "content": "Earthquake survivors in Turkey, Syria and elsewhere recount stories of lost loved ones, injuries, and the difficult task of finding them amidst collapsed buildings and debris."
  },
  {
    "title": "Turkey earthquake: Three Britons missing, says Foreign Office",
    "link": "https://www.bbc.co.uk/news/uk-64557448?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:30:31 GMT",
    "content": ": 35 British nationals are missing in the earthquake in Turkey. The Foreign Office is supporting them directly. The likelihood of large-scale British casualties remains low."
  },
  {
    "title": "Turkey earthquake: Erdogan announces three-month state of emergency in quake area",
    "link": "https://www.bbc.co.uk/news/world-europe-64548985?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:04:53 GMT",
    "content": "- Turkish President Erdogan has announced a three-month state of emergency in 10 provinces worst-affected by an earthquake."
  },
  {
    "title": "Turkey and Syria earthquake: \u2018It was like a doomsday scenario'",
    "link": "https://www.bbc.co.uk/news/world-middle-east-64538295?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 10:30:41 GMT",
    "content": "In Syria, the 7.8-magnitude earthquake has killed dozens of people and injured hundreds more. International organisations are struggling to reach the affected areas due to a shortage of resources."
  },
  {
    "title": "Turkey earthquake: Before and after images show extent of destruction",
    "link": "https://www.bbc.co.uk/news/world-europe-64544998?at_medium=RSS&at_campaign=KARANGA",
    "published": "Tue, 07 Feb 2023 13:09:12 GMT",
    "content": ":\n\nAt least 5,000 people have been killed in a series of earthquakes and aftershocks in Turkey, Syria and the surrounding region."
  },
```
