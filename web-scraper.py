import requests
from bs4 import BeautifulSoup

page_content = requests.get("https://admission.funaab.edu.ng/2026/")

soup = BeautifulSoup(page_content.text, "html.parser")

heading = soup.find("h1")

sub_heading = soup.find("h2")

links = soup.find_all("a")

scraped_links = []

print(heading.text)
print(sub_heading.text)

for link in links:
    link_text = link.get_text(strip=True)
    url = link.get("href")
    if link_text and url:
        scraped_links.append({
            "text": link_text,
            "url": url
        })

for scraped_link in scraped_links:
    print(scraped_link['text'])