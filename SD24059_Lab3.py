import json
import operator
import streamlit as st
import pandas as pd

# --------------------------------------------------
# 1. RULES: Use the five rules given in the lab brief
# --------------------------------------------------

DEFAULT_RULES = [
    {
        "name": "Top merit candidate",
        "priority": 100,
        "conditions": [
            ["cgpa", ">=", 3.7],
            ["co_curricular_score", ">=", 80],
            ["family_income", "<=", 8000],
            ["disciplinary_actions", "==", 0]
        ],
        "action": {
            "decision": "AWARD_FULL",
            "reason": "Excellent academic & co-curricular performance, with acceptable need"
        }
    },
    {
        "name": "Good candidate - partial scholarship",
        "priority": 80,
        "conditions": [
            ["cgpa", ">=", 3.3],
            ["co_curricular_score", ">=", 60],
            ["family_income", "<=", 12000],
            ["disciplinary_actions", "<=", 1]
        ],
        "action": {
            "decision": "AWARD_PARTIAL",
            "reason": "Good academic & involvement record with moderate need"
        }
    },
    {
        "name": "Need-based review",
        "priority": 70,
        "conditions": [
            ["cgpa", ">=", 2.5],
            ["family_income", "<=", 4000]
        ],
        "action": {
            "decision": "REVIEW",
            "reason": "High need but borderline academic score"
        }
    },
    {
        "name": "Low CGPA – not eligible",
        "priority": 95,
        "conditions": [
            ["cgpa", "<", 2.5]
        ],
        "action": {
            "decision": "REJECT",
            "reason": "CGPA below minimum scholarship requirement"
        }
    },
    {
        "name": "Serious disciplinary record",
        "priority": 90,
        "conditions": [
            ["disciplinary_actions", ">=", 2]
        ],
        "action": {
            "decision": "REJECT",
            "reason": "Too many disciplinary records"
        }
    }
]

# --------------------------------------------------
# 2. RULE ENGINE
# --------------------------------------------------

OPS = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le
}


def condition_matches(facts, condition):
    field, op, value = condition
    return field in facts and op in OPS and OPS[op](facts[field], value)


def rule_matches(facts, rule):
    # All conditions must be TRUE (AND)
    return all(condition_matches(facts, c) for c in rule["conditions"])


def run_rules(facts, rules):
    matched = [r for r in rules if rule_matches(facts, r)]
    matched.sort(key=lambda r: r["priority"], reverse=True)

    if not matched:
        return {
            "decision": "REVIEW",
            "reason": "No rule matched. Manual review is required."
        }, []

    return matched[0]["action"], matched


# --------------------------------------------------
# 3. STREAMLIT INTERFACE
# --------------------------------------------------

st.set_page_config(page_title="Scholarship Advisory System",
                   page_icon="🎓", layout="wide")

st.title("🎓 Scholarship Advisory System")
st.caption("BSD3513 Artificial Intelligence | Lab Report 3")

if "rules" not in st.session_state:
    st.session_state.rules = DEFAULT_RULES

if "rules_json" not in st.session_state:
    st.session_state.rules_json = json.dumps(
        DEFAULT_RULES, indent=2, ensure_ascii=False
    )

tab1, tab2, tab3 = st.tabs(["Evaluation", "Rules", "Testing"])

# --------------------------------------------------
# TAB 1: APPLICANT EVALUATION
# --------------------------------------------------

with tab1:
    st.subheader("Applicant Information")

    col1, col2 = st.columns(2)

    with col1:
        cgpa = st.number_input("CGPA", 0.0, 4.0, 3.50, 0.01)
        family_income = st.number_input(
            "Monthly Family Income (RM)", 0, 100000, 5000, 100
        )
        co_score = st.number_input(
            "Co-curricular Score", 0, 100, 70
        )

    with col2:
        service_hours = st.number_input(
            "Community Service Hours", 0, 10000, 40
        )
        semester = st.number_input(
            "Current Semester", 1, 14, 3
        )
        disciplinary = st.number_input(
            "Disciplinary Actions", 0, 100, 0
        )

    if st.button("Evaluate Applicant", type="primary"):
        facts = {
            "cgpa": cgpa,
            "family_income": family_income,
            "co_curricular_score": co_score,
            "community_service_hours": service_hours,
            "current_semester": semester,
            "disciplinary_actions": disciplinary
        }

        action, matched = run_rules(facts, st.session_state.rules)

        st.divider()
        st.subheader("Decision")
        st.write(f"### {action['decision']}")
        st.write(action["reason"])

        if matched:
            st.write(f"**Winning Rule:** {matched[0]['name']}")
            st.write("**Matched Rules:**")

            result = [
                {
                    "Rule": r["name"],
                    "Priority": r["priority"],
                    "Decision": r["action"]["decision"],
                    "Reason":r["action"]["reason"]
                }
                for r in matched
            ]
            st.dataframe(pd.DataFrame(result), hide_index=True)
        else:
            st.info("No rules matched. Refer the applicant for manual review.")

        with st.expander("View condition checking"):
            for rule in sorted(
                st.session_state.rules,
                key=lambda r: r["priority"],
                reverse=True
            ):
                st.write(f"**{rule['name']}**")
                for field, op, value in rule["conditions"]:
                    passed = condition_matches(facts, [field, op, value])
                    status = "True" if passed else "False"
                    st.write(f"- {field} {op} {value}: **{status}**")

# --------------------------------------------------
# TAB 2: JSON RULE EDITOR
# --------------------------------------------------

with tab2:
    st.subheader("Rule Configuration")
    st.write("View or edit the rules used by the system.")

    st.session_state.rules_json = st.text_area(
        "JSON Rules",
        value=st.session_state.rules_json,
        height=400
    )

    if st.button("Apply Rules"):
        try:
            new_rules = json.loads(st.session_state.rules_json)

            if not isinstance(new_rules, list):
                st.error("Rules must be a JSON list.")
            elif not all(
                isinstance(r, dict)
                and all(k in r for k in ["name", "priority", "conditions", "action"])
                for r in new_rules
            ):
                st.error("Each rule must contain name, priority, conditions and action.")
            else:
                st.session_state.rules = new_rules
                st.success("Rules updated successfully.")

        except json.JSONDecodeError as error:
            st.error(f"Invalid JSON: {error}")

    if st.button("Restore Default Rules"):
        st.session_state.rules = DEFAULT_RULES
        st.session_state.rules_json = json.dumps(
            DEFAULT_RULES, indent=2, ensure_ascii=False
        )
        st.success("Default rules restored.")

# --------------------------------------------------
# TAB 3: SIMPLE TESTING
# --------------------------------------------------

with tab3:
    st.subheader("Sample Test Cases")

    test_cases = [
        {
            "Test Case": "Full scholarship",
            "cgpa": 3.8, "co_curricular_score": 90,
            "family_income": 5000, "disciplinary_actions": 0
        },
        {
            "Test Case": "Partial scholarship",
            "cgpa": 3.5, "co_curricular_score": 70,
            "family_income": 9000, "disciplinary_actions": 0
        },
        {
            "Test Case": "Need-based review",
            "cgpa": 2.8, "co_curricular_score": 40,
            "family_income": 3000, "disciplinary_actions": 0
        },
        {
            "Test Case": "Low CGPA rejection",
            "cgpa": 2.2, "co_curricular_score": 50,
            "family_income": 5000, "disciplinary_actions": 0
        },
        {
            "Test Case": "Disciplinary rejection",
            "cgpa": 3.5, "co_curricular_score": 70,
            "family_income": 5000, "disciplinary_actions": 2
        }
    ]

    if st.button("Run Test Cases"):
        results = []

        for case in test_cases:
            facts = {
                "cgpa": case["cgpa"],
                "co_curricular_score": case["co_curricular_score"],
                "family_income": case["family_income"],
                "disciplinary_actions": case["disciplinary_actions"]
            }

            action, matched = run_rules(facts, st.session_state.rules)

            results.append({
                "Test Case": case["Test Case"],
                "Decision": action["decision"],
                "Winning Rule": matched[0]["name"] if matched else "None"
            })

        st.dataframe(pd.DataFrame(results), hide_index=True)

st.divider()
st.caption("This system is a decision-support prototype. Final scholarship "
           "decisions should be reviewed by the university committee.")
