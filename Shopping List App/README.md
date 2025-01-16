# Nákupní Seznam (Shopping List Application)
This project is a graphical user interface (GUI) application built with Python's tkinter library. It allows users to create and manage a shopping list, with functionality to add, edit, delete, and save/load items in various file formats such as CSV and Pickle.
## Features
- Add Items: Add a new item to the shopping list.
- Edit Items: Modify an existing item in the list.
- Delete Items: Remove an item from the list.
- Save/Load CSV: Save the shopping list to a CSV file or load it back into the app.
- Save/Load Pickle: Save the shopping list in Python's Pickle format or load it back into the app.
## Prerequisites
Make sure you have Python installed on your machine. This app uses built-in Python libraries (`tkinter`, `csv`, and `pickle`), so no additional dependencies are required.
## How to Run the Application
1. Clone the Repository

<code>git clone https://github.com/AshenVoid/AppShowcasePython.git</code>
<code>cd AppShowcasePython</code>

2. Run the Application
- Windows: <code>python shopping_list.py</code>
- Mac: <code>python3 shopping_list.py</code>

3. The application window will open, and you can start managing your shopping list.

## GUI Instructions
### Adding Items:
- Enter the item name in the input field.
- Click the "Add Item" button to add the item to the list.
### Editing Items:
- Select an item from the listbox.
- Enter the new name in the input field.
- Click the "Edit Item" button to update the selected item.
### Deleting Items:
- Select an item from the listbox.
- Click the "Delete Item" button to remove it.
### Saving and Loading Files:
- Use the "Save to CSV" or "Save to Pickle" buttons to save the list to a file.
- Use the "Load from CSV" or "Load from Pickle" buttons to load a saved list.
## File Formats Supported
- CSV:
  - A plain-text format for storing the shopping list.
  - Compatible with spreadsheet software like Microsoft Excel.
- Pickle:
  - A binary format used to serialize Python objects.
  - Efficient for storing and loading Python-native data structures.

## Example Workflow
1. Open the app and add several items to the list (e.g., "Milk", "Bread").
2. Save the list to a CSV or Pickle file.
3. Close the app and relaunch it.
4. Load the previously saved file to restore your list.
5. Modify, add, or delete items as needed.

## Customization

Feel free to extend the functionality of this application. (I might work on those in the future.) Here are some ideas:

- Add support for JSON file formats.

- Include a search or filter feature for the list.

- Enable multi-select for batch editing or deletion.

- Add a total count or categorization of items.

### License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

### Acknowledgments

This application was created as a simple example of using tkinter for GUI development in Python. It demonstrates basic CRUD operations and file handling using CSV and Pickle formats.