import pandas as pd
import matplotlib.pyplot as plt

# Read the cleaned dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Count payment methods
payment_counts = df["PaymentMethod"].value_counts()

# Create pie chart
payment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution")
plt.ylabel("")  # Hide the default y-axis label
plt.show()