# SEN-306-034-Assignment

# Week 6 Student Result Processing System

## 1. Project Description
The Student Result Processing System is a Python application designed to validate student information, calculate assessment scores, determine grades and calculate Grade Point Average (GPA).The project demonstrates high-quality routines, modularity, validation, automated testing, code review and refactoring.

## 2. Project Objectives
- Develop reusable and maintainable routines.
- Validate student information and assessment scores.
- Calculate total scores, grades and grade points.
- Calculate GPA using course credit units.
- Identify weaknesses in poorly written code.
- Improve code through refactoring.
- Verify program behaviour through automated testing.

## 3. Project File Structure
- main.py: Runs the main application.
- validation.py: Validates student details and scores.
- grading.py: Calculates grades and grade points.
- result_module.py: Processes results and GPA.
- test_grading.py: Tests the grading system.
- test_result_module.py: Tests result processing.
- original_routine.py: Contains the original routine.
- refactored_routine.py: Contains the improved routine.
- README.md: Contains project documentation.

## 4. Grading System
Score | Grade | Grade Point 
70-100 | A | 5 
60-69 | B | 4 
50-59 | C | 3 
45-49 | D | 2 
40-44 | E | 1 
0-39 | F | 0 

## 5. System Requirements
- Python 3
- Visual Studio Code
- Git
- Python unittest module

## 6. Setup Instructions

1. Open Visual Studio Code.
2. Open the project folder.
3. Open the integrated terminal.
4. Confirm Python is installed using: python --version

## 7. Execution Instructions
Run the main application using: python main.py. The application displays student information,total score, grade, grade point and GPA.

## 8. Automated Testing
Run all automated tests using: python -m unittest -v.The tests verify normal inputs, invalid inputs, boundary values, grade transitions, total scores and GPA calculations.

## 9. Boundary-Value Analysis

Boundary-value analysis is a software testing technique that examines values at and around the limits of an accepted input range.The valid score range is 0 to 100.

Input | Expected Result 
-1 | Invalid 
0 | F 
1 | F 
99 | A 
100 | A 
101 | Invalid

Grade transitions tested include:
- 39 and 40
- 44 and 45
- 49 and 50
- 59 and 60
- 69 and 70

These tests verify that grades change correctly at their specified boundaries.

## 10. Code Review

The original routine was reviewed and the following weaknesses were identified:
1. Unclear function and variable names.
2. Lack of input validation.
3. Incomplete grading policy.
4. Multiple responsibilities in one function.
5. Output is printed inside the processing routine.
6. Lack of documentation and error handling.
7. Individual operations are difficult to test.
8. The routine returns only the total score.

These weaknesses reduce readability, maintainability, reliability and testability.

## 11. Refactoring

The original routine was improved by:
- Using meaningful function and variable names.
- Separating validation from result processing.
- Separating calculation from output presentation.
- Centralising grading rules.
- Removing duplicated grading logic.
- Returning structured result data.
- Reusing existing functions.
- Adding automated tests.

The incomplete grading policy was also corrected to include grades D and E.

## 12. Version Control

Git is used to track changes made to the project. The initial implementation and the refactored implementation should be recorded in separate commits.


## 15. Conclusion

The project demonstrates the importance of high-quality routines in software engineering. Through modular programming, input validation, code review, refactoring and automated testing, the application becomes more reliable, readable, maintainable and reusable.
