## Functions for processing and converting grades

def gradeToNumber(grade):
    ## Converts a letter grade to a 4.0 scale value
    grade = grade.upper()
    # Base values
    if grade.startswith('A'): points = 4.0
    elif grade.startswith('B'): points = 3.0
    elif grade.startswith('C'): points = 2.0
    elif grade.startswith('D'): points = 1.0
    else: points = 0.0
    
    # Modifiers
    if '+' in grade and grade != 'A+': points += 0.3
    elif 'A+' in grade: points = 4.0 # Cap at 4.0 or as per your local scale
    elif '-' in grade: points -= 0.3
    
    return round(points, 2)

def numberToGrade(score):
    ## Converts a numeric average back to a letter grade
    if score >= 3.85: return 'A'
    elif score >= 3.5: return 'A-'
    elif score >= 3.15: return 'B+'
    elif score >= 2.85: return 'B'
    elif score >= 2.5: return 'B-'
    elif score >= 2.15: return 'C+'
    elif score >= 1.85: return 'C'
    elif score >= 1.5: return 'C-'
    elif score >= 1.15: return 'D+'
    elif score >= 0.85: return 'D'
    else: return 'F'

def validateGrades(grade_list):
    ## Ensures exactly 4 grades were entered
    return len(grade_list) == 4

def calculateFinalAvg(numbers):
    ## Drops lowest, checks for curve bonus, returns average
    numbers.sort()
    dropped = numbers.pop(0) # Remove lowest
    
    avg = sum(numbers) / len(numbers)
    
    # Weighted Logic: if remaining 3 are B- (2.7) or lower, add 0.25
    if all(n <= 2.7 for n in numbers):
        avg += 0.25
        
    return avg, dropped

def printSummaryBox(original_grades, lowest_num, avg, final_letter):
    print("-" * 40)
    print(f"|{'GRADE REPORT SUMMARY':^38}|")
    print("-" * 40)
    print(f"| Grades Entered: {', '.join(original_grades):<22} |")
    print(f"| Lowest Grade Dropped: {numberToGrade(lowest_num):<15} |")
    print(f"| Calculated Average: {avg:<17.2f} |")
    print(f"| Final Letter Grade: {final_letter:<17} |")
    print("-" * 40)