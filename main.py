import requests
from bs4 import BeautifulSoup

def search_sites(username):
    sites = ['https://twitter.com/', 'https://www.instagram.com/', 'https://www.facebook.com/', 'https://www.linkedin.com/', 'https://www.snapchat.com/']
    results = {}
    for site in sites:
        url = site + username
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            if soup.find('title'):
                results[site] = soup.find('title').text
    return results

username = input('Enter a username: ')
results = search_sites(username)
print(results)
