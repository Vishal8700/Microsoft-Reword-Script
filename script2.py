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
    queries = [
        'python programming',
        'machine learning',
        'web development',
        'data science',
        'artificial intelligence',
        'openai',
        'random topic',
        'gross domastic product',
        'india economy',
        'database',
        'operating system',
        'computer science',
        'placement',
        'vs code',
        'python 3.11'
        'android studio',
        'Shovels',
        'Rhinoceros',
        'Radiology',
        'Potatoes',
        'Skull',
        'Weaving',
        'Cricket',
        'Europe',
        'Hockey',
        'Water Skiing',
        'Coffin',
    ]

    # Loop to search random queries
    for query in queries:
        # Form the search URL
        id=secrets.token_hex(32)
        search_url = f'https://www.bing.com/search?q={query}&cvid={id}&gs_lcrp=EgZjaHJvbWUqBggCEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDQxMDFqMGoxqAIAsAIA&FORM=ANAB01&PC=ASTS'

        # Open the default web browser with the search URL
        webbrowser.open(search_url)

        # Pause for 10 seconds before the next search
        time.sleep(10)

if __name__ == "__main__":
    search_random_query()
