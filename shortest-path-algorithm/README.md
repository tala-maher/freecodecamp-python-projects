# Learn Algorithm Design by Building a Shortest Path Algorithm

This project is part of my learning journey in **algorithm design** and **graph theory**.  
Here, I implemented **Dijkstra’s Algorithm** step by step to calculate the shortest path between nodes in a weighted graph.  

---

## 🚀 Project Overview
The goal of this project is to understand how shortest path algorithms work by building one from scratch in Python.  
The program:
- Takes a graph represented as a dictionary of adjacency lists.  
- Calculates the shortest distances from a starting node to all other nodes.  
- Tracks the paths taken along the way.  
- Optionally returns only the shortest path to a specified target node.  

---

## 🧩 Concepts Learned
- Graph representation in Python using dictionaries.  
- Algorithm design step by step.  
- Tracking **unvisited nodes**, **distances**, and **paths**.  
- Using Python features like:
  - `list()` and `dict()` comprehensions  
  - Conditional (ternary) expressions  
  - Built-in functions like `min()` with custom keys  
- Handling mutable lists carefully with slicing to avoid reference bugs.  

---

## 🖥️ Example Usage
```python
# Define the graph
my_graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 6), ('D', 1)],
    'C': [('A', 5), ('B', 6), ('D', 2), ('E', 5)],
    'D': [('B', 1), ('C', 2), ('E', 1), ('F', 4)],
    'E': [('C', 5), ('D', 1), ('F', 2)],
    'F': [('D', 4), ('E', 2)]
}

# Call the function
shortest_path(my_graph, 'A', 'F')

---

## ✅ Output:
A-F distance: 7
Path: A -> B -> D -> E -> F
