# Test Cases for Python ABL Projects

These are sample test cases and expected results. Run each program in Python/PyCharm and capture screenshots of the actual console output. For interactive programs, follow the inputs in order. Amounts are in Indian rupees (Rs.).

## 1. Student Grade Calculator
| Test | Input marks (5 subjects) | Expected result |
|---|---|---|
| TC1 | 90, 85, 80, 95, 90 | Total 440/500; percentage 88.00%; Grade B |
| TC2 | 100, 100, 100, 100, 100 | Total 500/500; percentage 100.00%; Grade A |
| TC3 | 40, 50, 60, 55, 45 | Total 250/500; percentage 50.00%; Grade E |
| TC4 | 110, 80, 80, 80, 80 | Invalid marks message; program stops |

## 2. Electricity Bill Calculator
The current educational example uses these slabs: first 100 units at Rs. 1.50/unit, next 100 at Rs. 2.50/unit, and units above 200 at Rs. 4.00/unit.
| Test | Units | Expected result |
|---|---:|---|
| TC1 | 80 | Rs. 120.00 |
| TC2 | 150 | Rs. 275.00 |
| TC3 | 250 | Rs. 600.00 |
| TC4 | -5 | Units cannot be negative |

## 3. Simple ATM Menu Simulation
| Test | Input sequence | Expected result |
|---|---|---|
| TC1 | Choose 1, then 4 | Balance shown as Rs. 1000.00; exit message |
| TC2 | Choose 2, deposit 100, choose 1, choose 4 | Deposit successful; balance Rs. 1100.00 |
| TC3 | Choose 3, withdraw 1200, choose 4 | Insufficient balance |
| TC4 | Choose 9 | Invalid choice message |

## 4. Number Guessing Game
The example secret number is 7.
| Test | Guess | Expected result |
|---|---:|---|
| TC1 | 3 | Too low! |
| TC2 | 9 | Too high! |
| TC3 | 7 | Correct! You guessed in 1 attempt(s). |
| TC4 | 3, 7 | Too low, then correct in 2 attempts |

## 5. Student Attendance Calculator
| Test | Classes held | Classes attended | Expected result |
|---|---:|---:|---|
| TC1 | 40 | 32 | 80.00%; eligible |
| TC2 | 40 | 20 | 50.00%; below 75% |
| TC3 | 10 | 10 | 100.00%; eligible |
| TC4 | 0 | 0 | Invalid attendance data |
| TC5 | 20 | 21 | Invalid attendance data |

## 6. Basic Password Strength Checker
This checks only minimum length (8), at least one digit, and at least one uppercase letter. It is a beginner exercise, not a complete security assessment.
| Test | Password | Expected result |
|---|---|---|
| TC1 | Hello123 | Meets the basic rules |
| TC2 | hello123 | Needs improvement (no uppercase letter) |
| TC3 | HELLOABC | Needs improvement (no digit) |
| TC4 | Ab1 | Needs improvement (too short) |

## 7. Shopping Cart and Bill Calculator
Enter three items and prices for each test.
| Test | Item prices | Expected result |
|---|---|---|
| TC1 | Pen 10, Book 50, Bag 400 | Total Rs. 460.00 |
| TC2 | Apple 25.5, Milk 30, Bread 40 | Total Rs. 95.50 |
| TC3 | Item A -1 | Price cannot be negative; program stops |

## 8. Student Marks Analysis
| Test | Subject marks | Expected result |
|---|---|---|
| TC1 | 80, 90, 70 | Highest 90; lowest 70; average 80.00 |
| TC2 | 100, 100 | Highest 100; lowest 100; average 100.00 |
| TC3 | 0, 0, 0 | Highest 0; lowest 0; average 0.00 |
| TC4 | 110 | Marks must be between 0 and 100; program stops |
| TC5 | Subject count 0 | Enter a positive number of subjects |

## 9. Duplicate Removal Using Sets
| Test | Input numbers | Expected result |
|---|---|---|
| TC1 | 4 2 4 3 2 | Unique numbers: 2 3 4 |
| TC2 | 5 5 5 | Unique numbers: 5 |
| TC3 | 9 1 7 | Unique numbers: 1 7 9 |

## 10. Student Records Using Lists and Tuples
Enter three records in each test.
| Test | Example records | Expected result |
|---|---|---|
| TC1 | 101, Ravi, 85; 102, Sita, 92; 103, Arun, 78 | All three roll numbers, names, and marks displayed |
| TC2 | 201, Meena, 100; 202, Hari, 0; 203, Devi, 65 | All three records displayed, including boundary marks |
| TC3 | 301, Kiran, 110 | Marks must be between 0 and 100; program stops on the invalid mark |

## Screenshot checklist
- [ ] Project 1: normal result and invalid-mark test
- [ ] Project 2: bill calculation
- [ ] Project 3: balance/deposit or withdrawal test
- [ ] Project 4: correct guess
- [ ] Project 5: eligible and below-75% results
- [ ] Project 6: accepted and rejected examples
- [ ] Project 7: total bill
- [ ] Project 8: highest, lowest, average
- [ ] Project 9: duplicates removed
- [ ] Project 10: records displayed

**Important:** These are expected results, not proof of execution. Capture screenshots after running the actual Python programs in your own Python environment. Check the official faculty case-study list before final submission.
