# Mini-Project: The Luxury Resort Room Manager

## Objective
In this project, you will build a backend room management system for a premium resort right inside your Jupyter Notebook. 
You will apply Object-Oriented Programming (OOP) concepts to create a `ResortRoom` class that tracks the state of individual rooms (available or booked) and handles the logic for checking guests in and out.

## Prerequisites
Before you begin, ensure you understand:
* How to define classes and initialize attributes using `__init__`.
* How to manage and update the "state" of an object (e.g., changing a boolean from `False` to `True`).
* How to use `if/else` statements inside class methods.
* How to execute code cells in a Jupyter environment.

## Step-by-Step Instructions

### Step 1: Set Up Your Notebook
1. In your workspace, create a new file named `resort_manager.ipynb`.
2. All your code for this project will go inside the code cells of this notebook.

### Step 2: Define the Blueprint
1. In your first cell, create a class named `ResortRoom`.
2. Define the `__init__` method to take three parameters alongside `self`: `room_number` (int), `room_type` (string, e.g., "Villa" or "Suite"), and `nightly_rate` (float).
3. Inside `__init__`, set up those three attributes.
4. Add a fourth attribute called `self.is_booked` and set it to `False` by default (because a new room starts empty).

### Step 3: Create the Booking Method
1. Define a method called `book_room(self)` inside your class.
2. Inside this method, write an `if/else` check:
   * **If** the room is NOT booked (`if not self.is_booked:`), change `self.is_booked` to `True` and print a success message (e.g., "Room 101 successfully booked!").
   * **Else**, print a message saying the room is currently unavailable.

### Step 4: Create the Checkout Method
1. Define a method called `checkout(self)` inside your class.
2. Inside this method, write an `if/else` check:
   * **If** the room IS booked (`if self.is_booked:`), change `self.is_booked` back to `False` and print a checkout success message.
   * **Else**, print a message saying the room is already empty.

### Step 5: Check Availability Status
1. Define a method called `check_status(self)` inside your class.
2. This method should print a clean summary of the room. 
For example: "Room 101 (Villa) - $500/night - Status: Booked" (Hint: Use an `if/else` to print "Booked" or "Available" based on the boolean state).

*Note: To test your system, create a new code cell at the bottom of your notebook! Create an instance of a room 
(e.g., `oasis_villa = ResortRoom(101, "Villa", 850.00)`), call `.book_room()` on it, and then check its status. 
Press **Shift + Enter** to run the cell and verify your output!*