principle_amount_in_rupees = float(input("enter principle amount in rupees: "))
rate_of_interest_in_percentage = float(input("enter rate of interest in percentage: "))
time_in_years = float(input("enter time in years: "))
compound_interest = principle_amount_in_rupees * (pow((1+rate_of_interest_in_percentage/100), time_in_years)) -principle_amount_in_rupees
print("compound interest is; ", compound_interest)