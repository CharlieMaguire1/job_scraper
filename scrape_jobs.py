import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    url = 'https://www.indeed.co.uk/jobs?q=data+analysis&1=United+Kingdom'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 01.0.4472.124 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Taking the job postings and relevant details
    job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
    
    jobs_data = []
    for job in job_listings:
        title = job.find('h2', class_='title').text.strip()
        company = job.find('span', class_='company').text.strip()
        location = job.find('span', class_='location').text.strip()
        summary = job.find('div', class_='summary').text.strip()
        
        jobs_data.append({'Title': title, 'Company': company, 'location': location, 'Summary': summary})
    
    #Convert to DataFrame
    df = pd.DataFrame(jobs_data)
    df.to_csv('job_postings.csv', index=False)

if __name__ == '__main__':
    scrape_jobs()
    