import requests
import json

# Define the new job details
new_job = {
        'id': 3,
        'position': 'Data Sceibntist',
        'years': '8',
        'skills': 'R Python CNN ML OpenAi LLM Visualization Tools',
        'description': 'Highly Self Motivated and Highly skilled in Data Science',
        'salary': 1200
    }


# Convert the new job details to JSON format
new_job_json = json.dumps(new_job)

# Make a POST request to the endpoint
response = requests.post('https://jobslistapi.johnfuturs.repl.co/jobs', json=new_job_json)

# Check the response status code
if response.status_code == 201:
    print('New job successfully inserted.')
else:
    print('Failed to insert the new job.')
    

url = 'https://jobslistapi.johnfuturs.repl.co/jobs'
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    print(products)
else:
    print('Error:', response.status_code)
