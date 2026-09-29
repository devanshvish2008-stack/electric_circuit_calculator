
### `statement.md`

```markdown
# Project Statement

## 1. Problem Statement

Students and beginners often need to perform basic electrical calculations while studying electrical and electronic concepts. Calculating voltage, current, resistance, power, and equivalent resistance manually can take time and may result in calculation errors.

The Electric Circuit Calculator is developed to provide a simple and user-friendly solution for performing these common electrical calculations.

The project uses standard electrical formulas and allows users to enter the required values through a menu-driven Python program.

---

## 2. Scope of the Project

The scope of the Electric Circuit Calculator is to provide basic electrical calculations using Python.

The project currently covers:

- Voltage calculation
- Current calculation
- Resistance calculation
- Power calculation
- Series resistance calculation
- Parallel resistance calculation
- Basic error handling
- Repeated calculations through a menu system

The project is mainly focused on basic DC electrical calculations.
## 3. Target Users

The project is intended for:

- School students
- College students
- Beginners learning electrical concepts
- Beginners learning Python programming
- Students studying basic electrical engineering
- Users who need quick basic circuit calculations

---

## 4. High-Level Features

## 4.1 Voltage Calculation

The system calculates voltage using:

V = I × R

where:

- V = Voltage
- I = Current
- R = Resistance

---

## 4.2 Current Calculation

The system calculates current using:

I = V / R

where:

- I = Current
- V = Voltage
- R = Resistance

---

### 4.3 Resistance Calculation

The system calculates resistance using:

R = V / I

where:

- R = Resistance
- V = Voltage
- I = Current

---

### 4.4 Power Calculation

The system calculates electrical power using:

P = V × I

where:

- P = Power
- V = Voltage
- I = Current

---

### 4.5 Series Resistance

The system calculates the total resistance of resistors connected in series using:

Rtotal = R1 + R2 + R3 + ...

---

### 4.6 Parallel Resistance

The system calculates the equivalent resistance of resistors connected in parallel using:

1/Rtotal = 1/R1 + 1/R2 + 1/R3 + ...

---

### 4.7 Input Validation

The program checks for invalid values such as zero resistance when calculating current and zero current when calculating resistance.

---

### 4.8 Menu-Driven Interface

The program provides a simple menu that allows users to select the required calculation.

---

### 4.9 Multiple Calculations

Users can perform multiple calculations without restarting the program.

---

### 4.10 Exit Option

The program provides an exit option that allows users to safely close the calculator.