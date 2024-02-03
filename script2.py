import webbrowser
import time
import random
import secrets
def generate_random_cvid(length=32):
    return

random_cvid = generate_random_cvid()
print(random_cvid)

def search_random_query():
    # List of random queries
    queries = ['facebook',
               'youtube',
               'google',
               'gmail',
               'bing homepage quiz',
               'amazon',
               'bing',
               'news for you',
               'yahoo',
               'ebay',
               'top stories',
               'facebook log in',
               'weekly quiz',
               'yahoo mail',
               'walmart',
               'us news',
               'fox news',
               'bing weekly quiz',
               'google maps',
               'nfl',
               'covid-19',
               'news',
               'weather',
               'maps',
               'bing',
               'coronavirus',
               'cnn',
               'msn',
               'fox news',
               'google']


    # Loop to search random queries
    for query in queries:
        # Form the search URL
        id=secrets.token_hex(32)
        search_url = f'https://www.bing.com/search?q={query}&cvid={id}&gs_lcrp=EgZjaHJvbWUqBggCEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDQxMDFqMGoxqAIAsAIA&FORM=ANAB01&PC=ASTS'

        # Open the default web browser with the search URL
        webbrowser.open(search_url)

        # Pause for 10 seconds before the next search
        time.sleep(20)

if __name__ == "__main__":
    search_random_query()
