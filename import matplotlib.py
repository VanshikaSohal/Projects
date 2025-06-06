import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
bar_width = 0.25
x = range(len(df))

plt.bar([i - bar_width for i in x], df['Bubble Sort Time'], width=bar_width, label='Bubble Sort')
plt.bar(x, df['Merge Sort Time'], width=bar_width, label='Merge Sort')
plt.bar([i + bar_width for i in x], df['Quick Sort Time'], width=bar_width, label='Quick Sort')

plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Time Comparison')
plt.xticks(ticks=x, labels=df['Array Size'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 🔥 Save the plot as an image!
plt.savefig("benchmark_plot.png")

# Show it (optional)
plt.show()
