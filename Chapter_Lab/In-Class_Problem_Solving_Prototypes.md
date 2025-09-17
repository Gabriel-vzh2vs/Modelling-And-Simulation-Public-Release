(ICPS)=
# ICPS Prototypes

:::{note} A Note on the ICPSes in this section
:class: dropdown

This section is more of a view of possible in-class/in-lab graded work,
as many courses have adopted this format to great success at the University
of Virginia and beyond.
:::

## ICPS 1: Bayes vs Simulation (Using Mathematical Results to Build Simulations)

Facebook has a content team that labels pieces of content on the platform as spam or not spam. 90% of them are diligent raters and will label 20% of the content as spam and 80% as non-spam. The remaining 10% are non-diligent raters and will label 0% of the content as spam and 100% as non-spam. Assume the pieces of content are labeled independently from one another, for every rater. Given that a rater has labeled 4 pieces of content as good, what is the probability that they are a diligent rater?

Produce a Crude Monte Carlo Simulation that is able to reproduce these results from the closed-form formulation of Bayes' Theorem.

We will present a method for solving this with Bayes' Theorem, so the simulation based on this question
can be checked using an empirical method.

To use Bayes with the conditional probability established in the problem above, we need to understand the event space through establishing a prior. In this case, we are assuming that there is a 0.9 probability of a diligent rater with a 0.1 chance of a non-diligent rater.

From this, we can construct a table that defines the event space.

```{raw} latex
\begin{tabular}{|c|c|c|c|}
\hline
\multicolumn{2}{|c|}{Diligent: 0.9} & \multicolumn{2}{c|}{Non-diligent: 0.1} \\
\hline
Spam & Non-spam & Spam & Non-spam \\
\hline
0.2 & 0.8 & 0 & 1 \\
\hline
\end{tabular}
```

Once the probabilities $P(A|B)$, $P(B|A)$, $P(A)$, and $P(B)$ that constitute the Bayes Theorem are established, then it shall be possible to use a closed-form formula to calculate the probability of these events occurring.

These events are defined as the following:

- $P(B|A)$ is defined as four pieces of content marked as non-spam by a diligent rater which is equal to $0.8^4$;
- $P(A)$ = The probability of selecting a diligent rater which is equal to 0.9;
- $P(B)$ = four pieces of content are marked as non-spam by either type of rater which is equal to $0.9 * 0.8^4 + 0.1 (1)$.

Now, the Bayes Theorem:

$$P(A|B) = \frac{P(B|A) * P(A)}{P(B)}$$

And as the values constituting this theorem for answering the question above are known, they can be substituted below to analytically solve this problem.

$$0.787 = \frac{0.8^4 * 0.9}{0.9 * 0.8^4 + 0.1 (1)}$$

Simulation answer:

```{code} python3
import numpy as np

nrounds = 1000
four_non_spam_cases = 0
diligent_raters = 0

while four_non_spam_cases < nrounds:
    is_diligent = np.random.binomial(1, 0.9, 1)[0]

    spam_count = 0
    for j in range(4):
        is_spam = 0
        if is_diligent:
            spam_count += np.random.binomial(1, 0.2, 1)[0]

    if spam_count == 0:
        four_non_spam_cases += 1
        diligent_raters += is_diligent

simulated_probability = diligent_raters / nrounds

print(simulated_probability)
```


### ICPS-Extension 1: 

## ICPS 2: Coins from 538

While traveling in the Kingdom of Arbitraria, you are accused of a heinous crime. Arbitraria decides who’s guilty or innocent not through a court system, but a board game. It’s played on a simple board: a track with sequential spaces numbered from 0 to 1,000. The zero space is marked “start,” and your token is placed on it. You are handed a fair six-sided die and three coins. You are allowed to place the coins on three different (nonzero) spaces. Once placed, the coins may not be moved.

After placing the three coins, you roll the die and move your token forward the appropriate number of spaces. If, after moving the token, it lands on a space with a coin on it, you are freed. If not, you roll again and continue moving forward. If your token passes all three coins without landing on one, you are executed. On which three spaces should you place the coins to maximize your chances of survival?

## ICPS 3: Boarding Puzzle (Simulations Over Solving A Difficult Mathematical Problem)

One hundred people are lined up with their boarding passes showing their seats on the 100-seat Plane. The first guy in line drops his pass as he enters the plane, and unable to pick it up with others behind him sits in a random seat. The people behind him, who have their passes, sit in their seats until one of them comes upon someone sitting in his seat, and takes his seat in a new randomly chosen seat. This process continues until there is only one seat left for the last person.

## ICPS 4: Feller's coin-tossing (Using Simulation to Check Complex Mathematical Results)

If you flip a coin n times, what is the probability there are no streaks of k heads in a row?

The question might seem to be directly answerable by using the binomial distribution's PDF, but that is woefully
insufficient. This is because the streak we are measuring in this question is NOT independent,
a fundamental assumption of using the binominal distribution. This problem is actually related to
Feller's coin-tossing constants and Fibonacci numbers, which simulation can do both approaches!

## ICPS 5: Coupon Collector Problem (A Classical Statistical Problem that it is Easier to Use Crude Monte Carlo For)

A cereal company puts one of $n$ different collectible cards in each box. How many boxes do you expect to
buy before collecting all $n$ cards?

The following provides an analytic answer to the question posed above. This is included for
checking your simulation work.

We begin with a unique card, as the first box will always contain a card that is new to you.
Now, the probability of getting a second unique card is $\frac{n-1}/n$ which can be represented
as a bernoulli trial.
In this case, we notice that a series of bernoulli trials is the geometric
distribution as we are tracking the expected number until a success,
which is expressed as with:

$$\frac{1}{P(Success)} = \frac{n-1}$$

For the third unique card, the state space for possible new cards reduces to $n-2$,
so the probability is $\frac{n-2}{n}$ and the $E(trials)$ should be $\frac{n}{n-2}$.
This pattern continues for n until the entire
