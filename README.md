# Graph Visualizer & Matrix Analyzer

A Python tool designed for our graph theory homework to make analyzing and visualizing network structures a lot easier. Instead of calculating everything by hand, you can input an adjacency or incidence matrix, and the program will automatically generate a visual model of the graph. On top of that, it handles the heavier calculations for you, instantly computing both the Fundamental Cycle Matrix and the Cut-Set Matrix.

---

### Group Members

| No. | Name | NRP |
|---:|---|---|
| 1 | Ahmad Farras Favian Al Efasi | 5025251005 |
| 2 | Daniel Pedrosaputra | 5025251171 |

---

## Features

1. **Matrix Input**: Accepts user input for either an Adjacency Matrix or an Incidence Matrix.
2. **Graph Visualization**: Plots and displays the graph structure based on the provided input data.
3. **Advanced Calculations**: Automatically computes the:
   * Fundamental Cycle Matrix
   * Cut-Set Matrix

---

## How to Run / Access

The application is hosted online, allowing anyone with the link to access and use it directly in a web browser without local installation:

* **Live App URL**: [Graph Visualizer & Matrix Analyzer on Streamlit](https://graph-visualizer-w5-tegraf-t43pxpgczclcpj7y9duwpl.streamlit.app/)

---

## Sample Input & Output

### Sample Input
* **Graph Type**: Undirected Graph
* **Adjacency Matrix Configuration** (Example for a 4-vertex complete or connected graph):
  ```text
  0 1 1 0
  1 0 1 1
  1 1 0 1
  0 1 1 0

### Sample Output
<img width="1974" height="966" alt="image" src="https://github.com/user-attachments/assets/e2a1fc9a-230c-4721-84fe-d2b1bc78a1e3" />

## AI Tools Usage Disclosure
* **Tool**: Gemini
* **Usage**: AI was used during the preparation of this assignment to understand project requirements, structure the Streamlit web application, debug deployment errors, and format the repository documentation.
* **Prompts Used**:
  1. "Explain to me how we should approach this Graph Theory task for the Fundamental Cycle Matrix and Cut-Set Matrix."
  2. "Help me write the Python code using Streamlit and NetworkX to take an adjacency matrix input and visualize the graph and spanning tree."
  3. "Fix this error: ModuleNotFoundError: No module named 'networkx' in Streamlit Cloud."
  4. "How do I deploy this Streamlit app to Streamlit Community Cloud?"
  5. "Make a README file for the repository including our identities, prerequisites, how to run, and sample output."
