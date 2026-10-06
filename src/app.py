import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Graph Visualizer & Matrix Analyzer", layout="wide")

st.title("🔗 Graph Visualizer & Matrix Analyzer")
st.markdown("Group Homework: Matrix Representation, Spanning Trees, and Fundamental Matrices.")

# Sidebar for Input
st.sidebar.header("Graph Input")
default_matrix = "0, 1, 1, 0\n1, 0, 1, 1\n1, 1, 0, 1\n0, 1, 1, 0"
matrix_input = st.sidebar.text_area("Enter Adjacency Matrix (comma/space separated):", value=default_matrix, height=150)

try:
    # Parse matrix input
    lines = matrix_input.strip().split("\n")
    matrix = [[float(val.strip()) for val in line.replace(",", " ").split() if val.strip()] for line in lines]
    adj_matrix = np.array(matrix)
    
    # Create NetworkX Graph
    G = nx.from_numpy_array(adj_matrix)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Graph Visualization")
        fig, ax = plt.subplots(figsize=(5, 4))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', width=2, ax=ax)
        st.pyplot(fig)
        
    with col2:
        st.subheader("2. Spanning Tree & Fundamental Cycles")
        if nx.is_connected(G):
            # Find a spanning tree
            T = nx.minimum_spanning_tree(G)
            
            fig2, ax2 = plt.subplots(figsize=(5, 4))
            # Draw full graph faint, tree bold
            nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=700, edge_color='lightgray', ax=ax2)
            nx.draw_networkx_edges(T, pos, edge_color='red', width=2.5, ax=ax2)
            st.pyplot(fig2)
            st.caption("Red edges represent the Spanning Tree branches.")
        else:
            st.warning("Graph is disconnected. Fundamental cycle analysis requires a connected graph.")

    st.subheader("3. Matrix Properties")
    st.write(f"**Number of Vertices (Nodes):** {G.number_of_nodes()}")
    st.write(f"**Number of Edges:** {G.number_of_edges()}")

except Exception as e:
    st.error(f"Invalid matrix format or computation error: {e}")
