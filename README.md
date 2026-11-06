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
<img width="1916" height="822" alt="image" src="https://github.com/user-attachments/assets/90495cd9-dbcd-4c48-bb81-e88e29274568" />

The main interface provides three sections: Evaluation, Rules and Testing.

2. Applicant Information
<img width="1916" height="822" alt="image" src="https://github.com/user-attachments/assets/f6fb2b03-ca75-4f63-9271-b834be4fd8f6" />

Users can enter applicant details, including CGPA, family income, co-curricular score, community service hours, semester and disciplinary actions.

3. Scholarship Evaluation
<img width="1848" height="832" alt="image" src="https://github.com/user-attachments/assets/c36e287e-3ea5-4954-938d-b3a86419bc40" />

The system evaluates applicant information and generates a scholarship recommendation based on the predefined rules.

4. JSON Rule Configuration
<img width="1837" height="835" alt="image" src="https://github.com/user-attachments/assets/7c113d61-f82f-4ea0-88d4-c57cac767b45" />

The JSON editor allows users to view and modify the scholarship rules, including conditions, priorities and actions.

5. Rule Matching
<img width="1755" height="792" alt="image" src="https://github.com/user-attachments/assets/e6f77585-9548-489e-8c14-cf819e69f8c4" />

The inference engine checks all conditions and selects the matching rule with the highest priority.

6. System Testing
<img width="1863" height="787" alt="image" src="https://github.com/user-attachments/assets/84aabaf1-8649-48ac-a5ed-2a8b74cb7351" />

Different applicant scenarios are tested to verify the system's decision-making functionality.
