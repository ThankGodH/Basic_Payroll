# Basic_Payroll and Tax Calculator

Sample Input/Output Case 1:
---------------------------
Input:
Enter employee name: Alice
Enter hours worked: 45
Enter hourly rate: 20
Does the employee own property? (Yes/No): Yes

Output:
Employee Name: Alice
Gross Pay: $950.00
HST Deducted (13%): $123.50
Property Tax Deducted (1.2% on $300,000): $3600.00
Net Pay: $-2773.50

Sample Input/Output Case 2:
---------------------------
Input:
Enter employee name: Bob
Enter hours worked: 38
Enter hourly rate: 25
Does the employee own property? (Yes/No): No

Output:
Employee Name: Bob
Gross Pay: $950.00
HST Deducted (13%): $123.50
Net Pay: $826.50

Challenge & Reflection:
-----------------------
One challenge I faced was handling the overtime logic, particularly making sure that overtime only applied beyond 40 hours and was calculated correctly at 1.5x the hourly rate. I solved this by using `min()` and `max()` functions to cleanly separate regular and overtime hours.

This assignment helped me understand how real-world financial calculations involve conditionals, accurate arithmetic, and clear formatting. Writing this program improved my confidence with Python's input/output functions, rounding techniques, and conditional logic. I also appreciated the importance of user experience when displaying results clearly and understandably.
