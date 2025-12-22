import pandas as pd
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
