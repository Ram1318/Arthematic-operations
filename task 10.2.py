# Problem 10.2: Display a pie chart of programming language popularity

import matplotlib.pyplot as plt

# Sample Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create a pie chart
plt.pie(popularity,
        labels=languages,
        autopct='%1.1f%%',  # Display percentage with one decimal
        startangle=140,     # Rotate start angle for better visibility
        colors=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0', '#00BCD4'],
        shadow=True,
        explode=(0.05, 0.05, 0, 0, 0, 0))  # Slightly explode first two slices

# Add title
plt.title('Popularity of Programming Languages (Pie Chart)', fontsize=14)

# Equal aspect ratio ensures pie is drawn as a circle
plt.axis('equal')

# Display the chart
plt.show()
