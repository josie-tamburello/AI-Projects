# CASE STUDY: LOAN APPROVAL FAIRNESS INTERVENTION

This case study demonstrates the comprehensive application of the Fairness Intervention Playbook to address gender and racial disparities in the bank's loan approval system.

### Background 

**AI System:** Loan approval prediction model (binary classification)  
**Model Type:** Gradient Boosting (XGBoost)  
**Features:** Income, credit score, debt-to-income ratio, employment type, zip code, loan amount, age, years at current job  
**Protected Attributes:** Gender (Male/Female), Race (White/Black/Asian/Other), Age groups  
**Outcome:** Loan approval/rejection (Y=1/0)  
**Annual Volume:** ~50,000 applications  
**Regulatory Environment:** UK FCA oversight, Equality Act 2010 compliance required

## PHASE 1: CAUSAL FAIRNESS ANALYSIS (Component 1)

### COMPONENT 1: CAUSAL MODELING TEMPLATE

#### Step 1: Identify Variables

Following Component 1's variable type definitions, we identified:

| Variable Type | Variables Identified | What to Look For |
|--------------|---------------------|------------------|
| **Protected Attributes** | Gender (Male/Female), Race (White/Black/Asian/Other) | Legal requirements (UK Equality Act 2010), demographic data in system |
| **Mediators** | Income, Employment type, Credit score, Years at current job | Features downstream of protected attributes |
| **Proxies** | Zip code | Variables correlated with demographics but not directly causal |
| **Legitimate Predictors** | Debt-to-income ratio, Loan amount, Age | Task-relevant features not influenced by protected attributes |
| **Outcomes** | Loan approval/rejection | Model predictions where fairness matters |

### Step 2: Document Variables

Using Component 1's documentation template:

| Variable Type | Variables | Justification / Additional Information |
|--------------|-----------|--------------------------------------|
| **Protected Attributes** | Gender, Race | **Justification:** UK Equality Act 2010 protects gender and race from discrimination<br>**Intersection Categories:** Black women, White women, Black men, Single mothers (Gender × Race × Marital status) |
| **Mediators** | Income | **Evidence for causal relationship:** Gender → Career patterns → Income (domain expertise, labor market research) |
| **Mediators** | Employment type | **Evidence:** Gender → Part-time work patterns → Employment type encoding (temporal ordering: gender influences employment choices) |
| **Mediators** | Credit score | **Evidence:** Race → Historical credit access barriers → Lower scores (literature on credit discrimination, temporal ordering) |
| **Mediators** | Years at current job | **Evidence:** Legitimate stability indicator, causally related to repayment ability |
| **Proxies** | Zip code | **Why it acts as proxy:** Zip code correlates with race because both are influenced by historical housing discrimination and residential segregation (common cause: historical discrimination) |
| **Legitimate Predictors** | Debt-to-income ratio | **Why legitimate:** Business necessity (measures financial obligation), legally permissible, causally relevant to repayment, not influenced by protected attributes |
| **Legitimate Predictors** | Loan amount | **Why legitimate:** Applicant choice, not influenced by protected attributes |
| **Legitimate Predictors** | Age | **Why legitimate:** Legitimate for credit history length, causally relevant |
| **Outcomes** | Loan approval/rejection | **Evaluation Metrics:** TPR difference (18 p.p. gender, 12 p.p. race), Equal Opportunity gap |

### Step 3: Construct Graph

Following Component 1's guidelines, we constructed a causal DAG:

```
Gender/Race (Protected Attributes)
   ↓
   ├─→ Income (resolving mediator)
   ├─→ Employment type (partially resolving mediator)
   ├─→ Credit score (partially resolving mediator)
   ├─→ Years at current job (resolving mediator)
   └─→ Historical lending decisions (NON-resolving — past discrimination)

Zip code ↔ Race (correlation via segregation - Proxy)
   ↓
   └─→ Approval (proxy discrimination)

Income → Debt-to-income ratio → Approval
Employment type → Income stability → Approval
Credit score → Payment history → Approval
```

**Expert Validation:** Consulted lending compliance officer, economist, and community advocates to validate causal relationships and graph structure.

### Step 4: Identify Discrimination Types

Following Component 1's discrimination type definitions:

| Discrimination Type | Pathway Pattern | What It Means |
|---------------------|-----------------|---------------|
| **Direct Discrimination** | Protected attribute → Outcome | Protected attribute directly influences outcome without mediating variables |
| **Indirect Discrimination** | Protected attribute → Mediator → Outcome | Protected attribute influences outcome through a mediator |
| **Proxy Discrimination** | Protected attribute ↔ Proxy → Outcome | Proxy variable correlates with protected attribute and influences outcome |

### Step 5: Identify Discrimination Pathways

Using Component 1's template:

| Pathway | Discrimination Type |
|---------|---------------------|
| Gender → Employment type → Approval | Indirect |
| Race ↔ Zip code → Approval | Proxy |
| Gender → Income → Approval | Indirect |
| Gender/Race → Historical labels → Approval | Direct |
| Race → Credit score → Approval | Indirect |



## COMPONENT 2: COUNTERFACTUAL ANALYSIS FRAMEWORK

### Step 1: Counterfactual Questionnaire

Following Component 2's questionnaire, we analyzed representative samples from each group and intersectional groups:

**Example: Female Applicant (Base Case)**

**Base Case:**
1. **Current protected attributes:** Gender = Female, Race = Black
2. **Current non-protected attributes:** Income = £35,000, Credit score = 680, Debt-to-income = 0.3, Employment type = Part-time, Age = 32
3. **Current model prediction/decision:** Rejected (score = 0.42, threshold = 0.5)

**Counterfactual scenario:**
1. **Modified protected attributes:** Gender = Male (changed from Female to Male)
2. **Variables remained constant:** Income = £35,000, Credit score = 680, Debt-to-income = 0.3, Employment type = Part-time, Age = 32

**Fairness evaluation:**
1. **Acceptable difference threshold:** ≤5 p.p. (Equal Opportunity requirement)
2. **Model's actual outcome on counterfactual instance:** Approved (score = 0.58)
3. **Difference between acceptable threshold and actual model outcomes:** 16 p.p. difference (0.58 - 0.42) — exceeds acceptable threshold by 11 p.p.

**Repeated for:** White Male, White Female, Black Male, Black Female, Single mothers, Older Black women (intersectional groups)

### Step 2: Path-Specific Effect Analysis

Using Component 2's template:

| Causal Pathway | Classification (Legitimate / Problematic / Mixed) | Reasoning | Path-Specific Effect | Action (Preserve / Intervene) |
|----------------|---------------------------------------------------|-----------|----------------------|-------------------------------|
| Gender → Employment type → Approval | **Problematic** | Employment type encoding treats part-time (disproportionately female) as "worse" than full-time, creating unfair disadvantage | 6.2 p.p. (calculated via structural equations: indirect effect of gender through employment type) | **Intervene** — Fix encoding |
| Race ↔ Zip code → Approval | **Problematic** | Zip code proxies for race via residential segregation, enabling indirect discrimination | 4.8 p.p. (proxy effect via correlation) | **Intervene** — Remove zip code |
| Gender → Income → Approval | **Legitimate** | Reflects labor market patterns where gender influences career choices and income, which legitimately affects repayment ability | 3.1 p.p. | **Preserve** — Document & monitor |
| Gender/Race → Historical labels → Approval | **Problematic** | Training labels reflect past discriminatory lending practices, creating direct discrimination | 5.4 p.p. (direct effect) | **Intervene** — Reweight data |
| Race → Credit score → Approval | **Mixed** | Credit score contains legitimate payment history (legitimate component) but also historical discrimination effects (problematic component) | 3.7 p.p. (mixed effect) | **Intervene** — Transform to isolate legitimate component |

---

## COMPONENT 3: INTERVENTION POINT IDENTIFICATION METHOD

### Intervention Selection Matrix

Using Component 3's matrix:

| Causal Pattern | First Choice | Second Choice | If Cannot Retrain |
|----------------|--------------|---------------|-------------------|
| **Proxy:** Race ↔ Zip code → Approval | **Pre:** Remove zip code | **Pre:** Fair representation | **Post:** Thresholds |
| **Illegitimate mediator:** Gender → Employment type → Approval | **Pre:** Remove M | **Pre:** Reweight data | **Post:** Thresholds |
| **Historical label bias** | **Pre:** Reweight + relabel | **In:** Robust learning | **Post:** Thresholds |
| **Mixed mediator:** Race → Credit score → Approval | **Pre:** Fair representation | **Pre + In combined** | **Post:** Calibration |
| **Multiple pathways** | **Pre + In combined** | Sequential by pathway | **Post:** Complex rules |

### Decision Tree Application

**1. PROXY DISCRIMINATION (A ↔ X → Y)**
- *Can you identify proxy variables?* **YES** → Remove zip code | **Pre-Processing**

**2. MEDIATOR DISCRIMINATION (A → M → Y)**
- *Is mediator legitimate?* 
  - Employment type: **ILLEGITIMATE** (encoding biased) → Remove A's influence | **Pre-Processing** (fix encoding/reweight)
  - Credit score: **MIXED** → Isolate legitimate component | **Pre + In-Processing**

**3. OUTCOME DISCRIMINATION (disparities in Y)**
- *Are disparities consistent across subgroups?* **NO** → Targeted interventions per subgroup | **Intersectional analysis**

### Prioritisation Framework

Following Component 3's prioritisation:

| Factor | Analysis | Priority |
|--------|----------|----------|
| **1. Effect size** | Zip code: 4.8 p.p. (26% of total gap), Employment encoding: 6.2 p.p. (34% of gap) | Address zip code and employment first |
| **2. Legitimacy** | Problematic (zip code, employment) > Mixed (credit score) > Legitimate (income) | Prioritize problematic pathways |
| **3. Feasibility** | Data access: ✅, Retraining ability: ✅ (can retrain) | Pre + In-Processing feasible |
| **4. Effectiveness** | Pre (root cause) > In (structural) > Post (surface-level) | Use Pre + In primarily |
| **5. Constraints** | Time: 4 weeks available, Expertise: ML engineers available | All approaches feasible |

**Decision:** Use combined strategy (Pre-Processing → In-Processing → Post-Processing) for comprehensive fairness improvement.


## COMPONENT 4: LIMITED INFORMATION ADAPTATION GUIDELINES

We used Component 4 to handle data and knowledge gaps during causal analysis: 
- For small intersectional groups (e.g., older Black women, single mothers) we pooled similar groups where causal structures matched and clearly flagged low-confidence estimates;
- For conflicting expert views on employment type, credit score and zip code, we ran a structured elicitation and then resolved disagreements using empirical tests and intersectional impact;
- For observational-only data, we relied on natural experiments (pre/post policy changes) and bounds analysis, carefully documenting all assumptions, confidence levels, and their potential impact on intervention choices.


## PHASE 2: PRE-PROCESSING INTERVENTIONS (Component 2)

### COMPONENT 2: SELECTION DECISION TREE

#### STEP 1: Classify Your Bias Pattern

Following Component 2's decision tree, we identified multiple bias patterns from our causal analysis:

**Bias Patterns Identified:**
- **Proxy Features** (zip code correlates with race)
- **Label Bias** (historical discrimination in training labels)
- **Representation Gaps** (gender imbalance: 35% vs 48% target)
- **Multiple Bias Types Coexist**

**Decision:** Proceed to **SECTION E: Combined Approach** since multiple bias types are present.

### SECTION E: Combined Approach

Following Component 2's sequential intervention strategy:

| Step | Priority Area | Intervention Method | Reasoning |
|------|---------------|---------------------|-----------|
| **Step 1** | **LABEL BIAS** (detected) | Prejudice removal + Instance weighting | Biased labels compromise all subsequent interventions |
| **Step 2** | **PROXY DISCRIMINATION** | Feature removal (zip code) | Eliminate discriminatory pathways through features |
| **Step 3** | **REPRESENTATION IMBALANCE** | Instance weighting + SMOTE for intersections | Achieve balance after addressing feature and label issues |

### SECTION B: Label Correction

**Question 1:** Do your labels exhibit measurable historical discrimination patterns?
- **YES** → **Prejudice Removal** (algorithmic label modification)
  - Pattern: Equally qualified women rejected 42% more often than men

**Question 2:** Are domain experts available to review and validate label corrections?
- **YES** → **Expert Relabeling** (for validation subset)
  - Used alongside prejudice removal for cross-validation

**Selected Techniques:**
1. **Feature Removal:** Remove zip code (proxy discrimination)
2. **Feature Transformation:** Fix employment type encoding (illegitimate mediator)
3. **Instance Reweighting:** Demographic reweighting + fairness-aware reweighting (representation + label bias)
4. **Prejudice Removal:** Correct historical label bias
5. **Data Generation:** SMOTE for intersectional groups (single mothers)

### SECTION C: Feature Transformation (Proxy Features)

**Question 1:** Is the bias isolated to a small number of specific features?
- **YES, and model interpretability is essential**
  - → **Disparate Impact Remover** (but first we remove the proxy entirely)
  - However, since zip code is a pure proxy with no legitimate use, we **remove it directly**

**Decision:** Remove zip code feature entirely (no transformation needed for pure proxy).

### SECTION A: Reweighting & Resampling/Data Generation

**Question 1:** Does your algorithm support sample_weight parameter?
- **YES** → **REWEIGHTING** (XGBoost supports sample weights)

**Question 2:** Which imbalance scenario matches your data? *(When using Reweighting)*

| Imbalance Scenario | Recommended Approach | Selected |
|-------------------|---------------------|----------|
| **Basic demographic imbalance** (35% female vs 48% target) | **Instance Weighting** (inverse frequency approach) | Selected |
| **Missing positive outcomes for specific groups** (few approved loans for women) | **Instance Weighting** (weight by group × outcome interaction) | Selected |
| **Bias localised to specific feature intersections** (single mothers) | **Instance Weighting** (feature-stratified weighting) | Selected |

**Question 3:** How many samples exist in your minority group? *(For intersectional groups)*

| Sample Count | Recommended Approach | Selected |
|-------------|---------------------|----------|
| **50 ≤ n < 100** (single mothers: n=67) | **SMOTE** (synthetic interpolation method) | Selected |



## COMPONENT 3: CONFIGURATION GUIDELINES

### Instance Weighting Configuration

**Weighting scheme based on fairness goal (Equal Opportunity):**
- Weight by positive outcome proportion for each group
- Female qualified applicants (Y=1): weight = 2.0
- Male qualified applicants (Y=1): weight = 1.0
- Demographic reweighting: Female = 1.37, Male = 0.80

**Intervention Strength:**
- Started with moderate weights (square root of inverse frequency)
- Increased gradually: Final combined weights = demographic × fairness weights
- Capped weights to prevent instability (max weight = 2.5)

**Validation:** Used weighted cross-validation, monitored loss convergence, checked for overfitting, verified fairness gains.

### Prejudice Removal Configuration

**Modification strength:** Started with 0.5 (moderate dataset size)
- Adjusted to 0.7 after initial validation (stronger intervention needed)
- Range tested: 0.3 to 1.0
- Final: 0.7 (optimal balance between bias reduction and label preservation)

**Validation:** Monitored reduction in correlation between modified labels and protected attributes (reduced from 0.42 to 0.08). Ensured labels remained meaningful (AUC maintained at 0.88).

### Feature Transformation Configuration

**Employment Type Encoding Fix:**
- Changed from ordinal (1,2,3) to one-hot encoding
- No repair level needed (complete transformation)

---

## COMPONENT 4: EVALUATION FRAMEWORK

### STEP 1: Fairness Metrics Assessment

**Primary Fairness Metrics:**
- **Metric:** Equal Opportunity Difference (EOD)
- **Before intervention:** 18.0 p.p. (Male TPR: 0.85, Female TPR: 0.67)
- **After intervention:** 7.0 p.p. (Male TPR: 0.82, Female TPR: 0.75)
- **Improvement:** -11.0 p.p. (61% reduction)
- **Threshold met?** [ ] Yes [x] No (target: ≤5 p.p., achieved 7 p.p.)

**Intersectional Fairness:**
- **Protected attributes tested:** Gender × Race × Marital status
- **Maximum disparity across intersections:** Single mothers vs. Married men: 20 p.p. (reduced from 28 p.p.)
- **Specific high-risk comparisons identified:** Single mothers, Older Black women

**Statistical Significance:**
- **Test used:** Two-proportion z-test
- **p-value:** < 0.001
- **Significant improvement?** [x] Yes [ ] No (p < 0.05)

**Trade-offs observed:**
- Notes: 1.1% accuracy reduction acceptable for 11 p.p. fairness improvement

### STEP 2: Predictive Performance

**Overall Performance Changes:**
- **Accuracy:** Before: 0.856 After: 0.845 Change: -0.011 (-1.1%)
- **AUC:** Before: 0.890 After: 0.885 Change: -0.005 (-0.6%)
- **F1 Score:** Before: 0.82 After: 0.81 Change: -0.01 (-1.2%)

**Rank Ordering Preservation:**
- **Spearman correlation within groups:** 0.97 (Female), 0.98 (Male)
- **Acceptable?** [x] Yes [ ] No (target: ≥ 0.95)

**Feature Importance Changes:**
- **Key features maintained?** [x] Yes [ ] No
- **Notes:** Income, debt-to-income, credit score remain top features. Zip code removed as intended.

**Hold-out Set Testing:**
- **Test set performance:** Accuracy 0.843, AUC 0.883
- **Consistent with validation?** [x] Yes [ ] No

### STEP 3: Computational Efficiency

**Processing Time:**
- **Preprocessing time:** 45 minutes (for 50,000 samples)
- **Acceptable?** [x] Yes [ ] No

**Memory Requirements:**
- **Peak memory usage:** 2.3 GB
- **Acceptable?** [x] Yes [ ] No

**Training Time:**
- **Baseline training time:** 12 minutes
- **With intervention:** 15 minutes
- **Increase:** 25% (target: < 30%)

**Scaling Test:**
- **Dataset sizes tested:** 10K, 25K, 50K samples
- **Scaling behavior:** Linear scaling, acceptable

**Deployment Implications:**
- **Inference time impact:** 0% (pre-processing only affects training)
- **Production feasibility:** [x] Feasible [ ] Needs optimization [ ] Not feasible
- **Notes:** No inference overhead, only training-time preprocessing


## PHASE 3: IN-PROCESSING INTERVENTIONS (Component 3)

### COMPONENT 1: MODEL ARCHITECTURE ANALYSIS TEMPLATE

Following Component 3's template, we completed all questions:

**1. What model family are you working with?**
- Tree-based models (XGBoost - gradient boosting)

**2. How does your model learn?**
- [x] Batch (all data at once)
- [ ] Mini-batch (in small chunks)
- [ ] Online (continuously as new data arrives)

**3. What loss function does your model optimise?**
- Loss function: Binary cross-entropy
- Regularisation currently used: L2 regularization, early stopping
- Hyperparameter tuning approach: Grid search with cross-validation

**4. What are your fairness objectives?**
- Primary fairness definition(s): Equal Opportunity (TPR parity across groups)

**5. Is the chosen fairness objective likely to be feasible for your model without unacceptable performance loss?**
- [x] Yes
- [ ] Potentially with relaxed thresholds
- [ ] Likely involved unavoidable trade-offs

**6. How strictly must fairness be enforced?**
- [ ] Hard constraints (a hard rule that fairness must be met)
- [x] Soft penalties (a strong preference but not an absolute rule)
- [ ] Exploratory (something you are still exploring)

**7. What level of fairness assurance is required?**
- [ ] Formal, bounded guarantees (need to prove that unfairness cannot exceed a specific limit)
- [x] Measured improvement with monitoring (you must only show evidence of improvement and keep monitoring)
- [ ] Directional improvement only (the system just needs to be less unfair than before)

**8. How much optimisation instability and tuning complexity is acceptable?**
- [ ] Very low (training must work the same way every time)
- [x] Moderate (some tuning is acceptable but failures must be manageable)
- [ ] High (experimentation is acceptable)

**9. What are the model's technical and organisational constraints?**
- Available computational resources: CPU cluster, 32GB RAM per node
- Maximum acceptable training time increase: ≤ 30%
- Inference latency / throughput requirements: ≤ 50 ms per prediction
- Explainability requirements: Tree-based models acceptable (maintain interpretability)

**10. Does fairness need to be enforced across intersectional or multiple subgroups?**
- [ ] Single protected attribute only
- [x] Selected intersections (e.g., gender × race, single mothers)
- [ ] All relevant subgroups

### Compatibility Matrix Analysis

| In-Processing Technique | Linear Models | Tree-based Models | Neural Networks | Our Model (Tree-based) |
|------------------------|---------------|-------------------|-----------------|------------------------|
| **Constraint Optimisation** | High | **Low** | Medium | ❌ Not suitable |
| **Adversarial Debiasing** | Low | **Low** | High | ❌ Not suitable |
| **Fairness Regularisation** | High | **Medium** | High | ✅ Suitable |
| **Fair Representations** | Medium | **Low** | High | ❌ Not suitable |
| **Specialised Algorithms** | Medium | **High** | Low | ✅ Suitable |

**Decision:** Focus on **Fairness Regularisation** or **Specialised Algorithms** (fair tree splitting criteria).


## COMPONENT 2: TECHNIQUE SELECTION DECISION TREE

### Step 1: Model Architecture Assessment

**What type of model are you using?**
- Tree-based model → Go to Step 3B

### Step 2: Fairness Objective Selection

**What is your primary fairness definition?**
- Equal Opportunity

### Step 3B: Tree-based Model Approaches

**Equal Opportunity:**
- **Primary:** Specialised algorithms (e.g., fair splitting with weighted samples)
- **Alternative:** Fairness regularisation (e.g., regularised tree induction)

**Decision:** Use **Specialised Algorithms** (fair splitting criteria) as primary approach, with **Fairness Regularisation** as backup if specialized algorithms insufficient.

### Step 4: Compatibility and Constraint Check

**Confirm that the selected technique family:**
- Has Medium or High compatibility for tree-based models (Specialised Algorithms: High)
- Satisfies explainability constraints (tree-based models maintain interpretability)
- Satisfies deployment constraints (no inference overhead)

**Selected Technique:** **Specialised Algorithms** (fair splitting criteria for XGBoost)

---

## COMPONENT 3: IMPLEMENTATION PATTERN CATALOG

### Pattern 3: Fairness Regularisation

**Approach:** Incorporate fairness directly into the loss function as a soft penalty rather than a hard constraint.

**Implementation using Component 3's template:**

```python
# Using Component 3's Pattern 3 template
y_pred = model(X)

task_loss = cross_entropy(y_true, y_pred)

# Fairness penalty: TPR difference for Equal Opportunity
group_0 = y_pred[(z == 0) & (y_true == 1)]  # Male qualified applicants
group_1 = y_pred[(z == 1) & (y_true == 1)]  # Female qualified applicants
fairness_penalty = abs(mean(group_0) - mean(group_1))

loss = task_loss + lambda_fair * fairness_penalty

loss.backward()
optimizer.step()
```

**How we used this template:**
- **Trained model normally:** Started with existing XGBoost training loop
- **Defined fairness penalty:** TPR difference for Equal Opportunity (qualified applicants)
- **Tuned regularisation strength (lambda_fair):** Tested values [0.1, 0.5, 1.0, 5.0, 10.0]
  - Selected: lambda_fair = 5.0 (best balance: TPR gap 3.5 p.p., accuracy 0.837)
- **Evaluated trade-offs:** Trained with multiple lambda_fair values, selected based on fairness-performance balance

**Alternative: Specialised Algorithms (Fair Splitting Criteria)**

Since XGBoost doesn't natively support custom splitting criteria, we used sample weights from pre-processing combined with fairness monitoring:

```python
import xgboost as xgb

# Train with fairness-aware sample weights from pre-processing
model = xgb.XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    min_child_weight=1,
    max_depth=6,
    learning_rate=0.1,
    n_estimators=100
)

# Use combined weights from pre-processing (demographic + fairness weights)
model.fit(
    X_train_fair, y_train,
    sample_weight=combined_weights,
    eval_set=[(X_val, y_val)]
)

# Monitor fairness during training
fairness_metrics = calculate_fairness_metrics(model, X_val, y_val, protected_attr_val)
```

**Hyperparameter Tuning:**
- Tested lambda_fair values: [0.1, 0.5, 1.0, 5.0, 10.0]
- Selected: lambda_fair = 5.0 (optimal fairness-performance trade-off)
- Tested with different sample weight strengths from pre-processing

**Validation:**
- Gender TPR gap: 7 p.p. → 3.5 p.p. (-3.5 p.p.) ✅
- Race TPR gap: 9 p.p. → 5.2 p.p. (-3.8 p.p.) ✅
- Performance: Accuracy 0.845 → 0.837 (-0.8% additional, -1.9% cumulative)
- **Status:** Near compliance (gender gap <5 p.p., race gap slightly above)

---

## COMPONENT 4: INTEGRATION VERIFICATION FRAMEWORK

Following Component 4's Validation Testing Protocol:

### 1. Baseline Establishment

**Train model without fairness intervention:**
- **Model performance:** Accuracy: 0.856, AUC: 0.890, Precision: 0.78, Recall: 0.82
- **Fairness metrics:** Gender TPR gap: 18.0 p.p., Race TPR gap: 12.0 p.p.

### 2. Fairness Intervention Validation

**Chosen in-processing fairness technique:** Fairness Regularisation (Pattern 3)

**Train model with in-processing technique:**
- **Model performance:** Accuracy: 0.837, AUC: 0.887, Precision: 0.76, Recall: 0.80
- **Fairness metrics:** Gender TPR gap: 3.5 p.p., Race TPR gap: 5.2 p.p.

### 3. Fairness-Performance Trade-Off Analysis

**Compare baseline vs. in-processing:**
- **Model performance:** Accuracy: -0.019 (-1.9%), AUC: -0.003 (-0.3%), Precision: -0.02, Recall: -0.02
- **Fairness metrics:** Gender TPR gap: -14.5 p.p. (improvement), Race TPR gap: -6.8 p.p. (improvement)

### 4. Robustness Testing

**Subgroup performance (including intersections):**

| Intersection | Baseline TPR | After In-Processing TPR | Change |
|--------------|-------------|------------------------|--------|
| White Male | 0.88 | 0.84 | -0.04 |
| White Female | 0.82 | 0.81 | -0.01 |
| Black Male | 0.75 | 0.80 | +0.05 ✅ |
| Black Female | 0.62 | 0.78 | +0.16 ✅ |
| Single Mothers | 0.60 | 0.76 | +0.16 ✅ |

**Model performance:** Consistent across subgroups (accuracy variance <0.5%)

**Fairness metrics:** Consistent improvement across all intersectional groups

**Sensitivity to hyperparameter changes:**
- Tested lambda_fair ±20%: Fairness metrics stable (TPR gap variation <0.5 p.p.)
- Model performance stable (accuracy variation <0.3%)

**Behavior with distribution shifts:**
- Tested on temporal splits (different time periods): Fairness improvements maintained
- Performance stable across time periods

### Success Criteria Evaluation

- **Primary fairness metric improved by at least 10%:** Gender TPR gap improved by 80.6% (18 p.p. → 3.5 p.p.)
- **Performance decrease no more than 5%:** Accuracy decreased by 1.9% (within 5% threshold)
- **Consistent improvement across subgroups:** All intersectional groups show improvement
- **Stable behavior with minor hyperparameter changes:** TPR gap variation <0.5 p.p. with ±20% lambda_fair changes

## PHASE 4: POST-PROCESSING REFINEMENT (Component 4)

## COMPONENT 1: TRANSFORMATION SELECTION SYSTEM

### STEP 1: Identify your Primary Fairness Goal

Following Component 1's decision tree:

**Selected: Option 2: Equal opportunity**
- **Fairness issue:** Qualified individuals have unequal outcomes
- **Recommended techniques (in order):**
  1. Group-specific Threshold (Component 2) Applied
  2. Calibration techniques (Component 3): Platt Scaling Applied
  3. If disparities persist, consider Learned Transformation or Monotonic Transformation

**Status after Components 1 & 2:** TPR gap reduced to 0.8 p.p., no additional transformation needed.

### STEP 2: What Deployment Constraints Exist?

**Constraint 1:** Protected attributes unavailable at inference
- **Status:** Protected attributes ARE available at inference (legally permitted for fairness purposes)

**Constraint 2:** Regulatory requirement for explainability
- **Status:** Group-specific thresholds and Platt scaling are interpretable and auditable
- **Recommended techniques:** Group-Specific Threshold (Component 2), Calibration techniques (Component 3) Applied

**Constraint 3:** Real-time decision requirements
- **Status:** Precomputed parameters applied (thresholds and calibration parameters)
- **Recommended techniques:** Temperature Scaling and Score Normalisation (lightweight)
- **Applied:** Platt scaling is lightweight and efficient

### STEP 3: Check What Model Outputs Are Available

**1. Probability estimates:**
- Model outputs probability estimates (0-1 range)
- **Recommended techniques (in order):**
  1. Calibration techniques (Component 3) Applied (Platt Scaling)
  2. Probability-preserving transformations: Not needed (calibration sufficient)

### COMPONENT 2: THRESHOLD OPTIMISATION FRAMEWORK

### STEP 1: Choose a Fairness Goal

Following Component 2's options:

**Selected: OPTION 2: Equal Opportunity**
- **Fairness Goal:** Ensure qualified individuals have equal chances of being selected across groups
- **What threshold does:** Thresholds are adjusted so true positive rates match across groups
- **Mathematical formulation:** P(Ŷ=1|Y=1,A=a) = P(Ŷ=1|Y=1,A=b) for all groups a,b

### STEP 2: Search for Suitable Thresholds

Following Component 2's procedure:

**1. Split validation data by protected groups:**
- Male: 25,000 samples
- Female: 15,000 samples
- Intersections: Single mothers (1,200 samples), etc.

**2. For each group (including intersections):**

**Male Group:**
- Evaluated thresholds: [0.10, 0.12, 0.14, 0.15, 0.16, 0.18, 0.20]
- **Documented:**
  - Selection rate at each threshold
  - True positive rate at each threshold
  - False positive rate at each threshold
  - Overall performance metrics (accuracy, AUC)

**Female Group:**
- Evaluated thresholds: [0.10, 0.12, 0.14, 0.15, 0.16, 0.18, 0.20]
- **Documented:** Same metrics as Male group

**3. Identify threshold combinations satisfying Equal Opportunity:**
- Found: Male threshold = 0.15, Female threshold = 0.12 achieves TPR parity (both ~0.80)

**4. Filter by business constraints:**
- Minimum approval rate: 65% (must maintain)
- Acceptable performance loss: ≤5% accuracy reduction
- **Selected thresholds:** Male = 0.15, Female = 0.12 (meets all constraints)

**5. Documented:**
- **Selected thresholds:** Male: 0.15, Female: 0.12
- **Resulting fairness improvements:** TPR gap reduced from 3.5 p.p. to 0.8 p.p.
- **Performance trade-offs:** Accuracy: 0.837 → 0.835 (-0.2%), Approval rate maintained at 65%

### STEP 3: Decide How Thresholds are Applied

Following Component 2's options:

**Selected: Option 1: Group-specific thresholds**
- Each group gets its own threshold (Male: 0.15, Female: 0.12)
- **When to use:** Legally permitted and protected attributes are available at inference time ✅
- **Justification:** UK Equality Act 2010 allows group-specific adjustments for fairness purposes when documented and justified

### STEP 4: Deploy and Monitor

Following Component 2's monitoring requirements:

**Monitoring plan (quarterly):**
- **Model performance by group:** Track accuracy, AUC, precision, recall per group
- **Fairness metrics:** Track TPR gap, FPR gap, demographic parity gap
- **Score distribution drift:** Monitor score distributions for shifts over time

**Alert thresholds:**
- TPR gap >5 p.p. → Trigger review
- Score distribution shift >10% → Trigger recalibration

### STEP 5: Summary Report

Following Component 2's questionnaire:

1. **What is your chosen fairness goal?** Equal Opportunity (TPR parity)
2. **What are your validated sets of thresholds?** Male: 0.15, Female: 0.12
3. **What is your justification for how these thresholds are applied?** Group-specific thresholds legally permitted under UK Equality Act 2010 for fairness purposes; documented causal analysis justifies intervention; maintains business performance
4. **What is your monitoring plan?** Quarterly review of fairness metrics, performance by group, and score distribution drift

## COMPONENT 3: CALIBRATION IMPLEMENTATION TEMPLATE

### STEP 1: Is Calibration Needed?

Following Component 3's assessment procedure:

**1. Divide validation data by protected groups:**
- Male: 25,000 samples
- Female: 15,000 samples

**2. For each group:**

**Male Group:**
- **Reliability diagram:** Points align closely with diagonal (well-calibrated)
- **Expected Calibration Error (ECE):** 0.03
- **Maximum Calibration Error (MCE):** 0.05
- **Probability ranges:** Consistent calibration across all ranges (0-1.0)

**Female Group:**
- **Reliability diagram:** Points consistently above diagonal (systematic overestimation)
- **Expected Calibration Error (ECE):** 0.08
- **Maximum Calibration Error (MCE):** 0.12
- **Probability ranges:** Overestimation most pronounced in 0.3-0.6 range (3-5 percentage points)

**3. Cross-group comparison:**
- **Reliability curves:** Male curve aligns with diagonal, Female curve above diagonal
- **ECE comparison:** Male 0.03 vs. Female 0.08 (significant difference)
- **MCE comparison:** Male 0.05 vs. Female 0.12 (significant difference)
- **Miscalibration pattern:** Group-specific (symmetric would show similar patterns)
- **Regions of largest divergence:** 0.3-0.6 probability range (where many decisions are made)

**4. Final Decision:**
- ECE differs meaningfully across groups (0.03 vs 0.08)
- Same score corresponds to different risks across groups (70% score = 73% actual risk for women vs 70% for men)
- Probability scores are used in decision-making
- **Conclusion:** Calibration is needed

### STEP 2: Select an Appropriate Calibration Method

Following Component 3's options:

**Selected: OPTION 1: Platt Scaling (Parametric)**

**Rationale:**
- Miscalibration is smooth and approximately monotonic (reliability diagram shows consistent pattern)
- Validation data is moderate in size (15,000 female samples sufficient)
- Interpretability and auditability are important (regulatory requirements)
- Want to avoid overfitting (parametric approach more stable than non-parametric)

**When to use criteria met:**
- Moderate miscalibration: (ECE 0.08, not extreme)
- Limited/moderate validation data: (15K samples per group)
- Interpretability important: (regulatory compliance)
- Avoid overfitting: (parametric approach)

### STEP 3: Fit and Apply the Calibration Model

Following Component 3's guidelines:

**1. Fit calibration models separately for each demographic group:**
- Used dedicated calibration dataset (separate from training and test sets)
- Male calibration model: Fitted on 10,000 male validation samples
- Female calibration model: Fitted on 6,000 female validation samples

**2. Do not refit the base model:**
- Base XGBoost model remains unchanged

**3. Apply group-specific calibration transformations to raw outputs:**
- Male: Apply Platt scaling transformation
- Female: Apply Platt scaling transformation

**4. Use the same calibration method across groups:**
- Both groups use Platt scaling (consistent approach)

**5. Record fitted parameters for auditability:**
- Male: A = 1.02, B = -0.01
- Female: A = 0.98, B = -0.04

**6. Verify calibration improvement on held-out data:**
- **Re-plotted reliability diagrams per group:**
  - Male: Maintained alignment with diagonal (ECE: 0.03 → 0.02)
  - Female: Improved alignment (ECE: 0.08 → 0.03)
- **Calculated ECE/MCE values:**
  - Male ECE: 0.02, MCE: 0.04
  - Female ECE: 0.03, MCE: 0.05
- **Compared differences between groups:**
  - ECE gap: 0.05 → 0.01 (significant improvement)
  - MCE gap: 0.07 → 0.01 (significant improvement)

**Calibration Formulas:**
- **Men:** P(default) = 1/(1 + exp(-(1.02*score - 0.01)))
- **Women:** P(default) = 1/(1 + exp(-(0.98*score - 0.04)))


## COMPONENT 4: INTEGRATION WORKFLOW DESIGN

### STEP 1: Assessment Phase

Following Component 4's assessment requirements:

**Documented:**
- **Fairness Metrics:** 
  - Demographic parity gap: 4 p.p. (Male: 67%, Female: 63%)
  - Equal opportunity gap: 3.5 p.p. (Male TPR: 0.84, Female TPR: 0.805)
  - Equalized odds gaps: TPR gap 3.5 p.p., FPR gap 2.1 p.p.
- **Calibration Assessment:**
  - ECE for Men: 0.03, ECE for Women: 0.08
  - Reliability diagrams: Women show systematic overestimation (~3%)
  - Calibration pattern: "Women have systematically overestimated default risk by ~3%"
- **Performance Metrics:**
  - Accuracy: 0.837, AUC: 0.887, F1: 0.81
  - Business metrics: Approval rate 65%, Expected loss £2.3M annually
- **Operational Constraints:**
  - Protected attributes available at inference: Yes
  - Explainability requirements: Required (regulatory)
  - Real-time latency limits: ≤50ms per prediction
  - Regulatory restrictions: None (group-specific adjustments permitted)
- **ROC Analysis:**
  - Generated ROC curves per group to visualize fairness-performance trade-offs
  - Identified optimal operating points for each group

### STEP 2: Method Selection

Following Component 4's method selection:

**Selected techniques based on Component 3 decision tree:**
- **Primary:** Group-Specific Thresholds (Component 1) for Equal Opportunity
- **Secondary:** Calibration (Component 2) for Predictive Parity
- **Rationale:** Combined approach addresses both TPR gap and miscalibration

### STEP 3: Application Phase

Following Component 4's documentation requirements:

**Documented:**
- **All formulas with fitted parameters per group:**
  - Male calibration: P(default) = 1/(1 + exp(-(1.02*score - 0.01)))
  - Female calibration: P(default) = 1/(1 + exp(-(0.98*score - 0.04)))
- **Transformation factors:** Not applicable (no score transformation used)
- **Decision rules:** Group-specific thresholds (Male: 0.15, Female: 0.12)
- **Monitoring setup:**
  - Fairness metrics: TPR gap, demographic parity gap (weekly)
  - Performance metrics: Accuracy, AUC, approval rate (daily)
  - Calibration quality: ECE per group (monthly)
  - Alert thresholds: Fairness gap >5 p.p., ECE >0.05

**Validation:**
- Tracked both fairness and performance metrics during implementation
- Validated intervention on hold-out test set: Improvements generalized (TPR gap: 0.8 p.p. on test set)

### Monitoring & Maintenance

Following Component 4's monitoring requirements:

**Monitoring Metrics:**
- **Fairness Metrics:** Demographic parity gap, equal opportunity gap, equalized odds gaps (tracked weekly)
- **Calibration Quality:** ECE/MCE per group (assessed monthly for calibration drift)
- **Performance Metrics:** Accuracy, AUC, business metrics (approval rates, default rates)
- **Coverage Metrics:** Not applicable (not using rejection classification)

**Maintenance Actions:**
- Detect and respond to data or fairness drift
- Re-optimize thresholds quarterly or when drift detected
- Re-fit calibration models if ECE increases >0.05
- Set alert thresholds: Fairness gap >5 p.p., ECE >0.05
