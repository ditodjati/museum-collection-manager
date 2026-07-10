# Import the built-in datetime library to get the current date and year dynamically
import datetime
# Import the 'tabulate' library to print and format collections neatly in a table
from tabulate import tabulate



# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

# List containing collection data in the form of dictionaries.
# This is the ONE place collection data lives (single "source of truth").
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
    {"Collection ID": "P05", "Title": "The Last Supper", "Region of Origin": "Europe", "Place Discovered": "Milan, Italy", "Era": "Renaissance", "Year Discovered": 1498, "Type": "Painting", "Status": "Displayed"},
]

# The oldest year a piece could have been "discovered" is 0; the newest is
# "this year" - calculated automatically so we never have to hardcode
# a year (like "2026") that will go stale.
CURRENT_YEAR = datetime.date.today().year

# Columns that can be edited via the Update menu, and how each one should
# be validated. Using a dictionary here means adding a new editable column
# later is a ONE line change, instead of copy-pasting a whole new block.
TEXT_COLUMNS = ["Title", "Region of Origin", "Place Discovered", "Era", "Type", "Status"]
ALL_EDITABLE_COLUMNS = TEXT_COLUMNS + ["Year Discovered"]



# ---------------------------------------------------------------------------
# Small reusable "logic" helpers (no input()/print() -> easy to unit test)
# ---------------------------------------------------------------------------

def find_collection_by_id(collection_id):
    """Return the dictionary whose 'Collection ID' matches, or None if not found.
    This one function replaces three separate copy-pasted search loops that
    used to live inside update_data_collection(), delete_data_collection(),
    and read_data_collection().
    """
    # Loop through each individual item dictionary inside data_collection
    for item in data_collection:
        # Check if the current item's Collection ID matches the requested collection_id
        if item["Collection ID"] == collection_id:
            # If a match is found, return the dictionary of that matching item
            return item
    # Return None if the loop finishes and no matching ID is found
    return None


def is_duplicate_id(collection_id):
    """True if this Collection ID is already used by an existing record."""
    # Use find_collection_by_id to check if an item with this ID already exists
    return find_collection_by_id(collection_id) is not None


def matches_filter(item, filter_option, filter_value):
    """Return True if a single record matches the given filter.

    filter_option/filter_value are already validated by the caller.
    Text fields use a case-insensitive "contains" match so a visitor
    searching 'mona' will still find 'Mona Lisa'.
    """
    # Check if the filter option selected by the user is Collection ID
    if filter_option == "Collection ID":
        # Compare the string representation of the item ID exactly with the filter value
        return str(item["Collection ID"]) == filter_value
    # Check if the filter option selected by the user is Year Discovered
    if filter_option == "Year Discovered":
        # Compare the integer values of the item's year and the filter value exactly
        return int(item["Year Discovered"]) == int(filter_value)
    # All other fields are free-text partial, case-insensitive matches
    return filter_value.lower() in str(item[filter_option]).lower()


def is_valid_year(value):
    """True if value is an int between 0 and the current year (inclusive)."""
    # Validate that the integer year falls between 0 and the current system year
    return 0 <= value <= CURRENT_YEAR


# ---------------------------------------------------------------------------
# Menus
# ---------------------------------------------------------------------------

def greeting():
    """Print the welcome banner shown when the program starts."""
    # Print the application welcome message block
    print("\n          Welcome to Shangri-La Museum Application\n")


def main_menu():
    """Top-level menu loop. Routes the user to each feature's submenu."""
    # Map menu choice string keys directly to their corresponding function references
    menu_actions = {
        "1": read_menu,
        "2": create_menu,
        "3": update_menu,
        "4": delete_menu,
    }

    # Loop indefinitely to keep showing the main menu until explicit exit
    while True:
        # Display main navigation options to the screen
        print("""
        Menu:
              1. Show Collection
              2. Add Collection
              3. Update Collection
              4. Delete Collection
              5. Exit Program
              """)
        # Read the user's choice, stripping out accidental whitespace padding
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        # Handle system exit if the user chooses option 5
        if choice == "5":
            # Print appreciation message and break the loop to terminate
            print("\n        Thank You for Using Our Service!\n        Exiting Program...\n")
            break
        # Route execution to the chosen submenu if the option exists in the dictionary mapping
        elif choice in menu_actions:
            # Execute the routed submenu function
            menu_actions[choice]()
        # Handle all invalid out-of-bounds menu entries
        else:
            # Print an error warning message to guide user input
            print("The option you entered is invalid! Please choose between 1-5.")


def read_menu():
    """Submenu for viewing/searching collections."""
    # Run loop to continuously maintain the read data menu state
    while True:
        # Display reading data feature sub-navigation options
        print("""
        Read Data Menu:
            1. Show All Collections
            2. Search by Collection ID
            3. Search by Other Attributes
            4. Back to Main Menu
        """)
        # Capture and clean whitespace from the menu selection input
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        # Check if operations are attempted while data_collection is empty
        if not data_collection and choice in ("1", "2", "3"):
            # Inform the user that there is no data to perform operations on
            print("No Collections Available.")
            # Skip the rest of the loop and re-prompt the menu
            continue

        # Route to complete collection display feature
        if choice == "1":
            # Call function to display everything without filter
            read_data_collection()
        # Route to exact item look-up by ID feature
        elif choice == "2":
            # Capture the desired ID from user input
            collection_id = input("Enter Collection ID: ").strip()
            # Call function with specific arguments to filter by ID
            read_data_collection("Collection ID", collection_id)
        # Route to partial search engine feature
        elif choice == "3":
            # Trigger custom search routing workflow
            search_by_attribute()
        # Handle back tracking request from submenu to main menu
        elif choice == "4":
            # Print status message and break the infinite submenu loop
            print("Returning to Main Menu...")
            break
        # Handle invalid string selection bounds
        else:
            # Prompt user of input mismatch guidelines
            print("The option you entered is invalid! Please choose between 1-4.")


def read_data_collection(filter_option=None, filter_value=None):
    """Print collections as a table, optionally filtered by one attribute."""
    # Guard clause to exit early if there are no items to show
    if not data_collection:
        # Inform user of empty database state
        print("No Collections Available.")
        # Stop processing and exit function
        return

    # Check if a specific query option and its value were supplied to the function
    if filter_option and filter_value:
        # Run specialized type confirmation check if filtering by chronological year
        if filter_option == "Year Discovered":
            try:
                # Try converting value to an integer to ensure numeric data format
                int(filter_value)
            except ValueError:
                # Catch failures and alert user of bad string characters
                print("Invalid year format! Please enter a number.")
                # Exit early to prevent crashing down the line
                return
        # Construct list dynamically using list comprehension matching filter rules
        filtered_data = [item for item in data_collection
                          if matches_filter(item, filter_option, filter_value)]
    else:
        # Point reference directly to master collection if no filter parameters exist
        filtered_data = data_collection

    # Alert user if filter processing left no valid dictionaries remaining
    if not filtered_data:
        # Display data absence alert notice
        print("No Matching Data Found.")
        # Exit function gracefully
        return

    # Extract column titles dynamically from the dictionary keys of first entry
    headers = filtered_data[0].keys()
    # Compress all rows into separate matching lists containing values only
    rows = [item.values() for item in filtered_data]
    # Display the current header description label
    print("\nCollection List")
    # Format and present rows cleanly into terminal with reStructuredText syntax
    print(tabulate(rows, headers=headers, tablefmt="rst"))


def search_by_attribute():
    """Ask which attribute to search by, then run the search.

    Uses a small lookup table instead of a long if/elif chain, so adding
    a new searchable attribute is a one-line change.
    """
    # Define an authoritative sequence string list of all fields open to searches
    searchable_attributes = [
        "Title", "Region of Origin", "Place Discovered",
        "Era", "Year Discovered", "Type", "Status",
    ]

    # Join list entities using comma separators to generate human-readable text
    attribute_list = ", ".join(searchable_attributes)

    # Maintain retry loop for picking valid attributes
    while True:
        # Capture intended attribute field key name
        filter_key = input(f"Enter the Attribute to Filter by ({attribute_list}): ").strip()

        # Match the attribute name case-insensitively for a friendlier UX
        match = next((attr for attr in searchable_attributes
                      if attr.lower() == filter_key.lower()), None)

        # Handle failed attempts to find an attribute match from definition list
        if match is None:
            # Print error notice listing acceptable terms
            print(f"The attribute you entered is invalid! Valid Attributes: {attribute_list}.")
            # Restart loop iteration to query user again
            continue

        # Check if the matched uniform attribute choice points to numerical year
        if match == "Year Discovered":
            try:
                # Nested capture to strictly validate that input value can be transformed into integer
                filter_value = str(int(input("Enter Year Discovered to search (Numbers Only): ").strip()))
            except ValueError:
                # Inform of incorrect symbol or characters inside value entry
                print("Invalid year format! Please enter a number.")
                # Restart entry cycle to avoid breaking table print
                continue
        else:
            # Collect standard search strings for textual column look-up operations
            filter_value = input(f"Enter {match} to Search: ").strip()

        # Execute final query display utilizing uniform match parameters
        read_data_collection(match, filter_value)
        # Terminate loops upon successful search routine trigger
        break


def create_menu():
    """Submenu for adding a new collection record."""
    # Establish looping state for data entry routing options
    while True:
        # Print functional guidelines menu interface
        print("""
        Create Data Menu:
            1. Add New Collection
            2. Back to Main Menu
        """)
        # Clean external whitespace fields around selection value
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        # Direct processing to execution routine function
        if choice == "1":
            # Fire master registration insertion workflow
            create_data_collection()
        # Evaluate user requests to return back to higher levels
        elif choice == "2":
            # Post exit trace alert log and interrupt loop
            print("Returning to Main Menu...")
            break
        # Reject entries not aligning with specified boundaries
        else:
            # Prompt entry exception alert
            print("The option you entered is invalid! Please choose 1 or 2.")


def create_data_collection():
    """Collect input for, confirm, and save a brand-new collection record."""

    # Maintain input verification processing loop for distinct IDs
    while True:
        # Capture raw ID tracking target
        data_id = input("Enter Collection ID: ").strip()
        # Verify user did not bypass prompt with an empty string
        if not data_id:
            # Print warning constraint details
            print("Collection ID cannot be empty.")
            # Cycle to re-ask input
            continue
        # Check against existing elements using global identifier records tracker helper
        if is_duplicate_id(data_id):
            # Print duplicate prevention system alert warnings
            print("Collection ID already exists! Please enter a different ID.")
            # Restart loop parameters
            continue
        # Break loop processing upon gathering unique identity value
        break

    # Read and store accompanying characteristic text fields sequentially
    data_title = input("Enter Collection Title: ").strip()
    data_origin = input("Enter Region of Origin: ").strip()
    data_place = input("Enter Place Discovered: ").strip()
    data_era = input("Enter Era: ").strip()

    # Enter confirmation constraint block for validating chronological properties
    while True:
        try:
            # Parse entered characters cleanly into localized base numerical object
            data_year = int(input("Enter Year Discovered: ").strip())
            # Evaluate bounds integrity properties using global calendar constraints
            if is_valid_year(data_year):
                # Break the year loop once input matches bounds criteria
                break
            # Print validation boundary guidelines
            print(f"Year discovered must be between 0 and {CURRENT_YEAR}.")
        except ValueError:
            # Catch format parsing syntax exceptions from bad alphabetic entries
            print("Invalid year format! Please enter a number.")

    # Read and assign the remaining organizational type tracking information
    data_type = input("Enter Collection Type: ").strip()
    data_status = input("Enter Collection Status: ").strip()

    # Every text field must be non-empty (year is always valid at this point,
    # since the loop above only exits once it has a valid number)
    text_fields = [data_id, data_title, data_origin, data_place, data_era, data_type, data_status]
    # Check if any text fields remain blank using comprehensive short-circuit tracking
    if not all(text_fields):
        # Print field failure notice and terminate insertion routines instantly
        print("Invalid input! Please enter all data details.")
        # Halt system sub-routines from parsing broken records
        return

    # Build fresh structure mapping dictionary schema to construct historical record database block
    new_data = {
        "Collection ID": data_id,
        "Title": data_title,
        "Region of Origin": data_origin,
        "Place Discovered": data_place,
        "Era": data_era,
        "Year Discovered": data_year,
        "Type": data_type,
        "Status": data_status,
    }

    # Present verification logs summarizing prospective layout designs
    print("\nPlease Review The Entered Data:")
    # Render preview output elements neatly arranged in data table grids
    print(tabulate([new_data.values()], headers=new_data.keys(), tablefmt="rst"))

    # Execute interactive processing sequence confirming saving choice intent
    while True:
        # Prompt final approval parameters converting output directly into uniform casing
        confirm = input("Do you want to save the data? (Yes/No): ").strip().lower()
        # Evaluate affirmative storage approvals
        if confirm == "yes":
            # Append confirmed entry directly onto core primary array reference list
            data_collection.append(new_data)
            # Confirm execution message to clarify updates processed completely
            print("Data successfully saved! Returning to Create Data menu...")
            # Return flow control out of modification loops
            return
        # Process cancelation choices to prevent accidental record creation
        elif confirm == "no":
            # Inform of data record disposal trace activity log
            print("Data entry canceled. Returning to Create Data menu...")
            # Exit program segment loop returning upstream safely
            return
        # Throw runtime text formatting exceptions back onto user screens
        else:
            # Print standard verification option reminder alerts
            print("Invalid input! Please enter 'Yes' or 'No'.")


def update_menu():
    """Submenu for updating an existing collection record."""
    # Set localized interface sequence tracking container loops
    while True:
        # Render clean options outlining prospective functional actions
        print("""
        Update Data Menu:
            1. Update a Collection by Collection ID
            2. Back to Main Menu
        """)
        # Parse incoming configuration selections
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        # Handle requests addressing index data lookups
        if choice == "1":
            # Call primary update system modification engine logic functions
            update_data_collection()
        # Capture backtracking system command parameters
        elif choice == "2":
            # Post feedback messaging statement log strings
            print("Returning to Main Menu...")
            # Terminate internal execution routines immediately
            break
        # Reject arbitrary choices matching incorrect range items
        else:
            # Advise users of target operational menu restrictions
            print("The option you entered is invalid! Please choose 1 or 2.")


def prompt_for_new_value(column_name):
    """Ask the user for a new value for one column, validating as needed.

    Replaces the six nearly-identical copy-pasted input blocks from the
    original update function.
    """
    # Track down specific parameters addressing chronological database modifications
    if column_name == "Year Discovered":
        # Launch isolated correction validation sequences loop
        while True:
            try:
                # Enforce strict parsing constraints mapping inputs into dedicated integers
                value = int(input("Enter new value for Year Discovered (Numbers Only): ").strip())
                # Verify parsed value satisfies global calendar boundaries criteria
                if is_valid_year(value):
                    # Return safe integer object value directly back to caller functions
                    return value
                # Warn user regarding layout parameter constraints bounds
                print(f"Year discovered must be between 0 and {CURRENT_YEAR}.")
            except ValueError:
                # Capture anomalies if users key alphanumeric characters instead of digits
                print("Invalid year format! Please enter a number.")
    # Process text attributes validation
    else:
        # Process alphanumeric string fields parameters loops safely
        while True:
            # Intercept incoming textual modifications
            value = input(f"Enter new value for {column_name}: ").strip()
            # Enforce non-zero minimal length constraint logic safeguards
            if value:
                # Return confirmed textual properties variables strings directly
                return value
            # Block users from deleting critical definitions completely
            print("Invalid input! New value cannot be empty.")


def update_data_collection():
    """Find a record by ID, then update one or more of its fields."""
    # Ensure application logic halts instantly if database records are empty
    if not data_collection:
        # Display operational availability alerts on console screen
        print("No Collections Available.")
        # Terminate look-up operations immediately
        return

    # Request the precise search reference targeted for operational updates
    update_id = input("Enter the Collection ID of the item you want to update: ").strip()
    # Guard system behavior from responding to blank spaces entries requests
    if not update_id:
        # Remind user that core indices tracking parameters must contain content
        print("Collection ID cannot be empty.")
        # Halt task operations early
        return

    # Trigger shared mapping identity tracking helper search tools
    collection_to_update = find_collection_by_id(update_id)
    # Validate result instances objects returned from identity query lookup checks
    if not collection_to_update:
        # Warn user regarding identity record missing alerts errors
        print("The data you are looking for does not exist!")
        # Stop modification process immediately
        return

    # Print baseline tracking details summarizing existing record components configurations
    print("\nCurrent Data:")
    # Render clean layouts mapping data components to formatted visual presentation grid interfaces
    print(tabulate([collection_to_update.values()], headers=collection_to_update.keys(), tablefmt="rst"))

    # Establish interactive verification loops requesting authorization progress approvals
    while True:
        # Intercept routing validation choices inputs safely
        confirm = input("Continue update? (Yes/No): ").strip().lower()
        # Handle manual user cancelation execution commands safely
        if confirm == "no":
            # Display notification of task reversal and exit early
            print("Update canceled. Returning to Update Data Menu...")
            # Terminate function flow parameters gracefully
            return
        # Verify approval execution variables components configurations
        if confirm == "yes":
            # Escape confirmations cycles safely to pursue secondary modifications tasks
            break
        # Call attention to invalid tracking confirmations entries exceptions
        print("Invalid input! Please enter 'Yes' or 'No'.")

    
    # Enter secondary properties loop parsing precise data field corrections targets
    while True:
        # Enumerate acceptable modifications column categories to guide target parameters selection
        print("Valid columns to update: " + ", ".join(ALL_EDITABLE_COLUMNS))
        # Read column name update intent choice targets from application prompt
        column_input = input("Enter the Column You Want to Update: ").strip()

        # Execute uniform case matching lookups tracing down specific properties keys definitions
        column_name = next((c for c in ALL_EDITABLE_COLUMNS if c.lower() == column_input.lower()), None)
        # Handle cases where user names attributes missing from dictionary specifications
        if column_name is None:
            # Print configuration error details explicitly onto terminal output screens
            print("Invalid input! Please enter a valid column.")
            # Reiterate loops tasks workflow queries sequences
            continue

        # Invoke separate parameter checks sequence tool to fetch verified value corrections
        new_value = prompt_for_new_value(column_name)

        # Loop to handle specific storage verification transactions processing cycles
        while True:
            # Read transactional execution verification logs inputs variables
            confirm_update = input("Do you want to update the data? (Yes/No): ").strip().lower()
            # Commit mutations instantly upon matching positive authorization keys
            if confirm_update == "yes":
                # Inject updated properties elements cleanly onto corresponding targeted array reference keys
                collection_to_update[column_name] = new_value
                # Render comprehensive visual feedback structures detailing applied configuration alterations
                print(tabulate([collection_to_update.values()], headers=collection_to_update.keys(), tablefmt="rst"))
                # Post system success execution status notifications on visual panel logs
                print("Data successfully updated! Returning to Update Data Menu...")
                # Escape processing tasks completely back to primary interface segments
                return
            # Route processing parameters if users elect to roll back temporary corrections modifications
            elif confirm_update == "no":
                # Announce cancellation sequence procedures execution signals clearly
                print("Update canceled. Returning to Update Data Menu...")
                # Exit function parameters routines layout structures
                return
            # Inform users of missing values alignments matching confirmation rules parameters
            else:
                # Print explicit instructional guidelines parameters onto screens blocks
                print("Invalid input! Please enter 'Yes' or 'No'.")


def delete_menu():
    """Submenu for deleting an existing collection record."""
    # Keep running loops displaying interactive termination submenu configurations
    while True:
        # Render clean structural layouts defining functional termination system capabilities
        print("""
        Delete Data Menu:
            1. Delete a Collection by Collection ID
            2. Back to Main Menu
        """)
        # Capture raw selector selections values securely
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        # Branch operations to handle core records tracking index disposal tasks
        if choice == "1":
            # Fire master deletion workflow processing engine operations
            delete_data_collection()
        # Intercept navigational request tracking updates upstream
        elif choice == "2":
            # Display tracking state updates warnings information
            print("Returning to Main Menu...")
            # Break active loops context to return upstream to previous level
            break
        # Trap stray input entry items breaking expected array indexing guidelines
        else:
            # Throw validation errors warning rules alerts onto console display screens
            print("The option you entered is invalid! Please choose 1 or 2.")


def delete_data_collection():
    """Find a record by ID, confirm, and remove it from data_collection."""
    # Verify primary database container is populated before processing removal targets operations
    if not data_collection:
        # Post alert warning that removal tasks cannot query empty structural tables
        print("No Collections Available.")
        # Break execution workflow paths early
        return

    # Capture target tracker identity parameters planned for structural purging operations
    delete_id = input("Enter the Collection ID of the item you want to delete: ").strip()
    # Ensure tracking indices variables strings are populated with actual data elements
    if not delete_id:
        # Enforce validation notices explaining identity keys cannot pass empty lines
        print("Collection ID cannot be empty.")
        # Halt runtime operation sequences immediately
        return

    # Launch tracking search systems looking for matching target reference identity elements
    collection_to_delete = find_collection_by_id(delete_id)
    # Check if tracking dictionary targets exist or contain valid reference object elements
    if not collection_to_delete:
        # Warn system user that targeted item identities cannot be extracted from dataset arrays
        print("The data you are looking for does not exist!")
        # Exit purging tasks routine immediately to minimize system disruptions
        return

    # Present verification logs summarizing targeted data item assets slated for destruction
    print("\nPlease Review The Selected Data:")
    # Iterate across structural keys mapping internal layout pairs to descriptive lines components
    for key, value in collection_to_delete.items():
        # Format textual key items pairs visually inside workspace tracking displays
        print(f"{key}: {value}")

    # Maintain continuous verification loops processing critical database deletions confirmations
    while True:
        # Prompt user for final categorical confirmation of destructive database deletions actions
        confirm = input("Do you want to delete the data? (Yes/No): ").strip().lower()
        # Process positive confirmation triggers executing actual record separation workflows
        if confirm == "yes":
            # Invoke built-in native remove method arrays structures to erase targeted elements dictionaries
            data_collection.remove(collection_to_delete)
            # Log success notifications confirming record destruction workflows executed safely
            print("Data successfully deleted! Returning to Delete Data Menu...")
            # Break operational context looping modules returning flows back cleanly
            return
        # Intercept negative responses preventing unintended critical resource destruction operations
        elif confirm == "no":
            # Post transaction cancellation records alerts onto console outputs logs workspace
            print("Deletion canceled. Returning to Delete Data Menu...")
            # Exit loop processing frameworks returning execution focus back safely
            return
        # Remind user of specific input character terms validation specifications options bounds
        else:
            # Display error message instructing acceptable alternative selection modes choices options
            print("Invalid input! Please enter 'Yes' or 'No'.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

# Use standard idiom checking safeguards to assert that script runs as a primary process main call execution module
if __name__ == "__main__":
    # Fire introductory messaging strings banners welcome text frames logs
    greeting()
    # Trigger endless parent loop routing management interactions across nested modules subsystems
    main_menu()
