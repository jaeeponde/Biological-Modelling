Played around with modelling biological phenomena using differential equations

Central Dogma :
 - uses the ODE for transcription and translation
 - We can observe that protein synthesis starts slightly after mRNA synthesis
 - Both reach a steady state

Activation:
  - uses the ODE for activation of a gene by the translation of another 
  - the translation of gene 2 has the quantity of gene 1 as one of it's parameters for production
  
Repression:
  - uses the ODE for repression of a gene by the translation of another 
  - the translation of gene 2 has the quantity of gene 1 as one of it's parameters for production (which tends to 0 as gene 1 increases)

Negative Feedback Oscillator :
  - Gene 1 activates gene 2
  - Gene 2 activates gene 3
  - Gene 3 represses gene 1

Gillespie Algorithm :
  - Based on https://www.sciencedirect.com/science/article/abs/pii/0021999176900413

Stochastic Oscillator :
  - Combining the ODE's of all the previous simulations to create a stochastic oscillator for 3 genes by choosing random timepoints from an exponential distribution. 
