grades = [95, 88, 85, 75]
letter_grade = ['A', 'B+', 'B', 'C']
print('The original list ', letter_grade)
print('The zipped tuples ', list(zip(letter_grade, grades)))
print('Next is a map-lambda version')
result = list(map(lambda *a: a, letter_grade, grades))
print(result)