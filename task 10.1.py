# Problem 10.1: Display a bar chart of programming language popularity

import matplotlib.pyplot as plt

# Sample Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create a bar chart
plt.bar(languages, popularity, color=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0', '#00BCD4'])

# Add chart title and labels
plt.title('Popularity of Programming Languages', fontsize=14)
plt.xlabel('Programming Languages', fontsize=12)
plt.ylabel('Popularity (%)', fontsize=12)

# Add grid for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
