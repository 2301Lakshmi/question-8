"""
MRR Quarterly Analysis — 2024
Produces:
 - mrr_quarterly_2024.csv
 - mrr_trend.png
 - prints summary statistics

Author: generated with LLM assistance (Jules / ChatGPT Codex)
Verification email: 22f1000912@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path("analysis_output")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Quarterly MRR growth data (provided)
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
mrr_growth = [8.07, 8.69, 12.65, 13.04]

df = pd.DataFrame({
    "quarter": quarters,
    "mrr_growth": mrr_growth
})

# Save CSV to repo output
csv_path = OUT_DIR / "mrr_quarterly_2024.csv"
df.to_csv(csv_path, index=False)

# Compute average (round to 2 decimals for reporting)
average = df["mrr_growth"].mean()
print(f"Computed average (full precision): {average!r}")
print(f"Computed average (rounded 2d): {average:.2f}")

# Plot: bar + trend + benchmark + average
industry_target = 15.0

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(df["quarter"], df["mrr_growth"])
ax.plot(df["quarter"], df["mrr_growth"], marker='o')
ax.axhline(industry_target, linestyle='--', linewidth=1)
ax.text(3.05, industry_target+0.25, f"Industry target = {industry_target}", va='bottom')

ax.axhline(average, linestyle=':', linewidth=1)
ax.text(3.05, average+0.25, f"Average = {average:.2f}", va='bottom')

ax.set_title("MRR Growth by Quarter — 2024")
ax.set_ylabel("MRR Growth (%)")
ax.set_ylim(0, max(industry_target, max(mrr_growth)) + 5)

plt.tight_layout()
plot_path = OUT_DIR / "mrr_trend.png"
plt.savefig(plot_path)
plt.close(fig)

print(f"Saved CSV to: {csv_path}")
print(f"Saved plot to: {plot_path}")
