# COMPONENT 2: Organisational Integration Toolkit

## Purpose

This component establishes fairness governance across teams , defining who owns what, who makes which decisions and how fairness work is coordinated and recorded. 

## How this component relates to the rest of the playbook:

Where the Fair AI Scrum Toolkit operates at team level, the Organisational Integration Toolkit operates at organisation level. It:
- Sets cross-team fairness roles and decision authority.
- Aligns teams on shared fairness principles, metrics, and thresholds.
- Provides documentation structures so fairness decisions and trade-offs are traceable over time.

---

# FAIRNESS GOVERNANCE FRAMEWORK

## SECTION 1: Selecting Fairness Roles 

### Leadership Roles

#### STEP 1: Get familiar with the examples of types of leadership fairness roles and accountabilities present in organisations in the table below. 

| Role | Responsibilities |
|---|---|
| Chief AI Ethics Officer | Sets fairness vision and strategy aligned with business objectives, allocates resources for fairness initiatives, serves as final decision authority for major fairness trade-offs, reports fairness performance to the board and executive team, represents the organisation on fairness matters with regulators and the public and champions fairness culture and accountability. |
| Fairness Program Manager | Ensures alignment across teams, tracks fairness milestones, and maintains documentation consistency. |
| Technical Fairness Lead | Implements fairness testing pipelines, evaluates model bias, and validates mitigation strategies |
| Fairness Domain Specialist | Provide expertise in specific application areas (e.g., hiring, lending)/ |
| Executive sponsor | Provides strategic visibility, resources, and decision-making authority to enforce fairness commitments. |
| Fairness Champion | Ensures team backlogs include fairness tasks; raises fairness issues early; connects squad-level work to organisation-level governance and standards. |

#### STEP 2: Fill out the template below with inspiration from the table above to note the fairness roles in your organisation. Make sure you fill out the template for each relevant role. 

Template: 

Role title: 
[INSERT]  
Reporting to: 
[INSERT]  
Role purpose:
[INSERT]  
Key responsibilities:
[INSERT]  
Collaboration (who they work with regularly):
[INSERT]  
Expected outcomes (what success looks like): 
[INSERT]  
Required skills/experience: 
[INSERT]  

### Cross-Functional Responsibilities

#### STEP 3: Get familiar with the examples of types of cross-functional fairness responsibilities. 

| Function | Responsibilities |
|---|---|
| Data Science | Implement fairness metrics; conduct bias audits; develop mitigation approaches |
| Product management | Define fairness requirements; prioritize fairness work; ensure user testing includes diverse participants |
| Engineering | Create fairness test suites; implement fair feature engineering; build monitoring systems |
| Legal | Interpret fairness regulations; review fairness claims; assess compliance risk |
| Marketing | Ensure accurate fairness messaging; avoid overselling fairness capabilities |
| User Research | Include diverse research participants; investigate fairness impacts; identify bias patterns. |
| Executive Leadership | Set fairness vision; allocate fairness resources; establish accountability systems |

#### STEP 4:  Use the RACI model to make fairness work across functions explicit:

- R – Responsible: does the work  
- A – Accountable: owns the outcome and signs off (only one A per row)  
- C – Consulted: provides input before decisions  
- I – Informed: kept updated after decisions  

Here is an example of a fairness RACI matrix  which you can base your own on. Replace the columns/rows below with your own functions and adjust the RACI marks so every key fairness task has at least one accountable and at least one responsible. 

| Fairness Decision | Executive Leadership | Program manager | Data Science | Product | Legal | Marketing | Engineering | User Research |
|---|---|---|---|---|---|---|---|---|
| Define fairness definition | A | R | C | C | C | I | I | I |
| Approve fairness metrics thresholds | A | C | R | C | I | I | C | I |
| Conduct fairness audits | C | A | R | I | C | I | R | C |
| Manage intersectional analysis | A | C | R | R | C | I | R | I |
| Approve release criteria | A | C | R | R | C | I | R | I |
| Communicate results | A | R | C | C | C | R | I | I |
| Handle fairness incidents | A | R | R | C | C | I | R | C |
| Update governance and policies | A |  | R | C | C | C | I | I |

---

## SECTION 2: Selecting Fairness Governance Bodies:

#### STEP 1: Get familiar with the examples of types of fairness governance bodies and structures that exist in organisations. 

| Bodies | Responsibilities |
|---|---|
| Fairness Steering Committee | Executive-level body setting organization-wide fairness strategy, policies, and standards. |
| Fairness Review Board | Cross-functional group evaluating fairness of specific products or features |
| AI Ethics Working Group | Ongoing forum discussing emerging fairness challenges and developing guidance. |
| Community Advisory Council | External stakeholders providing diverse perspectives on fairness impacts |
| Fairness Technical Committee | Practitioners establishing technical standards for bias assessment and mitigation |

#### STEP 2: Fill out the template below with inspiration from the table above to note the governance bodies in your organisation. Make sure you fill out the template for each relevant body. 

Template: 

Name of body:
[INSERT]  
Purpose/ mandate:
[INSERT]  
Scope (what it decides on)
[INSERT]  
Membership (who sits on it) 
[INSERT]  
Meeting cadence
[INSERT]  
Decision authority (what it can approve) 
[INSERT]  

---

## SECTION 3: Decision Processes and Escalations Procedures

Now we will design how decisions flow. Where SECTION 1 defined who owns fairness work and established what governance bodies exist, this section focuses on how decisions move through your organisation efficiently and consistently, including escalation paths and verification gates.

#### STEP 1:  Establish multiple levels of fairness decisions with corresponding authority requirements to prevent decision bottlenecks while ensuring appropriate oversight. Use this three-tier framework to route decisions to the appropriate level. Tailor the example table below to your company. 

| Decision Tier | Example Decisions | Authority Level |
|---|---|---|
| Tier 1 (Strategic) | Fairness framework selection; Policy-level trade-offs; New protected attribute inclusion | Executive leadership; Ethics board |
| Tier 2 (Tactical) | Fairness metric selection; Threshold adjustments; Mitigation approach approval | Department leadership; Fairness program leads |
| Tier 3 (Operational) | Implementation details; Monitoring parameters; Technical adjustments | Team leads; Technical specialists |

#### STEP 2: Use the template below to escalate fairness decisions to the appropriate authority level. 

1. Categorise the Decision:  
Decision Type: [Strategic / Tactical / Operational], e.g.  
Impact Level:  
[ ] Critical: Significant bias affecting decisions  
[ ] Major: Notable disparity requiring mitigation  
[ ] Minor: Small disparities within acceptable thresholds  

2. Determine Authority Required:  
As identified above and the table setting out the decision tiers:  
[ ] Critical issues → Tier 1  
Decision forum: [INSERT, e.g. Executive leadership; Ethics board]  
Final Approver:  
[ ] Major Issues → Tier 2  
Decision forum: [INSERT, e.g.Department leadership; Fairness program leads]  
Final Approver:  
[ ] Minor Issues → Tier 3  
Decision forum: [INSERT, e.g.Team leads; Technical specialists]  
Final Approver:  

3. Route for Decision:  
Submit to: [Role/Title]  
Expected timeline:  
[ ] Critical issues: 48-hour initial response  
[ ] Major issues: 5 business day resolution timeline  
[ ] Minor issues: Addressed in regular development cycle  

---

## SECTION 4: Mandatory Governance Checkpoints 

Now we are enforcing checkpoints, also known as governance gates. At each stage of the AI development lifecycle, fairness consideration checkpoint should be accounted for. Use the following checklist and fill out the required authority at each stage. 

#### STEP 1: Gate 1 - Data Review. This stage ensures that training data fairness is verified before model training. 
Authority: [INSERT]  
[ ] Protected attributes identified and documented  
[ ] Data distribution analysis completed across groups  
[ ] Historical bias patterns assessed  
[ ] Sample size adequacy verified for all groups  

#### STEP 2: Gate 2 - Design Approval. This evaluates fairness in model architecture and feature selection. 
Authority: [INSERT]  
[ ] Fairness implications of architecture evaluated  
[ ] Fairness metrics defined and thresholds set  
[ ] Design decisions documented  

#### STEP 3: Gate 3 - Pre-deployment. This assesses fairness metrics before system release.
Authority: [INSERT]  
[ ] Fairness metrics calculated and validated  
[ ] All thresholds met or exceptions documented  
[ ] Intersectional analysis completed  
[ ] Monitoring systems configured  

#### STEP 4: Gate 4 - Monitoring. This establishes triggers for re-evaluation. 
Authority: [INSERT]  
[ ] Metric shift identified and documented  
[ ] Impact assessment completed  
[ ] Remediation plan developed  
[ ] Fairness Register updated  

---

## SECTION 5: Fairness Documentation Templates

This part shows you how to document your fairness decisions. This section ensures that every important fairness choice is written down, what was decided, why, and by whom, so future teams and auditors can understand and challenge it.

#### STEP 1: Start by filling out the Fairness Requirements Specification Template before any build work to define measurable fairness goals:

Fairness Requirements Specification Template (to be placed within the Model Card presented in Component 4).

1. Fairness Definitions: [Define what fairness means for this use case.]

2. Fairness Metrics & Threshold Values (primary and secondary)

| Metric | Threshold Value |
|---|---|
|  |  |
|  |  |
|  |  |

3. Protected Attributes

| Attribute | Source | Justification |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

4. Testing & Validation Criteria: [How fairness properties will be validated]

5. Trade-off Priorities: [How conflicts between fairness and other objectives should be resolved]

| Goal | Priority | Notes |
|---|---|---|
| Fairness |  |  |
| Accuracy |  |  |
| Explainability |  |  |
| Compliance |  |  |

6. Regulatory Notes: [Specific compliance obligations relevant to this application]

7. Documentation & Ownership: [Who maintains and reviews fairness requirements.]

#### STEP 2: Use the Fairness Decision Record every time a fairness-impacting choice is made. 

Fairness Decision Record Template 

Project Name:  
Model / Component:  
Date:  
Decision Owner:  
Contributors:  

1. Context: [Background information about the system, data, and application domain]

2. Decision Summary: [Clear statement of the fairness decision made] 

3. Alternatives Considered: [Other options considered and why they were rejected]

4. Rationale: [Explicit reasoning behind the selected approach] 

5. Stakeholders: [Who was involved in and affected by the decision] 

6. Trade-offs: [What was gained and sacrificed with this choice] 

7. Metrics & Thresholds: 

| Fairness Metric | Target | Justification | Validation Status |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

8. Limitations: [Known shortcomings of the selected approach] 

9. References: [Supporting research, regulations or precedents] 

#### STEP 3: Post-deployment, keep the Fairness Limitation Register below updated as new insights or incidents emerge. 

Fairness Limitation Register Template 

Model / System:  
Last Updated:  

Issue Monitoring: [Tracking known issues to drive future improvements]

| ID | Description | Affected Groups | Severity | Mitigation Plan | Owner | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

---

## SECTION 6: Metrics Dashboards and Monitoring 

This part focuses on measuring and tracking fairness in production. This section provides ready-to-use templates and frameworks that help you measure, visualize, and monitor fairness across AI systems. It enables immediate implementation of fairness tracking without requiring large-scale redesigns or engineering overhead.

#### STEP 1: Choose a small core set of metrics you will track everywhere, plus any domain-specific ones. Use the table below as a guide and note your selected metrics (including intersectional variants where possible).

| Metric Category | Example Metrics | Pros | Limitations |
|---|---|---|---|
| Group Fairness | Demographic Parity, Equal Opportunity, Equalized Odds | Easy to compute, interpretable | May hide within-group variations |
| Individual Fairness | Consistency scores, Counterfactual Fairness | Reflects personalized fairness | Requires detailed individual data |
| Process Fairness | Data representation stats, intervention effectiveness | Tracks fairness in data generation | May not capture outcome fairness |
| Outcome Fairness | Realised fairness in deployed contexts | Measures real-world impact | Needs user-level feedback data |

#### STEP 2: Decide how to display these metrics using the templates below. Each view should answer “What is the fairness status and what should I do with this information?” for its audience.

Dashboard Templates 

(1) Executive Dashboard View  
Fairness Health: [Stable/At Risk/Unstable]  
Top 3 Risk Indicators  
[insert description]  
[insert description]  
[Insert description]  
Required Actions:  
[LIST]  

(2) Management Dashboard View 

| Team | System | Fairness Metrics Threshold | Status | Actions |
|---|---|---|---|---|
| [Team] | [System Name] | [Insert e.g. DP gap] | [Stable/At risk/Critical] | [Insert] |

(3) Technical Dashboard View 

| Metric | Group 1 | Group  2 | Threshold | Status |
|---|---|---|---|---|
| Demographic Parity | [Insert metric result, e.g. 0.78] | [Insert metric result] | [Insert metric threshold] | [Met/Not met] |
| Equal Opportunity | [Insert metric result] | [Insert metric result] | [Insert metric threshold] | [Met/Not met] |
| Equalised Odds | [Insert metric result] | [Insert metric result] | [Insert metric threshold] | [Met/Not met] |

(4) Stakeholder View  
What we measure: [Plain-language summary of key metrics]  
Current status: [Short sentence per key group/intersection]  
What we’re doing about it: [Current or planned interventions]  
How to raise concerns: [Contact / process]  

#### STEP 3: Set up tiered monitoring and alerts. Use a tiered alert table to define when fairness drift should trigger a response, who is notified and how quickly they must act. Tailor thresholds and roles to your organisation.

Fairness Drift Alert Tracking Table:

| Tier | Metric Trigger | Notification | Response time | Resolution |
|---|---|---|---|---|
| 1 (Minor) | < 0.03 | Log entry - added to team backlog. | Within 2 weeks | Review the fairness drift and decide if action is needed. |
| 2 (Major) | 0.03 ≤ - < 0.07 | Send comms to Technical lead | Within 5 days | Model retraining |
| 3 (Critical) | ≥ 0.07 | Escalations to AI ethics Committee | Within 24 hours | Stop deployment and review |

---

## SECTION 7: Communication and Reporting 

This section translates your metrics and dashboards into tailored messages for different audiences so that fairness information leads to action rather than confusion.

#### STEP 1: Map audiences to communication styles. 

| Stakeholders | Primary Needs | Communication Approach |
|---|---|---|
| Technical Teams | Detailed metrics, reproducibility | Mathematical definitions with implementation details |
| Non-technical teams | “Are we fair enough?” “What do I do?” | Simple language and examples showing fairness properties |
| Executive Leadership | Risks, trends, strategic trade-offs | Impact metrics connecting fairness to company values |
| Regulators | Evidence of control and accountability | Compliance focused documentation with technical appendices. |

#### STEP 2: Define your fairness reporting plan. Fill in the template below using your dashboards and governance structure:

| Stakeholders | Dashboard Used | Format |
|---|---|---|
| Executives | Executive Dashboard | Monthly slide pack and quarterly deep dive |
| Technical Teams | Management and Technical Dashboards | Bi-weekly review in squads |
| Regulators/ Compliance | Documentation | As required (e.g. audit/ annual report) |
| External stakeholders | Stakeholder view | Annual impact report/ website update |

---

# REFERENCES:

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. In Proceedings of the 1st Conference on Fairness, Accountability, and Transparency (pp. 77-91). https://proceedings.mlr.press/v81/buolamwini18a.html 

Holstein, K., Wortman Vaughan, J., Daumé III, H., Dudik, M., & Wallach, H. (2019). Improving fairness in machine learning systems: What do industry practitioners need? In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (pp. 1- 
16). https://doi.org/10.1145/3290605.3300830 

Madaio, M. A., Stark, L., Wortman Vaughan, J., & Wallach, H. (2020). Co-designing checklists to understand organizational challenges and opportunities around fairness in AI. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (pp. 1- 
14). https://doi.org/10.1145/3313831.3376445 

Metcalf, J., Moss, E., Watkins, E. A., Singh, R., & Elish, M. C. (2021). Algorithmic impact assessments and accountability: The co-construction of impacts. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (pp. 735- 
746). https://doi.org/10.1145/3442188.3445935 

Rakova, B., Yang, J., Cramer, H., & Chowdhury, R. (2021). Where responsible AI meets reality: Practitioner perspectives on enablers for shifting organizational practices. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1), 1-23. https://doi.org/10.1145/3449081 

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (pp. 33-44). https://doi.org/10.1145/3351095.3372873 

Richardson, S., Bennett, M., & Denton, E. (2021). Documentation for fairness: A framework to support enterprise-wide fair ML practice. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society (pp. 1003-1012). https://doi.org/10.1145/3461702.3462553 

Vethman, S., Smit, Q. T. S., van Liebergen, N. M., & Veenman, C. J. (2025). Fairness beyond the algorithmic frame: Actionable recommendations for an intersectional approach. ACM Conference on Fairness, Accountability, and Transparency (FAccT '25).