import requests

# Set the URL of the ThingSpeak API
url = "https://api.thingspeak.com/update"

#Dummy data to test the system
temperature=30
humidity=72
rain_value=1

# Set the parameters of the request
params = {
    "api_key": "INSERT_API_KEY",
    "field1": temperature,
    "field2": humidity,
    "field3": rain_value
}
# Send the request to ThingSpeak
response = requests.get(url, params=params)
print("Data Sent Succesfully")
# Print the response from ThingSpeak
print(response.content)