print("Automobile Fuel Consumption Cost Calculator")
print("")
print("This program may assist in making a great decision about your new vehicle")
print("based on your monthly expenses. You will be required to enter the MPG for the vechicle")
print("you intrested in, the average number of miles expected to be driven each month")
print("and the cost per gallon for fuel")
print("")
print("The program will calculate the monthly fuel consumption cost")
print("")
veh_mpg = float(input("Please provide the vehcile's MPG: "))
print("")
miles_monthly = int(input("Please provide the average miles driven monthly: "))
print("")
fuel_cost = float(input("Please provide the cost of fuel per gallon: $"))



gallon_used_monthly = float(miles_monthly / veh_mpg)
gallon_cost_monthly = gallon_used_monthly * fuel_cost

print("")



print("Given price of fuel as ${}per gallon {} miles used monthly: ".format(fuel_cost,miles_monthly))
print("")
print("Gallons used each month: {:.1f} gallons".format(gallon_used_monthly))
print("")
print("Monthly cost of fuel: ${:.2f}".format(gallon_cost_monthly))
