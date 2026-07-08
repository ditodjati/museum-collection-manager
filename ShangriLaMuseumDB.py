# List containing collection data in the form of dictionaries
data_collection = [
    {"Collection ID": "F01", "Title": "Tyrannosaurus Rex Fossil", "Region of Origin": "North America", "Place Discovered": "Dakota, United States of America", "Era": "Cretaceous", "Year Discovered": 1990, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F02", "Title": "Mammoth Tusk", "Region of Origin": "Eurasia", "Place Discovered": "Siberia, Russia", "Era": "Pleistocene", "Year Discovered": 2003, "Type": "Fossil", "Status": "Under Restoration"},
    {"Collection ID": "F03", "Title": "Trilobite Fossil", "Region of Origin": "Africa", "Place Discovered": "Morocco", "Era": "Cambrian", "Year Discovered": 1995, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F04", "Title": "Ichthyosaur Skeleton", "Region of Origin": "Europe", "Place Discovered": "Holzmaden, Germany", "Era": "Jurassic", "Year Discovered": 1890, "Type": "Fossil", "Status": "Displayed"},
    {"Collection ID": "F05", "Title": "Megatherium Claw", "Region of Origin": "South America", "Place Discovered": "Argentina", "Era": "Pleistocene", "Year Discovered": 1788, "Type": "Fossil", "Status": "Stored"},
    {"Collection ID": "W01", "Title": "Oda Nobunaga's Katana: Heshikiri Hasebe", "Region of Origin": "Japan", "Place Discovered": "Kyoto, Japan", "Era": "Sengoku Period", "Year Discovered": 1987, "Type": "Weapon", "Status": "Stored"},
    {"Collection ID": "W02", "Title": "Napoleon Bonaparte's Saber", "Region of Origin": "Europe", "Place Discovered": "Paris, France", "Era": "Napoleonic Wars", "Year Discovered": 1815, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W03", "Title": "Viking Battle Axe", "Region of Origin": "Scandinavia", "Place Discovered": "Norway", "Era": "Viking Age", "Year Discovered": 1972, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W04", "Title": "Roman Gladius", "Region of Origin": "Europe", "Place Discovered": "Pompeii, Italy", "Era": "Roman Republic", "Year Discovered": 1875, "Type": "Weapon", "Status": "Displayed"},
    {"Collection ID": "W05", "Title": "Samurai Armor", "Region of Origin": "Japan", "Place Discovered": "Osaka, Japan", "Era": "Edo Period", "Year Discovered": 1923, "Type": "Weapon", "Status": "Stored"},
    {"Collection ID": "A01", "Title": "Venus of Willendorf", "Region of Origin": "Europe", "Place Discovered": "Willendorf, Austria", "Era": "Paleolithic", "Year Discovered": 1908, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A02", "Title": "Rosetta Stone", "Region of Origin": "Africa", "Place Discovered": "El-Rashid (Rosetta), Egypt", "Era": "Ptolemaic Period", "Year Discovered": 1799, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A03", "Title": "Terracotta Warrior", "Region of Origin": "China", "Place Discovered": "Xi'an, China", "Era": "Qin Dynasty", "Year Discovered": 1974, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A04", "Title": "Mayan Calendar Stone", "Region of Origin": "Mesoamerica", "Place Discovered": "Mexico City, Mexico", "Era": "Postclassic Period", "Year Discovered": 1790, "Type": "Artifact", "Status": "Displayed"},
    {"Collection ID": "A05", "Title": "Sumerian Cuneiform Tablet", "Region of Origin": "Middle East", "Place Discovered": "Iraq", "Era": "Bronze Age", "Year Discovered": 1929, "Type": "Artifact", "Status": "Stored"},
    {"Collection ID": "P01", "Title": "Mona Lisa", "Region of Origin": "Europe", "Place Discovered": "Florence, Italy", "Era": "Renaissance", "Year Discovered": 1517, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P02", "Title": "The Starry Night", "Region of Origin": "Europe", "Place Discovered": "Saint-Rémy-de-Provence, France", "Era": "Post-Impressionism", "Year Discovered": 1889, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P03", "Title": "The Great Wave off Kanagawa", "Region of Origin": "Japan", "Place Discovered": "Japan", "Era": "Edo Period", "Year Discovered": 1831, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P04", "Title": "Guernica", "Region of Origin": "Europe", "Place Discovered": "Madrid, Spain", "Era": "Modern Art", "Year Discovered": 1937, "Type": "Painting", "Status": "Displayed"},
    {"Collection ID": "P05", "Title": "The Last Supper", "Region of Origin": "Europe", "Place Discovered": "Milan, Italy", "Era": "Renaissance", "Year Discovered": 1498, "Type": "Painting", "Status": "Displayed"}
]

# Create an empty set to store used IDs
used_ids = set()

# Import the 'tabulate' library to print tables neatly
from tabulate import tabulate

# Function to display the welcoming greeting
def greeting():
    print("""
          Welcome to Shangri-La Museum Application
          """)

# Function to display the main menu
def main_menu():

    # Loop to keep displaying the menu until the user chooses to exit
    while True:
        
        # Display menu options
        print("""
        Menu:
              1. Show Collection
              2. Add Collection
              3. Update Collection
              4. Delete Collection
              5. Exit Program
              """)
        try: # Catch errors if the input is not a number
            menu_input = int(input("Enter the Menu Number You Want to Run: ").strip()) # Read menu input and remove spaces
            if menu_input == 1: # If user selects 1, run the read_menu() function
                read_menu()
            elif menu_input == 2: # If user selects 2, run the create_menu() function
                create_menu()
            elif menu_input == 3: # If user selects 3, run the update_menu() function
                update_menu()
            elif menu_input == 4: # If user selects 4, run the delete_menu() function
                delete_menu()
            elif menu_input == 5: # If user selects 5, break the loop and end the program
                print("""
        Thank You for Using Our Service!
        Exiting Program...
                      """)
                break
            else: # If the input is outside the 1-5 range
                print("The option you entered is invalid! Please choose between 1-5.")
                continue
        except ValueError: 
            print("The option you entered is invalid! Please enter a number.")

# Function to display the 'Read Data' submenu
def read_menu():
    while True:
        print("""
        Read Data Menu:
            1. Show All Collections
            2. Search by Collection ID
            3. Search by Other Attributes
            4. Back to Main Menu
        """)

        menu_input = input("Enter the Menu Number You Want to Run: ").strip()

        if menu_input == "1": # Display all collections
            if not data_collection: # Check if the collection is empty
                print("No Collections Available.")
            else:
                read_data_collection() # Display all collections
        
        elif menu_input == "2": # Search based on Collection ID
            if not data_collection:
                print("No Collections Available.")
            else:
                collection_id = input("Enter Collection ID: ").strip()
                read_data_collection("Collection ID", collection_id)
        
        elif menu_input == "3": # Search based on other attribute values
            if not data_collection:
                print("No Collections Available.")
            else:
                search_by_attribute()
        
        elif menu_input == "4": # Return to the main menu
            print("Returning to Main Menu...")
            break
        
        else:
            print("The option you entered is invalid! Please choose between 1-4.")

# Function to read data with or without filters
def read_data_collection(filter_option=None, filter_value=None):
    if not data_collection: # If data_collection is empty, display a message and exit the function
        print("No Collections Available.")
        return
    
    filtered_data = [] # Empty list to store data that matches the filter

    for i in range(len(data_collection)): # Loop through each item in data_collection
        item = data_collection[i] # Access the current element in the loop

        # If a filter is provided, perform data matching
        if filter_option and filter_value:
            if filter_option == "Collection ID": # Filter by Collection ID (must match exactly)
                if str(item["Collection ID"]) != filter_value:
                    continue # Skip iteration if it does not match
            elif filter_option == "Title":
                if filter_value not in item["Title"]: # Filter by Title (partial match)
                    continue
            elif filter_option == "Region of Origin":
                if filter_value not in item["Region of Origin"]: # Filter by Region of Origin
                    continue
            elif filter_option == "Place Discovered":
                if filter_value not in item["Place Discovered"]: # Filter by Place Discovered
                    continue
            elif filter_option == "Era":
                if filter_value not in item["Era"]: # Filter by Era
                    continue
            elif filter_option == "Type":
                if filter_value not in item["Type"]: # Filter by Type
                    continue
            elif filter_option == "Status":
                if filter_value not in item["Status"]: # Filter by Status
                    continue
            elif filter_option == "Year Discovered": # Filter by Year Discovered
                try:
                    if int(item["Year Discovered"]) != int(filter_value): # Compare as numbers
                        continue
                except ValueError: # Handle error if input is not a number
                    print("Invalid year format! Please enter a number.")
                    return
        
        filtered_data.append(item) # If it passes the filter, add it to filtered_data

    if not filtered_data: # If no matching data is found, display a message
        print("No Matching Data Found.")
    else:
        headers = filtered_data[0].keys() # Get column names from the first item
        rows = [item.values() for item in filtered_data] # Get values from each item
        print("\nCollection List")
        print(tabulate(rows, headers=headers, tablefmt="rst")) # Display in table format

# Function to search for collections based on specific attributes
def search_by_attribute():
    while True: # Loop so the user can try again if the input is incorrect
        filter_key = input("Enter the Attribute to Filter by: ").strip() # Receive attribute name input

        # If the entered attribute is "Year Discovered", validate it as a number
        if filter_key == "Year Discovered":
            try:
                filter_value = int(input("Enter Year Discovered to search (Numbers Only): ").strip())
                read_data_collection("Year Discovered", str(filter_value)) # Call read data function with filter
                break # Exit loop if input is valid
            except ValueError:
                print("Invalid year format! Please enter a number.") # Display error message if input is not a number

        # If the entered attribute is "Title", search based on title
        elif filter_key == "Title":
            filter_value = input("Enter Title to Search: ").strip()
            read_data_collection("Title", filter_value)
            break
        
        # If the entered attribute is "Region of Origin", search based on region of origin
        elif filter_key == "Region of Origin":
            filter_value = input("Enter Region of Origin to Search: ").strip()
            read_data_collection("Region of Origin", filter_value)
            break
        
        # If the entered attribute is "Place Discovered", search based on place discovered
        elif filter_key == "Place Discovered":
            filter_value = input("Enter Place Discovered to Search: ").strip()
            read_data_collection("Place Discovered", filter_value)
            break
        
        # If the entered attribute is "Era", search based on era
        elif filter_key == "Era":
            filter_value = input("Enter Era to Search: ").strip()
            read_data_collection("Era", filter_value)
            break
        
        # If the entered attribute is "Type", search based on collection type
        elif filter_key == "Type":
            filter_value = input("Enter Type to Search: ").strip()
            read_data_collection("Type", filter_value)
            break
        
        # If the entered attribute is "Status", search based on collection status
        elif filter_key == "Status":
            filter_value = input("Enter Status to Search: ").strip()
            read_data_collection("Status", filter_value)
            break
        
        # If the entered attribute is invalid, display an error message and the list of correct attributes
        else:
            print("The attribute you entered is invalid! Please enter a valid attribute.")
            print("Valid Attributes: Title, Region of Origin, Place Discovered, Era, Year Discovered, Type, Status.")

# Function to display the 'Create Data' submenu
def create_menu():
    while True:
        print("""
        Create Data Menu:
            1. Add New Collection
            2. Back to Main Menu
        """)
        menu_input = input("Enter the Menu Number You Want to Run: ").strip()

        if menu_input == "1": # Call the add data function
            create_data_collection()
        elif menu_input == "2": # Return to the main menu
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")

# Function to add a new collection to data_collection
def create_data_collection():
    
    # Use global variable used_ids to track already used IDs
    global used_ids

    while True:
        # Request Collection ID input
        data_id = input("Enter Collection ID: ").strip()
        if not data_id: 
            # If input is empty, display message and repeat
            print("Collection ID cannot be empty.")
            continue

        duplicate = False # To check for duplication
        for i in range(len(data_collection)): # Iterate to check every data entry
            if data_collection[i]["Collection ID"] == data_id:
                duplicate = True # Mark if ID already exists
                break
        
        if data_id in used_ids: # If ID exists in used_ids set
            print("Collection ID has already been used! Please enter a new Collection ID.")
            continue

        if duplicate:
            print("Collection ID already exists! Please enter a different ID.")
            continue
        else: 
            break # Exit loop if ID is valid
    
    # Request other collection details
    data_title = input("Enter Collection Title: ").strip()
    data_origin = input("Enter Region of Origin: ").strip()
    data_place = input("Enter Place Discovered: ").strip()
    data_era = input("Enter Era: ").strip()

    while True:
        try:
            data_year = int(input("Enter Year Discovered: ").strip())
            if 0 <= data_year <= 2026: # Year validation (updated to current year 2026)
                break
            else:
                print("Year discovered must be between 0 and 2026.")
        except ValueError: # Handle error if input is not a number
            print("Invalid year format! Please enter a number.")

    data_type = input("Enter Collection Type: ").strip()
    data_status = input("Enter Collection Status: ").strip()
    
    # Check if there is any empty input (Fixed: data_year is an int, so .strip() was removed)
    if not data_id or not data_title or not data_origin or not data_place or not data_era or not str(data_year) or not data_type or not data_status:
        print("Invalid input! Please enter all data details.")
        return

    # Display the entered data for confirmation
    print("\nPlease Review The Entered Data:")
    print(f"Collection ID: {data_id}")
    print(f"Title: {data_title}")
    print(f"Region of Origin: {data_origin}")
    print(f"Place Discovered: {data_place}")
    print(f"Era: {data_era}")
    print(f"Year Discovered: {data_year}")
    print(f"Type: {data_type}")
    print(f"Status: {data_status}")

    # Create a new dictionary with the entered data
    new_data = {
        "Collection ID": data_id,
        "Title": data_title,
        "Region of Origin": data_origin,
        "Place Discovered": data_place,
        "Era": data_era,
        "Year Discovered": data_year,
        "Type": data_type,
        "Status": data_status
    }
    print(tabulate([new_data.values()], headers=new_data.keys(), tablefmt="rst"))

    while True:
        # Confirm data storage
        confirm = input("Do you want to save the data? (Yes/No): ").strip().lower()
        if confirm == "yes":
            data_collection.append({
                "Collection ID": data_id,
                "Title": data_title,
                "Region of Origin": data_origin,
                "Place Discovered": data_place,
                "Era": data_era,
                "Year Discovered": data_year,
                "Type": data_type,
                "Status": data_status
            }) # Append data to collection
            used_ids.add(data_id) # Add ID to used_ids set
            print("Data successfully saved! Returning to Create Data menu...")
            return
        elif confirm == "no":
            print("Data entry canceled. Returning to Create Data menu...")
            return
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.") # Error message if input is invalid

# Function to display the 'Update Data' submenu
def update_menu():
    while True:
        print("""
        Update Data Menu:
            1. Update a Collection by Collection ID
            2. Back to Main Menu
        """)
        
        menu_input = input("Enter the Menu Number You Want to Run: ").strip()

        if menu_input == "1": # Call the update data function
            update_data_collection()
        elif menu_input == "2": # Return to the main menu
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")

# Function to update collection data
# Displays data based on the entered Collection ID, then asks for the column to update and its new value
def update_data_collection():
    # If data_collection is empty, display a message and exit
    if not data_collection:
        print("No Collections Available.")
        return

    # Request Collection ID input for the item to be updated
    update_id = input("Enter the Collection ID of the item you want to update: ").strip()

    # Validate if input is empty
    if not update_id:
        print("Collection ID cannot be empty.")
        return

    # Search for data with a matching Collection ID
    collection_to_update = None
    for item in data_collection:
        if item["Collection ID"] == update_id:
            # Display the found data in table format
            print("\nCurrent Data:")
            print(tabulate([item.values()], headers=item.keys(), tablefmt="rst"))
            collection_to_update = item
            break
    
    # If not found, display a message
    if not collection_to_update:
        print("The data you are looking for does not exist!")
        return

    # Display data to be updated
    print("\nPlease Review The Selected Data:")
    for key, value in collection_to_update.items():
        print(f"{key}: {value}")

    # Confirm if the user wants to proceed with the update
    while True:
        confirm = input("Continue update? (Yes/No): ").strip().lower()
        if confirm == "yes":
            break
        elif confirm == "no":
            print("Update canceled. Returning to Update Data Menu...")
            return
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")

    # List of valid columns and original column names for easy matching
    valid_columns = ["title", "region of origin", "place discovered", "era", "year discovered", "type", "status"]
    original_columns = ["Title", "Region of Origin", "Place Discovered", "Era", "Year Discovered", "Type", "Status"]

    # Loop to request the column to be updated
    while True:
        print("Valid columns to update: Title, Region of Origin, Place Discovered, Era, Year Discovered, Type, Status")
        column_to_update = input("Enter the Column You Want to Update: ").strip().lower()

        # Validate column input
        if column_to_update not in valid_columns:
            print("Invalid input! Please enter a valid column.")
            continue
        
        # Get the original column name based on the index
        column_index = valid_columns.index(column_to_update)
        column_name = original_columns[column_index]

        # Request new value based on the selected column
        if column_name == "Title":
            new_value = input("Enter new value for Title: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        elif column_name == "Region of Origin":
            new_value = input("Enter new value for Region of Origin: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        elif column_name == "Place Discovered":
            new_value = input("Enter new value for Place Discovered: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        elif column_name == "Era":
            new_value = input("Enter new value for Era: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        elif column_name == "Year Discovered":
            while True:
                try:
                    new_value = int(input("Enter new value for Year Discovered (Numbers Only): ").strip())
                    if 0 <= new_value <= 2026: # Updated validation upper limit to 2026
                        break
                    else:
                        print("Year discovered must be between 0 and 2026.")
                except ValueError:
                    print("Invalid year format! Please enter a number.")
        elif column_name == "Type":
            new_value = input("Enter new value for Type: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        elif column_name == "Status":
            new_value = input("Enter new value for Status: ").strip()
            if not new_value:
                print("Invalid input! New value cannot be empty.")
                continue
        
        # Confirm update from the user
        while True:
            confirm_update = input("Do you want to update the data? (Yes/No): ").strip().lower()
            if confirm_update == "yes":
                collection_to_update[column_name] = new_value
                print(tabulate([collection_to_update.values()], headers=collection_to_update.keys(), tablefmt="rst"))
                print("Data successfully updated! Returning to Update Data Menu...")
                return
            elif confirm_update == "no":
                print("Update canceled. Returning to Update Data Menu...")
                return
            else:
                print("Invalid input! Please enter 'Yes' or 'No'.")

# Function to display the 'Delete Data' submenu
def delete_menu():
    while True:
        print("""
        Delete Data Menu:
            1. Delete a Collection by Collection ID
            2. Back to Main Menu
        """)

        menu_input = input("Enter the Menu Number You Want to Run: ").strip()

        if menu_input == "1": # Call the delete data function
            delete_data_collection()
        elif menu_input == "2": # Return to the main menu
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")

# Function to delete a data collection
def delete_data_collection():
    # Check if data_collection is empty
    if not data_collection:
        print("No Collections Available.") # If empty, display message and exit function
        return  

    # Request Collection ID input for the item to be deleted
    delete_id = input("Enter the Collection ID of the item you want to delete: ").strip()

    # If input is empty, display error message and exit
    if not delete_id:
        print("Collection ID cannot be empty.")
        return

    # Initialize variable to store the collection to be deleted
    collection_to_delete = None
    for item in data_collection: # Loop through data_collection to find a matching ID
        if item["Collection ID"] == delete_id:
            collection_to_delete = item # If found, store the item in the variable
            break 
    
    # If no matching ID is found, display error message and exit
    if not collection_to_delete:
        print("The data you are looking for does not exist!")
        return

    # Display the selected data to be deleted
    print("\nPlease Review The Selected Data:")
    for key, value in collection_to_delete.items():
        print(f"{key}: {value}")

    # Confirm from the user whether to delete the data or not
    while True:
        confirm = input("Do you want to delete the data? (Yes/No): ").strip().lower()
        if confirm == "yes": # If yes, remove data from the list
            data_collection.remove(collection_to_delete) # .remove() is used to delete an item from the list
            print("Data successfully deleted! Returning to Delete Data Menu...")
            return
        elif confirm == "no": # If no, cancel deletion
            print("Deletion canceled. Returning to Delete Data Menu...")
            return
        else: # If input is not yes/no, display error message
            print("Invalid input! Please enter 'Yes' or 'No'.")

