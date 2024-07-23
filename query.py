import requests

# Define the URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/query"

# Define the query to send
query = {"query": "From which college he has done his masters education??"}

# Set the headers to indicate the content type
headers = {"Content-Type": "application/json"}

# Send the POST request
response = requests.post(url, json=query, headers=headers)

# Print the response from the server
print(response.json())
