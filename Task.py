"""
Personal Finance Calculator
Day 7 PM Take-Home Assignment
"""

def get_employee_data():
    """
    Collect employee financial details from user input.
    Returns:
        tuple: (name, annual_salary, tax_percent, monthly_rent, savings_percent)
    """
    name = input("Enter employee name: ")

    annual_salary = float(input("Enter annual salary: "))
    tax_percent = float(input("Enter tax bracket percentage: "))
    monthly_rent = float(input("Enter monthly rent: "))
    savings_percent = float(input("Enter savings goal percentage: "))

    return name, annual_salary, tax_percent, monthly_rent, savings_percent
def validate_inputs(annual_salary, tax_percent, monthly_rent, savings_percent):
    """
    Validates financial inputs according to assignment constraints.
    Raises:
        ValueError: If any validation fails.
    """
    if annual_salary <= 0:
        raise ValueError("Annual salary must be greater than 0.")

    if not 0 <= tax_percent <= 50:
        raise ValueError("Tax percentage must be between 0 and 50.")

    if monthly_rent <= 0:
        raise ValueError("Monthly rent must be greater than 0.")

    if not 0 <= savings_percent <= 100:
        raise ValueError("Savings percentage must be between 0 and 100.")

def calculate_finances(annual_salary, tax_percent, monthly_rent, savings_percent):
    """
    Calculates financial breakdown.
    Returns:
        dict: All computed financial metrics.
    """
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax

    savings_amount = net_salary * (savings_percent / 100)
    disposable_income = net_salary - monthly_rent - savings_amount

    rent_ratio = (monthly_rent / net_salary) * 100

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "annual_tax": monthly_tax * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }
def generate_report(name, annual_salary, tax_percent, savings_percent, monthly_rent, finance_data):
    """
    Generates and prints formatted financial summary report.
    """

    print("═" * 44)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("═" * 44)

    print(f"Employee : {name}")
    print(f"Annual Salary : ₹{annual_salary:,.2f}")

    print("─" * 44)
    print("Monthly Breakdown:")

    print(f"Gross Salary : ₹ {finance_data['monthly_salary']:,.2f}")
    print(f"Tax ({tax_percent}%) : ₹ {finance_data['monthly_tax']:,.2f}")
    print(f"Net Salary : ₹ {finance_data['net_salary']:,.2f}")
    print(
        f"Rent : ₹ {monthly_rent:,.2f} "
        f"({finance_data['rent_ratio']:.1f}% of net)"
    )
    print(
        f"Savings ({savings_percent}%) : "
        f"₹ {finance_data['savings_amount']:,.2f}"
    )
    print(f"Disposable : ₹ {finance_data['disposable_income']:,.2f}")

    print("─" * 44)
    print("Annual Projection:")

    print(f"Total Tax : ₹ {finance_data['annual_tax']:,.2f}")
    print(f"Total Savings : ₹ {finance_data['annual_savings']:,.2f}")
    print(f"Total Rent : ₹ {finance_data['annual_rent']:,.2f}")

    print("═" * 44)

def main():
    """
    Main execution function.
    """
    name, annual_salary, tax_percent, monthly_rent, savings_percent = get_employee_data()

    validate_inputs(annual_salary, tax_percent, monthly_rent, savings_percent)

    finance_data = calculate_finances(
        annual_salary,
        tax_percent,
        monthly_rent,
        savings_percent
    )

    generate_report(
        name,
        annual_salary,
        tax_percent,
        savings_percent,
        monthly_rent,
        finance_data
    )


if __name__ == "__main__":
    main()