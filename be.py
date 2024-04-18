import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Backend structure components
components = [
    'Web/Mobile Client', 'API Gateway', 'Authentication Service',
    'User Management Service', 'Wallet Service', 'Card Management Service',
    'Transaction Service', 'Reporting & Analytics Service', 'Group Expense Service',
    'Notifications Service', 'Admin Panel', 'Security Layer', 'Database'
]

# Define connections between components
connections = {
    'Web/Mobile Client': ['API Gateway'],
    'API Gateway': ['Authentication Service', 'User Management Service', 'Wallet Service',
                    'Card Management Service', 'Transaction Service', 'Reporting & Analytics Service',
                    'Group Expense Service', 'Notifications Service', 'Admin Panel'],
    'Authentication Service': ['Database'],
    'User Management Service': ['Database'],
    'Wallet Service': ['Database'],
    'Card Management Service': ['Database'],
    'Transaction Service': ['Database'],
    'Reporting & Analytics Service': ['Database'],
    'Group Expense Service': ['Database'],
    'Notifications Service': ['Database'],
    'Admin Panel': ['Database'],
    'Security Layer': ['API Gateway'],
    'Database': []
}

# Initialize figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, len(components)+1)
plt.axis('off')

# Draw components as rectangles
rectangles = {}
for i, component in enumerate(components):
    rect = mpatches.Rectangle((1, len(components) - i), 8, 0.6, ec="none")
    rectangles[component] = rect
    ax.add_patch(rect)
    rx, ry = rect.get_xy()
    cx = rx + rect.get_width()/2.0
    cy = ry + rect.get_height()/2.0

    # Add text in the middle of the rectangle
    ax.annotate(component, (cx, cy), color='black', weight='bold', 
                fontsize=10, ha='center', va='center')

# Draw connections between components
for comp, deps in connections.items():
    for dep in deps:
        # Get center of rectangles for the two components
        x1, y1 = rectangles[comp].get_xy()
        x1 += rectangles[comp].get_width() / 2.0
        y1 += rectangles[comp].get_height() / 2.0
        x2, y2 = rectangles[dep].get_xy()
        x2 += rectangles[dep].get_width() / 2.0
        y2 += rectangles[dep].get_height() / 2.0

        # Draw line with arrow from comp to dep
        plt.arrow(x1, y1, x2 - x1, y2 - y1, head_width=0.2, head_length=0.1, fc='k', ec='k')

# Set title
plt.title('Backend Structure for MoneyLink App')

# Show the plot
plt.show()



# Define the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Add boxes for each service in the backend
services = {
    'Authentication Service': (0.1, 0.8),
    'User Management Service': (0.1, 0.7),
    'Wallet Service': (0.1, 0.6),
    'Card Management Service': (0.1, 0.5),
    'Transaction Service': (0.1, 0.4),
    'Reporting & Analytics': (0.1, 0.3),
    'Group Expense Service': (0.1, 0.2),
    'Notifications Service': (0.1, 0.1),
    'API Gateway': (0.5, 0.8),
    'Security Layer': (0.5, 0.6),
    'Admin Panel': (0.5, 0.4),
    'Database': (0.5, 0.2)
}

# Draw boxes and labels for services
for service, (x, y) in services.items():
    ax.text(x, y, service, ha='center', va='center', fontsize=12)
    ax.add_patch(plt.Rectangle((x-0.1, y-0.05), 0.2, 0.1, fill=None, edgecolor='purple', lw=2))

# Add lines to indicate interactions
ax.arrow(0.3, 0.8, 0.15, 0, head_width=0.03, head_length=0.02, fc='blue', ec='blue')
ax.arrow(0.3, 0.1, 0.15, 0.67, head_width=0.03, head_length=0.02, fc='blue', ec='blue')

# Hide axes
ax.set_axis_off()

# Set the title
ax.set_title('Backend Services Architecture', fontsize=16)

# Display the plot
plt.show()
