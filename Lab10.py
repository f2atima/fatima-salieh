import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

plt.plot(x1, y1)
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

x2 = [1, 2, 3, 4, 5]
y2 = [5, 7, 6, 8, 10]

plt.scatter(x2, y2, s=100, color='green')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

x3 = [1, 2, 3, 4, 5]
y3_1 = [1, 2, 3, 4, 5]
y3_2 = [1, 4, 9, 16, 25]

plt.plot(x3, y3_1, label='Linear', marker='o')
plt.plot(x3, y3_2, label='Quadratic', linestyle='--', marker='s')
plt.title('Multiple Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.bar(categories, values)
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

langs = ['Python', 'Java', 'C++']
shares = [40, 35, 25]

plt.pie(shares, labels=langs, autopct='%1.1f%%')
plt.title('Pie Chart Example')
plt.show()

x4 = np.arange(1, 6)
y4_1 = x4
y4_2 = x4**2

plt.figure(figsize=(6, 6))

plt.subplot(2, 1, 1)
plt.plot(x4, y4_1, marker='o')
plt.title('First Subplot')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x4, y4_2, marker='s')
plt.title('Second Subplot')
plt.grid(True)

plt.tight_layout()
plt.show()

data = np.random.randn(1000)

plt.hist(data, bins=20)
plt.title('Histogram Example')
plt.savefig('histogram_example.png')
plt.show()

plt.boxplot(data)
plt.title('Box Plot Example')
plt.show()