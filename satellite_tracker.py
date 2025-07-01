import requests

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

try:
    response = requests.get(url) #Pulls data from the url specified above
    response.raise_for_status() #Check for HTTP request errors
    satellites = response.json() #Since the data from the website is in JSON format, this line turns that JSON text into a Python list of dictionaries

    print("First 10 Active Satellites:\n") #Prints the specified title
    for i, sat in enumerate(satellites[:10], start=1): #"Look at the first 10 satellites in our list (satellites[:10])." Enumerate(..., start=1) counts them as it goes (1,2,3,...)
        print(f"{i}. {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #This prints the satellite's number (i), its name (sat['OBJECT_NAME']), and its ID (sat['NORAD_CAT_ID'])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}") #This will print an error message if there is a problem with the HTTP request, such as a connection error or timeout.
    exit(1) #This will exit the program if there is an error with the HTTP request.

choice = input("\nEnter the number of the satellite you want details for (1-10): ") #This prompts the user to enter a number corresponding to one of the first 10 satellites listed above.

try:
    index = int(choice) - 1 #Convert user input to the right list index
    if not (0 <= index < 10): #Check if the index is within the range of the first 10 satellites
        print("Please pick a number between 1 and 10.") #This will print an error message if the user input is not a valid number (e.g., if they enter a number less than 1 or greater than 10).
    else:    
        sat = satellites[index]
        print("\nSatellite Details: ") #Prints the title for the satellite details
        print(f"Name: {sat['OBJECT_NAME']}") #Prints the name of the selected satellite
        print(f"NORAD ID: {sat['NORAD_CAT_ID']}") #Prints the NORAD ID of the selected satellite
        print(f"International Designator: {sat['OBJECT_ID']}") #Prints the international designator of the selected satellite
        print(f"Epoch: {sat['EPOCH']}") #Prints the epoch time of the selected satellite
        print(f"Inclination: {sat['INCLINATION']} degrees") #Prints the inclination of the selected satellite
        print(f"Eccentricity: {sat['ECCENTRICITY']}") #Prints the eccentricity of the selected satellite
        print(f"Mean Motion: {sat['MEAN_MOTION']} revs/day") #Prints the mean motion of the selected satellite
        print(f"RA Ascending Node: {sat['RA_OF_ASC_NODE']} degrees") #Prints the right ascension of the ascending node of the selected satellite
        print(f"Argument of Perigee: {sat['ARG_OF_PERICENTER']} degrees") #Prints the argument of perigee of the selected satellite
        print(f"Mean Anomaly: {sat['MEAN_ANOMALY']} degrees") #Prints the mean anomaly of the selected satellite
        
except ValueError:
    print("Please enter a valid number.") #This will print an error message if the user input is not a valid integer (e.g., if they enter a letter or symbol).



