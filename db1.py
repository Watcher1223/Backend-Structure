# import networkx as nx
# import pandas as pd
# import matplotlib.pyplot as plt

# def visualize_database_network(tables):
#     G = nx.DiGraph()

#     # Add nodes with attributes for tables
#     for index, row in tables.iterrows():
#         G.add_node(row['Table'], size=row['Attributes'])

#     # Define edges from foreign keys
#     edges = {
#         "Wallets": "Users",
#         "Cards": "Users",
#         "Transactions": ["Users", "Users"],  # Sender and Receiver
#         "Notifications": "Users",
#         "Chats": "Users",
#         "Groups": "Users",
#         "Group Memberships": ["Groups", "Users"],
#         "Fundraisers": "Groups"
#     }

#     for key, value in edges.items():
#         if isinstance(value, list):
#             for v in value:
#                 G.add_edge(key, v)
#         else:
#             G.add_edge(key, value)

#     # Plot
#     pos = nx.spring_layout(G, seed=42)  # positions for all nodes
#     nx.draw(G, pos, with_labels=True, node_size=[len(v) * 1000 for v in G.nodes.values()], node_color="skyblue", font_size=9)
#     plt.title('Database Schema Network')
#     plt.show()

# # Define the 'tables' DataFrame here
# tables = pd.DataFrame({
#     'Table': ['Users', 'Wallets', 'Cards', 'Transactions', 'Notifications', 'Chats', 'Groups', 'Group Memberships', 'Fundraisers'],
#     'Attributes': [5, 4, 6, 7, 5, 4, 4, 2, 4]  # Example attribute counts
# })

# # Call the visualization function with the defined tables
# visualize_database_network(tables)

# import os
# import networkx as nx
# import pandas as pd
# import matplotlib.pyplot as plt
# import imageio.v2 as imageio  # Updated import for imageio to avoid deprecation warning
# import tempfile

# def ensure_dir(file_path):
#     directory = os.path.dirname(file_path)
#     if not os.path.exists(directory):
#         os.makedirs(directory)

# def visualize_database_network(tables, save_path):
#     ensure_dir(save_path)  # Ensure the directory exists

#     G = nx.DiGraph()

#     # Define nodes and edges
#     for index, row in tables.iterrows():
#         G.add_node(row['Table'], size=row['Attributes'])

#     edges = {
#         "Wallets": "Users",
#         "Cards": "Users",
#         "Transactions": ["Users", "Users"],
#         "Notifications": "Users",
#         "Chats": "Users",
#         "Groups": "Users",
#         "Group Memberships": ["Groups", "Users"],
#         "Fundraisers": "Groups"
#     }

#     for key, values in edges.items():
#         if not isinstance(values, list):
#             values = [values]
#         for value in values:
#             G.add_edge(key, value)

#     pos = nx.spring_layout(G, seed=42)  # Node positions
#     frames = []

#     # Create frames for each edge
#     for key, values in edges.items():
#         if not isinstance(values, list):
#             values = [values]
#         for value in values:
#             plt.figure(figsize=(10, 7))
#             nx.draw(G, pos, with_labels=True, node_size=[G.nodes[v]['size'] * 1000 for v in G], node_color="skyblue", font_size=9)
#             plt.title('Database Schema Network')
#             plt_path = os.path.join(save_path, f"{key}_to_{value}.png")
#             plt.savefig(plt_path)
#             plt.close()
#             frames.append(imageio.imread(plt_path))

#     gif_path = os.path.join(save_path, "network_animation.gif")
#     imageio.mimsave(gif_path, frames, duration=0.5)
#     print(f"Animated GIF saved at {gif_path}")

# # Define the DataFrame and call the function
# tables = pd.DataFrame({
#     'Table': ['Users', 'Wallets', 'Cards', 'Transactions', 'Notifications', 'Chats', 'Groups', 'Group Memberships', 'Fundraisers'],
#     'Attributes': [5, 4, 6, 7, 5, 4, 4, 2, 4]
# })

# # Example directory path
# fixed_path = '/Users/alspenceramitojr/Desktop/' 
# visualize_database_network(tables, save_path=fixed_path)

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Define the DataFrame representing your tables and relationships
tables = pd.DataFrame({
    'Table': ['Users', 'Wallets', 'Cards', 'Transactions', 'Notifications', 'Chats', 'Groups', 'Subscriptions', 'Fundraisers'],
    'Attributes': [5, 4, 6, 7, 5, 4, 4, 2, 4]  # Just an example
})

# Initialize the graph
G = nx.DiGraph()

# Add nodes with attributes for tables
for index, row in tables.iterrows():
    G.add_node(row['Table'], size=row['Attributes'])

# Define edges from foreign keys
edges = [
    ("Users", "Wallets"),
    ("Wallets", "Cards"),
    ("Cards", "Users"),
    ("Transactions", "Cards"),
    ("Subscriptions", "Users"), 
    ("Chats", "Groups"),
    ("Groups", "Users"),
    ("Notifications", "Users"),
    ("Notifications", "Transactions"),
    ("Fundraisers", "Users"),
    # Assuming transactions link back to Users as sender/receiver
    # Add more edges as needed
]

# Set positions for all nodes - you might need to customize this layout
pos = nx.spring_layout(G, seed=42)

# Initialize a matplotlib figure
fig, ax = plt.subplots(figsize=(10, 7))

# This will be the update function for the animation
def update(num):
    if num < len(edges):
        G.add_edge(*edges[num])
    ax.clear()  # Clear the previous frame
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=[G.nodes[v]['size'] * 100 for v in G])
    ax.set_title("Database Schema Network")

# Create the animation
ani = FuncAnimation(fig, update, frames=len(edges), repeat=False)

# Save the animation
ani.save("network_animation.gif", writer='imagemagick', fps=1)

plt.show()  # Show the plot last
