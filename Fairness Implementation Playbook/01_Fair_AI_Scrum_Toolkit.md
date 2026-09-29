# COMPONENT 1: Fair AI Scrum Toolkit

## Purpose

Embedding fairness in daily agile development for individual teams. This is designed to assist teams in the product development of AI-based recruiting features. Standard scrum processes lack explicit fairness considerations. This stage defines how teams execute fairness work, by including fairness checkpoints at each stage of agile development.

## How this component links to the rest of the playbook

- Provides the team-level foundation for organizational fairness governance in **Component 2**.  
- Ceremony modifications include review points for architecture-specific fairness considerations in **Component 3**.  

---

# SECTION 1: Scrum Artifact Modification

## 1.1 User Stories

Please follow the steps below.

### STEP 1: Document your existing standard user story approach

Document your existing standard user story approach, e.g.:

> “As a recruiter, I want to filter candidates by experience level so I can focus on qualified applicants.”

Traditional user stories typically focus on functional requirements. This step helps identify fairness gaps.

---
### STEP 2: Enhance using the SAFE framework

Use the SAFE Template to document your findings. This framework provides structured approach to developing fairness-enhanced user stories. 

#### SAFE Framework

- **S**: Specify protected attributes (e.g., gender, age, ethnicity, educational background, geography).  
- **A**: Define actionable fairness metrics (e.g., equal opportunity difference ≤ 0.05).  
- **F**: Identify where fairness impacts the feature (ranking algorithm, resume parsing, scoring).  
- **E**: Establish measurable outcomes (e.g., bias report with disaggregated metrics generated at end of sprint).  

#### SAFE Template

**Specify protected attributes**  
[INSERT]

**Define actionable fairness metrics**  
[INSERT]

**Identify where fairness impacts the feature**  
[INSERT]

**Establish measurable outcomes**  
[INSERT]


---


### STEP 3: Draft fairness‑enhanced user stories

Based on your findings above, draft your fairness‑enhanced user stories starting with high‑risk features (features with greatest potential for bias or harm) using the User Story Template and User Story Example Library as inspiration.

#### User Story Template


> "As a [user], I want [functionality] so that [benefit], while ensuring [fairness requirement] across [protected groups]."

#### User Story Example Library

Refer to the example library below for domain‑specific samples:

| Domain | Traditional User Story | Fairness Enhanced User Story |
|--------|------------------------|------------------------------|
| Hiring | "As a recruiter, I want résumés categorized by relevant experience so I can efficiently screen candidates." | "As a recruiter, I want résumés categorized by relevant experience so I can efficiently screen candidates, ensuring that experience evaluation works with equivalent accuracy across demographic groups and non‑traditional career paths." |
| Lending | "As a loan officer, I want to see applicants ranked by risk score so I can focus on qualified candidates." | "As a loan officer, I want to see applicants ranked by risk score so I can focus on qualified candidates, ensuring equivalent score distribution across gender, race, and age groups." |
| Content Moderation | "As a content moderator, I want offensive comments automatically flagged so I can review them quickly." | "As a content moderator, I want offensive comments automatically flagged so I can review them quickly, ensuring equivalent flagging rates across content discussing different cultures, identities, and political views." |

#### Intersectional User Story Examples

 Use these examples to address intersectional considerations:

| Protected Groups | Intersectional Consideration | Enhanced User Story |
|------------------|------------------------------|---------------------|
| Gender × Race | Women of color face compounded barriers in hiring | "As a recruiter, I want to rank candidates by leadership potential, ensuring equivalent accuracy for intersectional groups (e.g., women of color, men of color, white women) not just single attributes (gender OR race separately)." |
| Age × Career Gaps | Older workers with caregiving gaps doubly disadvantaged | "As a hiring manager, I want to assess career progression, accounting for the intersection of age and career gaps to avoid penalizing caregivers disproportionately." |
| Geography × Socioeconomic Status | Rural low-income candidates face unique barriers | "As an admissions officer, I want to evaluate academic potential while ensuring equivalent evaluation for rural low-income students who face compounded resource limitations." |

---
### STEP 4: Document in the following format

#### USER STORIES

| Feature | Existing User Story Template | Fairness Enhanced User Story Template |
|--------|------------------------------|---------------------------------------|
| [INSERT] | [INSERT] | [INSERT] |
| [INSERT] | [INSERT] | [INSERT] |
| [INSERT] | [INSERT] | [INSERT] |

---
---

## 1.2 Acceptance Criteria

### STEP 1: Use the FAIR framework

Use the following FAIR framework to develop comprehensive fairness acceptance criteria. There are examples included within the Acceptance Criteria Example Library to guide your choices.

#### FAIR Framework

- **F** = Fairness metrics thresholds – quantitative fairness standards the feature must meet.  
- **A** = Auditing requirements – specific fairness tests that must be performed and documented.  
- **I** = Intersectional analysis – how performance across intersectional groups will be validated.  
- **R** = Reporting guidelines – how fairness results will be documented and communicated.  

#### Acceptance Criteria Example Library

| Element | Criteria |
|---------|----------|
| Fairness Metrics Thresholds | Demographic parity difference below 0.05 across all protected attributes. <br> Equal opportunity difference below 0.03 for all groups. <br> Prediction calibration error differences below 0.04 between any two groups. |
| Auditing Requirements | Dataset representation verified across all protected attributes. <br> Performance disaggregated across all identified demographic groups. <br> Regular bias testing during development. |
| Intersectional Analysis | Performance reported for key intersections (e.g., first‑generation × racial group × geography). <br> Maximum performance disparity of 0.07 between any two intersectional groups. |
| Reporting Guidelines | Comprehensive bias audit documentation before deployment. <br> Disaggregated metrics included in model cards. <br> Clear explanation of remaining disparities with justification. |
| Perspective Documentation | Positionality statement completed documenting team's perspectives and potential blind spots. <br> Stakeholder consultation log shows engagement with affected communities. <br> Decision log documents fairness trade-offs with explicit reasoning. <br> Limitations section identifies which groups/perspectives remain underrepresented in testing. |

**Note:** Vethman et al. (2025) recommend teams "document perspectives and decisions throughout the lifecycle of AI" and "be transparent on your efforts for accountability by transparent communication on any side effects."

---

### STEP 2: Fill out the template below

Provide justifications for each criteria point documented.

#### ACCEPTANCE CRITERIA

| Element | Criteria | Justification |
|---------|----------|---------------|
| Fairness Metrics Thresholds | [INSERT] | [INSERT] |
| Auditing Requirements | [INSERT] | [INSERT] |
| Intersectional Analysis | [INSERT] | [INSERT] |
| Reporting Guidelines | [INSERT] | [INSERT] |
| Perspective Documentation | [INSERT] | [INSERT] |

---

## 1.3 Definition of Done

### Purpose

To ensure fairness verification is a non‑negotiable part of completion, not an afterthought. Fairness must be demonstrably tested, documented, and reviewed before any model or feature is considered "done." This includes mandatory fairness validation steps before deployment.

### STEP 1: Review and identify gaps

Have a look at the table below for inspiration on how you can include fairness in your standard DoD elements. Analyse your current approach and identify any areas that have fairness gaps.

| Standard DoD Element | Fairness Extension |
|----------------------|-------------------|
| Code committed and peer reviewed | Code review includes fairness risk checklists (e.g., bias amplification, data leakage). |
| Unit/integration tests passed | Fairness unit tests run for key models and metrics (e.g., demographic parity, equal opportunity). Extend the definition of done to include disaggregated testing across intersectional subgroups. |
| Documentation updated | Fairness documentation included: bias reports, limitations, and mitigations; counterfactual analysis for high‑stakes decisions. |
| Acceptance criteria met | Fairness acceptance criteria validated and approved by the team. |
| Product Owner sign‑off | PO ensures fairness evidence is presented and logged before sign‑off. A fairness report is shared during each sprint review. |

#### Component-Specific Fairness DoD

Apply these additional criteria based on the ML system component being developed:

**For Data Components:**
- Bias audit using approved metrics (demographic parity, equal opportunity, calibration)
- Data representativeness verified across protected attributes and key intersections
- Data lineage documented (sources, transformations, potential bias introduction points)
- Missing data patterns analyzed by demographic group (is missingness informative?)

**For Model Components:**
- Fairness metrics meet organizational thresholds across test data AND intersectional subgroups
- Model cards include bias testing results, tested/untested groups, limitations
- Counterfactual analysis completed for high-stakes decisions (What if attribute X changed?)
- Fairness-accuracy trade-off explicitly documented and justified

**For UI/UX Components:**
- Diverse user testing (minimum 15 participants across 5 demographic groups)
- Explanation quality validated for non-technical users
- Interface tested for accessibility and cognitive load across education levels
- Override/appeal mechanisms available for automated decisions

### STEP 2: Document your extension

Use the following format to document your extension of fairness to the Definition of Done.

#### DEFINITION OF DONE

**Fairness gaps in standard DoD:**  
[INSERT]

**Fairness extension to DoD elements:**  
[INSERT]

**Component-specific fairness requirements:**  
[INSERT - specify Data/Model/UI/UX component type and applicable criteria]

---

## 1.4 Sprint Backlogs

### STEP 1: Document existing sprint backlog approach

Document the existing sprint backlog approach as a way to identify any fairness gaps.

### STEP 2: Determine capacity allocation

Analyse your application's fairness risk profile and determine an appropriate capacity allocation (**15–30%**) of sprint capacity (for each sprint) to fairness tasks. This will cover fairness analysis, fairness implementation and fairness testing.

**Research Guidance:** Teams typically need:
- 15% capacity: Low-risk features with well-understood fairness requirements
- 20-25% capacity: Medium-risk features or teams building fairness capabilities
- 25-30% capacity: High-risk features affecting protected groups significantly

### STEP 3: Review catalog of fairness tasks

#### Catalog of Fairness Tasks

| Fairness Task | Description |
|---------------|------------|
| Fairness analysis | Data bias audit, model evaluation across groups, intersectional performance testing. |
| Fairness implementation | Bias mitigation implementation, fair feature engineering, fairness constraint application. |
| Fairness testing | Acceptance criteria testing, fairness regression testing, documentation creation. |

### STEP 4: Apply prioritisation framework

Once capacity has been reserved and you have reviewed the catalog of fairness task types, use the following framework for prioritising and determining fairness actions:

- **Fairness Impact** – How significantly a feature could affect different demographic groups.  
- **Bias Risk** – The likelihood of undetected bias entering the system.  
- **Harm Severity** – The potential consequences of biased outcomes.  
- **Regulatory Exposure** – Legal or compliance risks from bias issues.  

### STEP 5: Document in the template below

Fill out the fairness capacity allocation percentage for transparency and accountability, followed by the prioritisation table.

#### SPRINT BACKLOGS

**Fairness capacity allocation:** [INSERT PERCENTAGE]  

**Fairness task:** [INSERT CATEGORY]

**Prioritisation Table**

- **Fairness Impact:** [Select Low / Medium / High]  
- **Bias Risk:** [Select Low / Medium / High]  
- **Harm Severity:** [Select Low / Medium / High]  
- **Regulatory Exposure:** [Select Low / Medium / High]  
- **Overall Status:** [Based on evaluation above, select Low Priority / Medium Priority / High Priority / Non‑Negotiable]

---

# SECTION 2: Ceremony Adaptation

## Purpose

Modifies sprint planning, daily standups, sprint reviews and retrospectives to incorporate fairness discussions. Vethman et al. (2025) emphasize the need to "dedicate time and effort to create a psychologically safe environment" within teams, noting that "conversations between different disciplines are bound to start with misunderstandings and disagreement before common language and shared goals are established." These ceremony modifications create structured opportunities for fairness discussions while building psychological safety.

---

### STEP 1: Identify fairness gaps

Document your existing ceremony approach as a way to identify any fairness gaps. Use the template below to document these fairness gaps.

#### Fairness Challenges

| Challenge Title | Description |
|----------------|-------------|
| [INSERT] | [INSERT] |

---

### STEP 2: Ceremony templates

#### Sprint Planning

**Date:** [INSERT]  

**Fairness Champion:**  
[INSERT NAME] (Note: Consider rotating this role every 2-4 weeks to distribute fairness knowledge across the team)

**Fairness capacity allocation:**  
[INSERT PERCENTAGE]

**Fairness actions to be completed:**  
[INSERT ITEMS]

**Fairness Ground Rules:**
- All bias concerns welcomed; no "obvious" question dismissed
- Disagreement expected and valued as part of the learning process
- Technical and non-technical perspectives equally important
- Focus on systems, not individuals ("the model has bias" not "you created bias")

**Psychological Safety Check:**
- Does anyone have fairness concerns they're hesitant to raise?
- Which demographic groups are we most uncertain about?
- Where do we need outside perspectives or expertise?

---

#### Daily Standup Question Template

**Date:** [INSERT]

| Questions | Response |
|-----------|----------|
| What fairness-related work did I complete yesterday? | [Team member response] |
| What fairness blockers or data issues do I see today? | [Team member response] |
| Are there fairness metrics or tests that need review? | [Team member response] |

**Note:** Keep fairness discussions brief (2-3 minutes). Detailed fairness investigations should be scheduled separately.

---

#### Sprint Review

**Date:** [INSERT]

**Fairness metrics (across demographic groups and their intersections):**  
- [INSERT]  
- [INSERT]

**Unresolved fairness issues:**  
[INSERT]

**Fairness validation gate:** Feature does NOT proceed to "Done" unless all fairness acceptance criteria are met. If fairness thresholds are not met, the feature returns to the backlog for remediation.

---

#### Retrospective Question Template

**Date:** [INSERT]

| Fairness-related Questions | Response | Purpose |
|----------------------------|----------|---------|
| Where did we detect bias earliest and how? | [Team member response] | Celebrate successes, identify effective practices |
| Where did we miss potential fairness problems (in particular for demographic groups and their intersections)? | [Team member response] | Learn from gaps without blame |
| What fairness metrics regressed? | [Team member response] | Track fairness as ongoing concern, not one-time fix |
| What fairness documentation proved most useful? | [Team member response] | Reinforce valuable practices |
| What fairness concern did we hesitate to raise? | [Team member response] | **Assess psychological safety** |
| Which community perspectives are we missing? | [Team member response] | **Identify blind spots** |
| What fairness trade-offs did we make and why? | [Team member response] | **Build institutional memory** |
| How can we improve for the next sprint? | [Team member response] | Continuous improvement |

---

### STEP 3: Refinement template

Complete this template after each sprint in order to refine and improve the approach above. The justification column provides a trace of decision‑making and transparency.

#### REFINEMENT

**Date:** [INSERT]

| Scrum Stage | Fairness Gaps | Fairness Touchpoints | Justification |
|-------------|---------------|----------------------|--------------|
| Sprint Planning | | | |
| Daily Standup | | | |
| Sprint Review | | | |
| Retrospective | | | |

---

## REFERENCES

Crenshaw, K. (1989). Demarginalizing the intersection of race and sex: A black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. *University of Chicago Legal Forum*, 1989(1), 139–167. https://chicagounbound.uchicago.edu/uclf/vol1989/iss1/8  

Holstein, K., Wortman Vaughan, J., Daumé III, H., Dudik, M., & Wallach, H. (2019). Improving fairness in machine learning systems: What do industry practitioners need? In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). https://doi.org/10.1145/3290605.3300830  

Hutchinson, B., et al. (2022). Towards accountability for machine learning datasets: Practices from software engineering and infrastructure. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 560–575). https://doi.org/10.1145/3531146.3533157  

Madaio, M. A., Stark, L., Wortman Vaughan, J., & Wallach, H. (2020). Co‑designing checklists to understand organizational challenges and opportunities around fairness in AI. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–14). https://doi.org/10.1145/3313831.3376445  

Martinez-Fernandez, S., et al. (2022). Software engineering for AI-based systems: A survey. *ACM Transactions on Software Engineering and Methodology*, 31(2), 1–59. https://doi.org/10.1145/3487043  

Raji, I. D., et al. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 33–44). https://doi.org/10.1145/3351095.3372873  

Rakova, B., Yang, J., Cramer, H., & Chowdhury, R. (2021). Where responsible AI meets reality: Practitioner perspectives on enablers for shifting organizational practices. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), 1–23. https://doi.org/10.1145/3449081  

Richardson, S., Bennett, M., & Denton, E. (2021). Documentation for fairness: A framework to support enterprise-wide fair ML practice. In *Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 1003–1012). https://doi.org/10.1145/3461702.3462553  

Suresh, H., et al. (2022). Towards intersectional feminist and participatory ML: A case study in supporting feminicide counterdata collection. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 667–678). https://doi.org/10.1145/3531146.3533132  

Veale, M., Van Kleek, M., & Binns, R. (2018). Fairness and accountability design needs for algorithmic support in high-stakes public sector decision-making. In *Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems* (pp. 1–14). https://doi.org/10.1145/3173574.3174014  

Vethman, S., Smit, Q. T. S., van Liebergen, N. M., & Veenman, C. J. (2025). Fairness beyond the Algorithmic Frame: Actionable Recommendations for an Intersectional Approach. *ACM Conference on Fairness, Accountability, and Transparency (FAccT '25)*.  























