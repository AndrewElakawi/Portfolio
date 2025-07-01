import requests #This imports the requests library, which allows us to make HTTP requests to retrieve data from a URL.

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

try:
    response = requests.get(url) #Pulls data from the url specified above
    response.raise_for_status() #Check for HTTP request errors
    satellites = response.json() #Since the data from the website is in JSON format, this line turns that JSON text into a Python list of dictionaries

    print("\nHow would you like to search for a satellite?")
    print("1. By Name") #This option allows the user to search for a satellite by its name.
    print("2. By NORAD ID") #This option allows the user to search for a satellite by its NORAD ID.
    search_type = input("Enter 1 or 2: ") #This prompts the user to choose how they want to search for a satellite, either by name or by NORAD ID.
    matches = [] #This initializes an empty list called matches, which will be used to store the satellites that match the user's search criteria.
    
    if search_type == "1":
        search = input("\nEnter a satellite name to search for: ") #This prompts the user to enter a satellite name to search for.
        for sat in satellites: #This loops through each satellite in the list of satellites.
            if search.lower() in sat['OBJECT_NAME'].lower():
                matches.append(sat) #This checks if the search term is in the satellite's name (sat['OBJECT_NAME']). The .lower() method makes the search case-insensitive. If a match is found, it adds the satellite to the matches list.
    elif search_type == "2":
        search = input("\nEnter a NORAD ID to search for: ").strip()
        for sat in satellites:
            if str(sat['NORAD_CAT_ID']) == search: #This prompts the user to enter a NORAD ID to search for.
                matches.append(sat) #If a match is found, it adds the satellite to the matches list.
    else:
        print("Invalid option. Please enter 1 or 2.")
        exit(1) #If the user enters an invalid option, this will print an error message and exit the program.

    if matches:
        print(f"\nFound {len(matches)} satellite(s) matching your search:\n") #This prints the number of matches found based on the user's search criteria.
        for i, sat in enumerate(matches[:10], start=1): #This loops through the first 10 matches (or fewer if there are not 10) and prints their details.
            print(f"{i}. {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #This prints the satellite's number (i), its name (sat['OBJECT_NAME']), and its ID (sat['NORAD_CAT_ID']).

        pick = input("\nEnter the number of the satellite you want details for (or press Enter to skip): ") #This prompts the user to enter a number corresponding to one of the matches listed above, or to press Enter to skip.
        if pick.isdigit(): #This checks if the user input is a digit (i.e., a number).
            pick_index = int(pick) - 1 #Convert user input to the right list index
            if 0 <= pick_index < len(matches[:10]): #Check if the index is within the range of the matches
                sat = matches[pick_index] #Get the selected satellite from the matches list
                print(f"\nYou picked: {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #Prints the name and ID of the selected satellite
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