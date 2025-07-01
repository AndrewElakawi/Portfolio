import requests

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

try:
    response = requests.get(url) #Pulls data from the url specified above
    response.raise_for_status() #Check for HTTP request errors
    satellites = response.json() #Since the data from the website is in JSON format, this line turns that JSON text into a Python list of dictionaries

    search = input("\nEnter a satellite name to search for: ") #This prompts the user to enter a satellite name to search for.
    matches = []
    for sat in satellites: #This loops through each satellite in the list of satellites.
        if search in sat['OBJECT_NAME'].lower(): #This checks if the search term is in the satellite's name (sat['OBJECT_NAME']). The .lower() method makes the search case-insensitive.
            matches.append(sat) #If a match is found, it adds the satellite to the matches list.

    if matches: #If there are any matches found, this block will execute.
        print(f"nFound {len(matches)} satellite(s) matching '{search}':\n") #This prints the number of matches found and the search term.
        for i, sat in enumerate(matches[:10], start=1): #This loops through the first 10 matches (or fewer if there are not 10) and prints their details.
            print(f"{i}. {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #This prints the satellite's number (i), its name (sat['OBJECT_NAME']), and its ID (sat['NORAD_CAT_ID']).

        pick = input("\nEnter the number of the satellite you want details for (or press Enter to skip): ") #This prompts the user to enter a number corresponding to one of the matches listed above, or to press Enter to skip.
        if pick.isdigit(): #This checks if the user input is a digit (i.e., a number).
            index = int(pick) - 1 #Convert user input to the right list index
            if 0 <= index < len(matches): #Check if the index is within the range of the matches
                sat = matches[index] #Get the selected satellite from the matches list
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
            else:
                print("Number out of range.") #This will print an error message if the user input is not a valid number (e.g., if they enter a number less than 1 or greater than 10).
        else:
            print("No satellite selected.") #If no valid number is entered, this will skip displaying details.
    else:
        print("No satellites found with that name.") #If no matches are found, this prints a message indicating that no satellites were found with the specified name.
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}") #This will print an error message if there is a problem with the HTTP request, such as a connection error or timeout.
    exit(1) #This will exit the program if there is an error with the HTTP request.