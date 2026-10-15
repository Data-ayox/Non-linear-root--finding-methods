## Comparison of Nonlinear Root-Finding Methods

## Overview
This project implements and compares two numerical methods for solving nonlinear equations: the Bisection Method and Newton's Method.

The comparison focuses on root estimates, convergence behaviour, iteration counts, and the effect of different initial guesses.

## Methods Used
- **Bisection Method:** Finds a root by repeatedly narrowing an interval that brackets the root.
- **Newton's Method:** Uses the function derivative and an initial guess to calculate successive root estimates.

## Equations Tested
1. \(f(x) = x^3 - x - 2\)
2. \(f(x) = x^2 - 2\)
3. \(f(x) = \cos(x) - x\)

## Tools and Libraries
- Python
- Matplotlib
- CSV
- Math
- OS

## Project Structure
```text
nonlinear-root-finding-methods/
├── root_finding.py
├── README.md
└── results/
    ├── method_comparison.csv
    ├── newton_initial_guesses.csv
    ├── screening_report.txt
    ├── equation_1_convergence.png
    ├── equation_2_convergence.png
    └── equation_3_convergence.png
```

## How to Run
1. Install Python.
2. Install Matplotlib:
   ```bash
   pip install matplotlib
   ```
3. Run the script:
   ```bash
   python root_finding.py
   ```

The program generates comparison results, a screening report, and convergence graphs in the `results` folder.

## Configuration
- Tolerance: `1e-8`
- Maximum iterations: `100`

## Key Learning Outcomes
- Implementing numerical root-finding methods in Python.
- Comparing convergence behaviour using residual plots.
- Understanding the importance of initial guesses in Newton's Method.
- Saving numerical results in CSV format.

## Conclusion
The project demonstrates two approaches to solving nonlinear equations. The Bisection Method provides a systematic approach when a valid bracketing interval is available, while Newton's Method can converge quickly with a suitable initial guess.
