# PRE-PROCESSING FAIRNESS TOOLKIT

## INTRODUCTION

Use this pre-processing fairness toolkit to correct biased data before training models. It provides structured methods to address representation gaps, proxy features and label bias so that downstream models learn from data that better reflects your fairness goals.

## PRE-PROCESSING TOOLKIT STRUCTURE

This toolkit has **4 core components** that work together:

- **Component 1 - Technique Catalog:** Documents available pre-processing approaches with their mathematical foundations, strengths, limitations, and use cases.

- **Component 2 - Selection Decision Tree:** Guides technique selection based on bias patterns, fairness definitions and and constraints.

- **Component 3 - Configuration Guidelines:** Provides parameter tuning guidance for different techniques.

- **Component 4 - Evaluation Framework:** Establishes a framework for measuring intervention effectiveness.

---

## COMPONENT 1: TECHNIQUE CATALOG

The Technique Catalog documents pre-processing approaches with their technical foundations and practical application guidance.

| Technique | Approach Type | What It Does | Mathematical Foundation | When to Use | Strengths | Limitations |
|-----------|---------------|--------------|------------------------|-------------|-----------|-------------|
| **Instance Weighting** | Reweighting | Assigns weights to training examples to balance group representation without changing the dataset | Weighted empirical risk: R̂_w(h) = (1/n) Σᵢ w(xᵢ, aᵢ) · L(h(xᵢ), yᵢ) where w(x,a) = P_target(A=a) / P_train(A=a) | Moderate imbalances (2:1 to 10:1), algorithm supports weights, need to preserve all data | Preserves all data, adjustable strength, no inference overhead, computationally efficient | Not all algorithms support weights, can increase variance with extreme weights, less effective for severe imbalances (>10:1) |
| **Prejudice Removal** | Reweighting | Modifies labels to reduce correlation with protected attributes while maintaining predictive utility | ŷᵢ* = argmin_y' (yᵢ - y')² + η · Disc(y', A) where Disc(y', A) = \|Cov(y', A)\| / (Var(y') · Var(A)) | Historical bias in decision-making, labels from biased human judgments, outcome recording biased | Targets label bias directly, maintains sample counts, tunable intervention strength | May introduce new biases, requires careful calibration, assumes labels can be meaningfully adjusted |
| **Oversampling** | Data Generation | Increases minority group representation by duplicating existing instances or generating synthetic examples | D'_minority = {xᵢ ~ Uniform(D_minority) : i = 1, ..., N_target} where N_target > \|D_minority\| | Severe class imbalances (>10:1), algorithms without weight support, need exact target distribution | Works with any algorithm, simple to implement, preserves all original data | Risk of overfitting through duplication, may not add new information, increases training time and memory |
| **Undersampling** | Data Generation | Reduces majority group representation by randomly selecting subset of instances | D'_majority = {xᵢ ~ Uniform(D_majority) : i = 1, ..., N_target} where N_target < \|D_majority\| | Severe imbalances with large datasets, computational constraints, majority group has redundant information | Reduces computational cost, works with any algorithm, achieves exact distributions | Discards potentially useful information, may lose important patterns, can reduce overall model performance |
| **Uniform Sampling** | Data Generation | Selects equal number of examples from each demographic group regardless of original distribution | \|D'_a\| = k for all groups a, creating balanced dataset | Need exact demographic parity, small to moderate dataset sizes, equal representation desired | Simple to implement, guarantees perfect balance, transparent approach | May oversample small groups excessively, discards majority data, can distort natural distributions |
| **Preferential Sampling** | Data Generation | Strategically selects examples that contradict biased patterns or reduce measured disparities | Select xᵢ with probability p(xᵢ) ∝ contribution to fairness objective | Specific bias patterns identified, need targeted intervention, sufficient data per group | Directly targets identified biases, more efficient than random sampling, maintains data quality | Requires fairness metric definition, complex implementation, may introduce new biases if misapplied |
| **SMOTE** | Data Generation | Generates synthetic minority examples by interpolating between existing instances | x_synthetic = xᵢ + λ(xⱼ - xᵢ) where xⱼ is k-nearest neighbor and λ ~ Uniform(0,1) | Moderate dimensionality (p<100), continuous features, minority samples 50-500 | Creates novel examples, reduces overfitting vs duplication, well-established method | May generate unrealistic examples, not appropriate for categorical features, k parameter affects quality |
| **Generative Models** | Data Generation | Uses deep learning models (VAEs, GANs) to synthesize realistic examples for underrepresented groups | Learn p(X\|A=a) then sample x_new ~ p(X\|A=a_minority) for minority groups | Severe underrepresentation (n<100), high-dimensional data, need realistic synthetic samples | Can generate highly realistic samples, captures complex distributions, scales to high dimensions | Computationally expensive, requires substantial data for training, difficult to validate quality, may amplify existing biases |
| **Disparate Impact Remover** | Feature Transformation | Transforms features to reduce correlation with protected attributes while preserving rank ordering | f̃ᵢ = λ · f̄_a + (1-λ) · fᵢ where λ ∈ [0,1] is repair level, f̄_a is group mean | Proxy discrimination (zip→race), need interpretability, regulated environments, rank preservation required | Preserves relative ordering, adjustable intensity (λ), maintains interpretability, computationally efficient | May reduce predictive power, most effective for continuous features, assumes linear relationships |
| **Fair Representation Learning** | Feature Transformation | Learns latent representations that remove demographic information while preserving task utility | min_φ L_task(φ) + α · L_fairness(φ) + β · L_reconstruction(φ) where L_fairness = I(Z; A) | Complex proxy discrimination, high-dimensional features, multiple proxy features, interpretability tradeable | Handles complex non-linear relationships, scales to high dimensions, addresses multiple protected attributes | Reduces interpretability, requires hyperparameter tuning, computationally intensive, difficult to audit |
| **Optimal Transport** | Feature Transformation | Transforms features by transporting source distribution to target distribution with minimal cost, moving data points along optimal transport plan | min_γ ∫ c(x,y) dγ(x,y) subject to marginal constraints, where γ is transport plan and c is cost function | Severe distribution shifts between groups, need theoretically-grounded transformation, continuous features | Theoretically principled, handles complex distribution shifts, preserves data geometry, smooth transformations | Computationally expensive (O(n³) naive, O(n² log n) with Sinkhorn), requires choosing cost function, sensitive to outliers |
| **Expert Relabeling** | Label Correction | Manual review and correction of training labels by domain experts using clear criteria | Human expert judgment with documented criteria and inter-annotator agreement validation | Historical bias in labels, need high accuracy, have domain expert resources | Most accurate when done carefully, provides gold standard labels, enables validation of automated approaches | Time-intensive, expensive, requires expert availability, may introduce annotator bias if not managed carefully |
| **Label Smoothing** | Label Correction | Softens hard labels by converting them to probabilistic distributions based on confidence or uncertainty | y_smooth = (1-α)·y_hard + α·y_uniform where α ∈ [0,1] controls smoothing strength | Noisy or uncertain labels, systematic bias unclear, need probabilistic label representation | Reduces overfitting to noisy labels, provides uncertainty quantification, computationally simple | May not address systematic bias, requires tuning smoothing parameter, less effective for clear discrimination patterns |
| **Counterfactual Labeling** | Label Correction | Adjusts labels based on causal analysis, modifying outcomes to reflect counterfactual scenarios where protected attributes differ | y_cf = f_causal(X, A←a', U) where causal model f_causal determines label under counterfactual protected attribute | Causal model available, need to address discrimination through causal pathways, want rigorous fairness | Directly addresses causal discrimination, theoretically principled, enables counterfactual fairness | Requires accurate causal DAG, computationally complex, assumes causal model correctness |
| **Conditional Generation** | Data Generation | Generates synthetic examples conditioned on protected attributes using conditional VAE/GAN architectures | Learn p(X\|A=a) using conditional generative model, then sample x_new ~ p(X\|A=minority) | Need realistic synthetic samples for specific demographic groups, have sufficient data to train conditional models | Fine-grained control over demographic composition, generates realistic samples for target groups, preserves complex feature relationships | Requires substantial training data, computationally expensive, needs careful validation of conditional quality |
| **Counterfactual Data Augmentation** | Data Generation | Creates matched pairs of examples differing only in protected attributes to train counterfactually fair models | Generate pairs (x, A=a) and (x_cf, A=a') where x_cf preserves causally independent features | Want model to learn counterfactual fairness, have causal model identifying causal structure | Directly operationalizes counterfactual fairness, helps models learn invariance to protected attributes, addresses causal discrimination | Requires accurate causal model, computationally intensive, may generate unrealistic combinations |
| **Causal/Synthetic Data Generation** | Data Generation | Generates entirely new fair datasets using generative models with explicit causal constraints from structural causal models | GAN/VAE with causal constraints: min_G max_D L_GAN + λ·L_causal where L_causal enforces causal structure | Need fair data respecting causal structure, want to address root causes of bias, have structural causal model | Most rigorous approach, addresses bias at causal level, creates data with desired fairness properties by design | Most complex to implement, requires accurate causal model, computationally very expensive, difficult to validate |


## COMPONENT 2: SELECTION DECISION TREE

This decision framework helps you navigate from identified bias patterns to suitable pre-processing interventions. Begin by examining your causal analysis findings to determine which bias mechanisms are present, then follow the corresponding pathway below. Account for intersections of demographic groups specifically throughout the process. 


### STEP 1: Classify Your Bias Pattern

1. Start by documenting your data sources, collection metholodogies and potential selection biases.
2. Document your bias patterns and refer to the table below to understand how to intervene. 


```
┌─────────────────────────────────────────────────────────────────┐
│                    START: Identify Bias Pattern                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────────────────┐
        │  Which bias pattern matches your causal analysis?    │
        └─────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┬──────────┴──────────┬──────────────┐
        │                     │                     │                     │              │
        ▼                     ▼                     ▼                     ▼              ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐ ┌───────────────┐
│ Representation│   │ Label Bias    │   │ Proxy Features │   │ Severe Under- │ │ Multiple      │
│ Gaps or       │   │ (Historical   │   │ (Features      │   │ representation│ │ Bias Types    │
│ Outcome       │   │ discrimination│   │ correlate with │   │ (<5%)         │ │ Coexist       │
│ Disparities   │   │ or annotator  │   │ protected      │   │               │ │               │
│               │   │ stereotypes)  │   │ attributes)    │   │               │ │               │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘   └───────┬───────┘ └───────┬───────┘
        │                   │                     │                   │                 │
        ▼                   ▼                     ▼                   ▼                 ▼
   Section A            Section B            Section C            Section D          Section E
```



### SECTION A: Reweighting & Resampling/Data Generation
*This section covers both resampling (selecting/duplicating existing data) and data generation (creating new synthetic examples).*

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECTION A: Representation Issues              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────────────────┐
        │  Question 1: Does your algorithm support            │
        │           sample_weight parameter?                 │
        └─────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
        ┌───────────────┐           ┌───────────────┐
        │      YES      │           │      NO       │
        │  REWEIGHTING  │           │ RESAMPLING/   │
        │               │           │ DATA GEN      │
        └───────┬───────┘           └───────┬───────┘
                │                           │
                ▼                           ▼
        ┌───────────────────┐       ┌───────────────────┐
        │   Question 2     │       │   Question 3      │
        │  (Reweighting)    │       │ (Resampling/Gen)  │
        └───────────────────┘       └───────────────────┘
```


**Question 2:** Which imbalance scenario matches your data? *(When using Reweighting)*

| Imbalance Scenario | Recommended Approach |
|-------------------|---------------------|
| **Basic demographic imbalance**<br>(e.g., 80% men, 20% women) | **Instance Weighting**<br>(inverse frequency approach) |
| **Missing positive outcomes for specific groups**<br>(e.g., few approved loans for minority group) | **Instance Weighting**<br>(weight by group × outcome interaction) |
| **Bias localised to specific feature intersections**<br>(e.g., only high-income men affected) | **Instance Weighting**<br>(feature-stratified weighting, balance outcomes within comparable feature ranges) |
| **Training stability concerns?** | **Instance Weighting**<br>(gradual ramp-up strategy)<br>Initial: sqrt(target_weight), maximum: 2-5× |

---

**Question 3:** How many samples exist in your minority group? *(When using Resampling/Data Generation)*

*Note: Resampling methods work with existing data (select/duplicate), while data generation creates new synthetic examples.*

| Sample Count | Recommended Approach | Type | Considerations |
|-------------|---------------------|------|---------------|
| **n ≥ 100** (excess majority samples) | **Undersampling**<br>(randomly downsample majority) | Resampling | Potential information loss |
| **n ≥ 100** (require additional minority samples) | **Oversampling**<br>(replicate minority instances) | Resampling | Overfitting risk |
| **50 ≤ n < 100** (continuous feature space) | **SMOTE**<br>(synthetic interpolation method) | Generation | Creates new synthetic points |
| **Able to prioritise by fairness impact** | **Preferential Sampling**<br>(targeted selection strategy) | Resampling | - |
| **n < 50** (critical underrepresentation) | **Generative Models**<br>(VAE/GAN architectures) | Generation | Thoroughly validate synthetic sample quality |

---

### SECTION B: Label Correction
*Addressing: Labels containing historical bias or annotator stereotypes*

**Question 1:** Do your labels exhibit measurable historical discrimination patterns?
*(Example: Equally qualified women rejected 42% more often than men)*

- **YES, the pattern is systematic and measurable**
  - → **Prejudice Removal** (algorithmic label modification)
  - Demands clear justification and thorough documentation

**Question 2:** Are domain experts available to review and validate label corrections?

- **YES** → **Expert Relabeling** (human review following established criteria)
  - Resource-intensive but highest accuracy
  - Use alongside prejudice removal for cross-validation

**Question 3:** Are labels characterised by noise or uncertainty rather than systematic bias?

- **YES** → **Label Smoothing** (probabilistic label adjustment)
  - Convert hard labels to probability distributions based on confidence levels

**Question 4:** Do you possess a validated causal model for counterfactual analysis?

- **YES** → **Counterfactual Labeling** (modify labels according to causal pathways)
  - Most theoretically sound approach but requires complete causal DAG
---

### SECTION C: Feature Transformation
*Addressing: Proxy discrimination (features that correlate with protected attributes)*

**Question 1:** Is the bias isolated to a small number of specific features?
*(Example: Zip code, education institution, communication style)*

- **YES, and model interpretability is essential**
  - → **Disparate Impact Remover**
  - Initial λ=0.5, adjust to 0.7-1.0 range
  - Maintains relative ordering within demographic groups

- **YES, but interpretability is not a priority**
  - → **Optimal Transport** (suitable for tabular data)
  - Mathematically rigorous, preserves information content

**Question 2:** Is the bias distributed across numerous features or present in high-dimensional data?
*(Example: Text descriptions, multiple correlated features)*

- **High-dimensional or unstructured data** (text, images)
  - → **Fair Representation Learning** (adversarial/VAE methods)
  - Constructs latent representations that mask protected attribute information

- **Multiple tabular features exhibiting complex relationships**
  - → **Optimal Transport** or **Fair Representations**
  - Selection depends on interpretability requirements

**Question 3:** Do specific intersectional groups demonstrate unique bias patterns?
*(Example: Black Women face unique discrimination)*

- **YES** → Implement transformation using **intersectional fairness transformations**
  - Modify features to eliminate correlation with combined attributes (e.g., race × gender)
  - Target intersectional combinations, not individual attributes separately

---

### SECTION D: Data Generation
*Addressing: Severe underrepresentation (<5%)*

**Question 1:** Is group representation critically low (<5%) or is your data extremely sparse?

- **YES, require realistic synthetic samples**
  - → **Conditional Generation** (conditional VAE/GAN architectures)
  - Model p(X|A=minority), produce synthetic examples
  - Quality check: assess sample realism

**Question 2:** Do you want your model to achieve counterfactual fairness?
*(What would happen if this person had a different protected attribute?)*

- **YES** → **Counterfactual Data Augmentation**
  - Generate matched example pairs that differ only in protected attributes
  - Requires validated causal model

**Question 3:** Do you need completely new fair datasets that respect causal relationships?

- **YES** → **Causal/Synthetic Data Generation** (structural causal model integration)
  - GAN/VAE architectures incorporating causal constraints
  - Most comprehensive approach but highest complexity

---
### SECTION E: Combined Approach
*Addressing: Multiple bias types present*

**When several bias patterns coexist, apply interventions sequentially:**

| Step | Priority Area | Intervention Method | Reasoning |
|------|---------------|---------------------|-----------|
| **Step 1** | **LABEL BIAS** (if detected) | Prejudice removal or expert relabeling | Biased labels compromise all subsequent interventions |
| **Step 2** | **PROXY DISCRIMINATION** | Disparate impact removal or fair representations | Eliminate discriminatory pathways through features |
| **Step 3** | **REPRESENTATION IMBALANCE** | Instance weighting or resampling | Achieve balance after addressing feature and label issues |


## COMPONENT 3: CONFIGURATION GUIDELINES

The Configuration Guidelines help tune each technique to your specific context.

### Instance Weighting 

**Select weighting scheme based on fairness goal:** 
- Demographic parity: weight by group proportion
- Equal opportunity: weight by positive outcome proportion for each group
- Equalized odds: weight by both true positive and false positive rates

**Set Intervention Strength:**
- Start with moderate weights (square root of inverse frequency)
- Increase gradually if fairness improvements fall short
- Cap weights to prevent instability

**Validate:** Use weighted cross-validation, monitor loss convergence, check for overfitting and verify fairness gains.

### Prejudice Removal 

- To use this technique, start with a modification strength of 0.5. For small datasets or regulated domains, use a conservative strength between 0.3 and 0.5. For large datasets or performance-critical applications, you can use a stronger strength between 0.5 and 1.0. Adjust the strength within the range of 0.1 to 2.0 based on your results.
- When validating, monitor the reduction in correlation between modified labels and protected attributes. Ensure that labels remain meaningful after modification - the technique should reduce bias while preserving the predictive signal in your labels.

### Feature Transformation Techniques

**Disparate Impact Remover:** 
- Target features strongly correlated with protected attributes and check predictive power preservation.
- Begin with repair level of 0.5
- Consider preserving ranks within groups for sensitive applications

**Optimal Transport:** Best for complex, multidimensional features where simpler methods don't work well. 

**Fair Representation Learning:** Best for scenarios requiring comprehensive transformation of the feature space, particularly when dealing with complex data types like text, images, or highly dimensional tabular data where simpler transformations might be insufficient.

---

## COMPONENT 4: EVALUATION FRAMEWORK

Use this template to assess your intervention effectiveness:

### STEP 1: Fairness Metrics Assessment

**Primary Fairness Metrics:**
- Metric: _______________ (e.g., DPD, EOD, Equalized Odds)
- Before intervention: _______________
- After intervention: _______________
- Improvement: _______________ (percentage or absolute change)
- Threshold met? [ ] Yes [ ] No

**Intersectional Fairness:**
- Protected attributes tested: _______________
- Maximum disparity across intersections: _______________
- Specific high-risk comparisons identified: _______________

**Statistical Significance:**
- Test used: _______________
- p-value: _______________
- Significant improvement? [ ] Yes [ ] No (p < 0.05)

**Trade-offs observed:**
- Notes: _______________

### STEP 2: Predictive Performance

**Overall Performance Changes:**
- Accuracy: Before: _______________ After: _______________ Change: _______________
- AUC: Before: _______________ After: _______________ Change: _______________
- F1 Score: Before: _______________ After: _______________ Change: _______________

**Rank Ordering Preservation:**
- Spearman correlation within groups: _______________
- Acceptable? [ ] Yes [ ] No (target: ≥ 0.95)

**Feature Importance Changes:**
- Key features maintained? [ ] Yes [ ] No
- Notes: _______________

**Hold-out Set Testing:**
- Test set performance: _______________
- Consistent with validation? [ ] Yes [ ] No


### STEP 3: Computational Efficiency

**Processing Time:**
- Preprocessing time: _______________ (seconds/minutes)
- Acceptable? [ ] Yes [ ] No

**Memory Requirements:**
- Peak memory usage: _______________ (GB)
- Acceptable? [ ] Yes [ ] No

**Training Time:**
- Baseline training time: _______________
- With intervention: _______________
- Increase: _______________ % (target: < 30%)

**Scaling Test:**
- Dataset sizes tested: _______________
- Scaling behavior: _______________

**Deployment Implications:**
- Inference time impact: _______________ % 
- Production feasibility: [ ] Feasible [ ] Needs optimization [ ] Not feasible
- Notes: _______________