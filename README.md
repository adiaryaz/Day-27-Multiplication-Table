# Day-27-Multiplication-Table
Day 27/100 - Python Program to Print Table of a Given Number

# Print Multiplication Table of a Given Number
A program to generate and display the multiplication table for any user-inputted integer using a standard iteration loop.

## 📝 Description

This program takes a number inputted by the user and dynamically generates its mathematical multiplication table. It utilizes a `for` loop combined with Python's built-in `range()` function to iterate from 1 up to a specified limit.

By default, the function is designed to multiply the number from 1 to 10, utilizing default parameters in the function definition (`limit=10`). It formats the output neatly on a line-by-line basis using f-strings, clearly showing the multiplicand, the multiplier, and the resulting product.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer value representing the base number for the table.

### Output:

* A prefix header stating: "Multiplication table of [number]:"
* Followed by 10 lines of formatted equations in the structure: `[number] x [iterator] = [result]`

### Rules:

1. The program must accept an integer input from the user.
2. The program must use a function (e.g., `table`) to process and display the output.
3. The function should use a `for` loop to iterate from 1 up to 10 (inclusive).
4. The calculation must multiply the user's input number by the current loop iterator (`i`).
5. Each resulting mathematical sentence must be printed on a new line.

---

## 💡 Examples

### Example 1 (Positive Integer)

**Input:**

```
5


```

**Output:**

```
Multiplication table of 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50


```

**Explanation:** The loop runs 10 times, multiplying the base number (5) sequentially by 1 through 10 and printing each equation.

### Example 2 (Negative Integer)

**Input:**

```
-3


```

**Output:**

```
Multiplication table of -3:
-3 x 1 = -3
-3 x 2 = -6
-3 x 3 = -9
-3 x 4 = -12
-3 x 5 = -15
-3 x 6 = -18
-3 x 7 = -21
-3 x 8 = -24
-3 x 9 = -27
-3 x 10 = -30


```

**Explanation:** The multiplication logic handles negative numbers perfectly, preserving standard mathematical rules (negative x positive = negative).

### Example 3 (Zero)

**Input:**

```
0


```

**Output:**

```
Multiplication table of 0:
0 x 1 = 0
0 x 2 = 0
0 x 3 = 0
0 x 4 = 0
0 x 5 = 0
0 x 6 = 0
0 x 7 = 0
0 x 8 = 0
0 x 9 = 0
0 x 10 = 0


```

**Explanation:** Anything multiplied by 0 results in 0. The format remains structurally correct while displaying the zero-property of multiplication.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-27-Multiplication-Table.git
cd multiplication-table


```

2. **Run the program**:

```bash
python main.py


```

Enter an integer when prompted to see its full 1-to-10 multiplication table printed to the console.
