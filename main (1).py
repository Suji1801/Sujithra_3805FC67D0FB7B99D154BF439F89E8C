def isleapyear(year):
if(year % 4==0 and year %100!=0)or year % 400==0:
retrun true
else:
retrun false

year=2013

if isleapyear(year):
print('{} is a leap year.'.format(year))
else:
print('{} is not a leap year.'.format(year))