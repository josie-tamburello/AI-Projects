# CAUSAL FAIRNESS TOOLKIT

## INTRODUCTION

The Causal Fairness Toolkit helps you understand where and how bias exists in your AI system before attempting to fix it. Rather than simply observing that statistically different demographic groups receive different outcomes, causal analysis reveals the underlying mechanisms that create these disparities. This understanding will reveal where intervention is most effective and optimal.

## CAUSAL FAIRNESS TOOLKIT OVERVIEW
1. **Component 1: Causal Modeling Template:** This provides you with a framework for mapping causal relationships that may create bias in your AI system.
2. **Component 2: Counterfactual Analysis Framework:** This part is for evaluating whether predictions would change under different values of protected attributes. 
3. **Component 3: Intervention Point Identification Method:** This determines optimal intervention points based on causal structures. 
4. **Component 4: Limited Information Adaptation Guidelines:** This shows you how to apply causal analysis with incomplete causal knowledge. 


## COMPONENT 1: CAUSAL MODELING TEMPLATE

This guide helps you identify and visualise key variable types in your AI system, so you can trace where bias may arise from problem formulation, data collection, feature engineering to model architescture and deployment. Here is an overview of what to expect in this component 1:

**Step 1:** Start by reviewing the variable type definitions and identify variables in your AI system.
**Step 2:** Based on above, document your findings using the template. 
**Step 3:** Use your documented variables to construct a causal graph that maps relationships between variables. 
**Step 4:** Analyse your causal graph to identify which discrimination pathway is applicable to each variable pathway identified. 
**Step 5:** Use the template to note down the identified discrimination type for each pathway. 

### Step 1: Identify Variables

| Variable Type | Definition | Example | What to Look For |
|--------------|------------|---------|------------------|
| **Protected Attributes** | Legally protected characteristics. Check jurisdiction-specific laws. Include intersectional combinations as causal mechanisms may differ across intersections. | Race, gender, age, disability. Intersection: Black women | Legal requirements in your jurisdiction, demographic data in your system, combinations of attributes that create unique discrimination patterns |
| **Mediators** | Variables causally influenced by protected attributes that transmit effects to outcomes.  | Employment history influenced by gender because women experience career breaks for caregiving | Features that are downstream of protected attributes—may be legitimate predictors but require careful classification |
| **Proxies** | Variables correlated with protected attributes through common causes, not direct causation. These enable indirect discrimination. | Zip code correlates with race due to residential segregation | Variables that correlate with demographics but aren't directly causal (e.g., geographic features, cultural markers) |
| **Confounding variables** | TO ADDD | Neighbourhood economic conditions, local housing markets, generational wealth | TO ADD |
| **Outcomes** | The decisions or predictions your system makes. These are what you're trying to make fair. | Loan approval, risk score, hiring decision | Your model's predictions or decisions where fairness matters |

### Step 2: Document Variables

Using domain expertise, use the table below to document each identified variable using the reference table above:


| Variable Type | Variables | Justification / Additional Information |
|--------------|-----------|--------------------------------------|
| **Protected Attributes** | [List variables, e.g., Gender, Race] | **Justification:** [Why are these protected? Reference legal requirements, e.g., UK Equality Act 2010 protects gender and race]<br>**Intersection Categories:** [List combinations, e.g., Black women, Race × Gender]|
| **Mediators** | [List variables] | **For each variable:** What is the evidence for causal relationship? (e.g., domain expertise, literature, temporal ordering). |
| **Proxies** | [List variables] | **For each variable:** Why do they act as proxies? What common cause explains the correlation? (e.g., "Zip code correlates with race because both are influenced by historical housing discrimination") |
| **Confounders** | [List variables] | TO ADD |
| **Outcomes** | [List variables] | **Evaluation Metrics:** [List metrics from Fairness Audit, e.g., TPR difference, PPV difference] |
   
### Step 3: Construct Graph

A causal graph (Directed Acyclic Graph or DAG for short) visualises how the variables identified above influence each other in your AI system.

**Guidelines:**
- Use arrows to represent causal relationships (e.g., X → Y means X causally influences Y)
- Use bidirectional dashed arrow (↔) to represent correlation without direct causation
- Distinguish protected attributes, mediators, proxies, and outcomes using different node shapes (e.g., squares, circles, diamonds) or different colors
- Explicitly represent intersectional categories as distinct nodes 
- Validate results with domain experts. 

### Step 4: Identify Discrimination Types

After constructing your causal graph, analyse which discrimination type exists for each pathway. This step is important because each causal mechanism requires different interventions. 


| Discrimination Type | Pathway Pattern | What It Means |
|---------------------|-----------------|---------------|
| **Direct Discrimination** | Protected attribute → Outcome | The protected attribute directly influences the outcome without any mediating variables (e.g. gender affecting loan approvals directly) |
| **Indirect Discrimination** | Protected attribute → Mediator → Outcome | The protected attribute influences the outcome through a mediator (e.g. a qualification measure)|
| **Proxy Discrimination** | Protected attribute ↔ Proxy → Outcome | A proxy variable correlates with the protected attribute (through common causes) and influences the outcome |


### Step 5: Identify Discrimination Pathways

Use this template to document your identified discrimination type for each pathway identified: 

| Pathway | Discrimination Type |
|---------|---------------------|
| Gender → Employment history → Approval | Indirect |
| Race ↔ Zip code → Approval | Proxy |
| Gender → Approval | Direct |
| [List your pathway] | [Type] |

### Step 6: Analysis of Discrimination pathways 

The next step is to mathematically calculate Structural Equation Models (SEMs) for each variable in the discrimination pathways identified in Step 5. This is to formalise the relationships between the variables expressed on the graphical representation.Follow the following steps: 

1. Conduct SEMs on each variable of the discrimination pathways identified above
2. Analyse the strength of associations along these pathways based off the results of SEMs 
3. Assess whether causal graph representations align with SEM results. 
4. Consider this analysis on different subgroups
4. Report back results on what the SEMs revealed, particularly from an intersectional perspective. 

## COMPONENT 2: COUNTERFACTUAL ANALYSIS FRAMEWORK

This part asks the question "Would this individual have received the same decision if they belonged to a different demographic group?". This component 2 is composed of 2 parts. Step 1 asks you to fill out a questionnaire to unravel the outcome differences when changing the values of protected attributes. Step 2 then explores which of the causal paths are legitimate or problematic, which will guide your intervention approach later. 

### Step 1: Counterfactual Questionnaire 

Take a note of your answers to all of these questions below. Make sure to repeat the steps below for a representative sample of individuals from each group and break it down by intersectional groups. 

**Base Case:**

1. What are the current protected attributes?
2. What are the current non-protected attributes? 
3. What is the current model prediction/decision?

**Counterfactual scenario**

1. What are your modified protected attributes? (e.g. changing gender to male)
2. Which variables remained constant? (e.g. credit score, income)

**Fairness evaluation:**

1. What is the acceptable difference threshold? 
3. What is the model's actual outcome on counterfactual instance? 
4. What is the difference between the acceptable threshold and actual model outcomes? 

### Step 2: Path-Specific Effect Analysis

Use this template to understand how much each causal pathway contributes to disparities. I have added guidance to each respective part of the table for you to follow when filling it out.  

| Causal Pathway | Classification (Legitimate / Problematic / Mixed) | Reasoning | Path-Specific Effect | Action (Preserve / Intervene) |
|----------------|---------------------------------------------------|-----------|----------------------|-------------------------------|
| [Describe pathway from protected attribute to outcome] | **Legitimate:** Fair difference based on task-relevant factors (e.g., skill, merit). **Problematic:** Difference based on bias/discrimination (e.g., gender). | [Explain using causal graph + domain expertise: why is this pathway legitimate or problematic?] | [Calculate using structural equations: Specify M = f_M(A, U_M) and Y = f_Y(A, M, U_Y), estimate parameters, then compute Total effect (A=a vs A=a' with M responding naturally), Direct effect (A=a vs A=a' holding M constant), or Indirect effect (Total - Direct). Report as percentage points or effect size.] | [Decide based on classification + effect size: preserve legitimate, intervene on problematic] |

### Step 3: Intersectional Analysis

Report back on the what the analysis reveals above in relation to specific intersections of groups (e.g. race and gender). 


## COMPONENT 3: INTERVENTION POINT IDENTIFICATION METHOD

Determine where to intervene based on causal analysis from Components 1-2. Use the matrix for quick lookup, then consult the decision tree for details.


### Intervention Selection Matrix

| Causal Pattern | First Choice | Second Choice | If Cannot Retrain |
|----------------|--------------|---------------|-------------------|
| **Direct:** A → Y | Pre: Remove A | In: Fairness constraint | Post: Thresholds |
| **Proxy:** A ↔ X → Y | Pre: Remove X | Pre: Fair representation | Post: Thresholds |
| **Illegitimate mediator:** A → M → Y | Pre: Remove M | Pre: Reweight data | Post: Thresholds |
| **Legitimate mediator:** A → M → Y | Document & monitor | In: Multi-objective opt. | Post: Thresholds |
| **Mixed mediator:** A → M → Y | Pre: Fair representation | Pre + In combined | Post: Calibration |
| **Multiple pathways** | Pre + In combined | Sequential by pathway | Post: Complex rules |
| **Historical label bias** | Pre: Reweight + relabel | In: Robust learning | Post: Thresholds |

*Pre = Pre-Processing | In = In-Processing | Post = Post-Processing*

### Decision Tree

**1. DIRECT DISCRIMINATION (A → Y)**

*Is protected attribute explicitly a feature?*
- **YES** → Remove feature (unless legally required) | Pre-Processing
- **NO** → Investigate implicit encoding (check model architecture, feature engineering) | In-Processing fairness constraints

**2. PROXY DISCRIMINATION (A ↔ X → Y)**

*Can you identify proxy variables?*
- **YES** → Remove or transform (e.g., remove zip code) | Pre-Processing
- **NO** → Adversarial debiasing (penalize representations encoding protected attribute) | In-Processing

**3. MEDIATOR DISCRIMINATION (A → M → Y)**

*Is mediator legitimate (task-relevant)?*
- **LEGITIMATE** → Preserve (document & monitor) OR intervene (multi-objective optimization)
- **ILLEGITIMATE** → Remove A's influence | Pre-Processing (remove feature/reweight)
- **MIXED** → Isolate legitimate component (e.g., credit score: keep payment history, remove demographic correlation) | Pre + In-Processing

**4. OUTCOME DISCRIMINATION (disparities in Y)**

*Are disparities consistent across subgroups?*
- **YES** → Group-specific thresholds | Post-Processing
- **NO** → Targeted interventions per subgroup | Intersectional analysis
- **Cannot retrain** → Post-Processing only (thresholds, calibration, reject option)

---

### Prioritisation Framework

**When multiple pathways exist, prioritise by:**

| Factor | Guidance |
|--------|----------|
| **1. Effect size** | Target largest contributors (e.g., 40% from zip code → address first) |
| **2. Legitimacy** | Problematic > Mixed > Legitimate |
| **3. Feasibility** | Data access + retraining ability determines Pre/In/Post options |
| **4. Effectiveness** | Pre (root cause) > In (structural) > Post (surface-level) |
| **5. Constraints** | Time: Post fastest (1 wk), Pre/In slower (2-4 wks); Expertise: Pre needs data science, In needs ML engineering |


## COMPONENT 4: LIMITED INFORMATION ADAPTATION GUIDELINES

There are inherent limitations of causal inference with observational data as experimiental intervention is not possible. Use this workflow to: (1) assess what information you have, (2) select adaptation strategies, (3) document assumptions and (4) identify robust interventions. Document all of your results. 

**Match your gaps to adaptation strategies below:**

### Challenge 1: Uncertain Causal Structure

**When to use:** Don't know true causal graph (which edges exist, direction of causation)

**Strategy:**
1. **Test multiple models:** Elicit 2-4 plausible DAGs from experts 
2. **Sensitivity analysis:** Run pathway analysis for each DAG, compare intervention recommendations
3. **Identify robust interventions:** Prioritize interventions recommended across all models
4. **Document assumptions:** Record evidence, confidence level, impact if wrong


### Challenge 2: Small Sample Sizes

**When to use:** Intersectional groups have n<50, limiting reliable effect estimation

**Strategy:**
1. **Matching:** Pool similar groups if causal structures match, document rationale
2. **Qualitative analysis:** Use expert elicitation to build DAGs even without quantitative data
3. **Flag uncertainty:** Explicitly mark low-confidence estimates


### Challenge 3: Conflicting Expert Opinions

**When to use:** Domain experts disagree on causal relationships

**Strategy:**
1. **Structured elicitation:** Individual interviews → group discussion → document rationale
2. **Identify disagreement sources:** Different domains, assumptions, or empirical vs. theoretical views
3. **Resolve:** Empirical testing (if possible), conservative approach (assume edge exists), or sensitivity analysis
4. **Document:** Record consensus level, dissenting opinions, decision rationale


### Challenge 4: Limited Observational Data

**When to use:** Can only observe correlations, no randomised experiments

**Strategy:**
1. **Natural experiments:** Look for policy changes or discontinuities providing quasi-random variation
2. **Instrumental variables:** Use two-stage least squares if valid instruments exist
3. **Bounds analysis:** Compute effect bounds under different assumptions (e.g., Manski bounds)
4. **Document assumptions:** List all identification assumptions (confounders, positivity, consistency)

### Challenge 5: Missing Protected Attributes

**When to use:** Protected attributes not collected (privacy/legal reasons)

**Strategy:**
1. **Qualitative analysis:** Build DAGs using domain knowledge, identify likely proxies
2. **Advocate for collection:** If feasible, collect with privacy protections (GDPR Art. 9 exemption)
3. **Difference-in-difference:** Examine how disparities changed after policy reforms in certain jurisdictions.

## OUTPUTS FOR SUBSEQUENT TOOLKITS

After completing the Causal Fairness Toolkit, you will have identified where and how bias occurs in your system. These outputs directly inform which intervention toolkits to use and how to configure them.
