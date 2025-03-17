import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "Data.csv"  # Make sure the filename matches exactly
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary of the dataset:")
print(df.describe())

# Set the figure size
plt.figure(figsize=(10, 5))

# Line plot of sensor readings over time
sns.lineplot(x=df.index, y=df.iloc[:, 1])  # Assuming second column is sensor data

# Set title and labels
plt.title("Sensor Data Over Time")
plt.xlabel("Time")
plt.ylabel("Sensor Value")

# Show the plot
plt.show()
