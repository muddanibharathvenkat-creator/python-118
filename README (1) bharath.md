# Python Programming -- 10 Real-World Cases

## Student Details

  Field                 Details
  --------------------- --------------------------------------------------------------
  Student Name          Muddani Bharath Venkat
  Roll Number          26001324
  Registration Number   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Branch / Department   CSE AI ML
  Year / Semester       1/1
  College Name          \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Subject / Course      \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Faculty Name          \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Academic Year         \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Submission Date       \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------

## Introduction

This assignment contains 10 Python programs based on simple real-world
situations. The programs use variables, user input, arithmetic
operations, and conditional statements such as `if`, `elif`, and `else`.

## Case 1: Scholarship Eligibility

**File:** `task1.py`

**Objective:** Check whether a student is eligible for a scholarship
based on marks, attendance, and family income.

**Inputs:** - Marks percentage - Attendance percentage - Family income

**Conditions:** - Marks must be at least 80%. - Attendance must be at
least 75%. - Family income must be ₹2,00,000 or less.

**Result:** Displays `Eligible for Scholarship` when all three
conditions are satisfied; otherwise, displays
`Not Eligible for Scholarship`.

## Case 2: Electricity Bill Calculation

**File:** `task2.py`

**Objective:** Calculate an electricity bill based on the number of
units consumed.

**Input:** Electricity units.

**Calculation:** - Up to 100 units: ₹2 per unit. - 101--200 units: ₹2
per unit for the first 100 units and ₹3 for each additional unit. -
Above 200 units: ₹2 per unit for the first 100 units, ₹3 for the next
100 units, and ₹5 for each unit above 200. - Add a fixed charge of ₹50.

**Result:** Displays the total electricity bill.

## Case 3: Hospital Bill with Discount

**File:** `task3.py`

**Objective:** Calculate a hospital bill and apply a discount when the
total charges reach the specified amount.

**Inputs:** - Consultation charge - Diagnostic charges - Treatment
charges

**Calculation:** 1. Add the three charges to get the total bill. 2. If
the total is ₹5,000 or more, calculate a 10% discount. 3. Otherwise, the
discount is zero. 4. Subtract the discount from the total to get the
final bill.

**Result:** Displays the total bill, discount, and final bill.

## Case 4: Employee Salary Calculation

**File:** `task4.py`

**Objective:** Calculate an employee's gross salary, deduction, and net
salary.

**Inputs:** - Basic salary - Allowances - Overtime pay - Incentive

**Calculation:** 1. Gross salary = Basic salary + Allowances + Overtime
pay + Incentive. 2. Deduction = 10% of gross salary. 3. Net salary =
Gross salary − Deduction.

**Result:** Displays the gross salary, deduction, and net salary.

## Case 5: Mobile Data Plan Comparison

**File:** `task5.py`

**Objective:** Calculate and compare the costs of two mobile data plans
based on data usage.

**Input:** Data usage in GB.

**Plan calculations:** - **Plan A:** ₹199 for up to 10 GB; after 10 GB,
add ₹20 for each additional GB. - **Plan B:** ₹299 for up to 20 GB;
after 20 GB, add ₹15 for each additional GB.

**Result:** Displays both plan costs and identifies the cheaper plan. If
the costs are equal, it displays `Both plans cost the same`.

## Case 6: Railway Fare Calculation

**File:** `task6.py`

**Objective:** Calculate railway fare based on travel distance and
passenger age.

**Inputs:** - Distance in kilometres - Passenger age

**Calculation:** 1. Base fare = Distance × ₹2. 2. Passengers below 12
years receive a 50% fare reduction. 3. Passengers aged 60 years or above
receive a 30% fare reduction. 4. Add ₹30 to the fare.

**Result:** Displays the total railway fare.

## Case 7: Shopping Bill Calculation

**File:** `task7.py`

**Objective:** Calculate a shopping bill with a discount and tax.

**Inputs:** - Product price - Quantity

**Calculation:** 1. Total = Product price × Quantity. 2. If the total is
₹2,000 or more, apply a 10% discount; otherwise, the discount is zero.
3. Tax = 5% of the amount after discount. 4. Final amount = Total −
Discount + Tax.

**Result:** Displays the total, discount, tax, and final amount.

## Case 8: Business Profit or Loss

**File:** `task8.py`

**Objective:** Determine whether a business has made a profit, a loss,
or neither.

**Inputs:** - Material cost - Labour cost - Machine cost - Selling price

**Calculation:** 1. Total cost = Material cost + Labour cost + Machine
cost. 2. Profit = Selling price − Total cost.

**Result:** - If profit is greater than zero, displays the profit. - If
profit is less than zero, displays the loss as a positive amount. - If
profit is zero, displays `No Profit No Loss`.

## Case 9: Travel Budget Management

**File:** `task9.py`

**Objective:** Check whether travel expenses are within the planned
budget.

**Inputs:** - Food expenses - Travel expenses - Hotel expenses - Total
budget

**Calculation:** 1. Total expenses = Food + Travel + Hotel. 2. Compare
total expenses with the budget.

**Result:** - If total expenses are less than or equal to the budget,
displays `Within Budget`. - Otherwise, displays the amount by which the
budget is exceeded.

## Case 10: College Event Fund Calculation

**File:** `task10.py`

**Objective:** Find the minimum number of students required to cover the
remaining college event cost after sponsorship.

**Inputs:** - Venue cost - Food cost - Transport cost - Sponsorship
amount - Registration fee per student

**Calculation:** 1. Total event cost = Venue + Food + Transport. 2.
Remaining amount = Total event cost − Sponsorship. 3. If the remaining
amount is zero or less, the number of students required is zero. 4.
Otherwise, divide the remaining amount by the registration fee and round
up to the next whole student when needed.

**Result:** Displays the total event cost, sponsorship, and minimum
number of students required.

------------------------------------------------------------------------

## Python Concepts Used

-   Variables and data types (`int`, `float`)
-   Taking input using `input()`
-   Displaying output using `print()`
-   Arithmetic operators (`+`, `-`, `*`, `/`)
-   Comparison operators (`>=`, `<=`, `>`, `<`)
-   Conditional statements (`if`, `elif`, `else`)
-   Compound conditions using `and`
-   Updating a variable using operators such as `+=` and `*=`

## How to Run the Programs

1.  Make sure Python is installed on your computer.
2.  Download or clone the project folder.
3.  Open the folder in a code editor or terminal.
4.  Run any program using:

``` bash
python task1.py
```

5.  Replace `task1.py` with `task2.py`, `task3.py`, and so on, to run
    the other cases.
6.  Enter the requested values when prompted.

## Files Included

  File Name     Case
  ------------- --------------------------------
  `task1.py`    Scholarship Eligibility
  `task2.py`    Electricity Bill Calculation
  `task3.py`    Hospital Bill with Discount
  `task4.py`    Employee Salary Calculation
  `task5.py`    Mobile Data Plan Comparison
  `task6.py`    Railway Fare Calculation
  `task7.py`    Shopping Bill Calculation
  `task8.py`    Business Profit or Loss
  `task9.py`    Travel Budget Management
  `task10.py`   College Event Fund Calculation

## Conclusion

These 10 programs demonstrate how Python can be used to solve basic
real-world calculation and decision-making problems using input,
arithmetic operations, and conditional statements.
