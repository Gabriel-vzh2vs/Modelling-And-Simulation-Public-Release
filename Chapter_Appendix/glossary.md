(sec:glossary)=
# Glossary

A glossary of common terms used throughout our text.

```{glossary}
**Experiments**
    refer to a single, complete execution of the simulation process driven 
    by a  set of randomly generated inputs. Additionally, The collection 
    of many  experiments forms the basis of the Monte Carlo Method.
    Mathematically, an experiment is a mapping from a sampled point 
    in the domain to a  point in the output space (Co-domain), 
    via the model function.

**Kurtosis** ($\gamma_2$)
    measures the "tailedness" (or "tail-heaviness") 
    of the probability distribution of a real-valued random variable. 
    It describes the sharpness of the peak and the weight of the tails 
    relative to a normal distribution. Kurtosis generally has three
    forms. *Mesokurtic* ($\gamma \approx 0$) The distribution has a kurtosis 
    similar to that of a normal distribution. Tails are neither particularly 
    heavy nor light. *Leptokurtic* ($\gamma_2 > 0$) The distribution has heavier 
    tails and a sharper peak than a normal distribution. This means there's 
    a higher probability of extreme values (outliers). *Platykurtic* 
    ($\gamma < 0) The distribution has lighter tails and a flatter peak 
    than a normal distribution. This means there's a lower probability of extreme values, 
    and values tend to be more clustered around the mean but less 
    peaked than a normal distribution.

**Skewness** ($\gamma_1$)
    measures the asymmetry of the probability distribution of a 
    real-valued random variable about its mean. Skewness has two types.
    *Positive* Skewness means that the distribution has a longer or fatter 
    tail on the right side and the distribution's PMF is 
    concentrated on the left. The mean is typically greater than the median.
    *Negative* Skewness mean that The distribution has a longer or fatter tail 
    on the left side and the mass of the distribution is concentrated on the 
    right. The mean is typically less than the median.

**The Strong Law of Large Numbers**
    implies that for almost every sequence of outcomes, 
    the sample average $\bar{X_n}$ will eventually 
    converge to $\mu$ as the number of trials $n$ goes to infinity. 
    The set of outcome sequences for which  $\bar{X_n}$ does not 
    converge to $\mu$ has a total probability of zero.

**The Weak Law of Large Numbers**
    says that for a sufficiently large number of trials 
    n, the probability that the sample average $\bar{X_n}$ will be off by greater 
    than $\epsilon$  from the true mean $\mu$ becomes very small, approaching zero. 
    Therefore, there is no guarantee that $\bar{X_n}$ will converge to 
    $\mu$, but rather that the chances of it straying significantly become increasingly 
    unlikely as n grows.
```
