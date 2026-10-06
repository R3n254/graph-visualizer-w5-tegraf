import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Graph Visualizer & Matrix Analyzer", layout="wide")

st.title("Graph Visualizer & Matrix Analyzer")
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
    
    # Ensure nodes are labeled starting from 1 for readability
    mapping = {node: i+1 for i, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Graph Visualization")
        fig, ax = plt.subplots(figsize=(5, 4))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', width=2, ax=ax)
        st.pyplot(fig)
        
    with col2:
        st.subheader("2. Spanning Tree")
        if nx.is_connected(G):
            T = nx.minimum_spanning_tree(G)
            
            fig2, ax2 = plt.subplots(figsize=(5, 4))
            nx.draw(G, pos, with_labels=True, node_color='lightgray', node_size=700, edge_color='lightgray', ax=ax2)
            nx.draw_networkx_edges(T, pos, edge_color='red', width=2.5, ax=ax2)
            st.pyplot(fig2)
            st.caption("Red edges represent the Spanning Tree branches.")
        else:
            st.warning("Graph is disconnected. Tree and fundamental matrix analysis require a connected graph.")

    st.markdown("---")
    st.subheader("3. Graph Properties")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write(f"**Number of Vertices (n):** {G.number_of_nodes()}")
    with col_p2:
        st.write(f"**Number of Edges (m):** {G.number_of_edges()}")

    if nx.is_connected(G):
        # Normalize and list all edges consistently
        all_edges = [tuple(sorted(e)) for e in G.edges()]
        tree_edges = [tuple(sorted(e)) for e in T.edges()]
        chords = [e for e in all_edges if e not in tree_edges]

        # --- Fundamental Cycle Matrix (B_f) ---
        st.subheader("4. Fundamental Cycle Matrix (B_f)")
        st.markdown("Rows represent chords, and columns represent all graph edges.")
        
        bf_matrix = []
        for chord in chords:
            u, v = chord
            # Find path in spanning tree between chord endpoints
            path = nx.shortest_path(T, source=u, target=v)
            path_edges = [tuple(sorted((path[i], path[i+1]))) for i in range(len(path)-1)]
            cycle_edges = path_edges + [chord]
            
            row = [1 if edge in cycle_edges else 0 for edge in all_edges]
            bf_matrix.append(row)
            
        if bf_matrix:
            df_bf = pd.DataFrame(bf_matrix, columns=[str(e) for e in all_edges], index=[str(c) for c in chords])
            st.dataframe(df_bf)
        else:
            st.info("No chords found (graph is already a tree).")

        # --- Fundamental Cut-Set Matrix (Q_f) ---
        st.subheader("5. Fundamental Cut-Set Matrix (Q_f)")
        st.markdown("Rows represent tree branches, and columns represent all graph edges.")
        
        qf_matrix = []
        for branch in tree_edges:
            # Remove branch to create two components
            T_temp = T.copy()
            T_temp.remove_edge(*branch)
            components = list(nx.connected_components(T_temp))
            comp1, comp2 = components[0], components[1]
            
            # Find edges crossing between the two components
            cut_set_edges = []
            for edge in all_edges:
                u, v = edge
                if (u in comp1 and v in comp2) or (u in comp2 and v in comp1):
                    cut_set_edges.append(edge)
                    
            row = [1 if edge in cut_set_edges else 0 for edge in all_edges]
            qf_matrix.append(row)
            
        if qf_matrix:
            df_qf = pd.DataFrame(qf_matrix, columns=[str(e) for e in all_edges], index=[str(b) for b in tree_edges])
            st.dataframe(df_qf)

except Exception as e:
    st.error(f"Invalid matrix format or computation error: {e}")
