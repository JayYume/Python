from grade_compute import *

def processLine():
    ## Handles the single-line dollar-sign input
    user_input = input("Enter 4 grades separated by $ (or 'Q' to quit): ")
    
    if user_input.upper() == 'Q':
        return 'QUIT'
    
    # Split by $ and clean whitespace
    grades = [g.strip() for g in user_input.split('$')]
    return grades

def main():
    while True:
        raw_grades = processLine()
        
        if raw_grades == 'QUIT':
            print("Exiting program...")
            break
            
        if not validateGrades(raw_grades):
            print("Error: Please enter exactly 4 grades.")
            continue
            
        # Convert letters to numbers
        num_grades = [gradeToNumber(g) for g in raw_grades]
        
        # Process math
        avg, lowest_val = calculateFinalAvg(num_grades)
        final_letter = numberToGrade(avg)
        
        # Output
        printSummaryBox(raw_grades, lowest_val, avg, final_letter)

if __name__ == "__main__":
    main()