# IMPLEMENTATION GUIDE

This guide provides practical advice for implementing the Fairness Intervention Playbook. It addresses intersectional fairness considerations, domain/problem-type adaptations and organisational requirements.

## INTERSECTIONAL FAIRNESS CONSIDERATIONS

### Causal Fairness Toolkit
- Include intersectional combinations (e.g., Black women, older immigrants) as separate categories
- Map causal pathways for intersectional groups (e.g., Gender × Race → Employment → Approval)
- Use Bayesian methods for intersectional groups with n<50
- Test all relevant intersections (minimum: race × gender)

### Pre-Processing Toolkit
- Use intersectional weights (e.g., weight by Gender × Race combinations)
- Apply SMOTE to intersectional groups with severe underrepresentation
- Validate improvements for all intersectional groups
- Report maximum disparity across all intersections

### In-Processing Toolkit
- Explicitly state intersectional requirements (e.g., "Selected intersections: gender × race, single mothers")
- Include intersectional penalties (e.g., TPR variance across all intersections)
- Test fairness metrics for all intersectional combinations
- Verify no intersection shows degradation

### Post-Processing Toolkit
- Evaluate thresholds for intersectional groups (e.g., single mothers, older Black women)
- Fit calibration models for intersections when sample sizes sufficient
- Test thresholds/calibration for intersectional groups
- Monitor intersectional metrics in production

### Best Practices

1. **Identify Relevant Intersections:** Start with most vulnerable combinations (e.g., race × gender × socioeconomic status)
2. **Handle Small Sample Sizes:** Use Bayesian methods for intersections with n<50, pool similar intersections when causal structures match
3. **Validate Intersectional Improvements:** Test all selected intersections after each intervention, report maximum disparity
4. **Monitor Intersectional Fairness:** Track intersectional metrics in production dashboards, set alert thresholds


## ADAPTABILITY GUIDELINES

### Domain Adaptations

#### Finance (Lending, Credit, Insurance)
- **Fairness Priorities:** Equal Opportunity, Predictive Parity
- **Common Bias Sources:** Historical discrimination in labels, zip code as proxy for race, credit scores reflect historical barriers
- **Recommended Sequence:** Causal Fairness → Pre-Processing (remove proxies, reweight) → In-Processing (Equal Opportunity constraints) → Post-Processing (threshold optimization + calibration)
- **Timeline:** 5-6 weeks (includes legal review)
- **Intersectional Focus:** Race × Gender, Race × Income, Age × Gender

#### Healthcare (Diagnosis, Treatment, Resource Allocation)
- **Fairness Priorities:** Equal Opportunity, avoid false negatives
- **Common Bias Sources:** Underrepresentation in clinical data, historical treatment access disparities, proxy features
- **Recommended Sequence:** Causal Fairness → Pre-Processing (SMOTE, reweight for recall) → In-Processing (Equal Opportunity constraint) → Post-Processing (threshold optimization)
- **Timeline:** 4-6 weeks (includes clinical validation)
- **Intersectional Focus:** Race × Gender × Age, Gender × Disability, Race × Socioeconomic Status

#### Hiring & Employment
- **Fairness Priorities:** Equal Opportunity, intersectional fairness
- **Common Bias Sources:** Historical hiring decisions, resume features as proxies, recommendation letter language differences
- **Recommended Sequence:** Causal Fairness → Pre-Processing (remove proxies, fair representation learning) → In-Processing (adversarial debiasing) → Post-Processing (threshold optimization)
- **Timeline:** 6-8 weeks (includes extensive legal review)
- **Intersectional Focus:** Race × Gender, Gender × Disability, Race × Age

### Problem Type Adaptations

#### Binary Classification
- **Fairness Definitions:** Demographic Parity, Equal Opportunity, Equalized Odds, Predictive Parity
- **Best Interventions:** Pre-Processing (reweighting, SMOTE), In-Processing (fairness regularization, constrained optimization), Post-Processing (threshold optimization, calibration)
- **Key Metrics:** TPR/FPR/FNR differences, intersectional metrics
- **Intersectional Considerations:** Test TPR/FPR for all intersectional combinations, apply intersectional reweighting

#### Regression
- **Fairness Definitions:** Statistical Parity, Bounded Group Loss, Individual Fairness
- **Best Interventions:** Pre-Processing (reweighting, fair representation learning), In-Processing (fairness regularization), Post-Processing (score transformation, calibration)
- **Key Metrics:** Group mean prediction differences, group MAE/MSE differences, intersectional mean/error differences
- **Intersectional Considerations:** Test mean predictions and errors for intersections, apply intersectional fairness constraints

#### Ranking
- **Fairness Definitions:** Exposure Parity, Representation Parity, Individual Fairness
- **Best Interventions:** Pre-Processing (reweight training pairs), In-Processing (fairness-aware learning to rank), Post-Processing (re-ranking, position-aware adjustments)
- **Key Metrics:** Exposure ratio, top-k representation proportions, intersectional exposure/representation
- **Intersectional Considerations:** Test exposure and representation for intersections, apply intersectional re-ranking


## IMPLEMENTATION GUIDELINES: ORGANISATIONAL CONSIDERATIONS

### Necessary Expertise

**ML Engineer:**
- Required: Fairness metrics computation, implementation of fairness techniques (Fairlearn, AIF360), pipeline integration
- Upskilling: Causal inference basics, intersectional fairness implementation
- Time Commitment: 50-100% during implementation phase

**Data Scientist:**
- Required: Causal graph construction, statistical testing, calibration assessment, intersectional analysis
- Upskilling: Domain-specific causal knowledge, fairness definitions
- Time Commitment: 30-50% during causal analysis and validation phases

**Domain Expert:**
- Required: Domain knowledge, feature classification (resolving vs. non-resolving), business impact assessment
- Upskilling: Causal graph interpretation, fairness definitions
- Time Commitment: 20-30% throughout project

**Legal/Compliance Officer:**
- Required: Regulatory requirements, risk assessment, documentation
- Upskilling: Technical fairness definitions, fairness-accuracy trade-offs
- Time Commitment: 10-20% during planning, validation, and deployment phases

### Integration with Development Processes

**ML Development Lifecycle Integration:**

| Development Stage | Fairness Activity | Toolkit(s) | Outputs |
|------------------|------------------|-----------|---------|
| Problem Framing | Review audit findings; identify bias sources | Causal Fairness | Causal graph, discrimination pathways, intersectional analysis |
| Data Collection & Preparation | Apply pre-processing interventions | Pre-Processing | Transformed training data, intersectional weights |
| Model Development | Embed fairness constraints in training | In-Processing | Fair model parameters, intersectional constraints |
| Model Evaluation | Validate fairness metrics across groups | Validation Framework | Fairness/performance metrics, intersectional results |
| Pre-Deployment | Apply post-processing refinements | Post-Processing + Validation | Production-ready fair model, intersectional thresholds |
| Deployment | Monitor fairness metrics | Ongoing monitoring | Fairness dashboards, intersectional alerts |


## WORKING WITH BLACK-BOX / THIRD-PARTY AI SYSTEMS (E.G., CHATGPT)

Many organisations increasingly rely on third-party or "black-box" AI systems (e.g., LLM APIs) for parts of their pipeline. These systems present distinct fairness, transparency and accountability challenges that must be explicitly addressed. When doing so, treat the third-party system as another node in your causal graph (Causal Fairness Toolkit) and ask where you can still intervene via Pre-Processing, In-Processing (on surrounding models) and Post-Processing.

### Key Decision Points 

- **Causal Fairness Toolkit:** Treat the black-box as a variable in your DAG; run discrimination pathway analysis and counterfactual checks to understand where vendor-driven effects occur and whether they are legitimate or problematic.
- **Pre-Processing Toolkit:** Control what you send into the vendor system—standardise and filter prompts, remove or transform proxies and apply intersectional reweighting when training any local models that use vendor outputs as features.
- **In-Processing Toolkit:** Apply fairness constraints not inside the vendor model but in your own models that wrap, gate or re-rank vendor outputs. 
- **Post-Processing Toolkit:** Use threshold optimisation, calibration and score transformation on vendor scores or derived scores to correct systematic disparities; combine this with rejection/deferral options so high-risk cases are escalated to humans rather than decided solely by the black box.

By explicitly walking through these decision points—with documented evidence and clear articulation of risks—you can justify when and how to use black-box / third-party systems, and when the residual risk is too high for certain high-stakes or vulnerable intersectional groups.

## WORKING WITH BLACK-BOX / THIRD-PARTY AI SYSTEMS (E.G., CHATGPT)

Many organisations use third-party AI systems (like ChatGPT or other AI services) that they cannot see inside or modify. These "black-box" systems create special fairness challenges: you cannot directly fix bias inside them, but you can still take steps to ensure fair outcomes.

### Key Decision Points

**1. Understanding How the Third-Party System Affects Fairness**
- **What this means:** Before using a third-party AI, map out how it fits into your decision process. Does it help make final decisions (like approving loans), or does it provide information that your team then uses? Does it treat different groups differently?
- **How to do this:** Use the Causal Fairness Toolkit to draw a simple diagram showing: (1) what information goes into the third-party system, (2) what it produces and (3) how that affects your final decisions. Test whether changing someone's protected characteristics (like race or gender) would change the outcome—if it would, that indicates potential bias.
- **Why this matters:** If the third-party system is making final decisions in high-stakes areas (like hiring or lending), and you cannot control or monitor it, you may be creating unfair outcomes without realising it.

**2. Controlling What Goes Into the System**
- **What this means:** You can control what information you send to the third-party AI. For example, if you are using ChatGPT to help screen job applications, you can remove information that might reveal someone's race or gender from the prompts you send.
- **How to do this:** Use the Pre-Processing Toolkit to: (1) clean and standardize the information you send to the vendor (2) remove or transform features that act as proxies for protected characteristics (like zip codes that correlate with race) and (3) if you train your own models using the vendor's outputs, ensure your training data represents all groups fairly.
- **Why this matters:** Even if the vendor's AI is biased, you can reduce harm by carefully controlling what information it sees and ensuring your own systems treat all groups fairly.

**3. Adding Your Own Fairness Checks**
- **What this means:** You can build your own models that review, filter, or re-rank the outputs from the third-party system. For example, if ChatGPT generates candidate rankings, you can build a separate model that ensures those rankings are fair across different groups.
- **How to do this:** Use the In-Processing Toolkit to train your own models that take the vendor's outputs and apply fairness rules. These "wrapper" models can ensure that even if the vendor's AI has biases, your final decisions are fair.
- **Why this matters:** This is often your best option for ensuring fairness when you cannot modify the vendor's system directly. However, you must test these wrapper models carefully to ensure they actually improve fairness and do not create new problems.

**4. Adjusting How You Use the System's Outputs**
- **What this means:** After the third-party system produces results, you can adjust how you interpret and act on those results. For example, you might use different decision thresholds for different groups, or you might send uncertain cases to human reviewers instead of relying solely on the AI.
- **How to do this:** Use the Post-Processing Toolkit to: (1) set different decision thresholds for different groups (where legally permitted), (2) calibrate scores so they mean the same thing across groups, and (3) create rules that send high-risk or uncertain cases to human review rather than making automated decisions.
- **Why this matters:** Even if you cannot change the vendor's system, you can still correct for unfair patterns in its outputs before making final decisions.

**5. Monitoring and Responding to Changes**
- **What this means:** Third-party AI systems can change without notice, which might suddenly make them less fair. You need to continuously monitor whether the system treats different groups fairly and have a plan to respond if problems arise.
- **How to do this:** Regularly check fairness metrics (like approval rates, error rates) across different groups. Track these metrics over time and set up alerts if fairness degrades. Ensure your contract with the vendor allows you to audit and test the system for fairness issues.
- **Why this matters:** Without monitoring, a vendor update could suddenly make your system unfair, and you might not notice until it causes real harm.

### Making the Decision

By working through these decision points—documenting what you can control, testing for fairness issues, and implementing appropriate safeguards—you can make informed decisions about when and how to use third-party AI systems. In some cases, especially for high-stakes decisions affecting vulnerable groups, the risks may be too high, and you may need to use systems you can fully control and audit instead.