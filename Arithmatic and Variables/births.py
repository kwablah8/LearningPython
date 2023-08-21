# Program to calculate number of births in a day

# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * \
    hours_per_day * days_per_year * num_years
print(total_secs)


# Create and set value of births_per_min variable
births_per_min = 250

# calc the value of births per day
births_per_day = births_per_min * (mins_per_hour * hours_per_day)
