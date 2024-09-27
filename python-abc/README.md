# Python - Abstract Classes and Interfaces

## Introduction:
Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

## Learning Objectives:

Abstract Classes: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
Interfaces and Duck Typing: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
Subclassing Standard Base Classes: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
Method Overriding: Employ method overriding to alter or enhance the behavior of base class methods.
Multiple Inheritance: Understand and apply multiple inheritance to form complex relationships between classes.
Mixins: Utilize mixins to compose behavior across unrelated classes.

## Tasks
0. Abstract Animal Class and its Subclasses
Objective:
Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.

1. Shapes, Interfaces, and Duck Typing
Objective:
Create an abstract class named Shape with two abstract methods: area and perimeter.
Implement two concrete classes: Circle and Rectangle, both inheriting from Shape. Each class should provide implementations for the area and perimeter methods.
Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.
Test the shape_info function with instances of both Circle and Rectangle.


2. Extending the Python List with Notifications
Objective:
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).


3. CountedIterator - Keeping Track of Iteration
Objective:
Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.

4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Objective:
Construct a FlyingFish class that inherits from both a Fish class and a Bird class. Within FlyingFish, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.


5. The Mystical Dragon - Mastering Mixins
Objective:
Design two mixin classes, SwimMixin and FlyMixin, each equipped with methods swim and fly respectively. Next, construct a class Dragon that inherits from both these mixins. Your aim is to show that a Dragon instance can both swim and fly.

