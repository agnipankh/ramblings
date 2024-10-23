Title: Deep Names for Common Ideas
Date: 2024-10-23 
Category: Technical
Tags: Bayesian
Slug: bayesian-1-20241023

Sometimes, we encounter complex names for concepts we’ve been using all along. Recently, I started exploring Dempster-Shafer Theory (more on that as I learn further) and came across the following:

### Principle of Insufficient Reason

Also known as the Principle of Indifference, which, despite sounding like a bourgeois view of the proletariat, is actually the assignment of equal probabilities to priors when no other evidence is available. For example, if no evidence is present for a coin (even if the coin might be biased), we would assign a 50/50 prior probability. This principle may have first been articulated by Bernoulli, Keynes, and possibly even Poincaré.

### Cromwell's rule

Another one which every practioner learns eventually but I learnt from Andrew Ng, is that we should not assign prior probabilities of 1 or 0 and only do that for statements that are logically true. 

> I beseech you, in the bowels of Christ, think it possible that you may be mistaken.
> - Oliver Cromwell

An example of use of this rule is provided by Zadeh, where a patient can have a symptom because of 3 diseases A, B, and C. Doctor John says that the patient has disease A with 99.5% probability and B with 0.5% probability. Doctor Bob says that the patient has disease C with 99.5% probability and B with 0.5% probability. Given the two facts, both Bayesian and Dempster-Shafer would say that the patient has disease B. This outcome is true even if the two doctors had a probability of 99.9999% certainty. The only time we dont come up with an answer is when the probability of disease A and C is 1. 




I might need to spend some time considering the deeper implications of this… or perhaps it’s just scientists giving fancy names to simple ideas.



