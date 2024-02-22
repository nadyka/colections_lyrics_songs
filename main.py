import requests
from bs4 import BeautifulSoup




def find_lyrics_link(website, singer, song):
    # Format the query string
    query = f"{singer} {song}".replace(' ', '+')
    url = f"https://www.google.com/search?q=site:{website}+{query}"
    
    # Send the HTTP request
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the search result links
    links = soup.find_all('a')
    
    # Extract the first link
    for link in links:
        href = link.get('href')
        if "url?q=" in href and not "webcache" in href:
            # Clean the URL
            clean_url = href.split("url?q=")[1].split("&sa=U")[0]
            if website in clean_url:
                return clean_url
    return "No link found"



print(find_lyrics_link('https://lyrics.lyricfind.com', 'Elton John', 'Candle in the Wind'))


