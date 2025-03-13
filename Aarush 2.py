print('Please enter number of days travelled:')
days_travelled = int(input())
full_weeks = days_travelled//7
remaining_days = days_travelled %7
print(days_travelled ,'days are',full_weeks,'weeks and',remaining_days,'days')