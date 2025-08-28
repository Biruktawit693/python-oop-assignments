# Python OOP Assignments

This repository contains two Python assignments demonstrating Object-Oriented Programming (OOP) concepts, including class design, inheritance, and polymorphism.

---

## Assignment 1: Design Your Own Class 🏗️

**Program Description:**  
This assignment involves designing a class representing a real-world object — in this case, a **Smartphone**. The program demonstrates how to create objects with unique attributes and methods, and also shows inheritance through a specialized subclass.

**Classes & Features:**
- `Smartphone`: Base class with attributes `brand`, `model`, `storage` and methods `make_call()` and `take_photo()`.
- `GamingSmartphone`: Inherits from `Smartphone`, adds a `gpu` attribute, and a `play_game()` method.
- Constructor `__init__()` initializes objects with unique values.
- Demonstrates **inheritance** and **encapsulation**.

**Outcome:**  
Users can create smartphone objects, perform actions like making calls or taking photos, and explore how a subclass can extend the functionality of a parent class.

---

## Assignment 2: Polymorphism Challenge 🎭

**Program Description:**  
This assignment focuses on **polymorphism** by defining multiple classes with the same method `move()`, where each class implements it differently.

**Classes & Features:**
- `Vehicle`: Base class with a placeholder `move()` method.
- `Car`, `Plane`, `Boat`: Each inherits from `Vehicle` and defines `move()` differently:
  - `Car.move()` → prints "Driving 🚗"  
  - `Plane.move()` → prints "Flying ✈️"  
  - `Boat.move()` → prints "Sailing ⛵"  
- Demonstrates **polymorphism** and **inheritance**.

**Outcome:**  
Users learn how objects of different classes can share the same interface (`move()`) but behave differently, demonstrating the flexibility of OOP.

---

Both assignments together illustrate key OOP concepts in Python: **class design, constructors, inheritance, encapsulation, and polymorphism**, providing a strong foundation for more complex programming tasks.

