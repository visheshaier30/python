# Location Coordinate Processing System

# Storing GPS coordinates using tuples
location1 = (19.8762, 75.3433)  # Chhatrapati Sambhajinagar
location2 = ( 20.7072, 77.0030)  # Akola
location3 = (16.8676, 74.5704)  # Sangli

# Display coordinates
print("Location 1:", location1)
print("Location 2:", location2)
print("Location 3:", location3)

# Indexing
print("\nLatitude of Location 1:", location1[0])
print("Longitude of Location 1:", location1[1])

# Negative indexing
print("Longitude using negative index:", location1[-1])

# Tuple operations
print("\nTuple Length:", len(location1))

# Concatenation
combined = location1 + location2
print("Combined Tuple:", combined)

# Repetition
print("Repeated Location:", location1 * 2)

# Membership operation
print("\nIs latitude 18.5204 present?",
      18.5204 in location1)

# Comparison
print("Are Location 1 and Location 2 equal?",
      location1 == location2)

# Slicing
print("First coordinate value:", location1[:1])
print("Complete coordinate:", location1[:])