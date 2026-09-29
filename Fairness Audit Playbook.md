# FAIRNESS AUDIT PLAYBOOK

## PROBLEM STATEMENT

**Problem:** Companies increasingly use multiple AI systems across different teams and these systems now influence important decisions in areas such as hiring, operations, sales and legal. However, there is no structured and centralised process to evaluate whether these AI systems are fair. This inconsistency has already resulted in AI systems raising concerns related to discrimination, bias, reputational harm and potential legal exposure.

**Solution:** This Fairness Audit Playbook ("playbook") provides a standardised framework that engineering teams can use independently (with expert support only for complex cases) to systematically evaluate both existing and future AI systems, including third-party AI APIs.

## PLAYBOOK OVERVIEW

**Core components to uncover unfairness in your AI projects:**

1. Historical Content Assessment Tool: Identify historical patterns that may influence the fairness of the AI system.
2. Fairness Definition Selection Tool: Choose an appropriate definition of fairness based on the AI system.
3. Bias Source Identification: Determine where bias may be introduced and amplified through the AI development lifecycle.
4. Comprehensive Metrics: Assess the AI system's chosen metrics.
5. Fairness Audit Report: Compile the findings of all steps above.

**Implementation Guide:** Explain how to effectively use the playbook and apply this playbook across different domains and problem types.

**Validation Checklist:** Provide a checklist to ensure all key steps have been addressed before proceeding to deployment.

**Case Study:** Demonstrate how to apply the playbook using an AI-loan approval system as an example.

**Playbook Improvements:** Identify future improvements to this playbook itself.

---

## 1. CORE COMPONENTS

The playbook follows a sequential workflow where each component builds on the previous:

- Step 1 → Step 2: Historical patterns inform which fairness definitions are most relevant
- Step 2 → Step 3: Selected fairness definitions guide where to look for bias sources
- Step 3 → Step 4: Identified bias sources determine which metrics to calculate
- All Steps → Step 5: All findings integrate into comprehensive audit report

### STEP 1: HISTORICAL CONTEXT ASSESSMENT TOOL

#### INTRODUCTION

The Historical Context Assessment Tool is the first component of the Fairness Audit Playbook, guiding teams to identify domain-specific patterns of past discrimination and understand how they may resurface across the AI development lifecycle. By grounding the audit in historical insight, it enables engineering teams to anticipate and mitigate fairness risks before they materialise and directly inform the selection of appropriate fairness definitions in the next stage of the playbook.

#### RESEARCH

Firstly, start gathering historical information specific to your AI project domain by reviewing reputable and relevant literature, legal cases, regulatory guidance and perspectives from different demographic groups and their intersections across a wide time period. This background research will help you to answer the questionnaire below. Make sure to document your answers to these questions.

#### QUESTIONNAIRE

**Purpose of your AI project**
- What is the AI project designed to do?
- What decision or outcome does this AI project influence?
- How have similar decisions historically been made in this domain?

**Affected populations**
- Which demographic groups are impacted by decisions in this domain?
- Which groups or intersections of these groups have historically experienced disadvantage or exclusion?
- Are there documented cases of discrimination affecting these groups, or their intersections (e.g. disabled Muslim women)?

**Data Representation**
- What types of data have historically been used to make decisions in this domain?
- Have these data sources been influenced by discriminatory collection practices or institutional biases?
- Have certain groups been historically underrepresented during data collection?
- Have any features acted as proxies for sensitive protective attributes (e.g. race, gender)?
- Are there any missing data points on certain groups and intersections of groups?

**Variable Selection and Feature Engineering**
- Historically, which variables or attributes have been used to make decisions in this domain?
- Have any of these variables historically acted as proxies for protected characteristics?
- Have numerical representations of sensitive attributes historically oversimplified or distorted the lived experiences of affected communities?

**Algorithm selection**
- Historically, what kinds of models or algorithms have been used in this domain?
- Have these historical approaches disproportionately categorised certain groups in harmful ways?
- Have previous systems applied parameters or thresholds that resulted in disparities?

**Evaluation Framework**
- What evaluation metrics have historically been used in this domain?
- Are there any historical disparities which arise when using these metrics across demographic groups or intersections of groups?
- Have researchers criticised any of these metrics for failing to capture fairness-specific harms?

**Deployment Context**
- What historical biases or discrimination exist within the domain where your AI project will be deployed?
- Have past technologies in this domain produced harmful feedback loops that reinforced inequality?
- Historically, have monitoring systems failed to detect or prevent biased outcomes and if so, how?
- Are there past examples where user behaviour produced unequal access for certain groups?
- Are there any historical biases emerging from how past technologies are integrated with other systems?
- Are there any fairness/ discrimination-related legal requirements historically that have impacted your domain?

#### RISK CLASSIFICATION MATRIX

Next, use a risk classification matrix to categorise each identified historical pattern above by:

**Severity:** How harmful would this be if it occurred?
- **High:** Directly impacts fundamental rights or life outcomes.
- **Medium:** Creates significant disparities in opportunities or resources.
- **Low:** Creates differential experiences but with limited material impact.

**Likelihood:** How likely is this bias to occur?
- **High:** Pattern frequently appears in similar systems.
- **Medium:** Pattern occasionally appears in similar systems.
- **Low:** Pattern rarely appears in similar systems.

**Relevance:** How relevant is this harm to your AI project?
- **High:** Direct applicability to the system's domain/purpose.
- **Medium:** Partial applicability to certain system components.
- **Low:** Limited applicability but potential for manifestation.

#### FINDINGS

Create a report to note down the top priority key findings from answering the questions above and the risk classification. You can use the case study as inspiration for how to structure this. This report will feed directly into the Fairness Definition Selection Tool (Step 2).

---

### STEP 2: FAIRNESS DEFINITION SELECTION TOOL

#### INTRODUCTION

This Fairness Definition Selection Tool is the second component of the Fairness Audit Playbook. Its purpose is to assist you in documenting and selecting appropriate context-specific definitions of fairness based on the historical insights uncovered during Step 1 (Historical Context Assessment Tool). Please begin by answering the questions in the decision tree below (after the Fairness Definitions for your reference).

#### FAIRNESS DEFINITIONS

##### GROUP FAIRNESS METRICS

The following group fairness metrics are the most widely implemented fairness metrics across industries focusing on ensuring similar error rates or prediction distributions across demographic groups, just like how hygiene standards must be maintained in all restaurants, regardless of neighbourhood.

**1) Demographic Parity**

**Formulation**
```
P(Ŷ=1|A=a) = P(Ŷ=1|A=b)
```

**Explanation**
The probability of receiving a positive outcome must be identical across all demographic groups, regardless of qualifications. This ensures representation, regardless of qualification. E.g. If 10% of white applicants get hired, 10% of Black applicants should also get hired. This metric is especially used in regulated domains like lending or hiring.

**Limitations**
This is in direct conflict with individual fairness metrics. This requires lowering standards for some groups and ignores qualifications. Reject this metric if your focus is on merit-based principles.

**Applicability**
If there are any excluded or underrepresented groups showing up in historical analysis (Step 1). When all groups must have equal access to opportunities. E.g. a university outreach algorithm that displays career advertisements to different gender groups at equal rates to counteract historical underrepresentation.

**2) Equal Opportunity**

**Formulation**
```
P(Ŷ=1|Y=1,A=a) = P(Ŷ=1|Y=1,A=b)
```

**Explanation**
Ensures qualified individuals have equal chances of receiving positive outcomes across groups. For everyone who truly deserves to succeed (Y=1), the probability they are selected should be the same for all groups.

**Limitations**
Does not address false positive disparities; depends on trustworthy labels that may themselves contain historical bias.

**Applicability**
When you need to ensure that all qualified candidates have an equal chance (false negatives are more concerning than false positives). E.g. A medical screening tool ensures that patients with a particular condition have the same probability of being correctly identified regardless of race or socioeconomic status. Another example would be a scholarship eligibility model where missing qualified applicants is worse than awarding a few extra grants.

**3) Equalised Odds**

**Formulation**
```
P(Ŷ=1|Y=y,A=a) = P(Ŷ=1|Y=y,A=b) for y ∈ {0,1}
```

**Explanation**
All groups have equal rates of both correct positive and correct negative decisions (extension to Equal Opportunity). Prevents both types of errors from disproportionately affecting certain groups.

**Limitations**
More complex to implement; may reduce overall performance.

**Applicability**
High-stakes decisions where both types of errors (false positives and false negatives) matter. E.g. a recidivism prediction system where both wrongly detaining non-recidivating individuals and mistakenly releasing recidivating individuals have serious consequences that must be equitably distributed. Another example of use case would be a loan approval model where both granting loans to bad applicants and denying loans to good applicants are costly.

**4) Predictive Parity**

**Formulation**
```
P(Y=1 | Ŷ=1, A=a) = P(Y=1 | Ŷ=1, A=b)
```

**Explanation**
Predictions should have the same meaning across all groups; e.g., if AI says "80% chance," it is correct 80% of the time for everyone.

**Limitations**
Can conflict with equal error rates if base rates differ; may allow unequal treatment if calibrated correctly.

**Applicability**
If false positives are more harmful, make this a mandatory definition and any context where consistency of prediction meaning is critical, e.g. this is a good metric for when end-users see model scores directly. An example use case would be to protect against approving unqualified people (approving false positives), like a security screening tool where wrongly flagging people creates major inconvenience and reputational harm and end-users see predictions directly.

##### INDIVIDUAL FAIRNESS METRICS

The following individual fairness metrics evaluate whether an AI system treats similar individuals similarly, regardless of which demographic group they sit with in society. This is like a manager evaluating employees based on a standardised performance criteria.

**1) Individual Fairness**

**Formulation**
```
d_Y(\hat{Y}(x_i), \hat{Y}(x_j)) \leq L \cdot d_X(x_i, x_j)
```

**Explanation**
Two people with comparable qualifications or profiles should get similar outcomes, regardless of demographic group membership or protected attributes (e.g. race or gender).

**Limitations**
This is in direct conflict with group fairness metrics like demographic parity. Requires defining a "similarity metric"; can be difficult in practice. This metric must capture which features should be considered for determining similarity while being blind to protected attributes. It is important here to capture these attributes for intersectional analysis.

**Applicability**
In scenarios where treating individuals based on their unique profiles as opposed to their standing in society, is ethically appropriate. E.g. a medical triage system where two patients with nearly identical symptoms should get the same risk score, regardless of demographic differences.

**2) Counterfactual Fairness**

**Formulation**
```
P(\hat{Y}{A \leftarrow a}(U) = y | X = x, A = a) = P(\hat{Y}{A \leftarrow a'}(U) = y | X = x, A = a
```

**Explanation**
Combines individual and group fairness by considering predictions would change if protected attributes were different. Addresses the question: "Would this person receive the same treatment if they belonged to a different demographic group, all else being equal?".

**Limitations**
Again, the challenge is defining the appropriate similarity metrics as it requires domain knowledge and ethical reasoning. This is more complex than the others.

**Applicability**
When you need to account for causal relationships involving both individual and group fairness. This is especially useful in cases where certain laws require consideration of protected attributes.

#### QUESTIONNAIRE

The following questions aim to map fairness notions in the different stages of AI lifecycle to guide you to selecting the most appropriate Fairness Definition (listed above for ease of reference). Make sure to document your answers to these questions. I have offered a decision tree in some areas to guide you to the most appropriate fairness definitions, but it is up to you to weigh up all relevant factors and trade-offs when selecting them.

**Historical Context**
- Based on the Historical Context Assessment above (Step 1), are there any under-represented or excluded groups and their intersections?
  - If yes → Demographic Parity

**Purpose of your AI project**
- Which concept(s) of fairness (above) best aligns with the intended business purpose and ethical requirements of your AI system?
  - If false negatives are more harmful → Equal Opportunity
  - If false positive are more harmful → Predictive Parity
  - If both false positives and false negatives are harmful → Equalised Odds
- Is it important to give the same treatment to individuals regardless of their demographic groups?
  - If yes → Individual Fairness or Counterfactual Fairness

**Data Representation/ Variable Selection**
- Which concept of fairness determines the selection of variables in your AI project?
- Which definition of fairness determines how these variables should be encoded?

**Algorithm selection**
- Depending on the concept of fairness selected, what are the necessary pre-processing, in-processing and post-processing steps to follow?

**Evaluation Framework**
- What is your primary concern concerning fairness?
- Based on the above answer, how should different fairness measures be weighted?
- Are there any domain-specific thresholds providing concrete benchmarks for identifying problematic disparities? If not, what is an acceptable threshold of level of disparity for each fairness measure selected?

**Deployment Context**
- Will the AI system expose scores to users?
  - If yes → Predictive Parity

**Legal Context**
- In which country/countries will your AI system be launched/integrated?
- Which jurisdiction will your AI System operate in?
- Are there any fairness-related legal/compliance requirements related to your domain that must be abided by? (e.g. consider GDPR "special categories of personal data", UK Equality Act, Equal Credit Opportunity Act (ECOA), EU AI Act depending on your jurisdiction etc).
  - If yes → implement the strictest applicable standards.

**Intersectional Considerations**
- Which intersectional groups require specific fairness definitions?
- Do different intersections need different fairness priorities?
- Are there conflicts between fairness definitions when examining intersections?

**Trade-Off Analysis**
- Considering the trade-offs of each fairness measure, why have you selected some as primary metrics over others? Which fairness definitions are the most critical for your specific AI system?
- Based on the response above, what combination of non-competing Fairness definitions came up in your analysis?

#### FINDINGS

Produce a report using the table format below, specifying the chosen fairness definition, the rationale for their selection as expressed below (considering your responses to the decision tree above) and the level/rationale of priority for each metric (multiple fairness criteria cannot be simultaneously satisfied, you need to prioritise). You may also use the case study as additional inspiration on how to set out this report. This will directly feed into the Bias Source Identification Tool next (Step 3).

| Selected Fairness Definitions | Reasoning (consider historical context, business goals and stakeholder priorities) | Priority Level | Prioritisation Rationale |
|------------------------------|----------------------------------------------------------------------------------|----------------|--------------------------|
| e.g. Demographic Parity | Historical Context: Historical data show differential standardised test score distributions across racial and socioeconomic groups, reflecting systemic educational inequities rather than differences in student potential.<br><br>Business Goals: Primary goal is to ensure similar admission rates across groups regardless of score distributions.<br><br>Stakeholder Priorities: Leadership emphasizes finding the best candidates regardless of background. | e.g. primary metric/ secondary metrics (choose one) | e.g focusing on group fairness is more priority than treating similar individuals. |

---

### STEP 3: BIAS SOURCE IDENTIFICATION TOOL

#### INTRODUCTION

This Bias Source Identification Tool is the third component of the playbook with a purpose of pinpointing where bias may be introduced or amplified throughout the AI development lifecycle, from historical context to data collection and model deployment.

#### BIAS CATEGORISATION AND DETECTION METHOD OVERVIEW

To begin identifying potential sources of bias, review the taxonomy below. This taxonomy provides clear definitions, examples, and detection methods that will help you identify where each type of bias may occur in your system. Understanding these categories will also support you in answering the questionnaire that follows.

| Bias Category | Explanation | Detection Method |
|--------------|------------|------------------|
| Historical Bias | Bias resulting from pre-existing social inequities. For example, a hiring algorithm trained on historical hiring decisions may perpetuate patterns of gender discrimination in technical roles. | Extract documented discrimination patterns from the Historical Context Assessment results.<br>Compare outcome distributions across groups identified as high-risk<br>Analyse correlations between system predictions and historical patterns. |
| Representation Bias | Bias arising from who appears in the data, who is missing, and who is underrepresented. Watch out for indicators like demographic imbalances compared to the target population. For example, a medical diagnostic system trained primarily on data from young adult males may perform poorly for elderly female patients. | Document how samples were selected and the geographic, temporal and contextual factors that influenced data collection.<br>Compare demographic groups and their intersections identified as historically underrepresented with appropriate benchmarks (Step 1).<br>Based on the above, calculate representation ratios and statistical significance of disparities. |
| Feature Selection and Pre-processing Bias | Bias arising from how attributes are selected, pre-processed, encoded and the metrics chosen to measure them. For example, using standardised test scores as a proxy for aptitude may disadvantage groups with less access to test preparation resources. | Identify potential proxies for protected attributes that might enable indirect discrimination.<br>Review normalisation, encoding and imputation procedures for potential disparate impacts.<br>Analyse how missing data patterns vary across groups. |
| Model/Algorithm Bias | Bias arising from modeling choices that amplify or create disparities, e.g. algorithms that overfit majority patterns and regularization approaches that penalise minority patterns. Specifically, linear models assume relationships between features and tree-based methods segment the feature space in ways that may create splits for underrepresented groups with fewer samples. | Calculate performance disparities across demographic groups for different model architectures using identical training data.<br>Test regularisation effects on minority group performance.<br>Decompose performance metrics by demographic group to identify disparate optimisation patterns.<br>Establish acceptable disparity thresholds based on domain-specific requirements. Then, compare disparities before and after architecture modifications. |
| Evaluation Framework Bias | Bias arising from testing procedures and metrics that don't represent real-world performance or fairness. For example, evaluating a facial recognition system on a test set that doesn't include diverse skin tones will mask potential performance disparities in deployment. | Evaluate the chosen evaluation metrics and whether performance is on specific sub-groups or only in aggregate.<br>Examine performance of these metrics across both protected attributes and their intersections. |
| Deployment Bias | Bias arising from how systems are implemented and used in practice. For example, a recommendation system might create filter bubbles that limit exposure to diversity based on initial demographic patterns. | Set up a monitoring system to identify adaptation patterns across different user groups and their intersections.<br>Implement A/B testing to compare system versions with different feedback intervention strategies like strategic randomisation. |

#### QUESTIONNAIRE

The following questions help you trace bias sources across the full AI lifecycle. Each subsection corresponds to the bias categories above, guiding you to evaluate whether and where bias may emerge. Make sure to document your answers to these questions.

**Historical Bias**
- How might biases identified in the historical context and the chosen fairness definitions manifest in specific bias sources in the AI system?
- Which demographic groups and their intersections are most at risk of being unfairly impacted?

**Representation Bias**
- How was the data collected?
- Are there any missing or imbalanced groups in the data?
- Are the labels in the data biased or reflective of societal prejudices?
- Depending on the outcome of Step 2, are demographic groups and/or individuals being treated consistently according to the selected fairness definitions?

**Feature Selection and Pre-processing Bias**
- Are features selected or engineered in a way that discriminates against certain groups?
- Are encoding, normalisation or imputation decisions differentially harmful across demographic groups and their intersections?

**Model/Algorithm Bias**
- How may the model set-up and training process introduce bias?
- Does the choice of algorithm/model disadvantage certain groups and their intersections?
- What is the purpose for optimisation?
- How may your definition of loss function introduce bias?
- How may your choice of regularisation technique introduce bias?
- Are hyperparameters tuned in a way that leads to unfair outcomes for specific groups?

**Evaluation Framework Bias**
- Does the test data match the feature and demographic distribution of training data?
- Are underrepresented groups represented in the test data?
- Does the choice of evaluation metrics highlight fairness issues based on what aspects of performance they measure?

**Deployment Bias**
- What human biases could influence the use of the model's outputs?
- Does input data distributions change over time in response to system outputs? Do these shifts differ across demographic groups and their intersections?
- Does your choice of interface introduce any bias for certain demographic groups and their intersections?
- How might infrastructure and resource disparities within the deployment environment influence the fairness of your model's outcomes?
- How do your organisational workflows and decision processes interact with system outputs? Do they introduce bias for outcomes of different groups?

**Intersectional Bias Analysis**
- Which intersectional groups face unique bias sources not captured by single-attribute analysis?
- Are there bias sources that disproportionately affect specific intersections?

#### PRIORITY MATRIX

Next, use a priority framework to categorise each identified bias above by:

**Severity:** How harmful is this if the bias source remains unaddressed?
- **High:** Directly impacts fundamental rights or life outcomes.
- **Medium:** Creates significant disparities in opportunities, access or resources.
- **Low:** Creates differential experiences but with limited material impact.

**Scope:** How many users or decisions does this bias affect?
- **High:** Most or all user groups
- **Medium:** A moderate subset
- **Low:** A narrow or isolated group

**Persistence:** How likely is it that the bias compounds over time through feedback loops?
- **High:** Highly self-reinforcing
- **Medium:** May recur depending on context
- **Low:** Unlikely to persist

**Historical:** Does this bias reinforce historical patterns identified in Step 1?
- **High:** strongly linked to documented historical inequities
- **Medium:** Moderately linked
- **Low:** Weak or no connection

**Intervention:** How easy it is to detect and mitigate this bias?
- **High:** Easy to remedy at a low cost.
- **Medium:** Relatively reasonable cost of detection and remediation.
- **Low:** Extremely hard and expensive to detect and remedy.

Note down your findings in the following format:

| Bias Type | Severity | Scope | Persistence | Historical | Intervention | Overall Priority Level |
|-----------|----------|-------|-------------|------------|--------------|----------------------|
| E.g. Historical bias | E.g. High | E.g Medium | E.g. High | E.g. High | E.g. Medium | E.g. High |

Once you assign a Priority Level to each bias source, this score should be carried forward into the Findings Report below.

#### FINDINGS

Produce a report mapping the key potential biases across the AI lifecycle to specific groups and their intersections. Include the Priority Level generated in the Priority Matrix above, so the report clearly communicates which bias sources require urgent attention. This report will directly inform the selection of the Comprehensive Metrics (STEP 4).

| Bias Type | Description | Detection Evidence | Priority Level |
|-----------|-------------|---------------------|----------------|
| E.g. Representation Bias | E.g. Underrepresentation of older female applicants | E.g. Demographic imbalance ratios | E.g. High |

---

### STEP 4: COMPREHENSIVE METRICS

#### INTRODUCTION

This step assists you in selecting, calculating and communicating the most appropriate fairness metrics for your AI system, using inputs from Step 2 (Fairness Definition Selection) and Step 3 (Bias Source Identification).

#### WORKFLOW

**1. Metric Selection**
- Identify problem type (Classification/Regression/Ranking)
- Review selected fairness definitions from Step 2
- Select relevant metrics using tables below
- Determine harm direction (false positives vs false negatives) to prioritise metrics
- Document selected metrics and rationale

**2. Implementation Planning**
- Identify protected attributes and intersections to evaluate
- Assess sample sizes for each subgroup
- Determine statistical validation approach (bootstrap for large groups, Bayesian for small groups)
- Plan visualization format

**3. Calculation & Validation**
- Calculate metrics for all groups and intersections
- Compute confidence/credible intervals based on sample sizes
- Perform statistical significance testing with multiple comparison correction
- Conduct robustness checks across data splits
- Detect Simpson's Paradox through intersectional analysis

**4. Analysis & Reporting**
- Compare metrics against Step 2 thresholds
- Identify violated fairness definitions
- Prioritize disparities by magnitude, significance, and impact
- Create visualizations with uncertainty intervals
- Document limitations and actionable recommendations

#### METRIC SELECTION TABLES

**Classification Metrics**

| Fairness Definition | Suggested Metric | Explanation |
|---------------------|------------------|-------------|
| Demographic Parity | Positive Prediction Rate Difference/Ratio | Measures positive outcome rate differences across groups |
| Equal Opportunity | True Positive Rate (TPR) Difference/Ratio | Ensures qualified individuals are treated equally |
| Equalised Odds | TPR Difference/Ratio, FPR Difference/Ratio | Balances both false positives and false negatives |
| Predictive Parity | Positive Predictive Value (PPV) Difference/Ratio | Ensures predictions have equal meaning across groups |
| Individual Fairness | Lipschitz Consistency / Similarity-based Gap | Similar individuals get similar predictions |
| Counterfactual Fairness | Counterfactual prediction deviation | Whether predictions change when protected attributes change |
| Intersectional Fairness | All above metrics calculated across intersections | Reveals disparities hidden in aggregate |

**Regression Metrics**

| Fairness Goal | Suggested Metric | Explanation |
|---------------|------------------|-------------|
| Statistical Parity | Group outcome difference | Compares average predicted value across groups |
| Bounded Group Loss | MAE/MSE per group, Maximum Group Loss, Group Error Ratio | Checks whether some groups suffer higher error |
| Individual Fairness | Individual Consistency, Input–Output Sensitivity | Similar profiles should receive similar scores |

**Ranking Metrics**

| Fairness Goal | Suggested Metric | Explanation |
|---------------|------------------|-------------|
| Exposure Parity | Exposure Ratio, NDCG Difference across groups | Checks whether ranking exposure is fairly distributed |
| Representation Parity | Group Representation Ratio in top-k, Top-k Proportion Diff | Compares how often groups appear in top-k slots |
| Individual Fairness | Rank-Consistency Score, Similar-Item Rank Distance | Similar items should not be systematically pushed down |

**Important Note:** Multiple fairness metrics cannot always be simultaneously satisfied. Select metrics based on application context, measure multiple metrics to understand trade-offs, and document prioritization rationale.

#### KEY DECISIONS

**Harm Direction**
- **False positives more harmful** → Prioritize FPR Difference and PPV Difference
- **False negatives more harmful** → Prioritize FNR and TPR Difference  
- **Both harmful** → Use Equalised Odds and track both TPR and FPR differences

**Similarity Design** (for Individual & Counterfactual Fairness)
- What features define task-relevant similarity?
- What similarity metric will you use (e.g., learned embeddings, weighted Euclidean)?
- Will protected attributes be excluded from similarity calculation?
- How will you validate similarity consistency?

**Intersectional Analysis**
- Calculate metrics for all relevant intersections
- Compare to single-attribute baselines to detect Simpson's Paradox
- Set minimum sample size threshold (e.g., n ≥ 30) for reliable results
- Flag high-uncertainty results explicitly

**Data Partitioning**
- List all protected attributes and intersections to evaluate
- Assess sample sizes: Are they sufficient for each subgroup?
- For small groups: Use Bayesian methods or flag as exploratory
- For individual/counterfactual fairness: Define how pairs or counterfactual variants will be constructed

#### STATISTICAL VALIDATION

**Confidence/Credible Intervals**
- **Large groups (n > 100):** Bootstrap confidence intervals
- **Small groups (n < 100):** Bayesian credible intervals
- **Very small groups:** Flag as exploratory, document uncertainty explicitly

**Significance Testing**
- Perform appropriate statistical tests (null hypothesis: no disparity)
- Apply multiple comparison correction when evaluating multiple groups
- Distinguish statistically significant disparities from random variation

**Robustness Checks**
- Calculate metrics across different data splits (e.g., k=5 cross-validation)
- Test sensitivity to varying thresholds or model parameters
- Evaluate stability: Are disparities consistent across splits?

**Edge Cases**
- Groups with zero positive examples require special handling
- Consider aggregation strategies for very small intersectional groups while maintaining transparency

#### REPORTING REQUIREMENTS

Create visualizations and reports using these standardised templates to ensure fairness metrics are communicated clearly and consistently.

**System Fairness Disparity Chart**
- Bar chart showing primary metrics across groups with confidence/credible intervals
- Color-coding indicating statistical significance (e.g., red = significant violation, yellow = borderline, green = acceptable)
- Reference lines for acceptable thresholds from Step 2
- Include both point estimates and uncertainty intervals

**Intersectional Heatmap**
- Heatmap showing metric values across all intersectional groups
- Color gradient indicating magnitude of disparities (e.g., darker = larger disparity)
- Cell size or opacity indicating sample size (larger/opaque = more reliable)
- Include annotations for small sample sizes or high uncertainty

**Disparity Summary Table**
- Tabular format with columns: Group/Intersection, Metric Value, Confidence Interval, Threshold, Status (Pass/Fail/Uncertain)
- Sort by magnitude of disparity or priority level
- Include sample sizes and statistical significance flags

#### FINDINGS

Produce a report documenting:
- All calculated fairness metrics with statistical validation
- Comparison against Step 2 thresholds
- Identification of violated fairness definitions
- Intersectional analysis findings (including Simpson's Paradox detection)
- Prioritised recommendations linked to Step 3 bias sources

This report will form part of the overall Fairness Audit Report (Step 5). Use the case study as inspiration for structure.

---

### STEP 5: FAIRNESS AUDIT REPORT

The final stage is now to compile all the reports of the 4 previous steps and create an overall Fairness Audit Report.

---

## 2. IMPLEMENTATION GUIDE

This guide explains how to effectively use the Fairness Audit Playbook within your team's development lifecycle.

### Key Decision Points 

**Decision Point 1: Which historical patterns are most relevant?**
- **Evidence needed:** Academic literature, regulatory reports, documented discrimination cases
- **Risk if skipped:** Missing critical bias sources that manifest later

**Decision Point 2: Which fairness definition to prioritise?**
- **Evidence needed:** Analysis (false positives vs false negatives), legal requirements, stakeholder priorities
- **Risk if skipped:** Optimising for wrong fairness goal, potential legal non-compliance

**Decision Point 3: Which bias sources require immediate attention?**
- **Evidence needed:** Priority matrix scores, historical connection strength, potential impact
- **Risk if skipped:** Wasting resources on low-priority issues while high-risk biases persist

**Decision Point 4: Which fairness metrics should be calculated?**
- **Evidence needed:** Selected fairness definitions (from Step 2), problem type (classification/regression/ranking), identified bias sources (from Step 3), sample sizes for subgroups
- **Risk if skipped:** Calculating wrong metrics wastes computational resources; missing critical metrics means fairness issues go undetected; choosing metrics incompatible with fairness definitions leads to misleading conclusions

**Decision Point 5: What disparity thresholds are acceptable?**
- **Evidence needed:** Domain-specific benchmarks, regulatory guidance, statistical significance
- **Risk if skipped:** Either over-reacting to noise or missing real disparities

### Expertise & Time Requirements

**Required expertise:** ML engineers, domain experts, legal/compliance and stakeholders representing affected communities

**Typical timelines:**
- Moderate-risk systems: 2 - 4 weeks
- Complex / regulated systems: 4+ weeks

### Integration with Existing Development Processes

| Development Stage | Relevant Playbook Component | Purpose in Workflow |
|------------------|----------------------------|---------------------|
| Problem Framing | Historical Context Assessment | Identify past and ongoing inequities, define sensitive and intersectional groups, understand domain harm patterns. |
| Data Collection & Preparation | Historical Context Assessment + Bias Source Identification | Ensure sampling, labelling and feature engineering do not reproduce historical or structural harms; document high-risk bias sources early. |
| Model Design & Development | Fairness Definition Selection + Bias Source Identification | Select fairness definitions that align with domain priorities and legal risks; review modelling choices for potential bias pathways. |
| Pre-Deployment Evaluation | Comprehensive Metrics (Fairness Metrics Tool) | Calculate fairness metrics, including intersectional metrics; apply statistical validation and robustness testing; determine whether fairness definitions are met. |
| Deployment Governance | Fairness Audit Report | Combine all findings (context, definitions, bias sources, metrics) into a single audit; present risks and mitigation options to leadership and risk/compliance. |
| Post-Deployment Monitoring | Comprehensive Metrics (re-run periodically) | Track fairness drift, emerging disparities, and new risks; integrate into ongoing model monitoring processes. |

### Intersectionality Requirements

Intersectional fairness must be assessed at every step:
- **Step 1:** Identify historically marginalised intersections.
- **Step 2:** Select fairness definitions capable of revealing intersectional harms.
- **Step 3:** Flag bias sources that disproportionately affect particular intersections.
- **Step 4:** Calculate intersectional metrics and mark any small-sample results as uncertain.

### Adaptability Across Domains & Problem Types

This playbook is designed to be domain-agnostic, but teams must make a few domain and problem-specific choices.

**Domain-specific priorities (examples):**
- **Healthcare:** Prioritise **Equal Opportunity** and related recall/TPR metrics (missing true cases is most harmful). Carefully examine historical under-treatment of specific groups.
- **Finance:** Combine **Equal Opportunity** (avoiding exclusion of qualified applicants) with **Predictive Parity** (approved loans having comparable default risk across groups). Pay particular attention to variables that may act as proxies for protected attributes (e.g. ZIP code).
- **Hiring:** Emphasise **Equal Opportunity** and **intersectional representation** (e.g. selection rates across race × gender). Monitor both selection rates and error rates across intersections.

**Adaptation by problem type:**
- **Classification:** Use group and intersection-level metrics such as TPR/FNR/FPR, PPV and disparity measures (differences/ratios) aligned with the chosen fairness definitions.
- **Regression:** Focus on group error metrics (MAE/MSE per group, maximum group loss, error ratios) and, where relevant, group outcome differences (e.g. average predicted score by group).
- **Ranking:** Use exposure-based metrics (e.g. exposure ratio, NDCG differences) and representation metrics (e.g. proportion in top-k) across groups and key intersections to detect unfair visibility or opportunity.

Domain experts should always set thresholds.

### How the Playbook Can Be Improved Over Time

Teams should note:
- Missing or outdated metrics
- New regulatory requirements
- Intersectional gaps due to limited data
- Steps that were unclear or too heavy
- Where domain-specific templates are needed

---

## 3. VALIDATION CHECKLIST

Please review your Fairness Audit Report and ensure that the following points have been met to validate its effectiveness:

**Completeness Check**
- [ ] All five components completed with documented outputs
- [ ] Intersectional analysis conducted at each step
- [ ] All questionnaires answered with evidence

**Quality Assessment**
- [ ] Historical patterns verified against reputable sources
- [ ] Fairness definitions justified with clear rationale
- [ ] Bias sources mapped to specific system components
- [ ] Metrics validated with appropriate statistical methods

**Actionability Review**
- [ ] Findings translate to concrete technical recommendations
- [ ] Priorities clearly communicated to stakeholders
- [ ] Monitoring plan established for post-deployment

**Stakeholder Validation**
- [ ] Domain experts review historical context assessment
- [ ] Legal/compliance review fairness definitions
- [ ] Affected community representatives provide feedback 
- [ ] Leadership approves audit findings and recommendations

---

## 4. CASE STUDY

## 4. CASE STUDY

This case study demonstrates how to apply the Fairness Audit Playbook to an internal loan approval system used by a UK financial services company. The model predicts whether to approve or reject personal loan applications based on applicant data (e.g. income, employment history, credit score, existing debt). Its outputs directly affect access to credit, interest rates and financial stability, making fairness a high-stakes requirement.

**Key stakeholders:** Loan applicants, risk & credit teams, compliance/legal, senior leadership and regulators (FCA).

**Sensitive attributes:** Race/Ethnicity (White, Black, Asian, Mixed/Other), Gender (Male, Female, Non-binary), Age (18–25, 26–45, 46–65, 65+), Marital status (single, married, single parent). **Intersectional groups:** Black single mothers, elderly Asian men, etc.

### Applying the Playbook

#### Step 1: Historical Context Assessment

**Research**

The team reviews academic literature on lending discrimination, FCA regulatory reports, Equality Act enforcement cases and consults with community organisations representing affected groups.

**Questionnaire Responses**

**Purpose of your AI project**
- **What is the AI project designed to do?** Predict loan eligibility and default risk to support automated approval decisions for personal loans.
- **What decision or outcome does this AI project influence?** Determines who receives credit, on what terms (interest rates), and at what price; affects wealth-building and economic mobility.
- **How have similar decisions historically been made in this domain?** Historically made by loan officers using subjective criteria, credit scores and manual underwriting processes that have been documented to discriminate against certain groups.

**Affected populations**
- **Which demographic groups are impacted by decisions in this domain?** All loan applicants, with particular impact on Black, Asian, and other ethnic minority borrowers; women (especially single mothers); older adults; immigrants; low-income individuals.
- **Which groups or intersections of these groups have historically experienced disadvantage or exclusion?** Black and Asian borrowers face higher rejection rates even after controlling for creditworthiness. Single mothers and married women historically required male co-signers. Intersectional groups like Black single mothers, elderly Asian men, and immigrant women face compounded disadvantages.
- **Are there documented cases of discrimination affecting these groups, or their intersections?** Yes, extensive documentation including FCA investigations, Equality Act violations and studies showing persistent disparities in lending outcomes.

**Data Representation**
- **What types of data have historically been used to make decisions in this domain?** Credit scores, income, employment history, debt-to-income ratios, loan history, collateral and geographic location.
- **Have these data sources been influenced by discriminatory collection practices or institutional biases?** Yes, credit scoring systems have been criticized for encoding historical discrimination. Geographic data (postcodes) have been used for discriminatory practices.
- **Have certain groups been historically underrepresented during data collection?** Yes, recent immigrants, younger applicants with limited credit history and older women have thinner credit files.
- **Have any features acted as proxies for sensitive protective attributes?** Yes, postcode strongly correlates with ethnicity and socioeconomic status. Employer name and type may correlate with demographic groups.
- **Are there any missing data points on certain groups and intersections of groups?** Yes, missing income data is more common among certain groups (e.g., self-employed individuals, part-time workers) and imputation methods may introduce bias.

**Variable Selection and Feature Engineering**
- **Historically, which variables or attributes have been used to make decisions in this domain?** Credit score, income, employment status, debt-to-income ratio, loan amount, loan purpose, collateral, geographic location and relationship with the institution.
- **Have any of these variables historically acted as proxies for protected characteristics?** Yes, postcode is a well-documented proxy for ethnicity. Employment type and employer name may correlate with demographic groups.
- **Have numerical representations of sensitive attributes historically oversimplified or distorted the lived experiences of affected communities?** Yes, credit scores may not adequately capture the financial stability of individuals with non-traditional employment or those who have been historically excluded from credit markets.

**Algorithm selection**
- **Historically, what kinds of models or algorithms have been used in this domain?** Logistic regression, decision trees and more recently gradient boosting models (XGBoost, LightGBM).
- **Have these historical approaches disproportionately categorised certain groups in harmful ways?** Yes, models optimised for overall accuracy have been shown to perform worse for minority groups and tree-based methods may create splits that disadvantage underrepresented groups with fewer samples.
- **Have previous systems applied parameters or thresholds that resulted in disparities?** Yes, uniform thresholds across all groups can create disparities when base rates differ.

**Evaluation Framework**
- **What evaluation metrics have historically been used in this domain?** Overall accuracy, AUC-ROC, precision, recall, and default rates.
- **Are there any historical disparities which arise when using these metrics across demographic groups or intersections of groups?** Yes, aggregate metrics mask group-level disparities. Models with high overall accuracy may have significantly different error rates across groups.
- **Have researchers criticised any of these metrics for failing to capture fairness-specific harms?** Yes, accuracy and AUC metrics do not capture fairness concerns. Researchers have advocated for group-level metrics and intersectional analysis.

**Deployment Context**
- **What historical biases or discrimination exist within the domain where your AI project will be deployed?** Discriminatory underwriting and unequal access to credit are well-documented historical patterns in the UK.
- **Have past technologies in this domain produced harmful feedback loops that reinforced inequality?** Yes, credit scoring systems that penalise thin credit files create barriers for groups historically excluded from credit markets, reinforcing inequality.
- **Historically, have monitoring systems failed to detect or prevent biased outcomes and if so, how?** Yes, many institutions only monitor aggregate metrics, missing group-level disparities. Post-deployment monitoring has often been insufficient.
- **Are there past examples where user behaviour produced unequal access for certain groups?** Yes, loan officers may apply AI recommendations differently across groups, or certain groups may be less likely to apply due to historical exclusion.
- **Are there any historical biases emerging from how past technologies are integrated with other systems?** Yes, credit scoring systems integrated with other financial services may compound disparities.
- **Are there any fairness/discrimination-related legal requirements historically that have impacted your domain?** Yes, the Equality Act 2010 prohibits discrimination based on protected characteristics including race, sex, age, marital status, and other protected characteristics. GDPR also applies to processing of special category data.

**Risk Classification Matrix**

| Historical pattern | Severity | Likelihood | Relevance |
|-------------------|----------|------------|-----------|
| Under-approval of Black and Asian borrowers | High | High | High |
| Lower approval rates for single mothers | High | Medium | High |
| Discrimination via location-based criteria (postcode) | High | High | High |
| Underrepresentation of recent immigrants in training data | Medium | Medium | Medium |
| Gender bias in historical lending decisions | High | Medium | High |
| Intersectional harms (e.g., Black single mothers) | High | High | High |

**Findings Report**

**Top Priority Key Findings:**

1. **Historical Discrimination Patterns:** Strong evidence of ethnic and gender discrimination in lending, including discriminatory underwriting practices. These patterns are likely to be encoded in historical training data.

2. **Proxy Variables:** Postcode acts as a strong proxy for ethnicity and socioeconomic status, creating risk of indirect discrimination even if protected attributes are excluded.

3. **Representation Gaps:** Underrepresentation of recent immigrants, younger applicants, and older women in training data, with particularly small sample sizes for intersectional groups (e.g., Black single mothers, elderly Asian men).

4. **Intersectional Risk:** Multiple intersectional groups face compounded disadvantages that may not be visible in single-attribute analysis.

5. **Legal Requirements:** Must comply with Equality Act 2010, which prohibits discrimination based on protected characteristics including race, sex, age, and marital status. GDPR also applies to processing of special category personal data.

These findings directly inform fairness definition selection in Step 2, particularly highlighting the need for Equal Opportunity (to address historical exclusion) and intersectional analysis.

---

#### Step 2: Fairness Definition Selection

**Questionnaire Responses**

**Historical Context**
- **Based on the Historical Context Assessment above (Step 1), are there any under-represented or excluded groups and their intersections?** Yes, multiple groups identified including Black and Asian borrowers, single mothers, recent immigrants, and intersectional groups like Black single mothers.
  - **Decision:** Consider Demographic Parity, but this conflicts with merit-based lending principles. Equal Opportunity is more appropriate.

**Purpose of your AI project**
- **Which concept(s) of fairness best aligns with the intended business purpose and ethical requirements of your AI system?** The primary harm is false negatives (wrongly rejecting qualified applicants), which prevents access to credit and reinforces historical exclusion.
  - **Decision:** Equal Opportunity (primary) - ensures qualified individuals have equal chances of receiving positive outcomes.
- **Is it important to give the same treatment to individuals regardless of their demographic groups?** Yes, but group fairness is more critical given historical patterns. Individual fairness considerations will be monitored but are secondary.
  - **Decision:** Focus on group fairness metrics (Equal Opportunity), but monitor individual fairness concerns.

**Data Representation/Variable Selection**
- **Which concept of fairness determines the selection of variables in your AI project?** Variables should be selected to avoid proxies for protected attributes while maintaining predictive power. Fairness considerations require excluding or carefully handling postcode to prevent indirect discrimination.
- **Which definition of fairness determines how these variables should be encoded?** Encoding should not introduce bias. Missing data imputation must be evaluated for disparate impact across groups.

**Algorithm selection**
- **Depending on the concept of fairness selected, what are the necessary pre-processing, in-processing and post-processing steps to follow?** 
  - Pre-processing: Remove or carefully handle postcode to avoid proxy discrimination.
  - In-processing: Consider fairness constraints or group-aware optimisation to achieve Equal Opportunity.
  - Post-processing: Threshold adjustment to achieve Equal Opportunity if needed. 

**Evaluation Framework**
- **What is your primary concern concerning fairness?** Ensuring qualified applicants have equal chances of approval regardless of demographic group, particularly addressing historical exclusion of Black, Asian, and female applicants.
- **Based on the above answer, how should different fairness measures be weighted?** Equal Opportunity is primary (weight: 0.7), Predictive Parity is secondary (weight: 0.3) for risk management.
- **Are there any domain-specific thresholds providing concrete benchmarks for identifying problematic disparities? If not, what is an acceptable threshold?** For Equal Opportunity (TPR difference): ≤ 5 percentage points (aligned with FCA guidance). For Predictive Parity (PPV difference): ≤ 3 percentage points (industry standard for risk management).

**Deployment Context**
- **Will the AI system expose scores to users?** Yes, applicants may see risk scores or probability estimates.
  - **Decision:** Predictive Parity is important to ensure scores have consistent meaning across groups.

**Legal Context**
- **In which country/countries will your AI system be launched/integrated?** United Kingdom
- **Which jurisdiction will your AI System operate in?** UK-wide (Equality Act 2010 applies), plus FCA regulatory requirements
- **Are there any fairness-related legal/compliance requirements?** Yes, Equality Act 2010 prohibits discrimination based on protected characteristics. GDPR applies to processing of special category personal data. Must implement strictest applicable standards.
  - **Decision:** Equality Act compliance requires ensuring non-discriminatory access to credit, supporting Equal Opportunity as primary definition.

**Intersectional Considerations**
- **Which intersectional groups require specific fairness definitions?** Black single mothers, elderly Asian men, immigrant women, and other combinations identified in Step 1. All should be evaluated under Equal Opportunity.
- **Do different intersections need different fairness priorities?** All intersections should be evaluated under Equal Opportunity, but some may require additional attention due to compounded disadvantages identified in Step 1.
- **Are there conflicts between fairness definitions when examining intersections?** Potential conflict between Equal Opportunity and Predictive Parity if base rates differ significantly across intersections, requiring careful monitoring.

**Trade-Off Analysis**
- **Considering the trade-offs of each fairness measure, why have you selected some as primary metrics over others?** Equal Opportunity directly addresses the historical harm of excluding qualified applicants, which is the most critical legal and ethical concern. Predictive Parity supports risk management but is secondary.
- **Based on the response above, what combination of non-competing Fairness definitions came up in your analysis?** Equal Opportunity (primary) + Predictive Parity (secondary). These can be monitored simultaneously, though perfect satisfaction of both may not be achievable if base rates differ.

**Findings Report**

| Selected Fairness Definitions | Reasoning (consider historical context, business goals and stakeholder priorities) | Priority Level | Prioritisation Rationale |
|------------------------------|----------------------------------------------------------------------------------|----------------|--------------------------|
| Equal Opportunity | **Historical Context:** Historical lending practices (e.g. discriminatory underwriting) systematically denied loans to qualified Black, Asian, female, and intersectional applicants despite similar repayment ability. Step 1 identified strong evidence of historical exclusion patterns.<br><br>**Business Goals:** Ensure the model correctly approves applicants who would repay, without sacrificing creditworthiness. Primary goal is merit-based lending with equal access.<br><br>**Stakeholder Priorities:** Regulators (FCA) and compliance teams prioritise non-discriminatory access to credit per Equality Act 2010. Applicants expect fair evaluation based on merit. Legal team emphasizes avoiding discrimination claims.<br><br>**Legal Requirements:** Equality Act 2010 compliance requires ensuring non-discriminatory access, directly supporting Equal Opportunity. | Primary | Addressing false negatives (wrongly rejecting qualified applicants) is the most critical harm in lending. Equal Opportunity directly targets historical exclusion patterns identified in Step 1 and aligns with legal requirements. This is the highest priority given legal risk and ethical concerns. |
| Predictive Parity | **Historical Context:** Ethnic minority borrowers have historically been perceived as higher risk, sometimes leading to overly conservative approvals or unfair scrutiny. Step 1 identified this pattern.<br><br>**Business Goals:** Ensure approved loans have comparable default risk across groups to maintain portfolio quality and regulatory compliance.<br><br>**Stakeholder Priorities:** Risk teams and regulators (FCA) require that approvals have consistent meaning to avoid unsafe lending practices. Business stakeholders need confidence that model scores are calibrated.<br><br>**Deployment Context:** Scores are exposed to users, requiring consistent meaning across groups. | Secondary | Supports regulatory defensibility and risk management, ensuring model scores are meaningful. However, this does not directly address historical exclusion of qualified applicants. Secondary priority allows monitoring while prioritizing Equal Opportunity. |

**Thresholds Established:**
- Equal Opportunity (TPR difference): ≤ 5 percentage points
- Predictive Parity (PPV difference): ≤ 3 percentage points

---

#### Step 3: Bias Source Identification

**Questionnaire Responses**

**Historical Bias**
- **How might biases identified in the historical context and the chosen fairness definitions manifest in specific bias sources in the AI system?** Historical loan approval and default labels reflect past discriminatory lending practices. These biased labels become "ground truth" in training data, teaching the model to replicate discrimination. Equal Opportunity violations will manifest as lower TPR for historically excluded groups.
- **Which demographic groups and their intersections are most at risk of being unfairly impacted?** Black and Asian borrowers, single mothers, and intersectional groups like Black single mothers and elderly Asian men are at highest risk based on Step 1 findings.

**Representation Bias**
- **How was the data collected?** Training data consists of 10 years of past loan applications and outcomes from the company's historical records.
- **Are there any missing or imbalanced groups in the data?** Yes, underrepresentation of Black and Asian borrowers (30% of population but 15% of training data), recent immigrants (5% of population but 1% of training data), single mothers, and older women. Very small sample sizes for intersectional groups (e.g., Black single mothers: n=45, elderly Asian men: n=32).
- **Are the labels in the data biased or reflective of societal prejudices?** Yes, historical approval/rejection decisions and default labels likely encode past discrimination, as identified in Step 1.
- **Depending on the outcome of Step 2, are demographic groups and/or individuals being treated consistently according to the selected fairness definitions?** Initial analysis shows TPR disparities suggesting Equal Opportunity violations, requiring detailed investigation in Step 4.

**Feature Selection and Pre-processing Bias**
- **Are features selected or engineered in a way that discriminates against certain groups?** Yes, postcode is included and acts as a proxy for ethnicity and socioeconomic status. Employment type encoding may disadvantage non-standard work histories common among certain groups.
- **Are encoding, normalisation or imputation decisions differentially harmful across demographic groups and their intersections?** Yes, missing income data is more common among self-employed individuals and part-time workers (disproportionately certain demographic groups). Current imputation method (mean imputation) may underestimate stability for these groups.

**Model/Algorithm Bias**
- **How may the model set-up and training process introduce bias?** Gradient boosting model optimised primarily for overall AUC may favor majority-group patterns, reducing performance for minority and intersectional groups with fewer samples.
- **Does the choice of algorithm/model disadvantage certain groups and their intersections?** Tree-based methods segment feature space in ways that may create splits for underrepresented groups with fewer samples, potentially disadvantaging them.
- **What is the purpose for optimisation?** Overall AUC maximization.
- **How may your definition of loss function introduce bias?** Binary cross-entropy loss optimised for overall accuracy does not account for group-level performance, potentially allowing poor performance on minority groups.
- **How may your choice of regularisation technique introduce bias?** L2 regularization may penalize patterns specific to minority groups if they appear less frequently in training data.
- **Are hyperparameters tuned in a way that leads to unfair outcomes for specific groups?** Hyperparameters tuned using overall cross-validation performance may not detect group-level disparities.

**Evaluation Framework Bias**
- **Does the test data match the feature and demographic distribution of training data?** Yes, test data mirrors training data imbalances, limiting reliable evaluation for underrepresented and intersectional groups.
- **Are underrepresented groups represented in the test data?** Yes, but with very small sample sizes, leading to wide confidence intervals and unreliable metrics for intersectional groups.
- **Does the choice of evaluation metrics highlight fairness issues based on what aspects of performance they measure?** Current evaluation uses aggregate metrics (overall accuracy, AUC) which mask group-level disparities. Group-level fairness metrics are not currently calculated.

**Deployment Bias**
- **What human biases could influence the use of the model's outputs?** Loan officers may apply AI recommendations differently across groups, or certain groups may be less likely to apply due to historical exclusion, creating selection bias.
- **Does input data distributions change over time in response to system outputs? Do these shifts differ across demographic groups and their intersections?** Yes, if the model systematically rejects certain groups, those groups may stop applying, creating feedback loops that reinforce bias.
- **Does your choice of interface introduce any bias for certain demographic groups and their intersections?** Online application interface may be less accessible to certain groups (e.g., older adults, those with limited internet access).
- **How might infrastructure and resource disparities within the deployment environment influence the fairness of your model's outcomes?** Applicants with limited access to financial services infrastructure may be disadvantaged.
- **How do your organisational workflows and decision processes interact with system outputs? Do they introduce bias for outcomes of different groups?** Loan officers tend to rubber-stamp AI decisions in lower-value segments, amplifying any embedded bias. Limited human override in specific segments reduces ability to correct for bias.

**Intersectional Bias Analysis**
- **Which intersectional groups face unique bias sources not captured by single-attribute analysis?** Black single mothers face compounded risks from representation bias (small sample size), historical bias (both ethnic and gender discrimination), and feature bias (employment patterns, income stability). Elderly Asian men face similar compounded risks.
- **Are there bias sources that disproportionately affect specific intersections?** Yes, very small sample sizes for intersectional groups create representation bias that may not be visible in single-attribute analysis. Feature engineering decisions (e.g., employment encoding) may particularly disadvantage certain intersections.

**Priority Matrix**

| Bias Type | Severity | Scope | Persistence | Historical | Intervention | Overall Priority Level |
|-----------|----------|-------|-------------|------------|--------------|----------------------|
| Historical Bias | High | High | High | High | Medium | High |
| Representation Bias | High | Medium | High | High | Medium | High |
| Feature Selection and Pre-processing Bias | High | High | Medium | High | High | High |
| Model/Algorithm Bias | High | High | High | Medium | Medium | High |
| Evaluation Framework Bias | Medium | Medium | Low | Medium | High | Medium |
| Deployment Bias | High | Medium | High | High | Medium | High |

**Findings Report**

| Bias Type | Description | Detection Evidence | Priority Level |
|-----------|-------------|---------------------|----------------|
| Historical Bias | Historical loan approval and default labels reflect past discriminatory lending practices (e.g. unequal access to credit), which may be encoded as ground truth in training data. This directly conflicts with Equal Opportunity goals. | Disparities in historical approval rates across ethnicity, gender, and intersectional groups; alignment with documented discriminatory lending patterns from Step 1. Group-wise analysis shows lower historical approval rates for Black (45%) vs White (68%) applicants with similar credit profiles. | High |
| Representation Bias | Underrepresentation of Black and Asian borrowers, recent immigrants, single mothers, and older women. Very small sample sizes for some intersectional groups (e.g. Black single mothers: n=45, elderly Asian women: n=32). This limits reliable fairness evaluation and may cause model to underperform for these groups. | Demographic imbalance ratios: Black borrowers represent 15% of training data vs 30% of target population. Recent immigrants: 1% vs 5%. Intersectional groups have n < 50, leading to unstable metrics. Comparison to target population benchmarks from Step 1. | High |
| Feature Selection and Pre-processing Bias | Postcode acts as a proxy for ethnicity and socioeconomic status, enabling indirect discrimination. Employment type encoding disadvantages non-standard work histories. Missing income data imputation may underestimate stability for certain groups. | Correlation analysis shows postcode correlates 0.65 with ethnicity (using proxy measures). Group-level missingness patterns: 25% missing income for self-employed vs 5% for salaried employees. Post-imputation outcome shifts: imputed income groups show 8% lower approval rates. | High |
| Model/Algorithm Bias | Gradient boosting model optimized primarily for overall AUC (0.82), favoring majority-group patterns and reducing performance for minority and intersectional groups. Loss function does not account for group-level fairness. | Group-wise performance metrics show lower TPR for minority groups: White TPR = 0.85, Black TPR = 0.70, Asian TPR = 0.72. Intersectional groups show even lower TPR (Black single mothers: 0.60). Performance degradation after optimization suggests majority-group bias. | High |
| Evaluation Framework Bias | Test data mirrors training data imbalances, limiting reliable evaluation for underrepresented and intersectional groups. Aggregate metrics mask group-level disparities. | Comparison of training vs test demographic distributions shows similar imbalances. Wide confidence/credible intervals for small subgroups (e.g., Black single mothers: TPR 0.60 [0.45-0.75] due to n=45). Aggregate AUC of 0.82 masks 15 percentage point TPR gap. | Medium |
| Deployment Bias | Model deployed as score + threshold system; loan officers tend to rubber-stamp AI decisions in lower-value segments (<£10k loans), amplifying any embedded bias. Limited human override reduces ability to correct for bias. | Process audit showing 92% alignment between AI recommendation and final decision in low-value segments vs 65% in high-value segments. Limited human override: only 3% of low-value rejections are reviewed. This amplifies historical and algorithmic biases. | High |

These bias sources directly inform metric selection in Step 4, particularly highlighting the need for intersectional metrics and statistical validation accounting for small sample sizes.

---

#### Step 4: Comprehensive Metrics

**Workflow Application**

**1. Metric Selection**
- **Problem type:** Classification (approve/reject binary decision)
- **Selected fairness definitions from Step 2:** Equal Opportunity (primary), Predictive Parity (secondary)
- **Selected metrics using tables:** Equal Opportunity → TPR Difference and TPR Ratio. Predictive Parity → PPV Difference and PPV Ratio. Monitoring: Demographic Parity differences, FNR differences for intersectional analysis.
- **Harm direction:** False negatives are more harmful (wrongly rejecting qualified applicants) → Prioritize TPR/FNR metrics
- **Rationale documented:** TPR directly measures Equal Opportunity. PPV measures Predictive Parity. Intersectional metrics detect Simpson's Paradox.

**2. Implementation Planning**
- **Protected attributes and intersections:** Race/Ethnicity (White, Black, Asian, Mixed/Other), Gender (Male, Female), Age (18–25, 26–45, 46–65, 65+), Marital status (single, married, single parent). Key intersections: Black women, Black single mothers, elderly Asian men, etc.
- **Sample sizes assessed:** Large groups (n > 100): White (n=8,500), Black (n=1,200), Asian (n=900) → Bootstrap CI. Small groups (n < 100): Black single mothers (n=45), elderly Asian men (n=32) → Bayesian CI, flag as exploratory.

**3. Calculation & Validation**
- **Metrics calculated:** TPR and PPV for all groups and intersections
- **Confidence/credible intervals computed:** Bootstrap 95% CI for large groups, Bayesian 95% credible intervals for small groups
- **Statistical significance testing:** Two-proportion z-tests with Bonferroni correction (α = 0.05/12 = 0.0042 for 12 comparisons)
- **Robustness checks:** Metrics recalculated across 5 different train-test splits, showing consistent disparities
- **Simpson's Paradox detected:** Intersectional analysis reveals larger disparities than single-attribute analysis

**4. Analysis & Reporting**
- **Threshold comparison:** TPR differences exceed 5 p.p. threshold for multiple groups, violating Equal Opportunity
- **Violated fairness definitions identified:** Equal Opportunity violated for Black and Asian applicants. Predictive Parity shows smaller but notable violations.
- **Prioritisation:** Black single mothers show largest disparities (highest priority), followed by Black and Asian applicants overall
- **Visualizations created:** Bar charts with confidence intervals, intersectional heatmap, summary table
- **Recommendations:** Link to Step 3 bias sources (historical bias, representation bias, model bias)

**Key Decisions**

**Harm Direction:** False negatives more harmful → Prioritize TPR Difference and FNR Difference

**Intersectional Analysis:** 
- Calculate metrics for all relevant intersections
- Compare to single-attribute baselines: Single-attribute shows Black TPR = 0.70 vs White TPR = 0.85 (15 p.p. gap). Intersectional shows Black single mothers TPR = 0.60 vs White married men TPR = 0.88 (28 p.p. gap), revealing Simpson's Paradox
- Minimum sample size threshold: n ≥ 30 for reliable results. Groups with n < 30 flagged as exploratory
- High-uncertainty results flagged: Black single mothers (n=45) and elderly Asian men (n=32) have wide credible intervals but large point estimates

**Data Partitioning:**
- Protected attributes: Race/Ethnicity, Gender, Age, Marital status
- Intersections evaluated: All combinations with n ≥ 30
- Small groups: Use Bayesian methods, flag as exploratory
- Sample size assessment: Sufficient for single attributes, limited for intersections

**Statistical Validation Results**

| Group/Intersection | TPR | 95% CI | PPV | Sample Size | Status |
|-------------------|-----|--------|-----|-------------|--------|
| White | 0.85 | [0.83-0.87] | 0.92 | 8,500 | Pass |
| Black | 0.70 | [0.66-0.74] | 0.89 | 1,200 | **Fail** (15 p.p. gap) |
| Asian | 0.72 | [0.68-0.76] | 0.88 | 900 | **Fail** (13 p.p. gap) |
| Black single mothers | 0.60 | [0.45-0.75] | 0.85 | 45 | **Fail** (28 p.p. gap, high uncertainty) |
| White married men | 0.88 | [0.86-0.90] | 0.93 | 3,200 | Pass (reference) |

**Findings Report**

**Key Findings:**
1. **Equal Opportunity Violations:** TPR gaps exceed 5 p.p. threshold (Black: 15 p.p., Asian: 13 p.p.), statistically significant (p < 0.001).
2. **Simpson's Paradox:** Single-attribute shows 15 p.p. gap, intersectional shows 28 p.p. gap for Black single mothers vs White married men.
3. **Predictive Parity:** PPV differences smaller (3-4 p.p.) but notable.
4. **Small Sample Limitations:** Intersectional groups have wide credible intervals but large point estimates are warning signals.

**Prioritized Recommendations (Linked to Step 3 Bias Sources):**
1. Address Historical Bias: Label correction or re-weighting
2. Mitigate Representation Bias: Collect additional data for underrepresented groups
3. Remove Proxy Variables: Remove or carefully handle postcode
4. Modify Model Optimisation: Incorporate fairness constraints
5. Enhance Evaluation: Implement group-level monitoring
6. Address Deployment Bias: Human review for low-value segments

**Visualisations:** System Fairness Disparity Chart (bar chart with intervals), Intersectional Heatmap (color gradient with sample size indicators), Disparity Summary Table.

---

#### Step 5: Fairness Audit Report

Final report compiles all findings from Steps 1-4:
- **Executive Summary:** Key disparities (13-15 p.p. TPR gaps, up to 28 p.p. for intersections), recommended actions
- **Historical Context:** Discrimination patterns, risk classification
- **Fairness Definitions:** Equal Opportunity (primary) and Predictive Parity (secondary) with thresholds
- **Bias Sources:** Six bias sources with priority levels
- **Comprehensive Metrics:** Quantitative violations, intersectional disparities, statistical validation
- **Prioritized Recommendations:** Action items linked to bias sources
- **Monitoring Plan:** Ongoing group-level and intersectional tracking

Report presented to leadership, compliance and risk teams for review before mitigation.



---

## 5. PLAYBOOK IMPROVEMENTS

### Improve Workflow Integration
- Develop a standardised Fairness Audit Report template so teams can easily integrate results into existing risk and governance processes.
- Provide pre-filled documentation templates for questionnaire responses to streamline reporting and ensure consistency across teams.
- Explore automation opportunities, such as AI-assisted generation of findings based on questionnaire inputs.

### Enhance Decision Support Tools
- Introduce interactive decision trees for selecting fairness definitions, identifying bias sources, and choosing metrics based on domain context, harm type, intersectional risk, and legal constraints.
- Add a visual flowchart within the Fairness Definition Selection component to guide users through trade-offs aligned with business purpose, ethical principles, and regulatory requirements

### Expand Knowledge Resources
- Build a reusable repository of common bias sources and recommended metrics across domains (e.g., lending, hiring, healthcare).
- Expand the library of case studies to illustrate how the playbook applies across diverse real-world contexts and problem types.

### Enable Legal-Technical Alignment
Create a dedicated legal guidance section that:
- Summarises relevant anti-discrimination, AI governance, and sector-specific regulations.
- Translates legal standards into technical verification checklists and metric thresholds.
- Provides case studies demonstrating how legal requirements influence technical design decisions.
- Consider a multi-tiered playbook structure, allowing legal, engineering, product, and compliance teams to contribute to and build on each other's outputs.

### Strengthen Communication & Visualisation
- Develop intuitive visualisations of fairness trade-offs (e.g., how optimising for Equal Opportunity may affect Demographic Parity) without requiring deep mathematical expertise.
- Provide example-driven illustrations showing how different fairness definitions impact specific individuals and groups in practice.

