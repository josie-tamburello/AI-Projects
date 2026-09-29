# COMPONENT 3: Advanced Architecture Cookbook

This Advanced Architecture Cookbook provides specialised fairness implementation strategies for complex AI architectures. Each section helps teams diagnose common fairness risks, select an appropriate strategy and operationalise it.

---

## How to Use This Cookbook

1. **Identify your architecture type (below).**  
   - Large Language Model (LLM) → go to **Part A**  
   - Recommendation Algorithms → go to **Part B**  
   - Vision / Multi‑Modal → go to **Part C**

2. **In that Part, run STEP 1: Identify the fairness issue.**  
   - Map what you’re seeing in your system to the “Common Fairness Issues” table.  
   - Write down the categories and concrete examples for your system.

3. **Pick 2–4 strategies from the “Strategy Library” for that Part.**  
   - Combine prompt / architecture / data / monitoring strategies as needed.  
   - Implement them in code and pipelines.

4. **Connect back to Components 1 and 2.**  
   - Record your choices in a **Fairness Decision Record (FDR)**.  
   - Update **SAFE / FAIR** acceptance criteria and governance **gates** accordingly.

Use this loop each time you introduce a new architecture or discover a new fairness issue in an existing system.

---

## STEP 1: Identify your architecture

Select the architecture type that best matches your system:

What are your architecture types? Select from below:

- [ ] Large Language Model (LLM) → Go to Part A  
- [ ] Recommendation Algorithms → Go to Part B  
- [ ] Vision Model/ Multi-Modal → Go to Part C  

Once selected, go to the relevant Part and follow the steps in order.

---

# PART A: LLM

## Relevance

Large Language Models are trained on vast and imperfect datasets and their outputs often amplify historical, stereotypes and harmful content. As LLMs are foundation models, fairness issues can emerge from the entire pipeline including data, training, prompting strategies and deployment. This section provides architecture-specific fairness strategies to help teams diagnose, mitigate and monitor bias in LLMs.

---

## STEP 1: Identify the fairness issue

Review the Common Fairness Issues Library and align it to your LLM use case. Which issues show up in your system today? Note the category and an example output in the template below.

### Common Fairness Issues

| Category | Result |
|-----------|--------|
| Pre-training Bias |  |
| Representation Disparities | Underrepresentation of minority groups, cultures and languages. |
| Stereotype Encoding | Implicit associations between demographic groups and stereotypical attributes. |
| Distributional Bias | Overrepresentation of majority perspectives and cultural frameworks |
| Historical Discrimination | Encoding of historically discriminatory language and framing |
| Harmful Content | Inclusion of toxic, abusive, or discriminatory text |
| Emergent Behaviours |  |
| Instruction Following | Capability to understand and execute complex directives, including harmful ones |
| In-context Learning | Adaptation to biased examples provided in prompts |
| Sycophancy | Tendency to agree with user-stated biases or preferences |
| Jailbreaking Vulnerability | Susceptibility to adversarial prompts that bypass safety measures |
| Hallucination | Generation of plausible-sounding but false information with potential disparate impacts |

### Template

| Category | Example |
|----------|----------|
|  |  |
|  |  |

---

## STEP 2: Operationalise the selected strategy

Review the Strategy Library and implement the relevant strategies. Document what you changed and why. You will select a combination of strategies.

---

## Strategy Library

| Strategy | Explanation |
|-----------|-------------|
| **Prompt-Based Fairness Strategies** |  |
| **Fairness Prompting** | Explicit instructions directing models toward fair outputs  <br><br> e.g.  <br><br> “Evaluate this candidate based solely on their demonstrated skills, experience, and achievements. Do not make assumptions based on name, gender, ethnicity, age, or background. Focus only on job-relevant qualifications and provide evidence-based reasoning.” |
| **Self-critique Framework** | Prompts that ask models to evaluate their own outputs for bias  <br><br> e.g.  <br><br> “Step 1: Evaluate the candidate’s suitability for the role. Step 2: Review your evaluation and identify any potential bias, stereotypes, or unsupported assumptions. Revise the assessment if necessary to ensure fairness and consistency.” |
| **Scaffolded Generation** | Multi-step prompting that guides models through fair reasoning  <br><br> e.g.  <br><br> “Evaluate the candidate using the following structured steps: List the candidate’s key technical skills. List measurable achievements. Assess alignment with job requirements using only the above information. Provide a final recommendation based strictly on these criteria.” |
| **Counterfactual Prompting** | Testing alternative demographic framings to identify bias  <br><br> e.g.  <br><br> “Version A: Evaluate the candidate, John Smith, who graduated from a regional university and has 3 years of experience. Version B: Evaluate the candidate, Aisha Khan, who graduated from a regional university and has 3 years of experience.” |
| **Chain-of-Thought Fairness** | Explicit reasoning steps that mitigate implicit biases  <br><br> e.g.  <br><br> “Before giving your final recommendation: Explicitly state the objective criteria you are using. Explain how each piece of evidence supports your conclusion. Confirm that no assumptions about demographic characteristics influenced your reasoning Then provide your final decision.” |
| **Fine-tuning Strategies** |  |
| Balanced Fine-tuning Datasets | Creating demographically diverse examples |
| Fairness-specific RLHF | Reinforcement learning from human feedback prioritizing fairness |
| Counterfactual Data Augmentation | Training on demographic variations of the same content |
| Bias-targeted adapters | Small trainable components focusing on bias mitigation |
| Multi-objective Fine-tuning | Balancing task performance with explicit fairness metrics |
| **Safety Guardrails** |  |
| Filtering | Implement input filtering for harmful prompt patterns |
| Classification | Create output classification for detecting biased responses |
| Monitoring | Develop monitoring systems for emergent harmful behaviours |
| Intervention | Establish intervention protocols for identified issues |
| **Evaluation Strategies** |  |
| Red-teaming | Implement continuous systematic adversarial testing to identify fairness vulnerabilities |
| Counterfactual Evaluation | Testing model responses across demographic variations |
| Benchmark Suites | Implement standardised test sets targeting specific fairness dimensions |
| Human Evaluation Protocols | Structured human assessment of generative outputs |
| Multi-dimensional Measurement | Evaluating multiple fairness aspects simultaneously |

---

# PART B: Recommendation Algorithms

## Relevance

Recommendation algorithms personalise and rank content, meaning they shape what users see and which providers gain exposure. Common across education, media and e-commerce (for example, TikTok-style feeds), these systems create feedback loops where each interaction influences future recommendations. Fairness therefore becomes dynamic: what matters is not just prediction accuracy, but who gets seen.

The system must balance the interests of users, providers and the platform, while managing trade-offs between relevance and diversity, encouraging exploration and adjusting exposure appropriately for different users. Because of this, fairness in recommendation systems requires architecture-specific techniques that manage personalisation, exposure and feedback over time.

---

## STEP 1: Identify the fairness issue

### Common Fairness Issues Library

| Category | Result |
|-----------|--------|
| User-Side disparity | Some user groups receive less diverse, lower-quality, or stereotyped recommendations. Unequal access to relevant or opportunity-enhancing content across demographics. |
| Provider-Side disparity | Some creator/provider demographics receive systematically lower exposure, weaker reputation outcomes or reduced monetisation opportunities despite comparable quality. |
| Two-Sided Matching Bias | The algorithm disproportionately favours popular or established providers, limiting visibility for niche content and new entrants. Opportunity distribution becomes structurally imbalanced. |
| Platform Objective Bias | Optimisation prioritises short-term engagement over diversity, contextual sensitivity and long-term equity. Recommendations may lack meaningful variety or amplify manipulative patterns. |
| Exposure Bias | Systematic differences in visibility across demographic provider groups |
| Position Bias | Items in top positions receive disproportionate attention and clicks. |
| Presentation Bias | Prominently displayed items receive disproportionate attention. Attention concentration unrelated to true relevance. |
| Attention Scarcity Bias | Users can only view a limited subset of all possible recommendations. |
| Popularity Bias | Popular items receive more exposure, becoming more popular through increased visibility. |
| Data Collection Bias | System collects more data about recommended items, improving their future recommendations |
| Preference Reinforcement Bias | User biases reflected in clicks get amplified by personalisation algorithms |
| Cold Start Disadvantage | New or niche items suffer increasingly limited visibility over time. |

---

## STEP 2: Select a strategy

### Strategy Library

| Strategy | Purpose |
|-----------|----------|
| Re-ranking | Adjust the final ordering of recommendations to rebalance visibility while preserving core relevance. |
| Exposure & Diversity Balancing | Introduce explicit exposure or diversity objectives into ranking decisions. |
| Feedback Loop Correction | Prevent bias amplification by correcting for popularity effects. |
| Personalised Fairness Constraints | Apply fairness adjustments at the cohort or user level. |
| Multi-stakeholder Objectives | Embed fairness directly into the optimisation function. |
| Monitoring & Governance Framework | Establish structured logging and dashboards to detect drift. |
| Exploration-Exploitation Balancing | Adjust exploration rates to ensure new or underexposed items receive visibility. |
| Composite metrics | Evaluate system performance using multi-dimensional metrics. |

---

# PART C: Vision Model/ Multi-Modal

## Relevance

Vision and multi-modal models perceive the world through images, video, and combined sensory inputs such as text or sound, which means fairness challenges arise from how perception itself is learned and fused. Bias can enter before modelling even begins through the image capture pipeline (e.g., sensors, lighting, camera quality), and it can also emerge in what the model encodes. Interactions between modalities may amplify hidden bias.

---

## STEP 1: Identify the fairness issue

### Common Fairness Issues

| Category | Result |
|-----------|--------|
| Demographic Encoding | CNN layers extract features correlated with race, gender, and age even when such classification isn't the task |
| Attention Disparities | Visual attention mechanisms focus differently across demographic groups |
| Feature Attribution Variance | Model explanations show different salient features for different groups |
| Background Context Effects | Models rely on contextual cues correlated with demographics |
| Modality Divergence | Different bias patterns in each modality creating inconsistent outputs |
| Bias Amplification | Cross-modal interactions reinforcing biases present in individual modalities |
| Modality Dominance | One modality disproportionately influencing outputs for certain groups |
| Cross-Modal Artifacts | Fusion mechanisms creating new bias patterns absent from individual modalities |
| Missing Modality Effects | Performance disparities when inputs lack certain modalities |
| Capture Conditions | Lighting, camera settings, and environmental factors affecting demographic groups differently |
| Annotation Inconsistency | Human labelers applying different standards across demographic groups |
| Cultural Context Variation | Visual and audio cues having different meanings across cultures |
| Representation Imbalance | Severe underrepresentation of certain groups in standard vision datasets |
| Accessibility Gaps | Dataset collection methods excluding people with disabilities |
| Metric Mismatch | Standard fairness metrics failing to capture vision-specific performance differences |
| Contextual Variation | Performance changing dramatically across environmental conditions |
| Multi-Faceted Performance | Different error types having varying impacts across groups |
| Explanation Disparities | Attribution methods showing inconsistent explanations across demographics |
| Benchmark Limitations | Standard vision benchmarks lacking demographic diversity |
| Attribution Complexity | Difficulty explaining which visual features drive predictions for different groups |
| Cross-Modal Reasoning | Complex interactions between modalities creating opaque decision processes |
| Contextual Dependencies | Model behavior changing based on visual context in ways that affect fairness |
| Feature Visualisation Gaps | Inadequate tools for understanding learned visual representations |
| Explanation Inconsistency | Different explanation methods producing contradictory fairness insights |

---

## STEP 2: Select a strategy

### Strategy Library

| Strategy | Explanation |
|-----------|-------------|
| Audit | Audit training data for demographic representation across visual attributes and environmental conditions (e.g., lighting, background, camera type). |
| Data Collection | Develop data collection protocols enhancing demographic diversity and create annotation guidelines promoting consistent standards across groups. |
| Balanced Sampling & Augmentation | Implement balanced sampling and targeted augmentation strategies. |
| Architecture Selection | Choose model architectures that are conducive to fairness intervention. |
| Modality-Specific Fairness Components | Implement fairness mechanisms tailored to each modality. |
| Fusion Balancing | Design fusion mechanisms that balance modality influence fairly. |
| Attention Fairness Controls | Develop attention mechanisms that maintain consistency across demographic groups. |
| Representation Debiasing | Apply adversarial techniques or regularization methods to remove protected attribute signals. |
| Fair Embedding Design | Implement contrastive learning or embedding constraints. |
| Cross-Modal Consistency Constraints | Ensure fairness is maintained across modalities. |
| Modality Dropout for Robustness | Introduce modality dropout strategies to enhance robustness. |
| Vision-Specific Evaluation | Implement stratified and intersectional testing across diverse visual conditions. |

---

# REFERENCES

Beutel, A., Chen, J., Zhao, Z., & Chi, E. H. (2019). Data decisions and theoretical implications when adversarially learning fair representations. In *Proceedings of the 2019 Conference on Fairness, Accountability, and Transparency* (pp. 325–334). https://doi.org/10.1145/3287560.3287590  

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 610–623). https://doi.org/10.1145/3442188.3445922  

Biega, A. J., Gummadi, K. P., & Weikum, G. (2018). Equity of attention: Amortizing individual fairness in rankings. In *Proceedings of the 41st International ACM SIGIR Conference on Research & Development in Information Retrieval* (pp. 405–414). https://doi.org/10.1145/3209978.3210063  

Bolukbasi, T., Chang, K. W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. In *Advances in Neural Information Processing Systems* (pp. 4349–4357). https://proceedings.neurips.cc/paper/2016/file/a486cd07e4ac3d270571622f4f316ec5-Paper.pdf  

Bommasani, R., Hudson, D. A., Adeli, E., et al. (2021). On the opportunities and risks of foundation models. *arXiv preprint* arXiv:2108.07258. https://arxiv.org/abs/2108.07258  

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. In *Proceedings of the 1st Conference on Fairness, Accountability, and Transparency* (pp. 77–91). https://proceedings.mlr.press/v81/buolamwini18a.html  

Burke, R. (2017). Multisided fairness for recommendation. *Workshop on Fairness, Accountability, and Transparency in Machine Learning (FAT/ML)*. http://arxiv.org/abs/1707.00093  

Denton, E., Hanna, A., Amironesei, R., Smart, A., & Nicole, H. (2021). On the genealogy of machine learning datasets: A critical history of ImageNet. *Big Data & Society, 8*(2), 1–29. https://doi.org/10.1177/20539517211035955  

Diaz, M., Poblete, B., Wang, W., Singh, S., & Park, S. (2022). Vision model fairness evaluation in practice. In *Proceedings of the 2022 Conference on Fairness, Accountability, and Transparency* (pp. 386–398). https://doi.org/10.1145/3531146.3533163  

Doshi‑Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv preprint* arXiv:1702.08608. https://arxiv.org/abs/1702.08608  

Ekstrand, M. D., Das, A., Burke, R., & Diaz, F. (2022). Fairness in recommender systems. In P. Brusilovsky & D. He (Eds.), *Social Information Access* (pp. 371–429). Springer. https://doi.org/10.1007/978-3-030-90267-9_11  

Gat, I., Schwartz, I., Schwing, A., & Hazan, T. (2022). Multimodal fairness: Analyzing multimodal fusion for fairness in vision-language tasks. In *Proceedings of the 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 11837–11846). https://doi.org/10.1109/CVPR52688.2022.01154  

Ganguli, D., Hernandez, D., Lovitt, L., et al. (2023). Red teaming language models with language models. *arXiv preprint* arXiv:2202.03286. https://arxiv.org/abs/2202.03286  

Gehman, S., Gururangan, S., Sap, M., Choi, Y., & Smith, N. A. (2020). RealToxicityPrompts: Evaluating neural toxic degeneration in language models. In *Findings of the Association for Computational Linguistics: EMNLP 2020* (pp. 3356–3369). https://doi.org/10.18653/v1/2020.findings-emnlp.301  

Ge, Y., Liu, S., Gao, R., et al. (2021). Towards long-term fairness in recommendation. In *Proceedings of the 14th ACM International Conference on Web Search and Data Mining* (pp. 445–453). https://doi.org/10.1145/3437963.3441824  

Gururangan, S., Beltagy, I., Downey, D., Kurohashi, S., & Smith, N. A. (2022). Demix layers: Disentangling domains for modular language modeling. *arXiv preprint* arXiv:2108.05036. https://arxiv.org/abs/2108.05036  

Helberger, N., Karppinen, K., & D’Acunto, L. (2018). Exposure diversity as a design principle for recommender systems. *Information, Communication & Society, 21*(2), 191–207. https://doi.org/10.1080/1369118X.2016.1271900  

Hendricks, L. A., Burns, K., Saenko, K., Darrell, T., & Rohrbach, A. (2021). Women also snowboard: Overcoming bias in captioning models. In *Proceedings of the European Conference on Computer Vision* (pp. 793–811). https://doi.org/10.1007/978-3-030-58577-8_47  

Hohman, F., Wongsuphasawat, K., Kery, M. B., & Patel, K. (2020). Understanding and visualizing data iteration in machine learning. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). https://doi.org/10.1145/3313831.3376177  

Holstein, K., Wortman Vaughan, J., Daumé III, H., Dudik, M., & Wallach, H. (2019). Improving fairness in machine learning systems: What do industry practitioners need? In *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems* (pp. 1–16). https://doi.org/10.1145/3290605.3300830  

Liang, P. P., Wu, T., Zou, J., Raji, I. D., Prabhumoye, S., Deshpande, A., Morris, M. R., Bernstein, M., & Nushi, B. (2022). Holistic evaluation of language models. *arXiv preprint* arXiv:2211.09110. https://arxiv.org/abs/2211.09110  

Madras, D., Creager, E., Pitassi, T., & Zemel, R. (2018). Learning adversarially fair and transferable representations. In *Proceedings of the 35th International Conference on Machine Learning* (pp. 3384–3393). https://proceedings.mlr.press/v80/madras18a.html  

Mansoury, M., Abdollahpouri, H., Pechenizkiy, M., Mobasher, B., & Burke, R. (2020). Feedback loop and bias amplification in recommender systems. In *Proceedings of the 29th ACM International Conference on Information & Knowledge Management* (pp. 2145–2148). https://doi.org/10.1145/3340531.3412152  

Mehrotra, R., McInerney, J., Bouchard, H., Lalmas, M., & Diaz, F. (2018). Towards a fair marketplace: Counterfactual evaluation of the trade-off between relevance, fairness & satisfaction in recommendation systems. In *Proceedings of the 27th ACM International Conference on Information and Knowledge Management* (pp. 2243–2251). https://doi.org/10.1145/3269206.3272027  

Mitchell, M., Baker, D., Moorosi, N., Denton, E., Hutchinson, B., Hanna, A., & Smart, A. (2022). Diversity and inclusion metrics in subset selection. In *Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 138–149). https://doi.org/10.1145/3514094.3534154  

Noble, S. U. (2018). *Algorithms of oppression: How search engines reinforce racism*. NYU Press. https://doi.org/10.2307/j.ctt1pwt9w5  

Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2022). Beyond accuracy: Behavioral testing of NLP models with CheckList. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4902–4912). https://doi.org/10.18653/v1/2020.acl-main.442  

Singh, A., & Joachims, T. (2018). Fairness of exposure in rankings. In *Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining* (pp. 2219–2228). https://doi.org/10.1145/3219819.3220088  

Slack, D., Hilgard, S., Jia, E., Singh, S., & Lakkaraju, H. (2020). Fooling LIME and SHAP: Adversarial attacks on post hoc explanation methods. In *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society* (pp. 180–186). https://doi.org/10.1145/3375627.3375830  

Solaiman, I., Dennison, C., & Schulman, J. (2021). Process for adapting language models to society (PALMS) with values-targeted datasets. *arXiv preprint* arXiv:2106.10328. https://arxiv.org/abs/2106.10328  

Sonboli, N., Smith, J. J., Cabral, F. S., Cascade, L., & Burke, R. (2020). Fairness and diversity in recommendation: Literature review. *arXiv preprint* arXiv:2004.14355. https://arxiv.org/abs/2004.14355  

Steck, H. (2018). Calibrated recommendations. In *Proceedings of the 12th ACM Conference on Recommender Systems* (pp. 154–162). https://doi.org/10.1145/3240323.3240372  

Steed, R., & Caliskan, A. (2021). Image representations learned with unsupervised pre-training contain human-like biases. In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency* (pp. 701–713). https://doi.org/10.1145/3442188.3445932  

Wang, Z., Qinami, K., Karakozis, I. C., Genova, K., Nair, P., Hata, K., & Russakovsky, O. (2022). Towards fairness in visual recognition: Effective strategies for bias mitigation. In *Proceedings of the 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 8919–8928). https://doi.org/10.1109/CVPR52688.2022.00872  

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E. H., Le, Q. V., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *arXiv preprint* arXiv:2201.11903. https://arxiv.org/abs/2201.11903  

Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.-S., Cheng, M., Glaese, M., Balle, B., Kasirzadeh, A., et al. (2022). Taxonomy of risks posed by language models. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency* (pp. 214–229). https://doi.org/10.1145/3531146.3533088  

Zemel, R., Wu, Y., Swersky, K., Pitassi, T., & Dwork, C. (2013). Learning fair representations. In *Proceedings of the 30th International Conference on Machine Learning* (pp. 325–333). https://proceedings.mlr.press/v28/zemel13.html  

Zhang, B. H., Lemoine, B., & Mitchell, M. (2018). Mitigating unwanted biases with adversarial learning. In *Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society* (pp. 335–340). https://doi.org/10.1145/3278721.3278779  