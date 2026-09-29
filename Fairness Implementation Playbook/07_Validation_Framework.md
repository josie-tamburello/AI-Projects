# Validation Framework  

Answer the following questionnaire to uncover the effectiveness of your actions. These results should be communicated to internal stakeholders in a clear manner, via a dashboard or report.

**How to use this framework:**  
Teams should complete this questionnaire at least once per quarter (and after major releases) and compare answers over time to track whether fairness processes and outcomes are improving.


## Fair AI Scrum Toolkit  

### User stories  
- What percentage of user stories include explicit fairness considerations?  
- Did this meet the acceptable threshold?  

### Sprint backlogs  
- What is the frequency of fairness discussions in daily standups?  
- What is the completion rate of fairness tasks compared to functional tasks?  
- Did this meet the acceptable threshold?  

### Ceremony  
- **Process metrics:** when were bias issues detected in the development cycle? How did the team respond to these discoveries?  
- **Fairness outcome metrics:** how did these metrics improve or regress across demographic groups and their intersections resulting from ceremony insights?  

### Roles  
- Are fairness responsibility roles appropriately distributed?  
- Are there any remaining gaps or confusion?  

### Overall Fairness Improvements  
- Is there a reduction in fairness issues discovered post-deployment?  
- Are there improved fairness metrics in your deployed system?  
- Is there a decreased time to address identified bias issues?  


---

## Organisational Integration Toolkit  

### Fairness Roles  
- Have escalation paths been set up?  
- Have the necessary resources been allowed (headcount, budget, meeting time, time for process)?  
- Are stakeholders aware of their fairness responsibilities?  
- Have these been communicated effectively?  
- What is the percentage of identified fairness issues successfully addressed?  
- How long did it take for fairness issues to be resolved?  

### Fairness Bodies  
- Scale the side and formality of governance bodies to your company. Small companies might use cross-functional working groups whereas larger companies may opt for formal committees.  

### Documentation  
- What is the percentage of fairness decisions with complete documentation?  
- How quickly do teams respond to fairness issues based on the documentation?  

### Decision Processes and Escalation Procedures  
- Check the risk classification of the AI application to determine governance routes. Consider:  
  - How significant are potential harms?  
  - How much human oversight exists?  
  - Who might be affected?  
  - How many people could experience impact?  
- Create a diverse range of governance bodies spanning technical working group to broader fairness councils including domain experts.  
- Test decision frameworks before rolling out organisation wide using a pilot to refine authority levels and decision criteria.  

### Governance Checkpoints  
- Implement the highest value governance dates which is typically pre-deployment verification and data review.  

### Monitoring  
- Are stakeholders accessing and using the dashboards? (track usage data)  
- Are stakeholders correctly interpreting the dashboards? (set up surveys)  
- Are alerts surfaced in monitoring presenting actual fairness issues?  
- How quickly are teams flagging fairness issues?  

### Communication  
- Based on survey feedback, can team members understand fairness decisions made by others based on the documentation?  
- Is the documentation clearly communicated?  


---

## Advanced Architecture Cookbook  

### Architecture  
- Did you correctly identify the architecture type?  
- Did we document the main fairness issues as expressed in the playbook?  

### Testing & Results  
- Did we run fairness tests on multiple user groups?  
- Did we measure and record fairness metrics?  
- Did we compare before-and-after results for fairness interventions?  
- Did we review any trade-offs (accuracy, relevance, diversity)?  

### Review & Sustainability  
- Did another person or team review our fairness results?  
- Did we schedule a re-validation date (e.g., in 3–6 months)?  
- Did we store validation data and metrics for traceability?  


---

## Regulatory Compliance Guide  

### Risk Classification  
- Have you used cross-team expertise in filling out the risk classification questionnaire? (a combination of legal, technical etc).  
- Associated with the risk level of your application, have you covered all the necessary compliance requirements?  

### Regulatory mapping  
- Have you set up a regular cadence for reviewing changes in laws and regulations to stay abreast of these changes?  
- Have you covered all the high risk regulatory requirements?  

### Documentation  
- Have you filled out all the necessary compliance documentation in line with legal requirements?  
- Have you set a regular cadence for updating and checking continued compliance of your documentation with legal requirements?  

### Audit  
- Have you stress tested your audit trail design system ensuring it captures all the necessary elements?  
- If data processing of personal data is involved, have you ensured anonymisation or omission of capturing such data in logs in line with legal requirements under GDPR?  