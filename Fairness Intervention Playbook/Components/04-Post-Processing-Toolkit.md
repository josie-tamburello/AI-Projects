# POST-PROCESSING FAIRNESS TOOLKIT

## INTRODUCTION

This toolkit provides a structured approach to address fairness issues in already-trained models by modifying their predictions or decision thresholds. Use post-processing when you cannot retrain the model but need to reduce bias in its outputs.

**POST-PROCESSING OVERVIEW**
- **Component 1 - Transformation Selection System:** For choosing techniques based on constraints and goals.
- **Component 2 - Threshold Optimisation Framework:** Implements group-specific thresholds for different fairness definitions.
- **Component 3 - Calibration Implementation Template:** Fixes probability estimation disparities.
- **Component 4 - Integration Workflow Design** Shows how to add post-processing to production pipelines.

## COMPONENT 1: TRANSFORMATION SELECTION SYSTEM

The Transformation Selection System guides you through all post-processing options to determine which intervention is appropriate given your fairness goal and deployment constraints. This component is composed of two parts: (1) a Transformation Technique Catalog that provides a comprehensive overview of all available post-processing techniques and (2) a Decision Tree that helps you select the most appropriate techniques based on your specific situation.

**TRANSFORMATION TECHNIQUE CATALOG:**

The catalog below provides a comprehensive overview of all available post-processing techniques. Use it as a reference to understand what each technique does and when it's appropriate to use. This overview helps you familiarise yourself with the full range of options before making a selection below.

| Technique Name | What It Is | When to Use | Category |
|----------------|------------|-------------|----------|
| **Group-Specific Thresholds** | Adjusts decision thresholds differently for each protected group to equalize selection rates, true positive rates, or both | Need to satisfy demographic parity, equal opportunity, or equalized odds; working with black-box models; cannot retrain; need quick deployment | Threshold Optimization |
| **Platt Scaling** | Fits a logistic regression model to transform raw model outputs into calibrated probabilities, applied separately for each group | Working with parametric models; moderate miscalibration; need simple, interpretable calibration; have sufficient validation data per group | Calibration |
| **Isotonic Regression** | Non-parametric method that fits a piecewise constant function transforming scores to calibrated probabilities while preserving rank order | Need flexible, non-parametric calibration; miscalibration patterns are non-linear; rank ordering must be preserved; have moderate to large validation sets | Calibration |
| **Temperature Scaling** | Divides logits by a single temperature parameter before applying softmax, applied separately for each group | Working with neural networks; systematic miscalibration across groups; need simple, computationally efficient calibration; have limited validation data | Calibration |
| **Beta Calibration** | Uses a parametric beta distribution to model the relationship between predictions and outcomes | Need naturally bounded probability estimates; working with probabilistic classifiers; want parametric approach with good theoretical properties | Calibration |
| **Learned Transformation Functions** | Discovers optimal mappings from original predictions to fair outputs through optimization on validation data; can use optimization-based learning, transfer learning, or adversarial methods | Simple transformations insufficient; need to address complex fairness requirements; can afford optimization complexity; have substantial validation data | Prediction Transformation |
| **Quantile Mapping** | Transforms predictions so that quantiles match across groups | Need to align prediction distributions; working with continuous scores; want to ensure similar score distributions across groups | Prediction Transformation |
| **Optimal Transport** | Finds the minimum cost transformation that aligns prediction distributions across groups using mathematical transport theory | Need principled distribution alignment; working with complex, multidimensional prediction patterns; want mathematically rigorous approach | Prediction Transformation |
| **Distribution Matching** | Learns transformations that minimize the statistical distance (e.g., KL divergence, Wasserstein distance) between group distributions | Need to minimize statistical distance between distributions; working with complex distributional patterns; want learned transformations that optimize distribution similarity | Prediction Transformation |
| **Monotonic Transformations** | Adjusts scores while preserving the order of predictions within groups | Need to maintain rank ordering; working with risk scores or rankings; want transformations that don't reverse relative positions | Score Transformation |
| **Constrained Re-Ranking** | Modifies rank positions to satisfy fairness criteria while minimizing changes to original ranking | Working with ranking systems; need to ensure fair representation in top results; want to balance ranking quality with fairness | Score Transformation |
| **Score Normalisation** | Adjusts score scales across groups to ensure comparable interpretation | Need to make scores comparable across groups; working with different score ranges per group; want consistent score interpretation | Score Transformation |
| **Decision Flipping** | Strategically flips specific binary decisions from positive to negative (or vice versa) to achieve group fairness | Need discrete decision adjustments; working with binary classification; can accept some individual-level changes; want simple intervention | Decision Flipping |
| **Confidence-Based Rejection** | Uses prediction confidence to identify cases where automated decisions should be deferred to human judgment | Model confidence varies across groups; want to reduce fairness errors in uncertain cases; have human review capacity; need to balance automation with fairness | Rejection Option Classification |
| **Cost-Sensitive Rejection** | Prioritizes human review based on the fairness impact of potential algorithmic errors | Different errors have different fairness consequences; want to optimize human review allocation; need to focus limited review resources where they help most | Rejection Option Classification |


**DECISION TREE FOR TECHNIQUE SELECTION:** 

Use the decision tree below to guide your selection process. Work through each step based on your specific fairness goals, deployment constraints and model characteristics. The decision tree will help you narrow down from the full catalog to the most appropriate techniques for your situation.

**STEP 1: Identify your Primary Fairness Goal**

Start by identifying what kind of unfairness you are trying to fix.

*Option 1:* Demographic parity 
- *Fairness issue*: selection rates/ score discributions differ across groups. 
- *Recommended techniques (in order):* 
        - Group-Specific Threshold (Component 2)
        - If thresholds insufficient, Quantile Transformation or Distribution Matching to be applied after calibration.

*Option 2:* Equal opportunity
- *Fairness issue:* qualified individuals have unequal outcomes
- *Recommended techniques (in order):* 
        - Group-specific Threshold (Component 2)
        - Calibration techniques, e.g. Platt Scaling, Isotonic Regression and Temperature Scaling  (Component 3)
        - If disparities persist, consider Learned Transformation or Monotonic Transformation.

*Option 3:* Individual fairness 
- *Fairness issue:* Relative ordering or prioritisation is unfair 
- *Recommended techniques (in order):* 
    - Calibration techniques, e.g. Platt Scaling, Isotonic Regression and Temperature Scaling  (Component 3) if scores are probabilities
    - If ordering remains unfair, consider Score Normalisation or Monotonic Transformation


**STEP 2: What Deployment Constraints Exist?**

**Constraint 1:** You don't have access to protected attribute information when making predictions
- *Recommended techniques:* 
    - Learned Transformation (can learn group-agnostic transformation during training)
    - Score Normalisation (applied uniform transformations without group labels)
    - Single-threshold decision rules 

**Constraint 2:** Regulatory requirement that you must be able to explain how your fairness intervention works to regulators, auditors or stakeholders. 
- *Recommended techniques (in order):* 
    -  Group-Specific Threshold (Component 2 - simple and interpretable)
    -  Calibration techniques, e.g. Platt Scaling, Isotonic Regression and Temperature Scaling  (Component 3) 

**Constraint 3:** Predictions must be generated quickly with minimal computational overhead
- *Recommended techniques:*
    - Apply precomputed parameters to transformations 
    - Lightweight: Temperature Scaling and Score Normalisation

**STEP 3: Check What Model Outputs Are Available**
The model's output format determines which techniques are feasible. 

1. Probability estimates 
- *Recommended techniques (in order):* 
    - Calibration techniques (Component 3) 
    - Probability-preserving transformations only: Monotonic Transformations or Learned Transformation Functions that maintain probability properties

2. Raw scores
-  *Recommended techniques (in order):* 
    - Score Normalisation (adjust score scales for comparability)
    - Monotonic Transformations (preserve ordering while adjusting values)
    - Quantile Mapping or Distribution Matching 

3. Binary decisions only
-  *Recommended techniques (in order):* 
    - Decision flipping 
    - Rejection Option Classification: Confidence-Based Rejection or Cost-Sensitive Rejection 
    - Defer uncertain cases to human judgment


## COMPONENT 2: THRESHOLD OPTIMISATION FRAMEWORK

Following Component 1, you may move to this part if the technique is relevant. The Threshold Optimisation Framework improves fairness without retraining the model by adjusting how prediction/decision scores are converted into decisions. 

**STEP 1: Choose a Fairness Goal**

Start by selecting the fairness definition you want to satisfy. Your choice determines how thresholds are adjusted and evaluated.

- **OPTION 1: Demographic Parity:** 
    - Fairness Goal: Ensure all protected groups are selected at the same rate.
    - What threshold does: Thresholds are adjusted so each group has an equal probability of receiving a positive decision.
    - Mathematical formulation: P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups a,b

- **OPTION 2: Equal Opportunity:** 
    - Fairness Goal: Ensure qualified individuals have equal chances of being selected across groups.
    - What threshold does: Thresholds are adjusted so true positive rates match across groups.
    - Mathematical formulation: P(Ŷ=1|Y=1,A=a) = P(Ŷ=1|Y=1,A=b) for all groups a,b

- **Equalized Odds:** 
    - Fairness Goal: Ensure both true positive rates and false positive rates are equal across groups.
    - What threshold does: Thresholds are adjusted to balance both error types simultaneously.
    - Mathematical formulation: P(Ŷ=1|Y=y,A=a) = P(Ŷ=1|Y=y,A=b) for all y ∈ {0,1} and groups a,b

**STEP 2: Search for Suitable Thresholds**

Now, use validation data to test how different thresholds affect fairness metrics and model performance.

**Procedure**
1. Split validation data by protected groups (e.g. men/ women)
2. For each group (including intersections of groups):  
    - Evaluate model outcomes across a range of threshold values.
    - Document: 
        - Selection rate
        - True positive rate
        - False positive rate 
        - Overall performance metrics (e.g. accuracy, AUC)
3. Based on your chosen fairness goal, identify threshold combinations that satisfy the fairness condition. 
4. From the threshold combination candidates, keep only the thresholds that meet business constraints (e.g. minimum approval rates, acceptable performance loss)
5. Document: 
    - Selected thresholds 
    - Resulting fairness improvements 
    - Any performance trade-offs

**STEP 3: Decide How Thresholds are Applied:**

Next, you will determine how your selected thresholds will be used in production.   

- **Option 1:** Group-specific thresholds 
    - This means that each group gets its own threshold 
    - *When to use:* when legally permitted and protected attributes are available

- **Option 2:** Single threshold with transformed scores 
    - *When to use:* when protected attributes cannot be used

- **Option 3** Use sampling-based approaches when neither option works

**STEP 4: Deploy and Monitor**

Threshold optimisation is not to be done once and then forgotten. After deployment, it is essential to monitor thresholds regularly (e.g. quarterly) by: 
    - Model performance by group 
    - Fairness metrics
    - score distribution drift 

**STEP 5: Summary Report**
To summarise this Threshold Optimisation Framework, please fill out the questionnaire below. 

1. What is your chosen fairness goal? 
2. What are your validated sets of thresholds? 
3. What is your justification for how these thresholds are applied? 
4. What is your monitoring plan? 

## COMPONENT 3: CALIBRATION IMPLEMENTATION TEMPLATE

Following Component 1, you may move to this part if the technique is relevant. The Calibration Implementation Template ensures probability estimates mean the same thing across groups. Without calibration, a score of 20% might correspond to 25% actual risk for one group and 15% for another, which creates inaccurate decision-making even when thresholds are the same.

**STEP 1: Is Calibration Needed?:**

Before applying any calibration method, first determine whether calibration is needed and where miscalibration occurs.

1. Divide validation data by protected groups (e.g. gender, race)
2. For each group:
   - Plot reliability diagram (predicted vs. actual probabilities)
   - Calculate Expected Calibration Error (ECE)
   - Optionally calculate Maximum Calibration Error (MCE) for worst-case risk
   - Identify probability ranges regions with significant miscalibration (e.g. consistent over or under estimation)

*Look out for curves above the diagonal (which suggest overestimation) and curves below the diagonal (which suggest underestimation)*

3. Cross-group comparison:  
    - Compare reliability curves across groups  
    - Compare ECE/ MCE values across groups
    - Identify whether miscalibration is symmetric or group-specific
    - Report the regions of largest divergence

4. Final Decision
Subject to the points above, calibration is needed if: 
- ECE differs meaningfully across groups 
- The same score corresponds to different risks across groups 
- Probability scores are used in decision-making

**STEP 2: Select an Appropriate Calibration Method:**

**Group-Specific Calibration Methods**

Choose a calibration method based on your data size, model type and risk tolerance.

**OPTION 1:Platt Scaling (Parametric)** 
- *What it does:* Platt scaling fits a logistic regression model that maps raw model scores transforming raw scores to calibrated probabilities. 
- *When to use:* 
    - Miscalibration is smooth and approximately monotonic
    - Validation data is limited or moderate in size 
    - Interpretability and auditability are important 
    - You want to avoid overfitting

**OPTION 2:Isotonic Regression**
- *What it does:* Isotonic regression adjusts model predictions so that higher scores correspond to higher probabilities, while preserving the original order of predictions.
- *Formula:* \[
P(Y=1|s) = \frac{1}{1 + \exp(-(As + B))}
\]
- *When to use:* 
    - Validation data is very large 
    - Calibration errors varies across different score ranges 
    - Reliability diagrams show irregular patterns 
    - Preserve ranking 


**OPTION 3: Temperature Scaling**
- *What is does:* Temperature scaling adjusts how confident the model's predictions are by applying a single "temperature" parameter to all predictions, making them more or less confident while keeping their relative order.
- *Formula:* P(Y=1|s) = 1 / (1 + exp(-s/T))
- *When to use:* 
    - The model is a neural network
    - The main issue is overconfidence 
    - Computational simplicity is required (minimal intervention)


**STEP 3: Fit and Apply the Calibration Model:**

Once you have selected the method of choice above, follow the following guidelines on fitting the method.  

1. Fit calibration models separately for each demographic group using a dedicated calibration dataset (not a training or test set)
2. Do not refit the base model 
3. Apply group-specific calibration transformations to raw outputs
4. Use the same calibration method across groups unless strongly justified 
5. Record fitted parameters for auditability
6. Verify calibration improvement on held-out data by: 
    - Re-plotting reliability diagrams per group
    - Calculating ECE/ MCE values 
    - Comparing the differences between the groups.


## COMPONENT 4: INTEGRATION WORKFLOW DESIGN

The Integration Workflow Design guides you through implementing post-processing interventions from assessment through deployment. Follow this workflow to systematically address fairness issues in trained models.

**STEP 1: Assessment Phase**

Evaluate baseline fairness metrics (e.g., demographic parity, equal opportunity, equalized odds) and identify where intervention can help. 

**Document:**
- **Fairness Metrics:** Demographic parity gap, equal opportunity gap, equalized odds gaps (TPR/FPR) per group
- **Calibration Assessment (if applicable):** ECE/MCE per group, reliability diagrams, calibration pattern description (e.g., "Group A systematically overestimates risk by ~3%")
- **Performance Metrics:** Accuracy, AUC, F1, business metrics (approval rate, default rate), expected loss/cost
- **Operational Constraints:** Protected attribute availability at inference, explainability requirements, real-time latency limits, regulatory restrictions
- **ROC Analysis (for threshold optimization):** Generate ROC curves per group to visualise fairness-performance trade-offs

**STEP 2: Method Selection**

Choose suitable post-processing techniques based on the fairness gap type and deployment constraints. Use Component 1 (Transformation Selection System) decision tree to guide selection.

**STEP 3: Application Phase**

Implement selected techniques on validation data and document all parameters, formulas and configurations.

**Documentation Requirements:**
- All formulas with fitted parameters per group
- Transformation factors or learned function parameters
- Decision rules and threshold values
- Monitoring setup and metrics to track

**Validation:** Track both fairness and performance metrics during implementation. Validate intervention on hold-out test set to ensure improvements generalize beyond validation data.

### Monitoring & Maintenance

Continuously monitor fairness, calibration, and predictive performance post-deployment to detect drift and maintain intervention effectiveness.

**Monitoring Metrics:**
- **Fairness Metrics:** Demographic parity gap, equal opportunity gap, equalized odds gaps (tracked weekly)
- **Calibration Quality:** ECE/MCE per group (assessed monthly for calibration drift)
- **Performance Metrics:** Accuracy, AUC, business metrics (approval rates, default rates)
- **Coverage Metrics (if using rejection classification):** Automation rate, deferral patterns across groups

**Maintenance Actions:**
- Detect and respond to data or fairness drift (e.g., changing group distributions, calibration degradation)
- Re-optimize thresholds, re-fit calibration models, or adjust transformation parameters quarterly or when drift detected
- Set alert thresholds for when re-intervention is needed 

**Note on Intersectional Fairness (Critical Reminder)** Always evaluate fairness not only across individual protected groups but also across their intersections, for example, Black women, older immigrants, or young disabled individuals. Models can appear fair when looking at single attributes but still hide severe biases at these intersections, which often affect the most vulnerable populations. Intersectional validation ensures that fairness improvements are holistic, not superficial.