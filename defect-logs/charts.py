import matplotlib.pyplot as plt
import numpy as np

cats = ["Ambiguity","Vagueness","Incompleteness","Contradiction",
        "Non-verifiability","Redundancy","Infeasibility","Untraceability"]
high = [2,3,2,2,1,0,0,0]
med  = [2,2,8,0,2,0,1,0]
low  = [1,0,0,0,0,2,0,2]

x = np.arange(len(cats))
plt.figure(figsize=(10,6))
plt.bar(x, high, label="High", color="#d62728")
plt.bar(x, med, bottom=high, label="Medium", color="#ff9f1c")
plt.bar(x, low, bottom=np.array(high)+np.array(med), label="Low", color="#2ca02c")
plt.xticks(x, cats, rotation=35, ha="right")
plt.ylabel("Number of defects")
plt.title("PSVS Requirements: Defects by Category and Severity (n=30)")
plt.legend()
plt.tight_layout()
plt.savefig("../reports/defects_by_category.png", dpi=200)
