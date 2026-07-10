import datetime
from tabulate import tabulate


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


CURRENT_YEAR = datetime.date.today().year


TEXT_COLUMNS = ["Title", "Region of Origin", "Place Discovered", "Era", "Type", "Status"]
ALL_EDITABLE_COLUMNS = TEXT_COLUMNS + ["Year Discovered"]


def find_collection_by_id(collection_id):
    for item in data_collection:
        if item["Collection ID"] == collection_id:
            return item
    return None


def is_duplicate_id(collection_id):
    return find_collection_by_id(collection_id) is not None


def matches_filter(item, filter_option, filter_value):
    if filter_option == "Collection ID":
        return str(item["Collection ID"]) == filter_value
    if filter_option == "Year Discovered":
        return int(item["Year Discovered"]) == int(filter_value)
    return filter_value.lower() in str(item[filter_option]).lower()


def is_valid_year(value):
    return 0 <= value <= CURRENT_YEAR


def greeting():
    print("\n          Welcome to Shangri-La Museum Application\n")


def main_menu():
    menu_actions = {
        "1": read_menu,
        "2": create_menu,
        "3": update_menu,
        "4": delete_menu,
    }

    while True:
        print("""
        Menu:
              1. Show Collection
              2. Add Collection
              3. Update Collection
              4. Delete Collection
              5. Exit Program
              """)
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        if choice == "5":
            print("\n        Thank You for Using Our Service!\n        Exiting Program...\n")
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("The option you entered is invalid! Please choose between 1-5.")


def read_menu():
    """Submenu for viewing/searching collections."""
    while True:
        print("""
        Read Data Menu:
            1. Show All Collections
            2. Search by Collection ID
            3. Search by Other Attributes
            4. Back to Main Menu
        """)
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        if not data_collection and choice in ("1", "2", "3"):
            print("No Collections Available.")
            continue

        if choice == "1":
            read_data_collection()
        elif choice == "2":
            collection_id = input("Enter Collection ID: ").strip()
            read_data_collection("Collection ID", collection_id)
        elif choice == "3":
            search_by_attribute()
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose between 1-4.")


def read_data_collection(filter_option=None, filter_value=None):
    """Print collections as a table, optionally filtered by one attribute."""
    if not data_collection:
        print("No Collections Available.")
        return

    if filter_option and filter_value:
        if filter_option == "Year Discovered":
            try:
                int(filter_value)
            except ValueError:
                print("Invalid year format! Please enter a number.")
                return
        filtered_data = [item for item in data_collection
                          if matches_filter(item, filter_option, filter_value)]
    else:
        filtered_data = data_collection

    if not filtered_data:
        print("No Matching Data Found.")
        return

    headers = filtered_data[0].keys()
    rows = [item.values() for item in filtered_data]
    print("\nCollection List")
    print(tabulate(rows, headers=headers, tablefmt="rst"))


def search_by_attribute():
    searchable_attributes = [
        "Title", "Region of Origin", "Place Discovered",
        "Era", "Year Discovered", "Type", "Status",
    ]

    attribute_list = ", ".join(searchable_attributes)

    while True:
        filter_key = input(f"Enter the Attribute to Filter by ({attribute_list}): ").strip()

        match = next((attr for attr in searchable_attributes
                      if attr.lower() == filter_key.lower()), None)

        if match is None:
            print(f"The attribute you entered is invalid! Valid Attributes: {attribute_list}.")
            continue

        if match == "Year Discovered":
            try:
                filter_value = str(int(input("Enter Year Discovered to search (Numbers Only): ").strip()))
            except ValueError:
                print("Invalid year format! Please enter a number.")
                continue
        else:
            filter_value = input(f"Enter {match} to Search: ").strip()

        read_data_collection(match, filter_value)
        break


def create_menu():
    """Submenu for adding a new collection record."""
    while True:
        print("""
        Create Data Menu:
            1. Add New Collection
            2. Back to Main Menu
        """)
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        if choice == "1":
            create_data_collection()
        elif choice == "2":
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")


def create_data_collection():
    while True:
        data_id = input("Enter Collection ID: ").strip()
        if not data_id:
            print("Collection ID cannot be empty.")
            continue
        if is_duplicate_id(data_id):
            print("Collection ID already exists! Please enter a different ID.")
            continue
        break

    data_title = input("Enter Collection Title: ").strip()
    data_origin = input("Enter Region of Origin: ").strip()
    data_place = input("Enter Place Discovered: ").strip()
    data_era = input("Enter Era: ").strip()

    while True:
        try:
            data_year = int(input("Enter Year Discovered: ").strip())
            if is_valid_year(data_year):
                break
            print(f"Year discovered must be between 0 and {CURRENT_YEAR}.")
        except ValueError:
            print("Invalid year format! Please enter a number.")

    data_type = input("Enter Collection Type: ").strip()
    data_status = input("Enter Collection Status: ").strip()

    text_fields = [data_id, data_title, data_origin, data_place, data_era, data_type, data_status]
    if not all(text_fields):
        print("Invalid input! Please enter all data details.")
        return

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

    print("\nPlease Review The Entered Data:")
    print(tabulate([new_data.values()], headers=new_data.keys(), tablefmt="rst"))

    while True:
        confirm = input("Do you want to save the data? (Yes/No): ").strip().lower()
        if confirm == "yes":
            data_collection.append(new_data)
            print("Data successfully saved! Returning to Create Data menu...")
            return
        elif confirm == "no":
            print("Data entry canceled. Returning to Create Data menu...")
            return
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")


def update_menu():
    """Submenu for updating an existing collection record."""
    while True:
        print("""
        Update Data Menu:
            1. Update a Collection by Collection ID
            2. Back to Main Menu
        """)
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        if choice == "1":
            update_data_collection()
        elif choice == "2":
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")


def prompt_for_new_value(column_name):
    if column_name == "Year Discovered":
        while True:
            try:
                value = int(input("Enter new value for Year Discovered (Numbers Only): ").strip())
                if is_valid_year(value):
                    return value
                print(f"Year discovered must be between 0 and {CURRENT_YEAR}.")
            except ValueError:
                print("Invalid year format! Please enter a number.")
    else:
        while True:
            value = input(f"Enter new value for {column_name}: ").strip()
            if value:
                return value
            print("Invalid input! New value cannot be empty.")


def update_data_collection():
    """Find a record by ID, then update one or more of its fields."""
    if not data_collection:
        print("No Collections Available.")
        return

    update_id = input("Enter the Collection ID of the item you want to update: ").strip()
    if not update_id:
        print("Collection ID cannot be empty.")
        return

    collection_to_update = find_collection_by_id(update_id)
    if not collection_to_update:
        print("The data you are looking for does not exist!")
        return

    print("\nCurrent Data:")
    print(tabulate([collection_to_update.values()], headers=collection_to_update.keys(), tablefmt="rst"))

    while True:
        confirm = input("Continue update? (Yes/No): ").strip().lower()
        if confirm == "no":
            print("Update canceled. Returning to Update Data Menu...")
            return
        if confirm == "yes":
            break
        print("Invalid input! Please enter 'Yes' or 'No'.")

    
    while True:
        print("Valid columns to update: " + ", ".join(ALL_EDITABLE_COLUMNS))
        column_input = input("Enter the Column You Want to Update: ").strip()

        column_name = next((c for c in ALL_EDITABLE_COLUMNS if c.lower() == column_input.lower()), None)
        if column_name is None:
            print("Invalid input! Please enter a valid column.")
            continue

        new_value = prompt_for_new_value(column_name)

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


def delete_menu():
    """Submenu for deleting an existing collection record."""
    while True:
        print("""
        Delete Data Menu:
            1. Delete a Collection by Collection ID
            2. Back to Main Menu
        """)
        choice = input("Enter the Menu Number You Want to Run: ").strip()

        if choice == "1":
            delete_data_collection()
        elif choice == "2":
            print("Returning to Main Menu...")
            break
        else:
            print("The option you entered is invalid! Please choose 1 or 2.")


def delete_data_collection():
    """Find a record by ID, confirm, and remove it from data_collection."""
    if not data_collection:
        print("No Collections Available.")
        return

    delete_id = input("Enter the Collection ID of the item you want to delete: ").strip()
    if not delete_id:
        print("Collection ID cannot be empty.")
        return

    collection_to_delete = find_collection_by_id(delete_id)
    if not collection_to_delete:
        print("The data you are looking for does not exist!")
        return

    print("\nPlease Review The Selected Data:")
    for key, value in collection_to_delete.items():
        print(f"{key}: {value}")

    while True:
        confirm = input("Do you want to delete the data? (Yes/No): ").strip().lower()
        if confirm == "yes":
            data_collection.remove(collection_to_delete)
            print("Data successfully deleted! Returning to Delete Data Menu...")
            return
        elif confirm == "no":
            print("Deletion canceled. Returning to Delete Data Menu...")
            return
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    greeting()
    main_menu()
