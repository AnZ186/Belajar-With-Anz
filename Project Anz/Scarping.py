import requests
from bs4 import BeautifulSoup
import re

def scrape_anoboy(search_query):
    url = f"https://anoboy.app/search?keyword={search_query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    anime_list = []

    # Find all anime entries. This is highly dependent on the website structure and may break if Anoboy changes its design.
    anime_containers = soup.find_all('div', class_=re.compile(r'anime-item')) # Adjust class name if necessary

    for container in anime_containers:
        title_element = container.find('a', class_='anime-title')
        if title_element:
            title = title_element.text.strip()
            link = 'https://anoboy.app' + title_element['href']
            img_element = container.find('img')
            image = img_element['src'] if img_element and 'src' in img_element.attrs else None
            anime_list.append({'title': title, 'link': link, 'image': image})

    return anime_list

if __name__ == "__main__":
    search_term = input("Masukkan kata kunci pencarian: ")
    results = scrape_anoboy(search_term)

    if results:
        print("\nHasil Pencarian:")
        for anime in results:
            print(f"Judul: {anime['title']}")
            print(f"Link: {anime['link']}")
            print(f"Gambar: {anime['image']}")
            print("-" * 20)
    else:
        print("Tidak ditemukan anime yang sesuai.")