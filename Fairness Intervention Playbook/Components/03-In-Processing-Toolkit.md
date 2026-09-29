# IN-PROCESSING FAIRNESS TOOLKIT

## INTRODUCTION

The In-Processing Fairness Toolkit embeds fairness constraints directly into model training, creating structurally fair models rather than applying post-hoc corrections. By modifying the optimisation objective, training procedure or model architecture, in-processing methods ensure fairness is baked into the model's learned parameters.

## PRE-PROCESSING TOOLKIT STRUCTURE

This toolkit has 4 core components:

- **Component 1 - Model Architecture Analysis Template:** Identifies which techniques work with specific model types.

- **Component 2 - Technique Selection Decision Tree:** Guides users from fairness goals to in-processing methods.

- **Component 3 - Implementation Pattern Catalog:** Provides reusable code templates.

- **Component 4 - Integration Verification Framework:** Validates fairness improvements.

---

## COMPONENT 1: MODEL ARCHITECTURE ANALYSIS TEMPLATE

This template helps you analyse how well different in‑processing techniques fit your model and constraints. Note down your answers for each model you are using.

**1. What model family are you working with?** 
*This matters as different fairness techniques only work with certain model types* 

[Insert e.g. Linear models (logistic regression, linear SVM), Tree-based models (decision trees, random forests, gradient boosting), Neural networks (feedforward, convolutional, recurrent) or specify other]

**2. How does your model learn?**
*Understanding optimisation properties is essential for determining whether fairness constraints can be enforced during training*

- [ ] Batch (all data at once)
- [ ] Mini‑batch (in small chunks)
- [ ] Online (continously as new data arrives)

**3. What loss function does your model optimise?** 
- Loss function: (e.g. cross‑entropy, hinge, MSE)
- Regularisation currently used: (e.g. L1/L2, dropout, early stopping)
- Hyperparameter tuning approach: (e.g. grid search, Bayesian, manual)

**4. What are your fairness objectives?**
- Primary fairness definition(s): (e.g. Demographic Parity, Equal Opportunity, Equalized Odds or other)

**5. Is the chosen fairness objective likely to be feasible for your model without unacceptable performance loss?**
- [ ] - Yes 
- [ ] - Potentially with relaxed thresholds 
- [ ] - Likely involved unavoidable trade-offs 

**6. How strictly must fairness be enforced?** 
*Here you are deciding how non-negotiable fairness is in the system.*

  - [ ] Hard constraints (a hard rule that fairness must be met)
  - [ ] Soft penalties  (a strong preference but not an absolute rule)
  - [ ] Exploratory (something you are still exploring)

**7. What level of fairness assurance is required?** 
*This is about how strong you claims needs to be when someone asks "How fair is this system?"* 
- [ ]- Formal, bounded guarantees (need to prove that unfairness cannot exceed a specific limit)
- [ ]- Measured improvement with monitoring (you must only show evidence of improvement and keep monitoring)
- [ ]- Directional improvement only (the system just needs to be less unfair than before)

**8. How much optimisation instability and tuning complexity is acceptable?** 
- [ ]- Very low (training must work the same way every time)
- [ ]- Moderate (some tuning is acceptable but failures must be manageable)
- [ ]- High (experimentation is acceptale)

**9. What are the model's technical and organisational constraints?**
- Available computational resources: (CPU/GPU, memory limits)
- Maximum acceptable training time increase: (e.g. ≤ 30%)
- Inference latency / throughput requirements: (e.g. ≤ 50 ms per prediction)
- Explainability requirements: (e.g. must remain linear / tree‑based; neural nets acceptable)

**10. Does fairness need to be enforced across intersectional or multiple subgroups?**

- [ ] Single protected attribute only
- [ ] Selected intersections (e.g. gender × income)
- [ ] All relevant subgroups

**Compatibility Matrix (which techniques fit which model families)**

| In-Processing Technique | How it encodes fairness during training | Linear Models | Tree-based Models | Neural Networks | Key considerations (from materials) |
|------------------------|------------------------------------------|---------------|-------------------|-----------------|-------------------------------------|
| **Constraint Optimisation** | Adds explicit fairness constraints to the optimisation problem | **High** | **Low** | **Medium** | Works best with convex or relaxable objectives; often requires specialised solvers; difficult to integrate with standard tree training; can increase training time substantially; may impact explainability if approximations are used |
| **Adversarial Debiasing** | Uses an adversary to remove protected-attribute information from learned representations | **Low** | **Low** | **High** | Requires differentiable models and stable gradient flow; introduces training instability and tuning complexity; unsuitable for tree-based models; works best with larger datasets; explainability is reduced |
| **Fairness Regularisation** | Adds a fairness penalty term to the loss function (soft constraints) | **High** | **Medium** | **High** | Flexible and relatively stable; does not provide hard guarantees; penalty weight controls fairness–performance trade-off; easier to integrate into existing training pipelines; commonly used when strict constraints are infeasible |
| **Fair Representations** | Learns a new feature space optimised for fairness and utility | **Medium** | **Low** | **High** | Requires representation learning stage; often implemented via neural networks; may reduce interpretability of downstream models; adds complexity to training pipeline; effective when proxy features drive bias |
| **Specialised Algorithms** | Uses model-specific fair variants (e.g. fair trees, fair boosting) | **Medium** | **High** | **Low** | Designed specifically for certain model families; preserves model structure and explainability; limited availability across model types; typically preferred for tree-based models in regulated settings |

**How to use this matrix**

- “High” indicates techniques that integrate naturally with the model’s training process.
- “Medium” indicates techniques that are feasible but may require approximation, relaxation or trade-offs.
- “Low” indicates techniques that are technically possible but impractical due to optimisation, explainability or stability constraints.

Use these ratings together with the model’s technical and organisational constraints to rule out unsuitable techniques before proceeding to the Technique Selection Decision Tree.

---

## COMPONENT 2: TECHNIQUE SELECTION DECISION TREE

This decision tree guides users from model architecture and fairness goals to appropriate in-processing techniques, using the outputs of the Model Architecture Analysis Template.

**Step 1: Model Architecture Assessment**

**What type of model are you using?**
- Linear model → Go to Step 3A
- Tree-based model → Go to Step 3B
- Neural network → Go to Step 3C
- Other → Consider model-agnostic approaches

**Step 2: Fairness Objective Selection** 

**What is your primary fairness definition?** 
- Demographic Parity 
- Equal Opportunity 
- Individual Fairness

Proceed to model specific branches below based on Step 1. 

**Step 3A: Linear Model Approaches**

- Demographic parity
    - Primary: Constraint optimisation with optimisation-based preprocessing
    - Alternative (if strict constraints infeasible): Fairness regularisation
- Equal opportunity
    - Primary: Constraint optimization with adjusted thresholds
    - Alternative: Fairness regularisation
- Individual fairness → Fairness regularisation (e.g.similarity-based regularization)

**Step 3B: Tree-based Model Approaches**

- Demographic parity
    - Primary: Specialised algorithms (e.g. fair splitting criteria)
    - Alternative: Fairness regularisation (e.g. regularised tree induction)
- Equal opportunity: 
    - Primary: Specialised algorithms (e.g. fair splitting with weighted samples)
    - Alternative: Fairness regularisation (e.g. regularised tree induction)
- Individual fairness → Fairness regularisation (e.g. regularised tree induction)

**Step 3C: Neural Network Approaches**

- Demographic parity
    - Primary: Adversarial debiasing
    - Alternative: Fairness regularisation
- Equal opportunity
    - Fairness regularisation (e.g. multi-task learning with fairness head)
    - Altnernative: Adversarial debiasing 
- Individual fairness → Fairness regulairsation (e.g. gradient penalties or contrastive learning)

**Step 4: Compatibility and Constraint Check**
Confirm that the select technique family: 
- Has Medium or High compatibility for the model type 
- It satisfied explanability and deployment contraints 

If not, select the listed alternative. 


## COMPONENT 3: IMPLEMENTATION PATTERN CATALOG

This catalog provides four implementation patterns for integrating fairness into model training. Each pattern includes a code implementation structure. 

**Pattern 1: Constraint Optimisation for Linear Models**

**Approach** This patterns enforces fairness as a hard rule during training. This pattern is best suited to simple, convex models where this fairness constraint is feasible. 

**Reusable code template**

```python
theta = initialize_parameters()

def task_loss(theta, X, y):
    y_pred = model(X, theta)
    return cross_entropy(y, y_pred)

def fairness_constraint(theta, X, z):
    y_pred = model(X, theta)
    group_0 = y_pred[z == 0]
    group_1 = y_pred[z == 1]
    return abs(mean(group_0) - mean(group_1))

minimize(
    objective=task_loss(theta, X, y),
    subject_to=[fairness_constraint(theta, X, z) <= epsilon]
)

```
**How to use this code template**
- Define your prediction task: Replace model(X, theta) and cross_entropy with your actual model and loss function.
- Choose a fairness definition: Modify fairness_constraint to reflect your chosen fairness metric
(e.g. demographic parity, equal opportunity).
- Set the tolerance parameter (epsilon): Smaller values enforce stricter fairness but may reduce feasibility or accuracy.
- Use a constrained optimiser: Implement the minimize(...) step using a solver that supports constraints.


**Pattern 2: Adversarial Debiasing for Neural Networks**

**Approach:** Train a model to maximize prediction accuracy while minimizing an adversary's ability to predict protected attributes.

**Reusable code template**

```python
representation = encoder(X)
y_pred = predictor(representation)

z_pred = adversary(gradient_reverse(representation))

task_loss = cross_entropy(y_true, y_pred)
adversary_loss = cross_entropy(z_true, z_pred)

loss = task_loss - lambda_adv * adversary_loss

loss.backward()
optimizer.step()
```

**How to use this template**
- Split your model into parts
    - encoder: learns internal representations
    - predictor: predicts the main outcome
    - adversary: predicts the protected attribute
- Apply gradient reversal: Use a gradient reversal mechanism so the encoder learns to hide protected information.
- Set the adversarial weight (lambda_adv): Higher values increase fairness pressure but may reduce task performance.
- Train both models together: Optimise the combined loss in a single training loop.

**Pattern 3: Fairness Regularisation** 

**Approach:** Incorporate fairness directly into the loss function as a soft penalty rather than a hard constraint.

**Reusable code template**
```python
y_pred = model(X)

task_loss = cross_entropy(y_true, y_pred)

group_0 = y_pred[(z == 0) & (y_true == 1)]
group_1 = y_pred[(z == 1) & (y_true == 1)]
fairness_penalty = abs(mean(group_0) - mean(group_1))

loss = task_loss + lambda_fair * fairness_penalty

loss.backward()
optimizer.step()
```

**How to use this template**
- Train your model normally: tart with your existing training loop.
- Define a fairness penalty: Replace fairness_penalty with a differentiable fairness metric.
- Tune the regularisation strength (lambda_fair): Increasing this value improves fairness at the cost of accuracy.
- Evaluate trade-offs: Train with multiple lambda_fair values to understand the fairness-performance balance.

**Pattern 4: Multi-Objective Scalarisation**

**Approach:** This pattern treats fairness and predictive performance as separate objectives and combines them into a single optimisation problem using a weighted sum. Rather than committing to a single fairness–performance balance upfront, the model is trained multiple times across a range of weighting values. Each trained model represents a different trade-off point.

**Reusable code template**
```python
def combined_objective(theta, lambda_weight):
    performance_loss = task_loss(theta, X, y)
    fairness_loss = fairness_metric(theta, X, y, z)
    return (
        (1 - lambda_weight) * performance_loss +
        lambda_weight * fairness_loss
    )

models = []
for lambda_weight in lambda_grid:
    theta = train_model(
        objective=lambda t: combined_objective(t, lambda_weight)
    )
    models.append(theta)

```
**How to use this template**
- Define separate objectives: Implement one loss for performance and one for fairness.
- Choose a range of weights (lambda_grid): Each value corresponds to a different fairness–performance trade-off.
- Train multiple models: Each trained model represents a different point on the Pareto frontier.
- Select a final model: Compare results and choose a model based on stakeholder priorities or policy requirements.


## COMPONENT 4: INTEGRATION VERIFICATION FRAMEWORK

After implmenting the selected in-processing fairness techniques, the next area of focus is now verification. The technique tou adopt is only suitable if it can show that it improves fairness and maintains acceptable model performance. The following framework helps you ensure that you chosen technique is sufficiently validated. Take notes as you go through. 


**Validation Testing Protocol:**

*1. Baseline establishment:*
- Train model without fairness intervention to establish a reference point and document: 
    - Model performance (e.g. accuracy, AUC, precision, recall): _______
    - Fairness metrics : _______

*2. Fairness Intervention validation:*
- Chosen in-processing fairness technique:_______
- Train model with your chosen in-processing technique and document: 
    - Model performance 
    - Fairnes metrics:________

*3. Fairness-Performance Trade-Off Analysis*
- Compare the results of the baseline and the in-processing fairness technique:
    - Model performance:______(improvemenet/drop)
    - Fairness metrics: ________(improvement/drop)

*3. Robustness testing:*
- Run the test on subgroup performance (including intersections of protected groups) and document: 
    - Model performance:_____
    - Fairness metrics : _____
- Record model performance/ fairness metrics results to changing parameters.
- Sensitivity to hyperparameter changes
- Behavior with distribution shifts

**Success Criteria:**
- Primary fairness metric improved by at least 10%
- Performance decrease no more than 5%
- Consistent improvement across subgroups
- Stable behavior with minor hyperparameter changes