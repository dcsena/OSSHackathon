import requests
from bs4 import BeautifulSoup

BASE_URL = "https://jobs.lever.co/"
TITLE_CLASS_NAME = "posting-title"
OUTPUT_DIR = "resources/"

COMPANIES = [
    "prelim", "netflix", "Anthropic", "mistral",
    "levelai", "welocalize", "weride", "whoop",
    "unlikely", "shieldai", "bostondynamicsaiinstitute",
    "sanctuary", "CopyAI", "cohere", "tonal",
    "kungfu", "futureof-life", "percipient",
    "covariant", "AIFund", "launchlabs", "people-ai",
    "cognite", "WisprAI", "aicamp", "tri", "heretic-fund",
    "pano", "fiddlerlabs", "flawlessai"
]  # site:https://jobs.lever.co/ AI

def get_job_links_for_company(company_name):
    page = requests.get(BASE_URL + company_name)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all('a', class_=TITLE_CLASS_NAME)
    return [link.get('href') for link in links if link.get('href')]

def get_all_jobs_for_company(company_name):
    job_links = get_job_links_for_company(company_name)
    for job_link in job_links:
        page = requests.get(job_link)
        job_id = job_link.split("/")[-1]
        page_url = "{}/{}-{}.html".format(OUTPUT_DIR, company_name, job_id)
        with open(page_url, 'w', encoding='utf-8') as file:
            file.write(str(page.content))

def save_all_jobs():
    for company in COMPANIES:
        get_all_jobs_for_company(company)


if __name__ == "__main__":
    save_all_jobs()