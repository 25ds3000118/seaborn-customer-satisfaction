import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic data generation (for reproducibility)
np.random.seed(42)
categories = ['Electronics', 'Home & Kitchen', 'Clothing', 'Sports', 'Beauty']
n = 200
data = {
    "category": np.random.choice(categories, size=n, p=[0.25,0.2,0.2,0.2,0.15]),
    "satisfaction": np.clip(np.random.normal(loc=4.0, scale=0.6, size=n), 1.0, 5.0)
}
df = pd.DataFrame(data)

# Styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

plt.figure(figsize=(8,8))
ax = sns.barplot(data=df, x="category", y="satisfaction", ci="sd", estimator=np.mean)
ax.set_title("Average Customer Satisfaction by Product Category", pad=15)
ax.set_xlabel("Product Category")
ax.set_ylabel("Average Satisfaction (1-5)")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
