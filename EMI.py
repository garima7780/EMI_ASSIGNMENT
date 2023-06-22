def calculate_emi(principal, tenure, interest_rate):
    # Convert interest rate from percentage to decimal
    interest_rate = interest_rate / 100

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate number of months
    months = tenure * 12

    # Calculate EMI
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)

    return emi


# Get user inputs
principal_amount = float(input("Enter the principal amount: "))
tenure_years = float(input("Enter the tenure in years: "))
interest_rate = float(input("Enter the interest rate: "))

# Calculate EMI
emi_amount = calculate_emi(principal_amount, tenure_years, interest_rate)

# Print the result
print(f"EMI amount: {emi_amount:.2f}")