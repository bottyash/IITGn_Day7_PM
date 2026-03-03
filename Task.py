"""
Day 7 – Personal Finance Calculator
Covers:
- Input validation
- Financial calculations
- Indian number formatting
- Comparison of two employees
- Financial health scoring
"""

import math


def format_indian_currency(amount):
    """
    Format number using Indian numbering system (lakhs/crores).
    Example: 1200000 -> 12,00,000.00
    """
    amount_str = f"{amount:.2f}"
    integer, decimal = amount_str.split(".")

    if len(integer) <= 3:
        return f"{integer}.{decimal}"

    last_three = integer[-3:]
    remaining = integer[:-3]

    pairs = []
    while len(remaining) > 2:
        pairs.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    if remaining:
        pairs.insert(0, remaining)

    formatted_integer = ",".join(pairs) + "," + last_three
    return f"{formatted_integer}.{decimal}"


def get_employee_data(employee_number):
    """
    Collect employee financial inputs.
    """
    print(f"\nEnter details for Employee {employee_number}")
    name = input("Name: ")
    annual_salary = float(input("Annual Salary: "))
    tax_percent = float(input("Tax Percentage (0-50): "))
    monthly_rent = float(input("Monthly Rent: "))
    savings_percent = float(input("Savings Percentage (0-100): "))

    return name, annual_salary, tax_percent, monthly_rent, savings_percent


def validate_inputs(annual_salary, tax_percent, monthly_rent, savings_percent):
    """
    Validate financial inputs.
    """
    if annual_salary <= 0:
        raise ValueError("Salary must be > 0.")

    if not 0 <= tax_percent <= 50:
        raise ValueError("Tax must be between 0-50%.")

    if monthly_rent <= 0:
        raise ValueError("Rent must be > 0.")

    if not 0 <= savings_percent <= 100:
        raise ValueError("Savings must be between 0-100%.")


def calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent):
    """
    Compute monthly & annual financial metrics.
    """
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount
    rent_ratio = (monthly_rent / net_salary) * 100
    disposable_ratio = (disposable_income / net_salary) * 100

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "disposable_ratio": disposable_ratio,
        "annual_tax": monthly_tax * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }


def financial_health_score(rent_ratio, savings_percent, disposable_ratio):
    """
    Custom scoring formula (0-100 scale).

    - Rent ratio ideal < 30%
    - Savings higher is better
    - Disposable ratio higher is better
    """

    rent_score = max(0, 30 - rent_ratio) * 2
    savings_score = savings_percent * 0.5
    disposable_score = disposable_ratio * 0.5

    total_score = rent_score + savings_score + disposable_score
    return min(100, round(total_score, 2))


def generate_report(name, annual_salary, tax_percent, savings_percent,
                    monthly_rent, finance_data):
    """
    Print formatted employee financial report.
    """

    print("═" * 50)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("═" * 50)

    print(f"Employee : {name}")
    print(f"Annual Salary : ₹{format_indian_currency(annual_salary)}")

    print("─" * 50)
    print("Monthly Breakdown:")

    print(f"Gross Salary : ₹ {format_indian_currency(finance_data['monthly_salary'])}")
    print(f"Tax ({tax_percent}%) : ₹ {format_indian_currency(finance_data['monthly_tax'])}")
    print(f"Net Salary : ₹ {format_indian_currency(finance_data['net_salary'])}")
    print(
        f"Rent : ₹ {format_indian_currency(monthly_rent)} "
        f"({finance_data['rent_ratio']:.1f}% of net)"
    )
    print(
        f"Savings ({savings_percent}%) : "
        f"₹ {format_indian_currency(finance_data['savings_amount'])}"
    )
    print(f"Disposable : ₹ {format_indian_currency(finance_data['disposable_income'])}")

    print("─" * 50)
    print("Annual Projection:")

    print(f"Total Tax : ₹ {format_indian_currency(finance_data['annual_tax'])}")
    print(f"Total Savings : ₹ {format_indian_currency(finance_data['annual_savings'])}")
    print(f"Total Rent : ₹ {format_indian_currency(finance_data['annual_rent'])}")

    score = financial_health_score(
        finance_data["rent_ratio"],
        savings_percent,
        finance_data["disposable_ratio"],
    )

    print("─" * 50)
    print(f"Financial Health Score: {score}/100")
    print("═" * 50)


def compare_employees(emp1, emp2):
    """
    Side-by-side comparison table.
    """
    print("\n" + "=" * 70)
    print("EMPLOYEE COMPARISON")
    print("=" * 70)

    print(f"{'Metric':<20}{emp1['name']:<20}{emp2['name']:<20}")
    print("-" * 70)

    print(
        f"{'Net Salary':<20}"
        f"{format_indian_currency(emp1['finance']['net_salary']):<20}"
        f"{format_indian_currency(emp2['finance']['net_salary']):<20}"
    )

    print(
        f"{'Savings':<20}"
        f"{format_indian_currency(emp1['finance']['savings_amount']):<20}"
        f"{format_indian_currency(emp2['finance']['savings_amount']):<20}"
    )

    print(
        f"{'Disposable':<20}"
        f"{format_indian_currency(emp1['finance']['disposable_income']):<20}"
        f"{format_indian_currency(emp2['finance']['disposable_income']):<20}"
    )

    print("=" * 70)


def main():
    """
    Main execution flow.
    """
    employees = []

    for i in range(1, 3):
        name, annual_salary, tax_percent, monthly_rent, savings_percent = (
            get_employee_data(i)
        )

        validate_inputs(annual_salary, tax_percent,
                        monthly_rent, savings_percent)

        finance_data = calculate_finances(
            annual_salary,
            tax_percent,
            monthly_rent,
            savings_percent,
        )

        generate_report(name, annual_salary, tax_percent,
                        savings_percent, monthly_rent, finance_data)

        employees.append({
            "name": name,
            "finance": finance_data
        })

    compare_employees(employees[0], employees[1])


if __name__ == "__main__":
    main()