Title: Making Decisions in the Face of Uncertainty—Again. 
Date: 2026-01-17
Category: Technical
Tags: Probability
Slug: probability-1-20250715
Cover: /images/technical/LLM_uncertainty.png




This is not the first time that I am encountering decisioning in the presence of uncertainty. At TruU we use various techniques (IP protected) to make reliable decisions in the presence of errors in Deep and traditional ML models. In addition, my PhD thesis involved making reliable decisions in the presence of floating point errors. 

LLM inferences are no different. Since this is language, their are errors beyond simple correctness to account for; something I encountered in our translation tools at TruU, where we had to grapple with a nuanced notion of correctness that also involved tone, style, and cultural appropriateness in addition to semantic correctness. For this article, I will focus only on semantic correctness. This article is primarily inspired by \[Liu et al. 2025, & Shorinwa et al. 2025\] before diving into the rabbit hole. 

This is an updated version of the article published a few months ago. 


## §1 White vs Black Box Approaches

Appraches differ if the internals of the LLMs are available for us or not. 


### §1.1 White Box Approaches

* **Average Negative Token Log-Probability** look at internal state of the model to compute the probabilities. For classifiers, this could just be looking at the weights of the final layer and normalizing, for generators this could mean taking the logit of each token, and computing a mean for all the tokens in the output\[Duan et al 2023, Kuhn et al. 2023\]. If $p_{ij}$ is the "weight" of the $j$'th token for the $i$th sentence, then the average confidence of the sentence is given by $$ \text{Average}(p_i) = -\frac{1}{L_i} \sum_j \log(p_{ij}) $$  where $L_i$ is the number of tokens in the sentence.  Other statistical metrics can be used as well. So, if $\text{Average}(p_i)$ is small, the model is more certain. 

* **Entropy** associated with the output distribution of token $j$ in sentence $i$ is defined as 
$$\mathcal{H}_{ij} = -\sum_{w \in \mathcal{D}} p_{ij}(w) \log (p_{ij})(w)$$ where $\mathcal{D}$  denotes the dictionary containing all possible words in the model and $w$ represents a word in $\mathcal{D}$.

* **Perplexity**  is the exponent of the __average negative token log-probability__. It is preferred by some researchers as it is more interpretable compared to negative log-prob. $$ \text{Perplexity}(p) = 2^{-\frac{1}{L_i} \sum_j \log(p_{ij}))} $$ A perplexity of $k$ intuitively means that a model has $k$ choices to choose from, whereas an __average negative log-probability__ has no meaning except lower is better. 


* **Models on Internal data of LLM** \[Ren et al. 2022\]  For LLMs with available input and output embeddings, this method trains a logistic regression classifier on concatenated question-answer embedding pairs labeled with correctness to produce a confidence function that can estimate the probability of correctness for any new LLM-generated answer given its question. 




### §1.2 Black Box Approaches

These approaches receive greater coverage due to their broader practical applicability. A lot of commercially available LLMs are closed sourced so producing some level of confidence on their outputs continues to be an important target.

* **Self-Verbalized Uncertainty** A lot of these ideas fall into the category of asking LLMs to reflect on their work. This can be as simple as asking LLM compute the confidence of its output, to different ways in which we can have LLMs self reflect on the results. There are many variations of this approach. 
	-  \[Wagner et al. 2024\] To evaluate an answer, one can ask a question and generate features by assuming the answer is correct or incorrect, creating various rationales for both cases, then asking a language model to predict the probability of correctness given the rationale (and vice versa), using these predictions to build a confusion matrix and estimate confidence—an approach that, while demonstrated for binary classification, can also be extended to multi-class questions.
	- \[Becker and Soatto 2024\] An interesting variant that goes a little deeper. Generate explanations for each of the answers. Figure out entailment probability of each of the explanations. Figure out the distribution of the answers given the explanation and then marginalize the explanations given an answer. My mathematical bent appreciates this approach but there is no way to say whether this is any better than any of the simpler ones. 
* **Semantic-Similarity Uncertainty** Ask LLM the same question multiple times using different random seeds or temperature settings. At that point we can go multiple routes. There is
    * **Graph Based: Pairwise Connections** Use Natural Language Inference (NLI) models to score entailment and contradiction between every pair of generated outputs. Create an adjacency matrix of this graph. Now one can bring the entire machinary of graph theory to bear on this problem. For example, we can look at Eccentricity of the graph. For a node $v$ in the graph $\mathcal{G}$,  $\text{ecc}(v)$ is the maximum **shortest path** distance from $v$ to any other node. $\text{ecc}(v) = \max\limits_{u \in V} \text{dist}(v, u)$. High eccentricity → wide semantic variability. $\text{radius}(\mathcal{G}) = \min\limits_{v \in V} \text{ecc}(v)$ and $\text{diameter}(\mathcal{G}) = \max\limits_{v \in V} \text{ecc}(v)$. By computing $\text{radius}$ and $\text{diameter}$ one can make various claims about the uncertainty in the result. In addition, we could compute spectral entropy, eigenvalue spread, and others. 
    * **Graph Based: Kernel Language Entropy**. In this approach an embedding space is chosen where the outputs are mapped. If $y_i$ are the various outputs from the question, then let $e_i$ be the corresponding embeddings. Then $$K(e_i, e_j) = \exp\left(-\frac{\|e_i - e_j\|^2}{2\sigma^2}\right)$$ can be used to create an $n \times n$ similarity matrix $K$, that can tell how semantically each output is to othes. Given this matrix we can compute either the spectral entropy or the Renyi entropy. Renyi entropy ($H_{KLE}$ shown below) measures the geometric dispersion of the responses is better for this graph, spectral entropy which measures the connectedness of the graph is better suited for the connection graph shown earlier. 

$$H_{KLE} = -\log\left(\frac{1}{n^2} \sum_{i=1}^{n} \sum_{j=1}^{n} K(e_i, e_j)\right)$$

* **Reasoning Uncertainty** Extend any of the previous approaches to Reasoning steps. For example in a Chain-of-Thought approach, measure uncertainty for each steps and then combine it, giving us CoT-UQ [Zhang et al. 2025]. Similarly Tree-of-Thought (ToT) can be extended to Tree-of-uncertain-Thought (ToUT) by computing uncertainties at each of the decision points \[Mo et al. 2024\]. This allows for backtracking when uncertainty is high. 

* **Conformal Prediction** Assume that you have a calibration set that follows the distribution of the population. If this assumption is met, this approach can deliver guaranteed results. So, $\mathcal{D}_{\text{cal}} = \{(x_i, y_i)\}_{i=1}^n$ where $x_i$ is an input (e.g. a prompt) and $y_i$ is its true label. Define a nonconformity score $S(x, \hat{y}, y)$ that tells you: how bad is the model's prediction $\hat{y}$, given the true answer $y$. For a simple classification example this could be $S = 1 - P(\hat{y})$. Now we compute the threshold $\tau$, such that the error is guaranteed to be less than $\alpha$. From the calibration set compute $s_i = S(x_i, \hat{y}_i, y_i) \text{ for } i = 1,\dots,n$. Then compute the $(1-\alpha)$-quantile of the scores: $\tau = \text{Quantile}_{1-\alpha}(s_i,\dots,s_n)$. This is the threshold for acceptable non-conformity. Given a new input $x_{new}$, create multiple outputs $\hat{y}_1,\dots,\hat{y}_k$. Select the predictions with $S(x_{new},\hat{y}_j) \leq \tau$. These are guaranteed to be correct with a probabilty $\geq 1 - \alpha$. \[Su, Jiayuan, et al. 2024\]. This approach can easily be extended for a white-box implementation so $S$ can take advantage of knowledge of the internal state of the LLM. 


## §2 Mechanistic Interpretability

Even though mechanistic interpretibility is a white box technique it deserves its own section because its perpose is to truly understand how LLM understands the world and perhaps the ability to interpret the results. Some concepts from this approach

* **Superposition, polysemanticity, and circular representations** Neural networks typically represent features in a straightforward manner where an n-dimensional space can encode n unique features—for instance, when the concept "Golden Gate" is present, a specific set of neurons will activate. However, LLM neural networks exhibit a phenomenon called superposition, where they represent more features than they have dimensions, meaning an n-dimensional space can capture m unique features when m > n, making interpretability significantly more challenging \[Elhage et al. 2022\]. The converse phenomenon is polysemanticity, where a single set of neurons can encode multiple different concepts. While these concepts may overlap, the prevailing theory suggests that features still exist as linear combinations of dimensions. Recent research has revealed even more complex representational structures, with \[Engels et al. 2024\] discovering features that are circularly dependent, finding that concepts like days of the week and months of the year are represented in circular patterns within the neural network's feature space.
* **Probing Classifier** Say we want to see if a particular hidden feature encodes the concept "animal". We send various sentences through the NN and get the values of various hidden layers. If we can train a NN that can predict an animal using some subsets of some hidden layers then we can say that those parameters encode the concept "animal" \[Yonatan 2022\]. 
* **Sparse Autoencoders (SAEs)** SAEs help solve the problem of superposition and polysemanticity but training a high dimensional autoencoder so that we can disentangle the polysemanticity and unique vectors encode unique concepts. This leads to more interpretable features, can allow for some control of the LLMs. So, if there is a region of the features which encodes uncertainty we can make the LLM overconfident by turning if off. 


## §3  Thoughts

The intellectual side of me really likes the previous section so that we can finally understand why certain decisions were made and make AI truly safe. However, the practioner side of me has more immediate concerns and looks like we have lots of choices to pick from. 

What I have found in practice to work best are:
* Use multiple models from different families, and use their ensemble.
* Rather than attempting to give a high fidelity answer, give an answer when u are sure but choose not to give an answer whenever in doubt. So, e.g. if you are using google, OpenAI and Anthropic as your models, give an answer with a lot of certainty when all three models agree and not give any answer when there is any disagreement.
* If you can find a calibration set matching the population, use Conformal Prediction, but as always genius is in the details. 


## §4 References

* \[Becker and Soatto 2024\] Becker, Evan, and Stefano Soatto. "Cycles of Thought: Measuring LLM Confidence through Stable Explanations." _arXiv preprint arXiv:2406.03441_ (2024).
* \[Duan et al 2023\] Jinhao Duan, Hao Cheng, Shiqi Wang, Chenan Wang,  Alex Zavalny, Renjing Xu, Bhavya Kailkhura, and  Kaidi Xu. 2023. Shifting attention to relevance: Towards the uncertainty estimation of large language  models. ArXiv preprint, abs/2307.01379.
* \[Elhage et al. 2022\] Elhage, Nelson, et al. "Toy models of superposition." arXiv preprint arXiv:2209.10652 (2022).
* \[Engels et al. 2024] Not All Language Model Features Are Linear. arXiv  preprint arXiv:2405.14860 (2024).  
* \[Kuhn et al. 2023\] Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. 2023.  Semantic uncertainty: Linguistic invariances for un-  certainty estimation in natural language generation.  ArXiv preprint, abs/2302.09664.
* \[Li, Moxin, et al. 2024 \] Li, Moxin, et al. "Think twice before assure: Confidence estimation for large language models through reflection on multiple answers." _arXiv preprint arXiv:2403.09972_ (2024).
* \[Liu et al. 2025\] Liu, X., Chen, T., Da, L., Chen, C., Lin, Z., & Wei, H. (2025). Uncertainty quantification and confidence calibration in large language models: A survey. arXiv preprint arXiv:2503.15850.
* \[Mo et al. 2024\] Shentong Mo and Miao Xin. 2024. Tree of uncertain thoughts reasoning for  large language models. In ICASSP 2024-2024 IEEE International Conference on  Acoustics, Speech and Signal Processing (ICASSP). IEEE, 12742–12746
* \[Pedapati et al. 2024\] Pedapati, Tejaswini, et al. "Large Language Model Confidence Estimation via Black-Box Access." _arXiv preprint arXiv:2406.04370_ (2024).
* \[Ren et al. 2022 \] Jie Ren, Jiaming Luo, Yao Zhao, Kundan Krishna, Mo-  hammad Saleh, Balaji Lakshminarayanan, and Pe-  ter J Liu. 2022. Out-of-distribution detection and  selective generation for conditional language models.  ArXiv preprint, abs/2209.15558.
* \[Shorinwa et al. 2025\] Shorinwa, O., Mei, Z., Lidard, J., Ren, A. Z., & Majumdar, A. (2025). A survey on uncertainty quantification of large language models: Taxonomy, open research challenges, and future directions. ACM Computing Surveys.
* \[Shrivastava et al. 2023 \] Vaishnavi Shrivastava, Percy Liang, and Ananya Kumar.  2023. Llamas know what gpts don’t show: Surrogate  models for confidence estimation. ArXiv preprint,  abs/2311.08877.
* \[Su, Jiayuan, et al. 2024\] Api is enough: Conformal prediction for large language models without logit-access." arXiv preprint arXiv:2403.01216 (2024).
* \[Wagner et al. 2024\]Wagner, Nico, et al. "Black-box Uncertainty Quantification Method for LLM-as-a-Judge." _arXiv preprint arXiv:2410.11594_(2024).
* \[Yonatan 2022\] Yonatan Belinkov. 2022. Probing classifiers: Promises, shortcomings, and advances. Computational Linguistics 48, 1 (2022)
Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert Huben, and Lee Sharkey. 2023. Sparse autoencoders ind highly interpretable  features in language models. arXiv preprint arXiv:2309.08600 (2023).
* \[Zhang et al. 2025\] Boxuan Zhang and Ruqi Zhang. 2025. CoT-UQ: Improving Response-wise  Uncertainty Quantification in LLMs with Chain-of-Thought. arXiv preprint  arXiv:2502.17214 (2025).
* \[Zhen et al. 2023\] Generating with Confidence: Uncertainty Quantification for Black-box Large Language Models. Transactions on Machine Learning Research (2023)






