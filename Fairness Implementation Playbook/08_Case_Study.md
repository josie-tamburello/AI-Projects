# Case Study 

## Component 1 - Fair AI Scrum Toolkit

#### SECTION 1: Scrum Artifact Modification

##### 1.1 User Stories

**STEP 1: Document your existing standard user story approach**

Sunshine Regiment documented their existing user story:

> “As a recruiter, I want to filter candidates by experience level so I can focus on qualified applicants.”

Traditional user stories typically focus on functional requirements. This helped the team identify fairness gaps.

---

**STEP 2: Enhance using the SAFE framework**

Sunshine Regiment used the SAFE Template from the toolkit to structure their analysis.

**SAFE Template (filled out):**

**Specify protected attributes**  
Gender, race/ethnicity, age, educational background, geography

**Define actionable fairness metrics**  
Equal Opportunity difference ≤ 0.03 across protected groups (primary fairness metric)

**Identify where fairness impacts the feature**  
- Ranking algorithm that orders candidates  
- Resume parsing and scoring logic  
- Shortlisting threshold used to decide which candidates advance  

**Establish measurable outcomes**  
- Bias report with disaggregated metrics across gender, race/ethnicity, age, and key intersections generated at the end of the sprint  
- Fairness metrics reviewed and validated before Gate 3 (Pre‑Deployment)  
- Any disparity above thresholds logged in the Fairness Limitation Register  

---

**STEP 3: Draft fairness‑enhanced user stories**

Based on their SAFE analysis, Sunshine Regiment drafted fairness‑enhanced user stories for high‑risk features using the toolkit’s template.

Using the **User Story Template**:

> "As a recruiter, I want candidates ranked by qualification score so I can efficiently identify top prospects, while ensuring equal opportunity (difference ≤ 0.03) across gender, race/ethnicity, age, and their intersections."

---

**STEP 4: Document in the following format**

### USER STORIES

| Feature           | Existing User Story Template                                                                 | Fairness Enhanced User Story Template |
|------------------|----------------------------------------------------------------------------------------------|---------------------------------------|
| Resume Screening | "As a recruiter, I want to filter candidates by experience level so I can focus on qualified applicants." | "As a recruiter, I want candidates ranked by qualification score so I can efficiently identify top prospects, while ensuring equal opportunity (difference ≤ 0.03) across gender, race/ethnicity, age, and their intersections." |

---

##### 1.2 Acceptance Criteria

**STEP 1: Use the FAIR framework**

Sunshine Regiment used the FAIR framework from the toolkit:

- **F** = Fairness metrics thresholds  
- **A** = Auditing requirements  
- **I** = Intersectional analysis  
- **R** = Reporting guidelines  

They also added **Perspective Documentation** as recommended in the toolkit’s example table.

---

**STEP 2: Fill out the template below**

### ACCEPTANCE CRITERIA

| Element                  | Criteria                                                                                                                         | Justification |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------|
| Fairness Metrics Thresholds | Demographic parity difference below 0.05 across all protected attributes. <br> Equal opportunity difference below 0.03 for all groups. <br> Prediction calibration error differences below 0.04 between any two groups. | Thresholds selected directly from the toolkit’s example library to align with organizational standards and provide multi‑metric coverage. |
| Auditing Requirements    | Dataset representation verified across all protected attributes. <br> Performance disaggregated across all identified demographic groups. <br> Regular bias testing during development (at least once per sprint). | Ensures that data imbalance and performance disparities are detected early and monitored continuously. |
| Intersectional Analysis  | Performance reported for key intersections (e.g., gender × race/ethnicity × age). <br> Maximum performance disparity of 0.07 between any two intersectional groups. | Captures compounded harms that would be missed by single‑attribute analysis, following intersectional guidance in the toolkit. |
| Reporting Guidelines     | Comprehensive bias audit documentation before deployment. <br> Disaggregated metrics included in the Model Card. <br> Clear explanation of remaining disparities with justification. | Provides a transparent record for internal and external stakeholders and supports audit readiness. |
| Perspective Documentation | Positionality statement completed documenting the team’s perspectives and potential blind spots. <br> Stakeholder consultation log maintained for affected user groups. <br> Key fairness decisions and trade‑offs documented in a Fairness Decision Record (FDR). | Implements Vethman et al. (2025)’s recommendation to document perspectives and decisions throughout the AI lifecycle. |

---

##### 1.3 Definition of Done

**STEP 1: Review and identify gaps**

Using the toolkit’s Definition of Done table, Sunshine Regiment compared their existing DoD and identified gaps: no fairness tests, no bias documentation, and no intersectional analysis.

---

**STEP 2: Document your extension**

### DEFINITION OF DONE

**Fairness gaps in standard DoD:**  
- No fairness testing requirements  
- No bias audit documentation  
- No fairness metrics validation  
- No intersectional testing requirement  
- No requirement to document fairness trade‑offs  

**Fairness extension to DoD elements:**  
- Code review includes fairness risk checklists (bias amplification, data leakage, proxy features).  
- Fairness unit/integration tests run for key models and metrics (demographic parity, equal opportunity, calibration), including disaggregated tests for intersectional subgroups.  
- Fairness documentation included in every sprint: bias reports, limitations, mitigation steps, and counterfactual analysis for high‑stakes decisions.  
- Fairness acceptance criteria (from the FAIR table) validated and approved by the team.  
- Product Owner sign‑off requires presentation of fairness evidence; a fairness report is shared in each sprint review.  

**Component‑specific fairness requirements (Model component – resume screening classifier):**  
- Model Card completed with fairness metrics and limitations.  
- Counterfactual analysis performed for sample candidates (e.g., changing name or gender without changing qualifications).  
- Fairness‑accuracy trade‑offs documented in an FDR.

---

##### 1.4 Sprint Backlogs

**STEP 1: Document existing sprint backlog approach**

Sunshine Regiment documented that previously, sprint backlogs only contained functional work and technical debt; fairness work was added ad‑hoc, if at all.

---

**STEP 2: Determine capacity allocation**

Based on the toolkit’s guidance (15–30% for fairness tasks) and the high‑risk nature of resume screening, the team allocated **20%** of sprint capacity to fairness tasks.

---

**STEP 3: Review catalog of fairness tasks**

From the toolkit’s catalog, Sunshine Regiment selected:

- **Fairness analysis:** Data bias audit, model evaluation across groups, intersectional performance testing  
- **Fairness implementation:** Bias mitigation implementation and fair feature engineering  
- **Fairness testing:** Acceptance criteria testing, fairness regression testing, documentation creation  

---

**STEP 4: Apply prioritisation framework**

Using the toolkit’s prioritisation elements:

- Fairness Impact – High (affects all candidates and hiring outcomes)  
- Bias Risk – High (historical bias in hiring data)  
- Harm Severity – High (direct impact on job opportunities)  
- Regulatory Exposure – High (employment and anti‑discrimination law)  

---

**STEP 5: Fill out the template below**

### SPRINT BACKLOGS

**Fairness capacity allocation:** 20%

**Fairness task:** Fairness analysis

**Prioritisation Table**

| Element            | Selection  |
|--------------------|-----------|
| Fairness Impact    | High      |
| Bias Risk          | High      |
| Harm Severity      | High      |
| Regulatory Exposure| High      |
| Overall Status     | Non‑Negotiable |

---

#### SECTION 2: Ceremony Adaptation

##### STEP 1: Identify fairness gaps

Using the toolkit’s **Fairness Challenges** template, Sunshine Regiment documented:

| Challenge Title           | Description                                         |
|---------------------------|-----------------------------------------------------|
| Late bias detection       | Bias issues discovered only during final testing.   |
| Missing intersectional analysis | Only single‑attribute fairness checked; intersections ignored. |

---

##### STEP 2: Ceremony templates

###### Sprint Planning

**Date:** 2025‑02‑01  

**Fairness Champion:**  
Sarah Chen  

**Fairness capacity allocation:**  
20%  

**Fairness actions to be completed:**  
- Data bias audit  
- Intersectional testing  
- Fairness metrics validation  

**Fairness ground rules (from toolkit):**  
- All bias concerns are welcomed; no question is “obvious”.  
- Disagreement is expected and valued as part of learning.  
- Technical and non‑technical perspectives are equally important.  
- Focus on systems, not individuals (e.g. “the model has bias”, not “you caused bias”).  

**Psychological safety check (toolkit‑aligned prompts):**  
- Does anyone have fairness concerns they’re hesitant to raise?  
- Which demographic groups are we most uncertain about?  

---

###### Daily Standup Template

**Date:** 2025‑02‑05  

| Questions                                       | Response                                                                 |
|-------------------------------------------------|--------------------------------------------------------------------------|
| What fairness-related work did I complete yesterday? | "Completed data distribution analysis; found 60% male candidates."        |
| What fairness blockers or data issues do I see today? | "Need to verify sample sizes for intersectional groups."                  |
| Are there fairness metrics or tests that need review? | "Equal Opportunity unit test failing for one demographic group."         |

---

###### Sprint Review

**Date:** 2025‑02‑15  

**Fairness metrics (across demographic groups and intersections):**  
- Equal Opportunity gap: 0.03 (within 0.03 threshold)  
- Gender × Race intersection: Maximum disparity 0.06 (within 0.07 threshold)  

**Unresolved fairness issues:**  
None  

**Fairness validation gate (from toolkit):**  
- Feature only moves to “Done” if all fairness acceptance criteria are met.  
- If any metric breaches thresholds, the feature returns to the backlog for remediation.

---

###### Retrospective Template

**Date:** 2025‑02‑15  

| Fairness-Related Question                                                                 | Response                                                                                     |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Where did we detect bias earliest and how?                                               | "During data review, found 60% male candidates; addressed with data augmentation."          |
| Where did we miss potential fairness problems (including intersectional groups)?         | "Initially missed intersectional analysis; now included in acceptance criteria."            |
| What fairness metrics regressed?                                                         | "None this sprint."                                                                          |
| What fairness documentation proved most useful?                                          | "Component 1 acceptance criteria template and SAFE analysis summary."                       |
| What fairness concern did we hesitate to raise?                                          | "Uncertainty about how to handle small sample sizes for older candidates; flagged for next sprint." |
| Which community perspectives are we missing?                                             | "Feedback from candidates with non‑traditional educational paths."                          |
| What fairness trade‑offs did we make and why?                                            | "Slight accuracy drop (0.5%) accepted to reduce Equal Opportunity gap below 0.03."          |
| How can we improve for the next sprint?                                                  | "Start intersectional analysis earlier; schedule a dedicated fairness review session mid‑sprint." |

---

##### STEP 3: Refinement Template

### REFINEMENT

**Date:** 2025‑02‑16  

| Scrum Stage     | Fairness Gaps                                 | Fairness Touchpoints                                  | Justification                                        |
|-----------------|-----------------------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Sprint Planning | No explicit fairness allocation previously    | 20% capacity allocated; fairness tasks prioritized    | Ensures fairness work is explicit and non‑optional.  |
| Daily Standup   | No fairness questions in standup              | Added three fairness questions from toolkit template  | Enables early detection of fairness issues.          |
| Sprint Review   | No fairness metrics presented                 | Fairness metrics presented with functional demos      | Increases transparency and accountability.           |
| Retrospective   | No structured fairness reflection             | Added full fairness‑focused retrospective template    | Supports continuous improvement and psychological safety. |

---

## Component 2 - Organisational Integration Toolkit

After teams applied Component 1, EquiHire established organizational governance using **Component 2: Organisational Integration Toolkit**.

### SECTION 1: Selecting Fairness Roles

#### STEP 1: Get Familiar with Leadership Roles

EquiHire reviewed the example roles table.

#### STEP 2: Fill Out Role Templates

EquiHire completed the role template for each position:

**Chief AI Ethics Officer:**
- **Role title:** Chief AI Ethics Officer
- **Reporting to:** CEO
- **Role purpose:** Set fairness vision and strategy; serve as final decision authority for major fairness trade-offs
- **Key responsibilities:** Allocate resources; report to board; represent organization with regulators
- **Collaboration:** Works with Fairness Program Manager, Legal, Executive Sponsor
- **Expected outcomes:** Company-wide fairness standards established; regulatory compliance maintained
- **Required skills/experience:** AI ethics expertise, regulatory knowledge, leadership experience

**Fairness Program Manager:**
- **Role title:** Fairness Program Manager
- **Reporting to:** Chief AI Ethics Officer
- **Role purpose:** Ensure alignment across teams; track fairness milestones
- **Key responsibilities:** Coordinate fairness work; manage governance bodies; maintain FDR registry
- **Collaboration:** Works with Technical Fairness Lead, Fairness Champions, Product Managers
- **Expected outcomes:** Cross-team conflicts resolved efficiently; documentation complete
- **Required skills/experience:** Program management, technical understanding of fairness

**Technical Fairness Lead:**
- **Role title:** Technical Fairness Lead
- **Reporting to:** Fairness Program Manager
- **Role purpose:** Implement fairness testing pipelines; evaluate model bias
- **Key responsibilities:** Design fairness test suites; conduct bias audits; approve Gate 1
- **Collaboration:** Works with Data Science teams, Engineering teams, Fairness Champions
- **Expected outcomes:** Fairness metrics accurately calculated; bias issues caught early
- **Required skills/experience:** Data science, ML engineering, fairness metrics expertise

**Fairness Champions (one per team):**
- **Role title:** Fairness Champion
- **Reporting to:** Team Lead
- **Role purpose:** Ensure team backlogs include fairness tasks; raise fairness issues early
- **Key responsibilities:** Attend Team Fairness Circle meetings; ensure Component 1 templates completed
- **Collaboration:** Works with team members, Technical Fairness Lead, Fairness Program Manager
- **Expected outcomes:** Fairness integrated into team sprints; team follows Component 1 processes
- **Required skills/experience:** Technical background, fairness awareness, team influence

#### STEP 3: Cross-Functional Responsibilities

EquiHire reviewed the cross-functional responsibilities table.

#### STEP 4: RACI Matrix

EquiHire created their RACI matrix:

| Fairness Decision | Executive Leadership | Fairness Program Manager | Data Science | Product | Legal | Engineering |
|-------------------|---------------------|--------------------------|--------------|---------|-------|------------|
| Define fairness definition | **A** | **R** | C | C | C | I |
| Approve fairness metrics thresholds | **A** | C | **R** | C | I | C |
| Conduct fairness audits | C | **A** | **R** | I | C | **R** |
| Approve release criteria | **A** | C | **R** | **R** | C | **R** |

---

### SECTION 2: Selecting Fairness Governance Bodies

#### STEP 1: Get Familiar with Governance Bodies

EquiHire reviewed the example governance bodies table.

#### STEP 2: Fill Out Governance Body Templates

**Fairness Steering Committee:**
- **Name of body:** Fairness Steering Committee
- **Purpose/mandate:** Set organization-wide fairness strategy, policies, and standards
- **Scope:** Company-wide fairness framework selection; policy-level trade-offs
- **Membership:** Chief AI Ethics Officer (Chair), CEO, Legal Counsel, Executive Sponsor
- **Meeting cadence:** Quarterly
- **Decision authority:** Can approve Tier 1 strategic decisions

**Fairness Review Board:**
- **Name of body:** Fairness Review Board
- **Purpose/mandate:** Evaluate fairness of specific products or features
- **Scope:** Fairness metric selection; threshold adjustments; Gate 2 and Gate 3 approvals
- **Membership:** Fairness Program Manager (Chair), Technical Fairness Lead, Product Lead, Legal
- **Meeting cadence:** Monthly
- **Decision authority:** Can approve Tier 2 tactical decisions

**Team Fairness Circles:**
- **Name of body:** Team Fairness Circle
- **Purpose/mandate:** Implement and monitor fairness controls at team level
- **Scope:** Implementation details; monitoring parameters; technical adjustments
- **Membership:** Team Lead, Fairness Champion, Technical team members, Product Owner
- **Meeting cadence:** Every sprint
- **Decision authority:** Can make Tier 3 operational decisions

---

### SECTION 3: Decision Processes and Escalation Procedures

#### STEP 1: Establish Decision Tiers

EquiHire created their decision tier table:

| Decision Tier | Example Decisions | Authority Level |
|---------------|-------------------|-----------------|
| Tier 1 (Strategic) | Fairness framework selection; Policy-level trade-offs | Fairness Steering Committee → Chief AI Ethics Officer |
| Tier 2 (Tactical) | Fairness metric selection; Threshold adjustments | Fairness Review Board → Fairness Program Manager |
| Tier 3 (Operational) | Implementation details; Monitoring parameters | Team Fairness Circle → Technical Fairness Lead |

#### STEP 2: Escalation Template - Resolving Fairness Definition Conflict

**The Problem:** Three teams using different fairness definitions.

**Escalation Process:**

1. **Categorise the Decision:**
   - Decision Type: **Strategic**
   - Impact Level: 
     - [x] **Critical:** Significant bias affecting decisions
     - [ ] Major
     - [ ] Minor

2. **Determine Authority Required:**
   - [x] Critical issues → Tier 1
   - Decision forum: **Fairness Steering Committee**
   - Final Approver: **Chief AI Ethics Officer**
   - [ ] Major Issues → Tier 2
   - [ ] Minor Issues → Tier 3

3. **Route for Decision:**
   - Submit to: **Fairness Steering Committee**
   - Expected timeline: 
     - [x] Critical issues: 48-hour initial response

**Decision Made:** Equal Opportunity selected as primary company-wide metric (difference ≤ 0.05).

**Documentation:** FDR-2025-001 created.

---

### SECTION 4: Mandatory Governance Checkpoints

#### STEP 1: Gate 1 - Data Review

**Authority:** Technical Fairness Lead

**Checklist:**
- [x] Protected attributes identified and documented
- [x] Data distribution analysis completed across groups
- [x] Historical bias patterns assessed
- [x] Sample size adequacy verified for all groups

#### STEP 2: Gate 2 - Design Approval

**Authority:** Fairness Review Board

**Checklist:**
- [x] Fairness implications of architecture evaluated
- [x] Fairness metrics defined and thresholds set
- [x] Design decisions documented

#### STEP 3: Gate 3 - Pre-deployment

**Authority:** Fairness Program Manager

**Checklist:**
- [x] Fairness metrics calculated and validated
- [x] All thresholds met or exceptions documented
- [x] Intersectional analysis completed
- [x] Monitoring systems configured

#### STEP 4: Gate 4 - Monitoring

**Authority:** Based on severity (Tier 1/2/3)

**Checklist:**
- [x] Metric shift identified and documented
- [x] Impact assessment completed
- [x] Remediation plan developed
- [x] Fairness Register updated

---

### SECTION 5: Fairness Documentation Templates

#### STEP 1: Fairness Requirements Specification (FRS)

Sunshine Regiment completed FRS template:

1. **Fairness Definitions:** Equal Opportunity - qualified candidates should have equal chance of being selected

2. **Fairness Metrics & Threshold Values:**

| Metric | Threshold Value |
|--------|----------------|
| Equal Opportunity (primary) | ≤ 0.05 |

3. **Protected Attributes:**

| Attribute | Source | Justification |
|-----------|--------|---------------|
| Gender | Application form | EU employment law protection |
| Race/Ethnicity | Application form | EU employment law protection |
| Age | Application form | EU employment law protection |

4. **Testing & Validation Criteria:** Disaggregated testing across all protected attributes and intersections

6. **Trade-off Priorities:**

| Goal | Priority | Notes |
|------|----------|-------|
| Fairness | High | Primary objective |
| Accuracy | Medium | Important but secondary |
| Compliance | High | Legal requirement |

7. **Regulatory Notes:** High Risk under EU AI Act; GDPR Art 22 applies

8. **Documentation & Ownership:** Fairness Program Manager maintains; Technical Fairness Lead reviews quarterly

#### STEP 2: Fairness Decision Record (FDR)

**FDR-2025-001:**
- Project Name: EquiHire Platform
- Model / Component: All systems
- Date: 2025-01-15
- Decision Owner: Chief AI Ethics Officer
- Context: Three teams using different fairness definitions
- Decision Summary: Equal Opportunity selected as primary company-wide metric
- Rationale: Aligns with EU employment law; creates consistency
- Metrics & Thresholds: Equal Opportunity ≤ 0.05 (primary)

#### STEP 3: Fairness Limitation Register

| ID | Description | Affected Groups | Severity | Mitigation Plan | Owner | Status |
|----|-------------|-----------------|----------|----------------|-------|--------|
| LIM-001 | Small sample size for intersectional group | Older candidates from minority groups | Medium | Bayesian methods applied | Technical Fairness Lead | Monitoring |

---

### SECTION 5: Metrics Dashboards and Monitoring

#### STEP 1: Select Metrics

EquiHire selected metrics:
- Group Fairness: Equal Opportunity (primary), Demographic Parity, Equalized Odds
- Process Fairness: Data representation stats
- Outcome Fairness: Post-deployment fairness gap

#### STEP 2: Dashboard Templates

**(1) Executive Dashboard View:**
- Fairness Health: Stable
- Top 3 Risk Indicators:
  1. Dragon Army - 6% demographic parity gap (being addressed)
  2. Chaos Legion - Red-teaming found bias patterns (mitigated)
  3. Sunshine Regiment - Stable

**(2) Management Dashboard View:**

| Team | System | Fairness Metrics Threshold | Status | Actions |
|------|--------|---------------------------|--------|---------|
| Sunshine Regiment | Resume Screening | EO gap: 0.03 (≤ 0.05) | Stable | Monitor |
| Chaos Legion | Interviewing (LLM) | Guardrail effectiveness: 95% | Stable | Continue red-teaming |
| Dragon Army | Job Matching | DP gap: 0.06 (≤ 0.05) | At Risk | Implement re-ranking |

**(3) Technical Dashboard View:**

| Metric | Group 1 | Group 2 | Threshold | Status |
|--------|---------|---------|-----------|--------|
| Equal Opportunity | 0.89 | 0.92 | 0.05 |  Met (0.03 gap) |

#### STEP 3: Tiered Monitoring and Alerts

| Tier | Metric Trigger | Notification | Response time | Resolution |
|------|----------------|--------------|---------------|------------|
| 1 (Minor) | < 0.03 | Log entry | Within 2 weeks | Review and decide if action needed |
| 2 (Major) | 0.03 ≤ Δ < 0.07 | Send comms to Technical lead | Within 5 days | Model retraining or mitigation |
| 3 (Critical) | ≥ 0.07 | Escalations to Review Board | Within 24 hours | Stop deployment and review |

---

### SECTION 6: Communication and Reporting

#### STEP 1: Map Audiences to Communication Styles

| Stakeholders | Primary Needs | Communication Approach |
|--------------|---------------|------------------------|
| Technical Teams | Detailed metrics, reproducibility | Mathematical definitions with implementation details |
| Non-technical teams | "Are we fair enough?" | Simple language and examples |
| Executive Leadership | Risks, trends, strategic trade-offs | High-level metrics; business impact |
| Regulators | Evidence of control and accountability | Formal documentation; audit trail |

#### STEP 2: Define Fairness Reporting Plan

| Stakeholders | Dashboard Used | Format |
|--------------|----------------|--------|
| Executives | Executive Dashboard | Monthly slide pack and quarterly deep dive |
| Technical Teams | Management and Technical Dashboards | Bi-weekly review in squads |
| Regulators/ Compliance | Documentation | As required (e.g. audit/ annual report) |

---

## Component 3 - Advanced Architecture Cookbook

After establishing governance (Component 2), teams applied **Component 3: Advanced Architecture Cookbook** for architecture-specific fairness strategies.

### Chaos Legion: LLM System

#### STEP 1: Identify Your Architecture

Chaos Legion selected: **Large Language Model (LLM) → Go to Part A**

#### PART A: LLM Fairness

##### STEP 1: Identify the Fairness Issue

Chaos Legion reviewed the Common Fairness Issues Library and filled out the template:

| Category | Example |
|----------|---------|
| Stereotype Encoding | Model associated names like "Aisha" with lower interview performance scores |
| Sycophancy | Model agreed with biased user prompts |
| Hallucination | Model generated false information with disparate impact on non-native English speakers |

##### STEP 2: Operationalise the Selected Strategy

Chaos Legion selected strategies from the Strategy Library:

**Prompt-Based Fairness Strategies:**
- **Fairness Prompting:** "Evaluate this candidate based solely on their demonstrated skills, experience, and achievements. Do not make assumptions based on name, gender, ethnicity, age, or background."
- **Self-critique Framework:** Two-step prompting for bias review
- **Scaffolded Generation:** Multi-step prompting guiding fair reasoning

**Safety Guardrails:**
- **Filtering:** Input filtering for harmful prompt patterns
- **Classification:** Output classification for detecting biased responses
- **Monitoring:** Monitoring systems for emergent harmful behaviours

**Evaluation Strategies:**
- **Red-teaming:** Continuous systematic adversarial testing
- **Counterfactual Evaluation:** Testing model responses across demographic variations

---

### Dragon Army: Recommendation System

#### STEP 1: Identify Your Architecture

Dragon Army selected: **Recommendation Algorithms → Go to Part B**

#### PART B: Recommendation Algorithm Fairness

##### STEP 1: Identify the Fairness Issue

Dragon Army reviewed the Common Fairness Issues Library:

| Category | Result |
|----------|--------|
| Provider-Side Disparity | Certain job categories received systematically lower exposure |
| Popularity Bias | Popular positions dominated recommendations |
| Cold Start Disadvantage | New job postings struggled to gain visibility |

##### STEP 2: Select a Strategy

Dragon Army selected strategies from the Strategy Library:

- **Re-ranking:** Adjust final ordering to rebalance visibility
- **Exposure & Diversity Balancing:** Introduce explicit exposure objectives
- **Exploration-Exploitation Balancing:** Adjust exploration rates for new positions
- **Monitoring & Governance Framework:** Establish structured logging and dashboards

---

## Component 4 - Regulatory Compliance Guide

Finally, EquiHire applied **Component 4: Regulatory Compliance Guide** to ensure regulatory compliance.

### SECTION 1: Risk Classification

#### STEP 1: Risk Classification Questionnaire

EquiHire's cross-functional team (Legal + Technical) completed the questionnaire:

**(1) Territory:**
- Does your application operate within the European Union or have European Union customers?
- **Answer: YES** → Proceed to "Scope - EU AI ACT"

**(2) Existing Compliance Strategy:**
- Do you currently have a compliance regime in place?
- **Answer: NO** → Proceed to Step 3

**(3) Scope - EU AI ACT:**
- Does your application do any prohibited activities?
- **Answer: NO** → Proceed to next question
- Does your application pose significant risk to health, safety, and fundamental rights? (E.g. recruitment tools)
- **Answer: YES** → **High Risk level under EU AI Act** → Proceed to "Scope - GDPR"

**(4) Scope - GDPR:**
- Does your application process any personal data?
- **Answer: YES** → Proceed to next question
- Does your application process any special category data?
- **Answer: YES** (race, ethnicity) → **High Risk level under GDPR** → Proceed to next question
- Does your application involve automated decision-making?
- **Answer: YES** → Proceed to next question
- Does your application have a legal or significant effect on individuals? (E.g. like in recruitment)
- **Answer: YES** → **High Risk** → Move to next step

**(5) Questionnaire Classification Outcome:**
- **Assigned risk level: High Risk** → Proceed to STEP 2

#### STEP 2: Quantitative Risk Scoring (TRS Calculation)

**TRS = (P × S) + E - M**

**EquiHire's Calculation:**
- **P (Probability):** 4
- **S (Severity):** 4
- **E (Exposure):** 3
- **M (Mitigation):** 2

**TRS = (4 × 4) + 3 - 2 = 17**

**TRS Tier:** > 15 → **High (Tier 1)**

#### STEP 3: Overall Risk Classification Outcome

**Result:** High Risk → Proceed to Section 2 (Regulatory Mapping)

---

### SECTION 2: Regulatory Mapping

#### STEP 1: Legal Framework Overview

EquiHire reviewed the risk levels table and confirmed their **High Risk** classification.

#### STEP 2: Regulatory Mapping Matrix

EquiHire used the High Risk Requirements matrix to identify compliance tasks:

**Key Compliance Tasks:**
- **Data Ingestion:** Automated bias-scan jobs in data pipeline (EU AI Act Art 10)
- **Model Training:** Training parameters logged in MLflow; Model Cards auto-generated (EU AI Act Art 11)
- **Pre-Deployment:** DPIA workflow triggered (GDPR Art 35); Human oversight feature added (EU AI Act Art 14)
- **Post-Deployment:** Immutable logging pipeline (EU AI Act Art 19); Fairness drift dashboards (EU AI Act Art 61)

---

### SECTION 3: Compliance Documentation Templates

EquiHire used the templates to create:

**(1) Model Card:**
- Application Overview (System Name, Version, Model Type)
- Legal Profile (Risk Tier: High, TRS: 17, DPIA Required: YES)
- Data Governance (Dataset sources, representativeness checks, bias mitigation)
- Fairness & Performance Metrics (metrics used, slice-level results, thresholds)
- Human Oversight Plan (oversight roles, manual review triggers, override workflow)
- Monitoring & Logging (drift monitoring frequency, audit logging location, retention period)

**(2) Transparency Disclaimer:**
- Added to user-facing interfaces: "This recommendation is AI-assisted. For more information about how this works, click here."

---

### SECTION 4: Audit Trail Design

EquiHire implemented the audit trail workflow:

**Audit Trail Workflow:** User action → Decision Engine → Event Broker (Kafka) → Audit Trail Storage

**Logging Categories:**
- **Risk Assessment:** TRS calculations, reviewer IDs (10-year retention)
- **Model Metric:** Fairness scores, slice-level results (5-year retention)
- **Override Event:** Decision IDs, who overruled, reasons (5-year retention)
- **Dataset Snapshot:** Dataset hashes, versions (Life of application + 2 years)
- **Incident Report:** Incident IDs, resolutions, affected users (10-year retention)

---

