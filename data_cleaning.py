import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
df = pd.DataFrame({
    "Name": ["Arun", "Bala", "Charan", "Divya", "Divya"],
    "Marks": [80, 65, None, 90, 90],
    "Attendance": [90, 75, 80, 95, 95]
})

print("Original Data:")
print(df)

# Fill missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

# Create bar chart
df.plot(x="Name", y="Marks", kind="bar",
        title="Student Marks")
plt.tight_layout()
plt.show()

# Create box plot
sns.boxplot(x=df["Marks"])
plt.title("Marks Distribution")
plt.show()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned dataset saved successfully!")