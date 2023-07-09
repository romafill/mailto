import sys
import requests

# Get the base URL from the command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <base_url>")
    sys.exit(1)
base_url = sys.argv[1]

# Define the authentication cookie(s)
cookie = {"wf_auth": "WzEs <snip> g9Il0="}

# Send a GET request to the page and save the response
response = requests.get(base_url, cookies=cookie)

# Find all occurrences of the "<a href="mailto:"" string in the response
start_index = 0
mailtos = []
while True:
    start_index = response.text.find("<a href=\"mailto:", start_index)
    if start_index == -1:
        break
    end_index = response.text.find("\"", start_index + 16)  # Find the next double quote after the "mailto:" string
    mailto = response.text[start_index + 16 : end_index]
    mailtos.append(mailto)
    start_index = end_index

# Print the email addresses
for email in mailtos:
    print(email)
