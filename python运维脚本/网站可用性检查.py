import requests

website = "https://www.baiu.com"

try:
    response = requests.get(website)
    if response.status_code == 200:
        print("Website is accessible.")
    else:
        print(f"Website is down. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Error connecting to the website:", str(e))
