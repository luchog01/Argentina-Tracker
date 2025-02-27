import requests

# Define the URL
url = "https://api.cafci.org.ar/fondo/420/clase/773/ficha"

# Define headers exactly as provided
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en,es-ES;q=0.9,es;q=0.8",
    "cache-control": "no-cache",
    "origin": "https://www.cafci.org.ar",
    "pragma": "no-cache",
    "referer": "https://www.cafci.org.ar/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
}

try:
    # Make the request
    response = requests.get(url, headers=headers)
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")