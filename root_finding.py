import math
import csv
import os
import matplotlib.pyplot as plt


# Create a folder to save our results
os.makedirs("results", exist_ok=True)

# Set the accuracy and maximum number of iterations
TOLERANCE = 1e-8
MAX_ITERATIONS = 100

# Step 2: Bisection Method

def bisection(f, a, b, tol=TOLERANCE,
              max_iter=MAX_ITERATIONS):

    if f(a) * f(b) >= 0:
        raise ValueError(
            "The function must have opposite signs at a and b."
        )

    history = []

    for iteration in range(1, max_iter + 1):
        midpoint = (a + b) / 2
        residual = abs(f(midpoint))

        history.append(
            (iteration, midpoint, residual)
        )

        if residual < tol or abs(b - a) / 2 < tol:
            return midpoint, history, "Converged"

        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return midpoint, history, "Maximum iterations reached"


# Step 3: Newton's Method

def newton(f, df, x0, tol=TOLERANCE,
           max_iter=MAX_ITERATIONS):

    x = x0
    history = []

    for iteration in range(1, max_iter + 1):
        fx = f(x)
        residual = abs(fx)

        history.append((iteration, x, residual))

        if residual < tol:
            return x, history, "Converged"

        derivative = df(x)

        if abs(derivative) < 1e-12:
            return x, history, "Derivative too close to zero"

        x = x - fx / derivative

        if not math.isfinite(x):
            return x, history, "Numerical failure"

    return x, history, "Maximum iterations reached"


# Step 4: Define the nonlinear equations

equations = [
    {
        "name": "Equation 1",
        "f": lambda x: x**3 - x - 2,
        "df": lambda x: 3*x**2 - 1,
        "a": 1,
        "b": 2,
        "guesses": [0.5, 1.5, 2.5],
    },
    {
        "name": "Equation 2",
        "f": lambda x: x**2 - 2,
        "df": lambda x: 2*x,
        "a": 1,
        "b": 2,
        "guesses": [0.5, 1.0, 2.0],
    },
    {
        "name": "Equation 3",
        "f": lambda x: math.cos(x) - x,
        "df": lambda x: -math.sin(x) - 1,
        "a": 0,
        "b": 1,
        "guesses": [0.0, 0.5, 1.0],
    },
]


# Step 5: Run and compare both methods

comparison_rows = []
guess_rows = []

for eq in equations:
    name = eq["name"]
    f = eq["f"]
    df = eq["df"]

    print("\n" + "=" * 45)
    print(name)

    # Run the Bisection Method
    bis_root, bis_history, bis_status = bisection(
        f, eq["a"], eq["b"]
    )

    print(
        f"Bisection root: {bis_root:.8f}, "
        f"iterations: {len(bis_history)}, "
        f"status: {bis_status}"
    )

    comparison_rows.append([
        name, "Bisection", "-", bis_root,
        len(bis_history), abs(f(bis_root)), bis_status
    ])

    # Run Newton's Method using the middle initial guess
    guess = eq["guesses"][1]

    new_root, new_history, new_status = newton(
        f, df, guess
    )

    print(
        f"Newton root: {new_root:.8f}, "
        f"iterations: {len(new_history)}, "
        f"status: {new_status}"
    )

    comparison_rows.append([
        name, "Newton", guess, new_root,
        len(new_history), abs(f(new_root)), new_status
    ])

    # Test different initial guesses for Newton's Method
    print("Newton initial guesses:")

    for guess in eq["guesses"]:
        root, history, status = newton(f, df, guess)

        print(
            f"  Start={guess}, root={root:.8f}, "
            f"iterations={len(history)}, status={status}"
        )

        guess_rows.append([
            name, guess, root, len(history),
            abs(f(root)), status
        ])


# Step 6: Create convergence graphs

    plt.figure(figsize=(8, 5))

    plt.semilogy(
        [item[0] for item in bis_history],
        [max(item[2], 1e-16) for item in bis_history],
        marker="o",
        label="Bisection"
    )

    plt.semilogy(
        [item[0] for item in new_history],
        [max(item[2], 1e-16) for item in new_history],
        marker="s",
        label="Newton's Method"
    )

    plt.xlabel("Iteration")
    plt.ylabel("Absolute residual |f(x)|")
    plt.title(f"Convergence Comparison: {name}")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        f"results/{name.lower().replace(' ', '_')}_convergence.png"
    )
    plt.close()


# Step 7: Save comparison results to CSV files

with open(
    "results/method_comparison.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)

    writer.writerow([
        "Equation",
        "Method",
        "Initial Guess",
        "Root",
        "Iterations",
        "Final Residual",
        "Status"
    ])

    writer.writerows(comparison_rows)


with open(
    "results/newton_initial_guesses.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)

    writer.writerow([
        "Equation",
        "Initial Guess",
        "Root",
        "Iterations",
        "Final Residual",
        "Status"
    ])

    writer.writerows(guess_rows)


print("\nComparison tables saved successfully!")


# Step 8: Save the screening report

report = """
SCREENING REPORT: NONLINEAR ROOT-FINDING METHODS

Objective:
This experiment compares the Bisection Method and Newton's
Method for solving three nonlinear equations.

Methodology:
Both methods use a tolerance of 1e-8 and a maximum of
100 iterations. Bisection uses an interval that brackets
a root, while Newton's Method uses initial guesses
and derivatives.

Results and Graph Interpretation:

Equation 1: f(x) = x^3 - x - 2
The graph compares the residual reduction of both methods.
Bisection progressively narrows the interval, while
Newton's Method updates the root estimate using the
derivative.

Equation 2: f(x) = x^2 - 2
The graph shows how the residual changes during iterations.
Bisection reduces the interval systematically, while
Newton's Method uses the derivative to improve its estimate.

Equation 3: f(x) = cos(x) - x
The graph compares the convergence behaviour of both methods.
Bisection narrows the interval containing the root, while
Newton's Method calculates successive estimates using
the derivative.

Effect of Initial Guesses:
Different initial guesses were tested for Newton's Method.
Its convergence depends on the starting value and the
derivative. The results are recorded in the CSV file.

Conclusion:
Both methods provide approaches to solving nonlinear
equations. Bisection is systematic when a valid interval
is available, while Newton's Method can converge faster
with a suitable initial guess. The graphs and CSV files
support the comparison.

"""

with open(
    "results/screening_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report.strip())

print("Screening report saved successfully!")
print("Check the results folder.")