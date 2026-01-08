[visualizingdata.py](https://github.com/user-attachments/files/24485513/visualizingdata.py)# visualizing-interesting-datasets
Visualizing two datasets
# Project 02: Visualizing Interesting Datasets

This project explores two datasets using Python and pandas, and visualizes them with matplotlib. The goal is to analyze the data and present insights clearly through two different types of plots.

---

## Plot 1: Bookings Data (Scatter Plot)

![Bookings Scatter Plot](Booking<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/59ff41ba-3854-43f9-bd4c-09a0a3a72ae4" />
s_plot.png)

This scatter plot visualizes the Bookings dataset, which contains data on Uber bookings and cancellations. Each point represents a booking, allowing us to see patterns and trends in cancellations versus completed bookings. The x-axis and y-axis are clearly labeled to make the relationship between the variables easy to interpret.

**Original dataset:** [Bookings Dataset](https://www.kaggle.com/datasets/hetmengar/ola-and-uber-ride-booking-and-cancellation-data/code)  
**Project instructions:** [Visualizing Datasets Project](https://yourprojectinstructionslink.com)

---

## Plot 2: Student Performance Data (Line Plot)

![Student Performance Line Plot]()<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/ef1ffdf7-4402-4e5c-bac8-1dd4a590fc9d" />


This line plot shows trends in the Student Performance dataset over time or across different categories. Two data sources are plotted together for comparison, allowing us to track differences in performance patterns. The x-axis and y-axis are labeled clearly to ensure readability.

**Original dataset:** [Student Performance Dataset](https://www.kaggle.com/datasets/neurocipher/student-performance)  
**Project instructions:** [Visualizing Datasets Project](https://yourprojectinstructionslink.com)

---

## Files in this Repository

- `visualizingdata.py` — Python script used to generate both plots  
- `Bookings.csv` — Dataset for the scatter plot  
- `StudentPerformance.csv` — Dataset for the line plot  
- `Bookings_plot.png` — Image of the scatter plot  
- `StudentPerformance_plot.png` — Image of the line plot  
- `README.md` — Project description and explanations
- https://github.com/teacher-aj/HeschelCS/tree/main/project_02_visualizing_datasets - Link to project instructions
- Code for the Graphs:
    [Uploading visuaimport pandas as pd
import matplotlib.pyplot as plt

bookings = pd.read_csv("Bookings.csv")
students = pd.read_csv("StudentPerformance.csv")

bookings["Date"] = pd.to_datetime(bookings["Date"])

status_counts = bookings.groupby(["Date", "Booking_Status"]).size().unstack(fill_value=0)

plt.figure()
plt.plot(status_counts.index, status_counts.iloc[:, 0], label=status_counts.columns[0])
plt.plot(status_counts.index, status_counts.iloc[:, 1], label=status_counts.columns[1])
plt.xlabel("Date")
plt.ylabel("Number of Bookings")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bookings_over_time.png")
plt.show()

plt.figure()
plt.scatter(students["Hours Studied"], students["Performance Index"])
plt.xlabel("Hours Studied")
plt.ylabel("Performance Index")
plt.tight_layout()
plt.savefig("study_vs_performance.png")
plt.show()
lizingdata.py…]()


---

This project demonstrates how Python and matplotlib can be used to analyze real-world datasets, providing more advanced insights and visualizations than standard tools like Excel.
