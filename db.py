import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame to simulate the database tables and their relationships.
tables = pd.DataFrame({
    'Table': ['Users', 'Wallets', 'Cards', 'Transactions', 'Notifications', 'Admins', 'Chats'],
    'Attributes': [
        len(['id', 'email', 'password_hash', 'created_at', 'last_login']),  # Count of attributes
        len(['id', 'user_id', 'balance', 'currency']),
        len(['id', 'user_id', 'card_number', 'expiry_date', 'cvv', 'type']),
        len(['id', 'sender_id', 'receiver_id', 'amount', 'currency', 'timestamp', 'status']),
        len(['id', 'user_id', 'message', 'timestamp', 'read_status']),
        len(['id', 'email', 'password_hash', 'created_at']),
        len(['id', 'email', 'password_hash', 'created_at'])
    ],
    'Foreign Keys': [
        '',  # Users table doesn't have a foreign key
        'user_id -> Users.id',
        'user_id -> Users.id',
        'sender_id -> Users.id, receiver_id -> Users.id',
        'user_id -> Users.id',
        ''  # Admins table doesn't have a foreign key
    ]
})

# Function to visualize the database table relationships
def visualize_database(tables):
    sns.set(style="whitegrid", palette="pastel")

    # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(10, 7))

    # Draw a barplot to show the number of attributes per table
    sns.barplot(x="Table", y="Attributes", data=tables, color="b")

    # Add annotations for foreign keys
    for i, row in tables.iterrows():
        plt.text(i, row['Attributes'] + 0.1, row['Foreign Keys'], color='black', ha="center")

    plt.ylabel('Number of Attributes')
    plt.title('Database Tables and Relationships')
    sns.despine(left=True, bottom=True)

    plt.show()

# Call the function to visualize the database
visualize_database(tables)
