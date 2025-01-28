import matplotlib.pyplot as plt


def calculate_net_salary(gross_salary, num_children):
    # Determine base tax rate
    if gross_salary < 1000:
        tax_rate = 0.10
    elif gross_salary < 2000:
        tax_rate = 0.12
    elif gross_salary < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # Determine child-based tax reduction
    if gross_salary < 2000:
        tax_reduction = 0.01 * num_children
    else:
        tax_reduction = 0.005 * num_children

    # Apply tax reduction but ensure it doesn't go below 0
    final_tax_rate = max(0, tax_rate - tax_reduction)

    # Calculate net salary
    net_salary = gross_salary * (1 - final_tax_rate)

    return net_salary


try:
    gross_income = float(input("Enter gross salary: "))
    num_kids = int(input("Enter number of children: "))

    if gross_income < 0 or num_kids < 0:
        print("Error: Salary and number of children cannot be negative.")
    else:
        net_income = calculate_net_salary(gross_income, num_kids)
        print(f"Net salary: {net_income:.2f}")

        # Plot the data
        plt.bar(["Gross Salary", "Net Salary"], [gross_income, net_income], color=['blue', 'green'])
        plt.ylabel("Amount in $")
        plt.title("Gross vs Net Salary")
        plt.show()

except ValueError:
    print("Invalid input! Please enter valid numbers.")
