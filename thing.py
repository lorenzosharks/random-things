import matplotlib.pyplot as plt

# Define energy values in megatons
hiroshima_energy = 0.015  # in megatons
st_helens_energy = 24  # in megatons
tsar_bomba_energy = 50
total_energy = 109_000_000  # in megatons
yearly_consumption = 143_421_053

# Create labels and sizes
labels = ['Hiroshima Bomb', 'Mount St. Helens', 'Tsar Bomba', 'Asteroid Collision', '(Worldwide) Yearly Consumption of Electricity']
sizes = [hiroshima_energy, st_helens_energy, tsar_bomba_energy, total_energy, yearly_consumption]

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(labels, sizes, color=['blue', 'green', 'red', 'purple', 'orange'])

# Add labels and title
ax.set_ylabel('Energy (Megatons of TNT)')
ax.set_title('Energy Comparison')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()
