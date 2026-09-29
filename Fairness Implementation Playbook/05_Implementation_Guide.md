# Implementation Guide

## How to Use This Playbook

This playbook is designed to be implemented in **phases**. It is not a one‑time compliance exercise, but an **operating model** for embedding fairness into AI development.

The recommended order is:

1. **Start at the team level → `Component 1: Fair AI Scrum Toolkit`**  
   Teach individual teams how to build fairness into their day‑to‑day work.

2. **Scale across the organisation → `Component 2: Organisational Integration Toolkit`**  
   Create roles, governance bodies, and decision processes that coordinate fairness work between teams.

3. **Apply architecture‑specific strategies → `Component 3: Advanced Architecture Cookbook`**  
   Use the LLM / Recommendation / Vision playbooks for system‑specific risks.

4. **Ensure regulatory alignment → `Component 4: Regulatory Compliance Guide`**  
   Map your systems to EU AI Act / GDPR risk levels and set up compliance artefacts.

5. **Monitor, validate, and refine continuously → `Components 6–8`**  
   Use the Adaptability Guidelines, Validation Framework, and Case Study to adjust and improve over time.

Each section below explains **how to operationalise Components 1 and 2 in practice**.

---

# Fair AI Scrum Toolkit

## Key Decision Points

### 1. Development of user stories

- **Where to start:**  
  Begin with features that have **highest bias or harm potential** (e.g., ranking, selection, triage).
- **What to do:**  
  - Rewrite user stories using the **SAFE Framework**.  
  - Check the **User Story Example Library** to align your wording with the playbook.
- **Practical tip:**  
  Capture SAFE outputs directly in your ticketing system (e.g., Jira description field), not in a separate document that will be forgotten.

### 2. Development of acceptance criteria

- **Define metrics before work begins:**  
  - Agree on **primary fairness metrics and thresholds** (e.g., EO ≤ 0.03, DP ≤ 0.05).  
  - Use the **FAIR Framework** (F = thresholds, A = audits, I = intersectional, R = reporting).
- **Involve the right people:**  
  - Partner with **domain experts** (e.g., recruiters, legal, DEI leads) when setting thresholds; they understand what “fair enough” means in your context.
- **Make them testable:**  
  - Write acceptance criteria so that a tester or data scientist can run a script and clearly say **pass / fail**.

### 3. Adaptation to sprint planning

- **Capacity allocation:**  
  - Expect that teams initially **underestimate fairness work by 40–60%**.  
  - Start by reserving **25–30% of sprint capacity** for fairness tasks, then adjust based on actual data over several sprints.
- **Backlog hygiene:**  
  - Create **specific, measurable** fairness tasks (e.g., “run EO/DP tests on v3 model”, “add intersectional slice analysis dashboard”) tied to SAFE/FAIR outputs.
- **Intersectionality:**  
  - When reserving capacity, ensure some time is explicitly earmarked for **intersectional analysis**, not only single‑attribute checks.

### 4. Continuous improvement

- After 2–3 sprints, run a **fairness‑focused retrospective**:
  - Which fairness tasks actually reduced issues?
  - Where did fairness work block or slow the team?
  - How should capacity / templates be adjusted?

---

## Limitations of the Fair AI Scrum Toolkit

When rolling out Component 1, keep these constraints in mind:

- **Inefficiencies:**  
  Adding too many checkpoints can make ceremonies unmanageable. Start lightweight, then add depth where metrics show recurring problems.
- **Expertise:**  
  Team members may lack fairness knowledge. Plan **training or learning time inside sprints** and/or bring in an external specialist for initial guidance.
- **Communication:**  
  Misalignment between teams is common. Use the **shared templates** (SAFE, FAIR, DoD, Sprint Backlogs) so that different teams speak the **same language** about fairness work.

---

## Resources for Fair AI Scrum

- **Time:**  
  - Expect ~**2 hours per team member** to complete the initial SAFE/FAIR/DoD setup for one feature area.
- **Expertise vs. team members:**  
  - Aim for a **mix** of fairness specialists and general team members.  
  - Avoid centralising all knowledge in one “fairness person”; distribute responsibilities across roles (PO, DS, Eng, UX).
- **Documentation:**  
  - Teams will need to **update existing artefacts** (user stories, acceptance criteria, DoD, sprint templates) rather than creating parallel documents.

---

# Organisational Integration Toolkit

## Fairness Roles

### Mid‑sized organisation approach (typical EquiHire‑style company)

- **Embed into existing roles with protected time:**  
  - Assign fairness responsibilities to current leaders (e.g., product managers, tech leads) and protect **~20% of their capacity** for fairness work.
- **Create lightweight governance instead of heavy committees:**  
  - Set up a part‑time **AI Ethics Committee / Fairness Review Board** with members drawn from Product, Data Science, Legal, and DEI.
- **Rotate fairness champions:**  
  - Have a **rotating fairness champion** in each squad so knowledge spreads and doesn’t depend on one person.
- **Use external experts selectively:**  
  - Bring in consultants for **high‑risk reviews** or when internal expertise is still developing, but pair them with internal staff for knowledge transfer.
- **Risk‑based governance:**  
  - Apply the **full governance stack** (roles, bodies, gates) to **high‑risk AI applications** (e.g., hiring, lending).  
  - Use lighter processes (fewer meetings, simpler documentation) for **lower‑risk systems**.

**Key principle:** Blend **embedded responsibilities** (inside teams) with **specialists** (program manager, ethics lead) so fairness is both owned and supported.

---

## Resources for Organisational Integration

- **Headcount:**  
  - You will need at least some **dedicated or partially dedicated** fairness capacity; the exact number depends on system risk and org size.
- **Decision rights:**  
  - Ensure that newly defined fairness roles (e.g., Fairness Program Manager, Technical Fairness Lead) have **clear authority**: what they can approve, what they can block, and what they must escalate.
- **Training:**  
  - Budget **$1,000–5,000 per role holder** for fairness / responsible AI training, especially for leadership and program roles.
- **Time for governance bodies:**  
  - Plan **2–8 hours per month per participant** for Steering Committee, Review Board, and working group meetings.
- **Process setup:**  
  - Expect **2–4 weeks** initially to adapt the provided templates (roles, RACI, gates, FDRs) and plug them into your existing operating model.

---

## Fairness Governance Bodies

- **Scale formality to your size and risk:**
  - **Small companies:** one cross‑functional **Fairness Working Group** that meets monthly.
  - **Mid‑sized companies:** separate **Steering Committee** (strategic) and **Review Board** (tactical).
  - **Large companies:** full stack (Steering Committee, Review Boards per domain, Technical Committee, possibly Community Advisory Council).

---

## Decision Processes and Escalation Procedures

- Use the **risk classification of each AI application** (from Component 4) to determine:
  - Which governance bodies must review it.
  - What **approval tier** is required (Strategic / Tactical / Operational).
- Before rolling out org‑wide:
  - **Pilot your decision framework** on one or two high‑risk systems.  
  - Measure **time to decision** and **number of escalations**, then refine authority levels and criteria.

---

## Governance Checkpoints

- Implement the **highest‑value gates first**:
  - **Gate 1 – Data Review** and **Gate 3 – Pre‑Deployment** for all high‑risk systems.
- Only add additional gates (e.g., design gate, monitoring gate) once the first two are working smoothly.

---

## Fairness Documentation

- **Timing:**  
  - Start creating **Fairness Decision Records (FDRs)** even before all governance structures are fully in place; they will become your historical record as governance matures.
- **Process:**  
  - Wherever possible, **integrate documentation into existing tools** (e.g., link FDR IDs in Jira tickets, store FRS/FDR templates in the same repo as code) instead of creating separate manual repositories.
- **Keep it current:**  
  - Schedule **regular reviews** (e.g., quarterly) to update FRS, FDRs, and Limitation Registers as systems and data evolve.

---

## Metric Dashboards

When creating dashboards to display fairness metrics:

- **Adapt to the audience:**  
  - Executive, management, technical, and stakeholder views may need different levels of detail and framing.
- **Avoid misleading visuals:**  
  - Use consistent scales, show thresholds, and add explanatory annotations. Where possible, provide **domain benchmarks**.
- **Show disaggregation and intersections:**  
  - Break overall metrics into **demographic group** performance and key **intersectional** slices. Heatmaps can help communicate complex intersectional patterns.

---

## Monitoring

- **Set realistic thresholds:**  
  - In your fairness drift tracking, choose thresholds that avoid constant noise while still surfacing meaningful changes; adjust after a few months of data.
- **Keep dashboards focused:**  
  - Start with a **small set of well‑understood metrics** and expand only when users are consistently interpreting them correctly.

## Resources for Monitoring

- Metric definition and validation: **2–4 weeks**  
- Dashboard design and refinement: varies with complexity  
- Monitoring system setup: **1–2 weeks per system**  
- Stakeholder training on dashboard interpretation: **2–4 hours per group**

---

# Advanced Architecture Cookbook 

## LLM:

**Combined Approach:** Use a combination of strategies as one will not fix everything. Each strategy will capture different bias manifestations.  

**Intersections:** Consider the intersectional element by using prompts that address intersection fairness, fine-tuning datasets with diverse intersectional representation and developing evaluation frameworks that assess outputs across demographic intersections.  

**Over-Safety:** Be aware that excessive safety constraints create overly conservative models. Balance this with targeted interventions for specific harmful behaviours.  

**Continuity:** Users will discover new ways of getting biased outputs so it is essential to implement continuous red-teaming.  

**Tailoring:** Make sure to tailor your fine-tuning with your domain expertise. Also ensure tailoring is reflected in specific prompt templates.  

**Metrics:** Do not settle for simple metrics, instead look for a multi-dimensional approach for evaluation composed of  some automated metrics, structured human evaluation and longitudinal testing.  

**Resources required:** be sure to implement fairness-focused fine-tuning datasets, red team capacity, allow time for evaluations and put in place the monitoring systems for deployment.  

---

## Recommendation Algorithms:

Frequent mistakes to watch out for in implementation include:  

- Treating fairness as a static metric. This will not work as recommenders are dynamic.  
- Measuring accuracy but ignoring exposure. A system can have equal relevance but still be unfair if visibility is unequal.  
- One-size-fits-all constraints. Personalisation is the product, so fairness must be context-aware and not uniform.  
- Post-processing without governance. Re-ranking helps this but without stakeholder decisions, it becomes arbitrary.  
- No longitudinal monitoring. Many harms appear only after weeks of feedback amplification.  

---

## Vision/Multi-Model:

**Separate:** Evaluate each modality separately first. Identify bias patterns in vision, text and audio before analysing fusion effects.  

**Inconsistent labelling:** Ensure annotation guidelines are clear and applied equally across all groups.  

**Modality conflict:** Ensure one input (e.g., image or text) does not dominate the final decision unfairly.  

**Environmental variation:** Test performance across different lighting, camera types, and backgrounds to avoid disadvantageing certain groups.  

**Hidden representation bias:** Use visualisation tools (e.g., saliency maps) to check what the model is focusing on and whether protected attributes influence decisions.  

### Key resources:

- Diverse visual data.  
- Vision-specific fairness tests.  
- Model visualization tools.  
- Cross-modal testing setup.  

---

## When explaining fairness work:

- To executives: focus on risk and reputation.  
- To product teams: focus on reliability across users.  
- To engineers: link fairness improvements to better robustness and generalisation.  

---

# Regulatory Compliance Guide

## Risk Classification:

**Legal expertise:** this is required for accurate interpretation especially in light of changing laws. Especially useful would be to hire a Data Protection Officer (DPO) to oversee GDPR obligations.  

**Cross-team collaboration:** the process of classifying the risk will require inputs from legal, technical and product teams to properly capture the assigned risk level set out in EU laws.  

## Audit Trail design:

Set up automated logging and evidence collection for ease. This entails building a logging pipeline (Kafka → Iceberg → Neo4j).  

## Monitoring:

Reclassify during sprints after every 3 to 6 months to ensure audit readiness.  

---

## Compliance Timeline:

| Stage of AI Lifecycle | What Must Be Done for Compliance | Evidence Produced |
|-----------------------|----------------------------------|-------------------|
| Before Building | Classify system risk; confirm if High-Risk under Annex III; decide if DPIA is required; consult DPO where necessary | Technical documentation/model card |
| During Design | Identify fairness and discrimination risks; define mitigation measures; prepare documentation templates; plan human oversight process | Technical documentation/model card |
| Before Deployment | Complete Technical Documentation; complete DPIA (if required); test fairness thresholds; test override mechanisms; ensure logging and monitoring are active | Technical documentation/model card and DPIA |
| At Launch | Activate monitoring dashboards; verify audit logging works; publish transparency notices for users | Logging record |
| During Operation | Monitor fairness drift regularly; review incidents and overrides; update documentation when models change; conduct periodic compliance reviews | Monitoring reports |
| System Retirement | Delete personal data where required; archive compliance artefacts; retain logs for legal retention period | Data deletion confirmation and retention records. |