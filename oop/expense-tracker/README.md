# Java Expense Tracker

## Overview

A simple, console-based expense tracking application built with Java. It allows users to record, manage, and analyse their personal expenses while practising Java fundamentals, object-oriented programming, and data structures.

## Features and Operations

1. Add Expense: record an expense with a description, amount, category, and unique ID.
2. View All Expenses: display all recorded expenses.
3. View Single Expense: retrieve an expense using its ID.
4. Update Expense: modify an existing expense.
5. Delete Expense: remove an expense using its ID.
6. Search Expenses: find expenses by description.
7. Filter Expenses: filter expenses by category.
8. Calculate Total Expenses: calculate the total amount spent.
9. View Category Summary: calculate total spending for each category.
10. View Expense Summary: display the number of expenses, total spending, average expense, and largest expense.

## Technology Stack

* Java
* ArrayList for in-memory storage
* Object-Oriented Programming (OOP)

## Data Model

Each expense contains:

* id: unique identifier
* description: what the money was spent on
* amount: amount spent
* category: expense category

## Storage

Expenses will initially be stored in an ArrayList. Data will be lost when the application terminates. PostgreSQL can be introduced later for persistent storage.

## Learning Objectives

* Practise Java fundamentals and OOP.
* Understand collections, loops, and conditional statements.
* Implement CRUD operations.
* Practise input validation and exception handling.
* Learn basic application structure and separation of concerns.

## How to Run

1. Install the JDK.
2. Clone or download the project.
3. Compile the Java source files.
4. Run the Main class.

## Future Improvements

* Integrate PostgreSQL using JDBC.
* Build a REST API using Spring Boot.
* Add automated tests using JUnit.
