import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic data
np.random.seed(42)
categories = ["Electronics", "Home & Kitchen", "Clothing", "Sports", "Beauty"]
n = 200
data = {
    "category": np.random.choice(categories, size=n, p=[0.25,0.2,0.2,0.2,0.15]),
    "satisfaction": np.clip(np.random.normal(loc=4.0, scale=0.6, size=n), 1.0, 5.0)
}
df = pd.DataFrame(data)

# Styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Force EXACT pixel output: 512x512 px
fig = plt.figure(figsize=(8, 8), dpi=64)   # 8in * 64dpi = 512px exactly

ax = sns.barplot(data=df, x="category", y="satisfaction", ci="sd", estimator=np.mean)
ax.set_title("Average Customer Satisfaction by Product Category", pad=15)
ax.set_xlabel("Product Category")
ax.set_ylabel("Average Satisfaction (1–5)")
plt.xticks(rotation=25, ha="right")

# IMPORTANT: DO NOT use bbox_inches="tight"
plt.savefig("chart.png", dpi=64)
plt.close()
