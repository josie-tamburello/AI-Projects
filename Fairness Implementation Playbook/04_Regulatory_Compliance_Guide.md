# COMPONENT 4: Regulatory Compliance Guide

## Purpose

This section helps teams translate legal requirements (like the EU AI Act and GDPR) into concrete engineering tasks.

## How to navigate this component: 

- Complete Section 1 risk classification questionnaire
- Calculate TRS score 
- Review regulatory mapping matrix (Section 2) for your risk tier
- Generate required documentation using templates (Section 3)
- Set up audit trail logging (Section 4)
- Follow compliance timeline throughout development (Look at implementation guidelines) 

---

# SECTION 1: Risk Classification 

This risk classification questionnaire below helps you determine how risky each AI system is. The goal is to ensure that higher-risk AI systems automatically trigger stronger governance, documentation and oversight. Please could each cross-teams (legal, technical) work together to answer the questions below, document your answers and follow the decision tree. 

## STEP 1: Risk classification questionnaire: 

### (1) Territory: 
Does your application operate within the European Union or have European Union customers?  
If YES → Proceed to next section “Scope - EU AI ACT”  
If NO → Stop here, this application is not captured by EU laws. 

### (2) Existing Compliance Strategy: 
Do you currently have a compliance regime in place that factors in EU AI ACT and GDPR compliance requirements?  
If YES → Proceed to the next question.  
If NO → Proceed to Step 3.  
Have you correctly identified your risk level and compliance requirements under these EU laws, in line with the decision tree below (you may also view the table under Step 1 of Section 2: Regulatory Mapping for a more detailed overview of risk levels)?  
If YES → move to STEP 2.  
If NO → Go to Step 3. 

### (3) Scope - EU AI ACT:
Does your application do any of the following: a system for social scoring, exploiting vulnerable groups, subliminal manipulation, untargeted scraping of facial images or emotion recognition in workplaces?  
If YES → Stop here and do not proceed, this application is prohibited under EU AI Act, you cannot deploy or advance this application. Jump to Step 2 to confirm with TRS scoring.  
If NO → Proceed to next question.  
Does your application pose significant risk to health, safety, and fundamental rights? E.g. recruitment tools, employee monitoring, credit scoring and medical devices?  
If YES → Your application is considered a High Risk level under the EU AI Act.Proceed to section “Scope - GDPR”.  
If NO → Proceed to the next question.  
Does your application interact with consumers or impersonate humans? e.g.,chatbots, deepfakes?  
If YES → your application is considered a Limited Risk level under the EU AI Act. Proceed to section “Scope - GDPR”.  
If NO –: Proceed to the next question.  
Does your application have little risk to humans, such as spam filters and AI in video games?  
If YES → Your application is considered Minimal Risk under the EU AI act. Proceed to section “Scope - GDPR”.  
If NO → Proceed to next section “Scope - GDPR” 

### (4) Scope - GDPR:
Does your application process any personal data? (e.g. names, email address, mobile numbers)?  
If YES → Proceed to the next question.  
If NO → Take the risk level associated outlined in “Scope - EU AI ACT” above and move to the next question.  
Does your application process any special category data (e.g. personal data related to health information, race, ethnicity, religion?)  
If YES → this is considered High Risk level under GDPR and Article 9 of GDPR imposes additional conditions to be met. Proceed to the next question.  
If NO → Take the risk level associated outlined in “Scope - EU AI ACT” above and move to the next question.  
Does your application involve automated decision-making (decisions without human input?)  
If YES → proceed to the next question.  
If NO → Take the risk level associated outlined in “Scope - EU AI ACT”  
Does your application have a legal or significant effect on individuals, e.g. like in recruitment?  
If YES → your application is to be considered High Risk. Move to the next step.  
If NO → Take the risk level associated outlined in “Scope - EU AI ACT”. Move to the next step. 

### (5) Questionnaire Classification outcome: 
What is your assigned risk level as per the steps above?  
If High Risk and Limited Risk → proceed to STEP 2.  
If Unacceptable Risk → Do not proceed. You cannot deploy such an application. Revisit your product development process and tweak in line with EU requirements.  
If Minimal Risk → It is up to you whether to proceed as this would be voluntary compliance, not a legal requirement. Proceed to STEP 2 to further confirm this risk level quantitatively. 

---

## STEP 2: Quantitative Risk Scoring 

The Total Risk Score (TRS) provides a quantitative assessment of your AI system's risk level, to supplement the qualitative classification from Step 1. This scoring mechanism helps determine the appropriate governance tier and compliance requirements for your system.

TRS = (P x S) + E - M 

Where  
P = Probability (1-5) of harm occurring  
S= Severity (1-5) per Annex III category  
E = Exposure Factor (1-3) = EU citizens x duration of effect bracket  
M = Mitigation readiness (0 - 4) - design controls already in place. 

### TRS Tiers: 

| TRS Range | Risk Tier |
|---|---|
| > 15 | High (Tier 1) |
| 8 - 14 | Limited (Tier 2) |
| < 7 | Minimal (Tier 3) |

*As mentioned above, for minimal risk, compliance remains voluntary. 

---

## STEP 3: Overall Risk Classification Outcome

If High Risk or Limited Risk→ Proceed to Section 2 and follow the mapping to compliance tasks  
If Unacceptable Risk from Step 1 → Do not proceed. You cannot deploy such an application. Revisit your product development process and tweak in line with EU requirements  
If Minimal Risk→ It is up to you whether to proceed as this would be voluntary compliance, not a legal requirement. 

---

# SECTION 2: Regulatory Mapping 

## STEP 1: Legal Framework Overview 

Now we have established the risk level of your application, familiarise yourself with the laws we will be referring to in this playbook and the regulatory status of each risk level. 

The legal requirements considered in this playbook are: 

European Union AI Act: This legislation presents a risk-based framework for categorising AI systems into unacceptable, high-risk and limited-risk tiers with varying requirements. The table below gives you a snapshot of the risk levels, status, enforcement dates and max fines to understand the importance of this legislation. 

| Risk Level | Definition | Regulatory Status | Enforcement | Max Fines |
|---|---|---|---|---|
| Unacceptable Risk | Violates fundamental rights; includes systems for social scoring, exploiting vulnerable groups, subliminal manipulation, untargeted scraping of facial images, emotion recognition in workplaces. | Prohibited | 2 February 2025 | €35M or 7% of global annual turnover |
| High Risk | AI systems which pose significant risk to health, safety, and fundamental rights. E.g. recruitment tools, employee monitoring, credit scoring and medical devices. | Permitted subject to compliance with requirements (risk assessments, conformity checks, documentation, human oversight). | 2 August 2026 for Annex III systems and 2 August 2027 for others | €15M or 3% of global annual turnover |
| Limited/ Transparency Risk | Systems that interact with consumers or impersonate humans. e.g.,chatbots, deepfakes. | Permitted subject to transparency and information obligations. | 2 August 2026 | €15M or 3% of global annual turnover |
| Minimal Risk | Systems with little to no risk, such as spam filters and AI in video games; generally permitted without restriction. | Permitted with no restrictions. | N/A | N/A |

General Data Protection Regulations (GDPR) Article 22: where AI is used to make decisions that have a legal or significant effect on individuals like in recruitment, Article 22 of the UK GDPR applies. This says that individuals have the  “right not to be” subject to automated decision making unless (1) they give explicit consent (2) it is necessary for a contract or (3) it is required by law. 

---

## STEP 2: Regulatory Mapping Matrix

Now based on your risk classification above in Section 1 (whether High Risk or Limited Risk), consider how legal requirements translate to compliance tasks practically for your application in question. List out the legal requirements that apply depending on the risk level. 

### High Risk Requirements: 

| AI Development Lifecycle Phase | Legal Requirement | Requirement Description | Compliance Task | Acceptance Criteria |
|---|---|---|---|---|
| Data Ingestion | EU AI ACT Art 10 (2)(f) - Data Imbalances | Ensure training, validation, and testing datasets are representative, bias-mitigated and fully documented. | Implement automated bias-scan jobs in the data pipeline (e.g., Airflow DAG). Store reports in an S3 “conformity bucket.” | Bias scan executed on every dataset refresh. Report uploaded and reviewed. Data imbalance ratios remain within defined thresholds. |
| Model Training | EU AI ACT Art 11 (2) - Technical Documentation | Maintain traceable training records, document model logic, and describe implemented mitigations. | Automatically log training parameters, datasets, and risk controls in MLflow. Auto-generate a Model Card for each merge to production. | Every deployed model version includes: TRS tier, fairness metrics, mitigation steps, dataset lineage, and reviewer sign-off. |
| Whole Lifecycle | EU AI ACT Article 9 Risk Management | Establish continuous risk identification, evaluation, and mitigation throughout the AI system lifecycle. | Maintain a live Risk Register linked to model releases. Require structured risk review at design, deployment, and post-market stages. | Risk assessment completed before every release. Residual risks documented. Deployment blocked if Art 9 review is incomplete. |
| Pre-deployment | EU AI ACT Art 14 (4)(d) - Human Oversight | Guarantee meaningful human oversight, including the ability to override or halt automated decisions. | Add an “Override & Reason” feature to the admin dashboard. Require reason codes for all manual overrides. | Override events logged with user ID, timestamp, and justification. At least one oversight test case executed before release. |
| Pre-deployment | EU AI ACT Art 16 - Provider Obligations | Providers must ensure compliance controls, documentation, monitoring and corrective action processes are in place. | Embed compliance gates into CI/CD workflows. Assign Responsible AI Owner approval before production deployment. | No deployment permitted without compliance checklist completion. Named accountable approver recorded for each release. |
| Post-Deployment | EU AI ACT Art 19 - Automatic Logging | No deployment permitted without compliance checklist completion. Named accountable approver recorded for each release. | Build an immutable logging pipeline (Kafka → Iceberg Table → Evidence Graph). Capture model outputs, override events, retraining triggers. | Logs hashed daily; Merkle root verified. 100% traceability available for all critical decision events. |
| Post-Deployment | EU AI ACT Art 61 (1) Monitoring | Continuous monitoring is required to detect fairness drift, bias emergence, or performance degradation. | Deploy fairness drift dashboards (Prometheus + Grafana). Schedule daily drift detection jobs with compliance auto-alerting. | Fairness drift remains below threshold. Incidents acknowledged within SLA. Monthly monitoring report archived. |
| Pre-Deployment | GDPR Art 35 - DPIA | A Data Protection Impact Assessment is mandatory where AI processing poses high risk to individual rights and freedoms. | Trigger DPIA workflow automatically for Tier 1–2 systems. Require DPO review and approval prior to launch. | DPIA completed and signed before deployment. Risks and mitigations documented and stored in Compliance Folder. |
| Whole Lifecycle | EU AI ACT Art 18 - Record Keeping | Maintain required compliance artefacts for auditability and statutory retention periods. | Apply version-controlled archiving: auto-store Model Cards, DPIAs, bias reports, and risk logs in a “Compliance Folder” (10-year retention). | All required artefacts are stored and retrievable within 24 hours. Access control verified quarterly. Logs available for external audit. |
| Pre-Deployment | GDP Art 22 - Automated Decision Making | Individuals have the right not to be subject to solely automated decisions with significant effects unless lawful exceptions apply. | Flag legally significant decisions. Require lawful basis capture (consent/contract/legal duty) and provide human appeal workflow. | Users can request human review. Appeal outcomes logged. Automated decisions cannot be final without an oversight mechanism. |

### Limited Risk Requirements: 

| AI Development Lifecycle Phase | Legal Requirement | Requirement Description | Compliance Task | Acceptance Criteria |
|---|---|---|---|---|
| Pre-Deployment | EU AI Act Art 52 – Transparency Obligations | Users must be informed when interacting with an AI system unless this is obvious from context. | Display clear UI disclosure (“AI-assisted recommendation”). Provide an explanation link in user workflow. | Disclosure visible before interaction. Compliance proof logged at deployment. |
| Pre-Deployment | EU AI Act Art 50 – Synthetic Content Disclosure | AI-generated or manipulated content must be clearly labelled to prevent deception. | Add watermarking and disclaimer text to generated outputs. | All generated media includes visible disclosure label and metadata tag. |

---

# SECTION 3: Compliance Documentation Templates

Here are examples of documentation in response to the legal requirements listed above. NOTE: This is not exhaustive and will need continuous review to maintain up-to-date and be tailored to the specific circumstances of the application. Please consult the legal team for elaboration. The templates below provide engineers with clear, reusable structures while ensuring legal compliance.

## (1) Technical Documentation/ Model Card Template

Legal basis:  
EU AI Act Article 11: Requirement to prepare and maintain technical documentation before placing a high-risk AI system on the market.  
EU AI Act Annex IV: Specifies the mandatory content of the technical documentation file.  
EU AI Act Article 10: Data governance obligations, including representativeness and bias mitigation of datasets.  
EU AI Act Article 9: Lifecycle risk management system and documentation of mitigation measures.  
EU AI Act Article 14: Human oversight requirements, including override mechanisms and escalation procedures.  
EU AI Act Article 61: Post-market monitoring obligations, including continuous performance and fairness tracking.  
EU AI Act Articles 18 and 19: Record-keeping and automatic logging requirements for auditability and traceability.  

Template: 

Application Overview:  
Model ID / Hash:  [Auto-generated from commit SHA]  
Commit SHA:** [Git commit hash]  
Dataset Version:** [Dataset hash/version identifier]  
System Name:  [Application name]  
Version: [Model version number]  
Model Type: [e.g., Neural Network, Random Forest, etc.]  
Date Created: [Auto-filled timestamp]  
Last Updated: [Auto-filled timestamp]  

Legal Profile:  
Risk Tier: [High/ Limited/Moderate]  
TRS Score: [Total Risk Score calculated]  
Annex III Category: [Relevant category from EU AI Act Annex III]  
DPIA Required? YES/NO  
GDPR Lawful Basis: [Consent/ Legitimate Interests/ Legal obligation]  

Scope:  
Intended Purpose: [Description of what the system is designed to do]  
Out-of-Scope Use Cases: [List what the system should not be used for]  

Data Governance:  
Dataset Source + Version Hash:  
Representativeness Checks: [Description of checks performed to ensure dataset representativeness]  
Bias Mitigation Applied: [List of bias mitigation techniques used during data preparation and training]  

Fairness & Performance Metrics  
Metrics Used (e.g., demographic parity):  
Slice-Level Results: [Performance metrics broken down by protected groups]  
Thresholds + Justification: [Fairness thresholds set and rationale for those thresholds]  
Overall Performance Metrics: [Accuracy, precision, recall, F1-score, etc.]  

Human Oversight Plan:  
Oversight Roles :[Who is responsible for oversight (e.g., Product Manager, Compliance Officer)]  
Manual Review Triggers: [Conditions that require human review]  
Override Workflow: [Step-by-step process for human override of automated decisions]  
Escalation Procedures: [How to escalate when issues are detected]  

Monitoring & Logging:  
Drift Monitoring Frequency: [How often fairness/performance drift is checked]  
Audit Logging Location: [Where logs are stored]  
Retention Period: [How long logs are retained]  
Change-Log (Auto-appended on every merge): Date, commit, who, what changed, reason, reviewer  

## (2) DPIA Template

Legal basis:  
GDPR Article 35: Mandatory Data Protection Impact Assessment for high-risk processing activities.  
GDPR Article 22: Restrictions and safeguards relating to solely automated decision-making with legal or similarly significant effects.  

Template:

Data Protection Impact Assessment for [NAME OF INITIATIVE]  
Version [NUMBER]  
Dated: [ASSESSMENT DATE]  

Document History: 

| Version Number | Summary of Change | Date |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Reviewers:

| Reviewer Name | Role | Version Reviewed | Date |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Executive Summary: 

High-level description of Initiative:  
[SUMMARY]  
Why a DPIA is required:  
[SUMMARY]  
Scope of Initiative's processing:  
[SUMMARY].  
Purposes of processing:  
[SUMMARY]  
Security of Processing  
[SUMMARY OF TECHNICAL AND ORGANISATION MEASURES TO PROTECT PERSONAL DATA]  

## (3) Transparency Disclaimer Template

Legal basis:  
EU AI Act Article 50: Obligation to disclose synthetic or AI-generated content (e.g., deepfakes or generated images).  
EU AI Act Article 52: Transparency duties requiring users to be informed when interacting with AI systems, unless obvious from context.  

Template: 

Disclaimer template to be used under every AI-generated image:

"Disclaimer: This image was generated by an AI system and is not a real photograph"

Disclaimer template for AI-assisted interactions:

"This recommendation is AI-assisted. For more information about how this works, click here."

---

# SECTION 4: Audit Trail Design  

Purpose: This ensures that every AI decision, model update and override can be traced, proven and verified later. This is essential in order to comply with Article 19 and 61 re logging and retention. Use the table under “Logging Categories” as your starting point and make it more bespoke to your circumstances (e.g. re Access Control).  

Audit Trail Workflow: User action → Decision Engine → Event Broker (Kafka) → Audit Trail Storage (which includes: 1. Immutable Log, 2. Monitoring API and 3. Evidence Graph Service.  

Logging Categories: 

| Category | Data Example | Reasoning | Retention | Access Control |
|---|---|---|---|---|
| Risk Assessment | Who accessed and timestamp, TRS calculation, reviewer ID | Shows how you classified risk | 10 years | Compliance Team, DPO |
| Model Metric | Fairness scores, performance metrics, slice-level results | Proves model was evaluated and tracked | 5 years | Data Science Team, Compliance Team |
| Override Event | Decision ID, who overruled and reason | Demonstrates human oversight as per Art 14. | 5 years | Compliance Team |
| Dataset Snapshot | Dataset hash, dataset version | Proves what data version was used for training | Life of application + 2 years | Data Science Team |
| Incident Report | Incident ID, resolution, timestamp, affected users sound | Incident reporting in line with EU AI Act Art 54 | 10 years | Compliance, DPO |

---

# REFERENCES

Bieker, F., Norton, H. L., & Hansen, M. (2021). Documenting for accountability: A review of automated decision system documentation implementations. Journal of Technology Law & Policy, 25(2), 75-97. https://doi.org/10.5195/tlp.2021.245 

Black, J., & Murray, A. D. (2021). Regulating AI and machine learning: Setting the regulatory agenda. European Journal of Law and Technology, 12(1), 738- 
762. https://doi.org/10.2139/ssrn.3372560 

Bradford, A. (2020). The Brussels effect: How the European Union rules the world. Oxford University Press. https://doi.org/10.1093/oso/9780190088583.001.0001 

Crenshaw, K. (1989). Demarginalizing the intersection of race and sex: A black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. University of Chicago Legal Forum, 1989(1), 139-167. https://chicagounbound.uchicago.edu/uclf/vol1989/iss1/8 

Ebers, M., Hacker, P., & Smuha, N. (2022). The European approach to regulating artificial intelligence. Common Market Law Review, 59(1), 75-112. https://doi.org/10.54648/cola2022003 
 
Edwards, L., & Veale, M. (2018). Enslaving the algorithm: From a 'right to an explanation' to a 'right to better decisions'? IEEE Security & Privacy, 16(3), 46- 
54. https://doi.org/10.1109/MSP.2018.2701152 

Fjeld, J., Achten, N., Hilligoss, H., Nagy, A., & Srikumar, M. (2020). Principled artificial intelligence: Mapping consensus in ethical and rights-based approaches to principles for AI. Berkman Klein Center Research Publication No. 2020-1. https://doi.org/10.2139/ssrn.3518482 

Greene, D., Hoffmann, A. L., & Stark, L. (2021). Better, nicer, clearer, fairer: A critical assessment of the movement for ethical artificial intelligence and machine learning. Hawaii International Conference on System Sciences. https://doi.org/10.24251/HICSS.2021.754 

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1, 389-399. https://doi.org/10.1038/s42256-019-0088-2 

Greenleaf, G., & Cottier, B. (2020). 2020 ends a decade of 62 new data privacy laws. Privacy Laws & Business International Report, 163, 24-26. https://ssrn.com/abstract=3572611 

Hoofnagle, C. J., van der Sloot, B., & Borgesius, F. Z. (2019). The European Union general data protection regulation: What it is and what it means. Information & Communications Technology Law, 28(1), 65-98. https://doi.org/10.1080/13600834.2019.1573501 

Kaminski, M. E., & Malgieri, G. (2021). Algorithmic impact assessments under the GDPR: Producing multi-layered explanations. International Data Privacy Law, 11(2), 125- 
159. https://doi.org/10.1093/idpl/ipaa020 

Metcalf, J., Moss, E., Watkins, E. A., Singh, R., & Elish, M. C. (2021). Algorithmic impact assessments and accountability: The co-construction of impacts. In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (pp. 735- 
746). https://doi.org/10.1145/3442188.3445935 
 
Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency (pp. 33-44). https://doi.org/10.1145/3351095.3372873 
 
Yeung, K., Howes, A., & Pogrebna, G. (2020). AI governance by human rights-centred design, deliberation and oversight: An end to ethics washing. In M. D. Dubber, F. Pasquale, & S. Das (Eds.), The Oxford Handbook of Ethics of AI (pp. 77-106). Oxford University 
Press. https://doi.org/10.1093/oxfordhb/9780190067397.013.5 