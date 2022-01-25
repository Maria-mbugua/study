#1000 kes invest with 10% return each
#one year = 1000x1.1 
# two years = 1000x 1.1 x 1.1
#7 years ?
#15years ?

savings=1000
var_growth_multiplier=1.1
var_seven_years=7
var_fifteen_years=15


#calculate total for 7years
var_total_seven_year_return= savings*pow(var_growth_multiplier,var_seven_years)
print("total after seven years is : "+ str(var_total_seven_year_return))



#calculate total for 15 years
var_total_fifteen_year_return=savings*pow(var_growth_multiplier,var_fifteen_years)
print("total after fifteen years is : "+ str(var_total_fifteen_year_return)) 