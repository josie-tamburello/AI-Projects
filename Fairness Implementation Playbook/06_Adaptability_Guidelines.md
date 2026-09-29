# Adaptability Guidelines

## Purpose

This guide helps you adapt the Fairness Implementation Playbook across different domains (healthcare, finance, education, etc.) and problem types (classification, regression, recommendation, etc.). While the playbook's core structure remains the same, specific elements need domain and problem-type adaptations.


## Section 1: Domain-Specific Adaptations

### Healthcare

**Protected Attributes:**
- Age, gender, race/ethnicity, disability status, socioeconomic status, geographic location
- **Special considerations:** Health conditions may be correlated with protected attributes but cannot be used as proxies

**Fairness Metrics:**
- Equal Opportunity (primary) - equal access to healthcare recommendations
- Calibration - prediction accuracy should be consistent across groups
- **Threshold:** Equal Opportunity difference ≤ 0.03 (stricter due to health impact)

**Regulatory Context:**
- HIPAA (US), GDPR (EU), Medical Device Regulations
- **Component 4:** Often High Risk due to health impact
- **Component 2:** May require medical ethics board involvement

**Component 1 Adaptations:**
- User stories must consider patient safety alongside fairness
- Acceptance criteria should include clinical validation requirements
- Sprint capacity: 25-30% (higher due to regulatory complexity)

**Component 2 Adaptations:**
- Governance bodies should include medical professionals and ethics boards
- Decision tiers may require clinical review for certain decisions
- Documentation must meet medical device documentation standards

**Component 3 Adaptations:**
- Classification models: Focus on diagnostic accuracy fairness
- Regression models: Focus on risk score calibration across groups
- Recommendation systems: Ensure treatment recommendations are fair

**Component 4 Adaptations:**
- Risk classification: Often High Risk (TRS typically 15-20)
- DPIA required for most healthcare AI systems
- Audit trail must support medical device regulations

---

### Finance (Lending, Credit Scoring)

**Protected Attributes:**
- Race, gender, age, marital status, geographic location
- **Special considerations:** Income and credit history may correlate with protected attributes but must be used carefully

**Fairness Metrics:**
- Equal Opportunity (primary) - equal approval rates for qualified applicants
- Demographic Parity (secondary) - representation balance
- **Threshold:** Equal Opportunity difference ≤ 0.05

**Regulatory Context:**
- Fair Lending Act (US), GDPR (EU), Financial Conduct Authority (UK)
- **Component 4:** High Risk for credit decisions
- **Component 2:** May require compliance officer involvement

**Component 1 Adaptations:**
- User stories must consider regulatory compliance alongside fairness
- Acceptance criteria should include explainability requirements (regulatory requirement)
- Sprint capacity: 20-25%

**Component 2 Adaptations:**
- Governance bodies should include compliance officers
- Decision tiers may require regulatory review for threshold changes
- Documentation must support regulatory audits

**Component 3 Adaptations:**
- Classification models: Focus on approval/rejection fairness
- Regression models: Focus on interest rate fairness (if applicable)
- Recommendation systems: Ensure financial product recommendations are fair

**Component 4 Adaptations:**
- Risk classification: High Risk for credit decisions (TRS typically 15-18)
- DPIA required for automated credit decisions
- Audit trail must support financial regulations

---

### Education

**Protected Attributes:**
- Race/ethnicity, socioeconomic status, first-generation status, disability status, geographic location
- **Special considerations:** Academic performance may correlate with socioeconomic factors

**Fairness Metrics:**
- Equal Opportunity (primary) - equal access to educational opportunities
- Demographic Parity (secondary) - representation in programs
- **Threshold:** Equal Opportunity difference ≤ 0.05

**Regulatory Context:**
- FERPA (US), GDPR (EU), Education-specific regulations
- **Component 4:** Medium to High Risk depending on use case
- **Component 2:** May require education administrators

**Component 1 Adaptations:**
- User stories must consider educational equity
- Acceptance criteria should include intersectional analysis (first-generation × race × socioeconomic status)
- Sprint capacity: 20%

**Component 2 Adaptations:**
- Governance bodies should include educators and student representatives
- Decision tiers may require educational review
- Documentation should support educational transparency

**Component 3 Adaptations:**
- Classification models: Focus on admission/recommendation fairness
- Regression models: Focus on grade prediction fairness
- Recommendation systems: Ensure course/program recommendations are fair

**Component 4 Adaptations:**
- Risk classification: Medium to High Risk (TRS typically 10-15)
- DPIA may be required for student data processing
- Audit trail must support educational regulations

---

### Criminal Justice

**Protected Attributes:**
- Race, gender, age, socioeconomic status
- **Special considerations:** Historical bias in criminal justice data requires careful handling

**Fairness Metrics:**
- Equalized Odds (primary) - equal true positive and false positive rates
- Calibration (secondary) - risk scores should be calibrated across groups
- **Threshold:** Equalized Odds difference ≤ 0.03 (stricter due to high stakes)

**Regulatory Context:**
- Criminal justice regulations, data protection laws
- **Component 4:** High Risk (TRS typically 18-22)
- **Component 2:** May require legal and community oversight

**Component 1 Adaptations:**
- User stories must consider justice and fairness principles
- Acceptance criteria should include community impact assessment
- Sprint capacity: 25-30%

**Component 2 Adaptations:**
- Governance bodies should include legal experts and community representatives
- Decision tiers require careful oversight due to high stakes
- Documentation must support legal proceedings

**Component 3 Adaptations:**
- Classification models: Focus on prediction fairness (recidivism, risk assessment)
- Regression models: Focus on risk score calibration
- Recommendation systems: Ensure resource allocation is fair

**Component 4 Adaptations:**
- Risk classification: High Risk (TRS typically 18-22)
- DPIA required
- Audit trail must support legal requirements

---

## Section 2: Problem Type-Specific Adaptations

### Classification Problems

**Common Use Cases:**
- Binary classification: Loan approval, hiring decisions, medical diagnosis
- Multi-class classification: Risk categorization, disease classification

**Component 1 Adaptations:**
- **SAFE Framework:** Focus on classification accuracy fairness
- **FAIR Framework:** Use classification-specific metrics (Equal Opportunity, Equalized Odds, Demographic Parity)
- **Acceptance Criteria:** Include confusion matrix analysis across groups

**Component 2 Adaptations:**
- **Decision Tiers:** Classification threshold adjustments may require Tier 2 review
- **Governance Gates:** Gate 3 should verify classification fairness across all classes

**Component 3 Adaptations:**
- **LLM:** Use classification-specific prompting strategies
- **Recommendation:** Not typically applicable
- **Vision:** Focus on classification accuracy across demographic groups

**Component 4 Adaptations:**
- **Risk Classification:** Classification systems often High Risk if they affect individuals
- **Documentation:** Model Cards should include per-class performance metrics

**Fairness Metrics for Classification:**
- Equal Opportunity (TPR difference)
- Equalized Odds (TPR and FPR differences)
- Demographic Parity (selection rate difference)
- Calibration (prediction probability accuracy)

---

### Regression Problems

**Common Use Cases:**
- Risk scoring: Credit scores, insurance premiums, medical risk scores
- Price prediction: Housing prices, salary prediction
- Resource allocation: Budget allocation, resource distribution

**Component 1 Adaptations:**
- **SAFE Framework:** Focus on prediction accuracy fairness
- **FAIR Framework:** Use regression-specific metrics (Calibration, Prediction Error Parity)
- **Acceptance Criteria:** Include error distribution analysis across groups

**Component 2 Adaptations:**
- **Decision Tiers:** Score threshold adjustments may require Tier 2 review
- **Governance Gates:** Gate 3 should verify calibration across groups

**Component 3 Adaptations:**
- **LLM:** Use regression-specific prompting (numerical prediction fairness)
- **Recommendation:** Not typically applicable
- **Vision:** Focus on regression accuracy across groups

**Component 4 Adaptations:**
- **Risk Classification:** Regression systems often High Risk if scores affect decisions
- **Documentation:** Model Cards should include calibration plots and error distributions

**Fairness Metrics for Regression:**
- Calibration (prediction accuracy consistency)
- Prediction Error Parity (equal error rates across groups)
- Conditional Statistical Parity (equal predictions conditional on true values)

---

### Recommendation Systems

**Common Use Cases:**
- Content recommendation: Job matching, course recommendations, product recommendations
- Resource recommendation: Treatment recommendations, financial product recommendations

**Component 1 Adaptations:**
- **SAFE Framework:** Focus on exposure and diversity fairness
- **FAIR Framework:** Use recommendation-specific metrics (Exposure Diversity, Provider-Side Fairness)
- **Acceptance Criteria:** Include exposure analysis across groups

**Component 2 Adaptations:**
- **Decision Tiers:** Re-ranking parameter adjustments may require Tier 2 review
- **Governance Gates:** Gate 3 should verify exposure fairness

**Component 3 Adaptations:**
- **Recommendation:** Use Component 3, Part B strategies (re-ranking, exposure balancing)
- **LLM:** Not typically applicable
- **Vision:** Not typically applicable

**Component 4 Adaptations:**
- **Risk Classification:** Recommendation systems often Limited to High Risk depending on impact
- **Documentation:** Model Cards should include exposure metrics and diversity measures

**Fairness Metrics for Recommendation:**
- Exposure Diversity (visibility across groups)
- Provider-Side Fairness (creator/provider exposure)
- User-Side Fairness (recommendation quality across user groups)
- Position Bias Correction

---

### Ranking Problems

**Common Use Cases:**
- Search ranking: Job search results, candidate ranking
- Priority ranking: Patient triage, resource prioritization

**Component 1 Adaptations:**
- **SAFE Framework:** Focus on ranking position fairness
- **FAIR Framework:** Use ranking-specific metrics (Position Bias, Ranking Fairness)
- **Acceptance Criteria:** Include position distribution analysis

**Component 2 Adaptations:**
- **Decision Tiers:** Ranking algorithm adjustments may require Tier 2 review
- **Governance Gates:** Gate 3 should verify ranking fairness

**Component 3 Adaptations:**
- **Recommendation:** Use Component 3, Part B strategies (re-ranking, position bias correction)
- **LLM:** Use ranking-specific prompting
- **Vision:** Not typically applicable

**Component 4 Adaptations:**
- **Risk Classification:** Ranking systems often Medium to High Risk
- **Documentation:** Model Cards should include position bias analysis

**Fairness Metrics for Ranking:**
- Position Bias (equal visibility across positions)
- Ranking Fairness (equal opportunity for top positions)
- Exposure Distribution (fair distribution across ranking positions)

---
