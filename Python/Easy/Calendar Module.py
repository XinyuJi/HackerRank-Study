# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    input_date = input()
    input_date = input_date.split()
    weekdays = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
    weekday = calendar.weekday(int(input_date[2]), int(input_date[0]), int(input_date[1]))
    print(weekdays.get(weekday))
