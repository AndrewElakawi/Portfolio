import requests

try:
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json" # Download active satellites list from Celestrak
    response = requests.get(url) #Pulls data from the url specified above
    response.raise_for_status() #Check for HTTP request errors
    satellites = response.json() #Since the data from the website is in JSON format, this line turns that JSON text into a Python list of dictionaries

    print("First 10 Active Satellites:\n") #Prints the specified title
    for i, sat in enumerate(satellites[:10], start=1): #"Look at the first 10 satellites in our list (satellites[:10])." Enumerate(..., start=1) counts them as it goes (1,2,3,...)
        print(f"{i}. {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #This prints the satellite's number (i), its name (sat['OBJECT_NAME']), and its ID (sat['NORAD_CAT_ID'])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}") #This will print an error message if there is a problem with the HTTP request, such as a connection error or timeout.
