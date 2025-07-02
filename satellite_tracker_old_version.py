import requests #This imports the requests library, which allows us to make HTTP requests to retrieve data from a URL.

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

# The following code retrieves satellite data from the specified URL and allows the user to search for satellites by name or NORAD ID.
# It uses the requests library to fetch the data, which is in JSON format, and then parses it into a Python list of dictionaries.

try:
    response = requests.get(url)
    response.raise_for_status()
    satellites = response.json()

    print("\nHow would you like to search for a satellite?")
    print("1. By Name")
    print("2. By NORAD ID")
    search_type = input("Enter 1 or 2: ")
    matches = [] #This initializes an empty list called matches, which will be used to store the satellites that match the user's search criteria.

    # The following code block handles the user's search input based on their choice.
    # If the user chooses "1" (name), it prompts them to enter a satellite name
    # If the user chooses "2" (NORAD ID), it prompts them to enter a NORAD ID
    # If the user enters an invalid option, it prints an error message and exits the program

    if search_type == "1":
        search = input("\nEnter a satellite name to search for: ")
        for sat in satellites:
            if search.lower() in sat['OBJECT_NAME'].lower(): #The .lower() method makes the search case-insensitive.
                matches.append(sat)
    elif search_type == "2":
        search = input("\nEnter a NORAD ID to search for: ").strip() #The .strip() method removes any leading or trailing whitespace from the input.
        for sat in satellites:
            if str(sat['NORAD_CAT_ID']) == search: 
                matches.append(sat)
    else:
        print("Invalid option. Please enter 1 or 2.")
        exit(1)

    # The following code block checks if any matches were found based on the user's search criteria.
    # If matches are found, it prints the number of matches and details for each match.
    # If no matches are found, it prints a message indicating that no satellites were found with the specified name or NORAD ID.
    # If the user selects a match, it prints detailed information about the selected satellite.

    if matches:
        print(f"\nFound {len(matches)} satellite(s) matching your search:\n")
        for i, sat in enumerate(matches[:10], start=1): #This loops through the first 10 matches (or fewer if there are not 10) and prints their details.
            print(f"{i}. {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})") #This prints the satellite's number (i), its name (sat['OBJECT_NAME']), and its ID (sat['NORAD_CAT_ID']).

        pick = input("\nEnter the number of the satellite you want details for (or press Enter to skip): ")
        if pick.isdigit(): #This checks if the user input is a digit
            pick_index = int(pick) - 1 #Convert user input to the right list index
            if 0 <= pick_index < len(matches[:10]): #Check if the index is within the range of the matches
                sat = matches[pick_index] #Get the selected satellite from the matches list
                print(f"\nYou picked: {sat['OBJECT_NAME']} (NORAD ID: {sat['NORAD_CAT_ID']})")
                print(f"International Designator: {sat['OBJECT_ID']}")
                print(f"Epoch: {sat['EPOCH']}")
                print(f"Inclination: {sat['INCLINATION']} degrees")
                print(f"Eccentricity: {sat['ECCENTRICITY']}")
                print(f"Mean Motion: {sat['MEAN_MOTION']} revs/day")
                print(f"RA Ascending Node: {sat['RA_OF_ASC_NODE']} degrees")
                print(f"Argument of Perigee: {sat['ARG_OF_PERICENTER']} degrees")
                print(f"Mean Anomaly: {sat['MEAN_ANOMALY']} degrees")
            else:
                print("Number out of range.") #This will print an error message if the user input is less than 1 or greater than 10.
        else:
            print("No satellite selected.")
    else:
        print("No satellites found with that name.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}") #This will print an error message if there is a problem with the HTTP request, such as a connection error or timeout.
    exit(1)