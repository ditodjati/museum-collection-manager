# Museum Collection Management System

A Python-based command-line interface (CLI) application designed to manage museum collections efficiently. This project represents a comprehensive implementation of **CRUD (Create, Read, Update, Delete)** operations using basic Python data structures and advanced logical validation.

---

## 📌 Project Overview
This application serves as a digital registry for the **Shangri-La Museum**. It allows museum administrators to organize, track, and update various historical items, ranging from prehistoric fossils and ancient weapons to priceless paintings and cultural artifacts. 

The data is stored dynamically in a memory-based collection using structured dictionaries within a list, ensuring fast access and manipulation during runtime.

---

## 🚀 Key Features

The system is strictly divided into 5 main modules accessible via the **Main Menu**:

### 1. Show Collection (Read)
* **Show All**: Displays all items currently registered in the museum.
* **Search by ID**: Performs a strict, exact match search using the unique `Collection ID`.
* **Search by Attributes**: Offers flexible searching capabilities across other data keys, such as `Title`, `Region of Origin`, `Place Discovered`, `Era`, `Type`, and `Status`.

### 2. Add Collection (Create)
* Allows administrators to insert new historical items into the system.
* **Strict ID Validation**: Prevents duplicate entries by checking against existing data and previously deleted records.
* **Data Integrity**: Ensures no vital information fields are left empty.

### 3. Update Collection (Update)
* Enables modifications to specific fields of an existing item based on its `Collection ID`.
* Provides dynamic column selection (e.g., updating only the `Status` or `Location` without overriding other details).
* Includes a dual-stage confirmation (`Yes`/`No`) before applying permanent changes.

### 4. Delete Collection (Delete)
* Removes an item from the active database using its specific `Collection ID`.
* Features a safety review screen displaying the full item details before final deletion confirmation.

---

## 📊 Data Structure & Attributes

Each museum item is represented as an entity with the following fields:

| Attribute | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **Collection ID** | String | Unique identifier (Primary Key) | `F01`, `W01`, `P01` |
| **Title** | String | The official name of the item | `Mona Lisa` |
| **Region of Origin** | String | Continental or cultural region | `Europe` |
| **Place Discovered** | String | Exact location/city of discovery | `Florence, Italy` |
| **Era** | String | Historical period | `Renaissance` |
| **Year Discovered** | Integer | The calendar year it was found | `1517` |
| **Type** | String | Category classification | `Fossil`, `Weapon`, `Artifact`, `Painting` |
| **Status** | String | Current physical state/location | `Displayed`, `Storaged`, `Restoration` |

---

## 🛠️ Requirements & Installation

This application utilizes the `tabulate` library to output clean, well-formatted ASCII tables directly onto the terminal.

### Prerequisites
Make sure you have Python 3.x installed on your local machine.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone [https://github.com/ditodjati/museum-collection-manager.git](https://github.com/ditodjati/museum-collection-manager.git)
2. Navigate to the project directory:
   ```bash
   cd museum-collection-manager
3. Install the required dependency:
   ```bash
   pip install tabulate

## 💻 How to Run

You can run this application through two different formats provided in this repository:

### Running the Script (.py)

Execute the native Python script via your terminal:
```bash
python "ShangriLaMuseumDB.py"
```

### Running the Notebook (.ipynb)

If you prefer a step-by-step interactive environment:

1. Open your Jupyter Notebook environment or VS Code.
2. Launch the `*.ipynb` file.
3. Run the code cells sequentially to initiate the museum database interface.

## 🛡️ Robust Validation Highlights
* Input Error Handling: Employs `try-except` blocks to intercept non-integer inputs on numeric menus and years, preventing code crashes.
* Range Constraints: Validates that historical discovery years must sit within a logical historical framework (e.g., up to the current modern era).
