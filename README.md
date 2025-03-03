# 90-Minute Probability & Statistics Class Guide

**Target Audience:** Students learning basic probability and statistics.

**Materials:**

* Balls (e.g., tennis balls, soft balls)
* Targets (e.g., buckets, marked areas on a wall)
* Paper and pens for recording results
* Computers with Python and Pandas installed (or access to online Python environments like Google Colab)

**Class Structure:**

## 1. Introduction (10 minutes)

* **Welcome and Introduction:** Briefly introduce the topic of probability and statistics.
* **Activity Overview:** Explain the activity: each student will throw a ball 10 times, recording their success rate. Groups will then analyze the data using Python.
* **Learning Objectives:**
    * Understand the concept of probability.
    * Calculate mean and standard deviation.
    * Use Python (Pandas) for data analysis.
    * Learn to record data.

## 2. Individual Throws (20 minutes)

* **Demonstration:** Demonstrate the throwing technique and target.
* **Student Practice:** Students practice a few throws to get a feel for the activity.
* **Data Collection:** Students perform 10 throws each, recording whether each throw was a success (hit the target) or a failure (missed the target).
* **Individual Percentage Calculation:** Students calculate their individual success percentage (number of successes / 10).

## 3. Group Formation and Data Sharing (10 minutes)

* **Group Formation:** Divide the class into groups of 3 or 4 students.
* **Data Sharing:** Students share their individual success percentages within their groups.
* **Data recording:** Each group will record each member's individual results.

## 4. Python Data Analysis Setup (15 minutes)

* **Introduction to Pandas:** Briefly introduce the Pandas library in Python, explaining its use for data manipulation and analysis.
* **Code Template:** Provide the following Python code template (or display it on a screen):

```python
import pandas as pd
import numpy as np

# Create an empty DataFrame
data = {'Student': [], 'Success_Percentage': []}
df = pd.DataFrame(data)

# Example: Adding data (students will fill this in)
# Example data for group of 3
# df = pd.DataFrame({'Student': ['Student1', 'Student2', 'Student3'],
#                   'Success_Percentage': [0.7, 0.5, 0.8]})
# Students will fill in the dataframe above with their data.
print("Enter the student names and their success percentages.")

while True:
    student_name = input("Enter student name (or type 'done'): ")
    if student_name.lower() == 'done':
        break
    try:
        success_percentage = float(input(f"Enter {student_name}'s success percentage (0-1): "))
        df = pd.concat([df, pd.DataFrame({'Student': [student_name], 'Success_Percentage': [success_percentage]})], ignore_index=True)
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\nDataframe:")
print(df)

# Calculate the mean and standard deviation
mean_percentage = df['Success_Percentage'].mean()
std_percentage = df['Success_Percentage'].std()

print(f"\nMean Success Percentage: {mean_percentage:.2f}")
print(f"Standard Deviation: {std_percentage:.2f}")


 * Explanation: Explain the code:
   * Importing Pandas and NumPy.
   * Creating an empty DataFrame.
   * How to input data.
   * Calculating the mean and standard deviation using Pandas.
   * How to print the resulting dataframe and calculations.
 * Access to Python: Ensure students have access to Python (either installed on their computers or through an online environment like Google Colab).
5. Data Input and Analysis (25 minutes)
 * Data Input: Students input their group's data into the Python code.
 * Running the Code: Students run the code to calculate the mean and standard deviation for their group's success percentages.
 * Discussion: Groups discuss their results:
   * What does the mean represent?
   * What does the standard deviation represent?
   * How does the standard deviation relate to the variability of their group's performance?
 * Observation: Instructor goes around the room, helping with code issues, and answering questions.
6. Wrap-up and Discussion (10 minutes)
 * Class Discussion: Discuss the overall findings of the class.
   * How did the individual success percentages vary?
   * How did the group means and standard deviations vary?
   * What factors might influence a person's success rate?
 * Real-World Applications: Discuss real-world applications of probability and statistics (e.g., sports, weather forecasting, data analysis).
 * Q&A: Answer any remaining student questions.
 * Summary: Briefly recap the key concepts learned.

