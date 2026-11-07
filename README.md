# Scholarship Advisory System
### BSD3513 – Introduction to Artificial Intelligence | Lab Report 3

## 1. Project Overview

This project develops a **Scholarship Advisory System** using a Python-based Rule-Based System. The application assists a university scholarship committee in evaluating scholarship applicants based on their academic performance, financial background, co-curricular involvement and disciplinary records.

The system uses predefined IF–THEN rules to evaluate applicant information and generate scholarship recommendations.

- **Live Application:** [(https://lab-report-3-46ay4a5zpdpan84hx44exu.streamlit.app/)]
- **GitHub Repository:** [(https://github.com/chanwanwen/LAB-REPORT-3)]

## 2. Objectives

- Understand knowledge representation using rule-based systems.
- Implement an inference engine using Python.
- Evaluate scholarship applicants using predefined conditions.
- Support editable JSON rules and priority-based decisions.
- Develop and deploy an interactive web application using Streamlit.

## 3. Technologies Used

- Python
- Streamlit
- Pandas
- JSON
- GitHub

## 4. System Features

- **Applicant Information:** Enter CGPA, monthly family income, co-curricular score, community service hours, current semester and disciplinary actions.
- **Rule-Based Engine:** Evaluate applicant information using IF–THEN conditions.
- **Priority-Based Decisions:** Select the matching rule with the highest priority.
- **JSON Rule Editor:** View, modify and restore scholarship rules.
- **Evaluation Results:** Display scholarship decisions, reasons and matched rules.
- **System Testing:** Test different applicant scenarios.

## 5. Scholarship Decisions

| Decision | Description |
|---|---|
| AWARD_FULL | Full scholarship recommendation |
| AWARD_PARTIAL | Partial scholarship recommendation |
| REVIEW | Requires further assessment |
| REJECT | Not eligible under the matching rule |

## 6. Project Structure

```text
SD24059_Lab3/
│
├── SD24059_Lab3.py
├── requirements.txt
└── README.md
```

## 7. Installation and Setup

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Navigate to the project folder**

```bash
cd SD24059_Lab3
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the application**

```bash
streamlit run SD24059_Lab3.py
```

## 8. Project Documentation

1. Main Application Interface
![Main page Interface](images/Main_page.png)

The main interface provides three sections: Evaluation, Rules and Testing.

2. Applicant Information
![Main page Interface](images/Main_page.png)

Users can enter six applicant details: CGPA, monthly family income, co-curricular score, community service hours, current semester and number of disciplinary actions.

The system uses these details to evaluate the applicant against the predefined scholarship rules.

3. Scholarship Evaluation
![Scholarship Evaluation](images/Decision.png)

Click Evaluate Applicant to start the evaluation process. The inference engine checks the applicant's information against all five predefined rules and generates a scholarship recommendation.

The result includes the rule, priority, decision, and reason.

4. JSON Rule Configuration
![Rule Configuration](images/Rule_configuration.png)

Each rule is assigned a priority value. When multiple rules match an applicant, the system selects the rule with the highest priority.

The application also displays a table of matched rules, including their priorities and corresponding decisions.

5. Rule Matching
![Rule Matching](images/Condition_check.png)

Users can expand the condition-checking section to view whether each condition is satisfied.

Each condition is displayed as True or False, helping users understand how the system reaches its decision.

6. System Testing
![System Testing](images/Testing.png)

The Testing tab provides five sample applicant scenarios, including full scholarship, partial scholarship, need-based review and rejection cases.

Users can run the test cases and view the resulting decisions and winning rules.
