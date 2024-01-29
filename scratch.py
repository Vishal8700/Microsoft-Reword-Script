import webbrowser
import time
import random

def search_random_query():
    # List of random queries
    queries = [
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

    url= [
        '&cvid=d34057db5781462d8ea8311ced98c5c8&gs_lcrp=EgZjaHJvbWUqBggBEC4YQDIGCAAQRRg5MgYIARAuGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAuGEAyBggIEEUYQdIBCDI5MzFqMGoxqAIAsAIA&FORM=ANAB01&PC=ASTS',
        '&cvid=abb42c33945b4f37af413e4f66aabbde&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBBzcwOWowajGoAgCwAgA&FORM=ANAB01&PC=ASTS',
        '&cvid=f7c8bcdd4d7f401fb6727fbbed93fbc8&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQg0MjIyajBqMagCALACAA&FORM=ANAB01&PC=ASTS',
        '&cvid=31f0bf14218e4794aa6389830d1f91b4&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgxMTA2ajBqMagCALACAA&FORM=ANAB01&PC=ASTS',
        '&cvid=ac503f89276b45a5864e2c8b9c314f83&gs_lcrp=EgZjaHJvbWUqBggCEAAYQDIGCAAQRRg5MgYIARAAGEAyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDQxMDFqMGoxqAIAsAIA&FORM=ANAB01&PC=ASTS',
        '&cvid=d7bffdadd5c14695a21bd8591a422325&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQRRg8MgYICBBFGEHSAQc5MzdqMGoxqAIAsAIA&FORM=ANAB01&PC=ASTS',
        'https://www.bing.com/search?q=mnc&cvid=ef44c9bd4e2845a5aac724bc1cbbaa2f&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgxMDI1ajBqMagCALACAA&FORM=ANAB01&PC=ASTS',
    ]
    for query in queries:

        random_url = random.choice(url)


        search_url = f'https://www.bing.com/search?q={query}{random_url}'


        webbrowser.open(search_url)


        time.sleep(5)



if __name__ == "__main__":
    search_random_query()
