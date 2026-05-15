# Object-Oriented Programming (OOP) Fundamentals

Welcome to the OOP Mastering Series. This repository is dedicated to exploring the core pillars of Object-Oriented Programming, providing clear explanations, code examples, and practical project assignments for each concept.

## Overview

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data (fields/attributes) and code (methods/behaviors).

---

## 1. Constructors
Constructors are special methods used to initialize objects. They are called when an instance of a class is created.

*   **Key Concept:** Setting up the initial state of an object.
*   **Project Assignment:** User Profile System
    *   Implement a system where a User object is initialized with essential details (username, email, age) using different constructor types (default, parameterized).

---

## 2. Encapsulation
Encapsulation is the bundling of data and the methods that operate on that data into a single unit (class), and restricting direct access to some of the object's components.

*   **Key Concept:** Data Hiding & Access Modifiers (Private, Public, Protected).
*   **Project Assignment:** Bank Account Manager
    *   Create a BankAccount class where the balance is private. Use Getters and Setters with validation logic (e.g., preventing negative deposits).

---

## 3. Abstraction
Abstraction involves hiding complex implementation details and showing only the necessary features of an object.

*   **Key Concept:** Abstract Classes & Interfaces.
*   **Project Assignment:** Smart Home Controller
    *   Define an abstract Device class with methods like turnOn() and turnOff(). Implement specific devices like Light and Thermostat that handle their own complex logic.

---

## 4. Inheritance
Inheritance allows a class (subclass) to acquire the properties and behaviors of another class (superclass).

*   **Key Concept:** Code Reusability & "Is-A" Relationship.
*   **Project Assignment:** Vehicle Fleet Management
    *   Create a base Vehicle class. Derive specialized classes like Car, Truck, and Motorcycle that inherit common traits (speed, fuel) but add their own unique features.

---

## 5. Polymorphism
Polymorphism allows objects of different types to be treated as objects of a common base type, often through method overriding or overloading.

*   **Key Concept:** "Many Forms" & Method Overriding.
*   **Project Assignment:** Universal Media Player
    *   Create a base MediaFile class with a play() method. Implement AudioFile and VideoFile that override play() to perform different actions (playing sound vs. rendering video).

---

## Getting Started
1. Navigate to the specific principle directory.
2. Review the code implementation for each principle.
3. Complete the assigned project challenge.

---

## Inspired By
This project is inspired by the book "Java: The Complete Reference, Ninth Edition".
