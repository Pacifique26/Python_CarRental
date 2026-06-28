# Python_CarRental

### Car 🚗 Rental Management System (Python) 🚗

## Introduction

The Car Rental Management System is a simple command-line application developed in Python using Object-Oriented Programming (OOP) principles. The project simulates the operations of a car rental shop, allowing customers to rent cars on an hourly, daily, or weekly basis and calculate rental charges upon return.

The application demonstrates the practical implementation of Python classes, object interaction, user input validation, inventory management, and billing logic. It is an ideal beginner-to-intermediate level project for learning OOP concepts and building real-world console applications.

## Key Insights and Code Methodology

The project is structured around two primary classes:

### 1. CarRental Class

Responsible for managing the rental shop operations.

#### Main responsibilities:

- Maintains the available car inventory.
- Displays available cars.
- Processes hourly, daily, and weekly rentals.
- Updates stock after each rental.
- Calculates rental charges when cars are returned.
- Restores returned cars to inventory.

### 2. Customer Class

Represents a customer renting vehicles.

#### Main responsibilities:

- Requests the number of cars.
- Stores rental information: Number of cars, Rental basis, Rental time
- Returns rental information for billing.

## Program Workflow
1) Initialize the rental shop with available cars.
2) Display a menu-driven interface.
3) Customer selects a rental option.
4) Validate customer input.
5) Reduce available stock after successful rental.
6) Store rental details.
7) Calculate the rental duration and bill when the customer returns the car.
8) Restore stock and reset customer information.

# Programming Concepts Used
- Object-Oriented Programming (Classes & Objects)
- Constructors (__init__)
- Instance Variables
- Conditional Statements
- Loops (while)
- Exception Handling (try-except)
- Date and Time Handling (datetime)
- User Input Validation
- Inventory Management
- Modular Programming

## Guide for Users

#### Step 1
Run the main Python file.
python main.py

#### Step 2
##### Select an option from the menu:
1. Display available cars
2. Rent hourly
3. Rent daily
4. Rent weekly
5. Return cars
6. Exit

#### Step 3
##### Enter the number of cars you want to rent.
The system will:
- Validate the request.
- Check stock availability.
- Record the rental time.

#### Step 4
##### Return the rented cars.
The system automatically:
- Calculates the rental duration.
- Computes the rental cost.
- Updates the available inventory.

#### Rental Rates
Rental Type	Cost
- Hourly	$5 per hour
- Daily	$20 per day
- Weekly	$60 per week

## Summary

The Car Rental Management System is a beginner-friendly Python project that demonstrates the practical application of Object-Oriented Programming concepts through a real-world business scenario. It provides a simple yet effective implementation of inventory management, customer interaction, rental tracking, and automated billing using Python's built-in libraries.

This project serves as an excellent foundation for learning software design principles and can be extended into a full-featured desktop or web application by integrating databases, graphical interfaces, authentication, and advanced business logic.

## What Should Be Improved

Although the project successfully demonstrates the fundamentals of a rental management system, several enhancements can make it more robust and realistic:

- Store customer records using unique customer IDs.
- Support multiple customers simultaneously.
- Save rental information in a database (SQLite/MySQL/PostgreSQL).
- Persist rental records using files or databases instead of memory.
- Add discount offers (e.g., family or long-term rental discounts).
- Improve billing calculations for partial days and weeks.
- Include overdue charges and late return penalties.
- Generate rental receipts or invoices.
- Implement login/authentication for administrators and customers.
- Develop a graphical user interface (GUI) using Tkinter or PyQt.
- Build a web-based version using Flask or Django.
- Add unit tests to improve software reliability.
- Enhance error handling and logging.
- Apply better project structure by separating models, services, and user interface into different modules.
