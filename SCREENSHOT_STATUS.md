# Execution and Screenshot Status

This file tracks the execution/screenshot attempt for the 10 case studies.

## TinyFish browser run

Run: https://agent.tinyfish.ai/runs/819e219b-83a0-4104-8d8c-c796da0236dc

- **Case study 1 — Student Grade Calculator:** TinyFish reported a successful run, but its displayed output format did not exactly match the current `01_student_grade_calculator/main.py` file. Treat this as an unverified run, not a final test screenshot.
- **Case study 2 — Electricity Bill Calculator:** TinyFish reported unexpected values (115500 units and Rs. 577050.00 for the intended 150-unit input). This is an invalid test result and must not be accepted as a passing screenshot.
- **Case studies 3–10:** Not executed in this browser run.

## Screenshot status

No verified program-output screenshots have been uploaded yet. The browser run page above records the attempt, but it is not a substitute for a screenshot of each program running correctly.

## Required next steps

1. Run each `main.py` file using the inputs in [TEST_CASES.md](TEST_CASES.md).
2. Confirm that the visible output matches the program and test case.
3. Capture a screenshot of the actual output for each case study.
4. Save each screenshot inside its matching project folder, for example:
   `01_student_grade_calculator/screenshots/test-run.png`.
5. Update this file with the verified screenshot links after uploading them.

Do not label a screenshot as a successful test unless the output matches the code and test inputs.
