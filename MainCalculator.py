import CalculatorFunctions as calc

# Asking for the function to the user
function = str(input("Digite aqui sua função: "))
print (f"\nFUNCTION\n{function}\n")

# Define the search break vales to look for roots
start, end, increase, counter = calc.fixed_break()

# Finding "y" values" in function of "x" values between start/end
x_values,y_values = calc.find_values(counter, start, increase, function)
print (f"X VALUES\n{x_values}\n\nY VALUES\n{y_values}\n\n")

# Identify breaks where signal chances (when the graph line pass throught x axis)
change_breaks = calc.identifier(x_values,y_values)
print (f"CHANGE BREAKS\n{change_breaks}\n")

# Refine the breaks till answer the criterion established to find roots
roots= calc.refiner(change_breaks, function)
print (f"ROOTS\n{roots}\n")