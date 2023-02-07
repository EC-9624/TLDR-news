import os
import openai
import json
from dotenv import load_dotenv
from Scraper import final_list
import time
load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")


def limit_rate_of_requests():
    requests = []
    rate_limit = 10
    time_period = 60  # in seconds
    current_time = time.time()
    requests.append(current_time)

    # Remove any requests that were made more than the time period ago
    requests = [r for r in requests if current_time - r < time_period]

    # Check if the number of requests in the current time period is within the rate limit
    if len(requests) > rate_limit:
        raise Exception("Rate limit exceeded. Try again later.")


def summarize_text(text):
    response = openai.Completion.create(
        model="text-curie-001",
        prompt=text+"TL;DR",
        temperature=0.7,
        max_tokens=80,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )

    summary = response.choices[0].text.strip()
    return summary


def summarize_list():
    for d in final_list:
        try:
            limit_rate_of_requests()
            d['content'] = summarize_text(d['content'])
        except Exception as e:
            print(e)


summarize_list()


def writeJson():

    filename = "data.json"
    with open(filename, 'w') as file:
        file.write(json.dumps(final_list, indent=2))


writeJson()
