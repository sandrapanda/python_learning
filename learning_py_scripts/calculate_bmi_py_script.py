LEARNING PYTHON 2017	
Script:
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]		## declare the dataset and its data

def bmi_calculation(weight, height):			## define function and its input variables
	return (weight / (height ** 2))			## declare what function does, calculates

for values in patients:					## define loop, its dataset and input variable(s)
	(weight, height) = values				## define what input variables represent
	bmi = bmi_calculation(weight, height)		## define its output variable and how it is calculated
	print(bmi)						## display output variable results


========================
Result:
21.60493….
22.16066….
51.90311….
