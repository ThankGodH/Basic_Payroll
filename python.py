# payroll_calculator.py

def main():
    print("=== Payroll and Tax Calculator ===")
    
    # Collect input
    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    owns_property = input("Does the employee own property? (Yes/No): ").strip().lower()

    # Calculate regular and overtime pay
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(0, hours_worked - 40)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    # Tax deductions
    hst = gross_pay * 0.13
    property_tax = 0
    if owns_property == "yes":
        property_tax = 300000 * 0.012

    total_deductions = hst + property_tax
    net_pay = gross_pay - total_deductions

    # Output summary
    print("\n=== Pay Summary ===")
    print(f"Employee Name: {name}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"HST Deducted (13%): ${hst:.2f}")
    if property_tax > 0:
        print(f"Property Tax Deducted (1.2% on $300,000): ${property_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

if __name__ == "__main__":
    main()
