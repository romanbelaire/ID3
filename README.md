Roman Belaire

Project 1 (ID3)

ID3 Implementation in Python
----------------------------

File ID3.py contains my implementation of the ID3 decision tree
algorithm. To run the program, execute it as a python script followed by
the .csv file path containing the dataset you'd like to create a tree
for, i.e. \$ python ID3.py health.csv

**Program limitations:**

-   Requires Pandas version 0.23.4 or greater. Older versions may work,
    > but this was the version I used when programming the algorithm.

<!-- -->

-   The algorithm also assumes a binary classification problem.
    > Multi-value input features are okay, but the class column must be
    > binary. If it is not, the program will select one value as
    > positive and the rest as negative.

<!-- -->

-   The dataset must be encoded into discrete integers before running.
    > The algorithm may still work if this is not done for the feature
    > columns, however the class column (y-value) **must** be binary and
    > encoded to 1 or 0 output. As I understand it, this is a limitation
    > of the ID3 algorithm itself; workarounds exist but are considered
    > a different, more robust algorithm.

Decision Tree Complete Working
------------------------------

> Calculations for the ID3 algorithm are as follows:
>
> $E(S)\  = \  - \frac{6}{10}(\log_{2}(\frac{6}{10})\  + \  - \frac{4}{10}(\log_{2}(\frac{4}{10})\  = 0.971$
>
> $IG(S,\ HasJob)\  = \ E(S)\  - \ P(HasJob_{0})E(HasJob_{0})\  - P(HasJob_{1})E(HasJob_{1})$,
> where
>
> $E(HasJob_{0})\  = \  - \frac{2}{4}\text{lo}g_{2}(\frac{2}{4})\  + \  - \frac{2}{4}\text{lo}g_{2}(\frac{2}{4})\  = \ 1.0$,
> and
>
> $E(HasJob_{1})\  = \  - \frac{4}{6}\text{lo}g_{2}(\frac{4}{6})\  + \  - \frac{2}{6}\text{lo}g_{2}(\frac{2}{6})\  = 0.918$;
>
> $P(HasJob_{0})\  = \ \frac{4}{10}$
>
> $P(HasJob_{1})\  = \ \frac{6}{10}$
>
> Giving us the calculation:
>
> $IG(S,\ HasJob)\  = \ 0.971\  - \ \frac{2}{6}(0.918)\  - \ \frac{2}{4}(1.0)\  = \ 0.01997\  \approx 0.02$
>
> $IG(S,\ Insurance)\  = \ E(S)\  - \ P(insurance_{0})E(insurance_{0})\  - P(insurance_{1})E(insurance_{1})$,
> where
>
> $E(insurance_{0})\  = \  - \frac{4}{8}\text{lo}g_{2}(\frac{4}{8})\  + \  - \frac{4}{8}\text{lo}g_{2}(\frac{4}{8})\  = \ 1.0$,
> and
>
> $E(insurance_{1})\  = \  - \frac{2}{2}\text{lo}g_{2}(\frac{2}{2})\  = 0.0$;
>
> $P(insurance_{0})\  = \ \frac{8}{10}$
>
> $P(insurance_{1})\  = \ \frac{2}{10}$
>
> Giving us the calculation:
>
> $IG(S,\ HasJob)\  = \ 0.971\  - \ \frac{8}{10}(1.0)\  - \ \frac{2}{10}(0.0)\  = \ 0.17$
>
> $IG(S,\ Vote)\  = \ E(S)\  - \ P(Vote_{0})E(Vote)\  - P(Vote_{1})E(Vote_{1})$,
> where
>
> $E(Vote_{0})\  = \  - \frac{4}{4}\text{lo}g_{2}(\frac{4}{4})\  = \ 0.0$,
> and
>
> $E(Vote_{1})\  = \  - \frac{6}{6}\text{lo}g_{2}(\frac{6}{6})\  = 0.0$;
>
> $P(Vote_{0})\  = \ \frac{4}{10}$
>
> $P(Vote_{1})\  = \ \frac{6}{10}$
>
> Giving us the calculation:
>
> $IG(S,\ HasJob)\  = \ 0.971\  - \ \frac{4}{10}(0.0)\  - \ \frac{6}{10}(0.0)\  = \ 0.971$
>
> **This is our highest information gain, so we pick *vote* as our
> root.**

Decision Tree
-------------

Once we select Vote as our root, we partition the dataset into subsets
corresponding to the value of Vote that we branch to. Since each subset
is a pure subset, we make each branch a leaf node for our decision tree:

We can use this tree to evaluate new points of data:

  **Has Job**   **Has Insurance**   **Voted**   **Decision:**
  ------------- ------------------- ----------- ---------------
  No            Yes                 Yes         Leave-Alone
  Yes           No                  Yes         Leave-Alone
  No            Yes                 No          Force-Into

Program Output
--------------

**The program output supports our equations:**

  ----------------------------------------------------------------------------------
  $ python ID3.py health.csv\
  Has\_Job Has\_Insurance Voted Action\
  0 1 1 1 0\
  1 1 0 1 0\
  2 1 0 0 1\
  3 0 0 1 0\
  4 0 0 0 1\
  5 1 1 1 0\
  6 1 0 1 0\
  7 1 0 0 1\
  8 0 0 1 0\
  9 0 0 0 1\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Action @ 1\
  -(6/10)-0.7369655941662062 + -(4/10)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Action: 0.9709505944546686\
  -(4/6)-0.5849625007211563 + -(2/6)-1.5849625007211563 + = 0.9182958340544896\
  Entropy for Has\_Job @ 1: 0.9182958340544896\
  \
  -(2/4)-1.0 + -(2/4)-1.0 + = 1.0\
  Entropy for Has\_Job @ 0: 1.0\
  \
  0.9709505944546686 - (6/10)0.9182958340544896 - (4/10)1.0 = 0.01997309402197489\
  Information Gain for Has\_Job: 0.01997309402197489\
  \
  \
  -(6/10)-0.7369655941662062 + -(4/10)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Action: 0.9709505944546686\
  -(2/2)0.0 + = 0.0\
  Entropy for Has\_Insurance @ 1: 0.0\
  \
  -(4/8)-1.0 + -(4/8)-1.0 + = 1.0\
  Entropy for Has\_Insurance @ 0: 1.0\
  \
  0.9709505944546686 - (2/10)0.0 - (8/10)1.0 = 0.17095059445466854\
  Information Gain for Has\_Insurance: 0.17095059445466854\
  \
  \
  -(6/10)-0.7369655941662062 + -(4/10)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Action: 0.9709505944546686\
  -(6/6)0.0 + = 0.0\
  Entropy for Voted @ 1: 0.0\
  \
  -(4/4)0.0 + = 0.0\
  Entropy for Voted @ 0: 0.0\
  \
  0.9709505944546686 - (6/10)0.0 - (4/10)0.0 = 0.9709505944546686\
  Information Gain for Voted: 0.9709505944546686\
  \
  \
  Node created: Action @ 1 -\> Voted, IG = 0.9709505944546686\
  removing Voted from \[\'Has\_Job\', \'Has\_Insurance\', \'Voted\'\]\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Voted @ 1\
  Pure Subset; Leaf Node created: Voted @ 1 -\> 0\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Voted @ 0\
  Pure Subset; Leaf Node created: Voted @ 0 -\> 1

  ----------------------------------------------------------------------------------

Generalized Use
---------------

Additionally, this algorithm implementation can be used for other
datasets as well. This is demonstrated by running the algorithm on the
'tennis' dataset provided in the slides; Our output equations are
correct and the resulting tree matches the tree in the slides:

  ------------------------------------------------------------------------------------------------------------
  $ python ID3.py tennis.csv\
  Outlook Humidity Wind Play\
  0 0 1 0 0\
  1 0 1 1 0\
  2 1 1 0 1\
  3 2 1 0 1\
  4 2 0 0 1\
  5 2 0 1 0\
  6 1 0 1 1\
  7 0 1 0 0\
  8 0 0 0 1\
  9 2 0 0 1\
  10 0 0 1 1\
  11 1 1 1 1\
  12 1 0 0 1\
  13 2 1 1 0\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Play @ 1\
  -(9/14)-0.6374299206152917 + -(5/14)-1.4854268271702415 + = 0.9402859586706309\
  Entropy for Play: 0.9402859586706309\
  -(3/5)-0.7369655941662062 + -(2/5)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Outlook @ 0: 0.9709505944546686\
  \
  -(4/4)0.0 + = 0.0\
  Entropy for Outlook @ 1: 0.0\
  \
  -(3/5)-0.7369655941662062 + -(2/5)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Outlook @ 2: 0.9709505944546686\
  \
  0.9402859586706309 - (5/14)0.9709505944546686 - (4/14)0.0 - (5/14)0.9709505944546686 = 0.2467498197744391\
  Information Gain for Outlook: 0.2467498197744391\
  \
  \
  -(9/14)-0.6374299206152917 + -(5/14)-1.4854268271702415 + = 0.9402859586706309\
  Entropy for Play: 0.9402859586706309\
  -(4/7)-0.8073549220576043 + -(3/7)-1.222392421336448 + = 0.9852281360342516\
  Entropy for Humidity @ 1: 0.9852281360342516\
  \
  -(6/7)-0.22239242133644802 + -(1/7)-2.8073549220576046 + = 0.5916727785823275\
  Entropy for Humidity @ 0: 0.5916727785823275\
  \
  0.9402859586706309 - (7/14)0.9852281360342516 - (7/14)0.5916727785823275 = 0.15183550136234136\
  Information Gain for Humidity: 0.15183550136234136\
  \
  \
  -(9/14)-0.6374299206152917 + -(5/14)-1.4854268271702415 + = 0.9402859586706309\
  Entropy for Play: 0.9402859586706309\
  -(6/8)-0.4150374992788438 + -(2/8)-2.0 + = 0.8112781244591328\
  Entropy for Wind @ 0: 0.8112781244591328\
  \
  -(3/6)-1.0 + -(3/6)-1.0 + = 1.0\
  Entropy for Wind @ 1: 1.0\
  \
  0.9402859586706309 - (8/14)0.8112781244591328 - (6/14)1.0 = 0.04812703040826932\
  Information Gain for Wind: 0.04812703040826932\
  \
  \
  Node created: Play @ 1 -\> Outlook, IG = 0.2467498197744391\
  removing Outlook from \[\'Outlook\', \'Humidity\', \'Wind\'\]\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Outlook @ 0\
  -(3/5)-0.7369655941662062 + -(2/5)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Play: 0.9709505944546686\
  -(3/3)0.0 + = 0.0\
  Entropy for Humidity @ 1: 0.0\
  \
  -(2/2)0.0 + = 0.0\
  Entropy for Humidity @ 0: 0.0\
  \
  0.9709505944546686 - (3/5)0.0 - (2/5)0.0 = 0.9709505944546686\
  Information Gain for Humidity: 0.9709505944546686\
  \
  \
  -(3/5)-0.7369655941662062 + -(2/5)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Play: 0.9709505944546686\
  -(2/3)-0.5849625007211563 + -(1/3)-1.5849625007211563 + = 0.9182958340544896\
  Entropy for Wind @ 0: 0.9182958340544896\
  \
  -(1/2)-1.0 + -(1/2)-1.0 + = 1.0\
  Entropy for Wind @ 1: 1.0\
  \
  0.9709505944546686 - (3/5)0.9182958340544896 - (2/5)1.0 = 0.01997309402197489\
  Information Gain for Wind: 0.01997309402197489\
  \
  \
  Node created: Outlook @ 0 -\> Humidity, IG = 0.9709505944546686\
  removing Humidity from \[\'Humidity\', \'Wind\'\]\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Humidity @ 1\
  Pure Subset; Leaf Node created: Humidity @ 1 -\> 0\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Humidity @ 0\
  Pure Subset; Leaf Node created: Humidity @ 0 -\> 1\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Outlook @ 1\
  Pure Subset; Leaf Node created: Outlook @ 1 -\> 1\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Outlook @ 2\
  -(3/5)-0.7369655941662062 + -(2/5)-1.3219280948873622 + = 0.9709505944546686\
  Entropy for Play: 0.9709505944546686\
  -(3/3)0.0 + = 0.0\
  Entropy for Wind @ 0: 0.0\
  \
  -(2/2)0.0 + = 0.0\
  Entropy for Wind @ 1: 0.0\
  \
  0.9709505944546686 - (3/5)0.0 - (2/5)0.0 = 0.9709505944546686\
  Information Gain for Wind: 0.9709505944546686\
  \
  \
  Node created: Outlook @ 2 -\> Wind, IG = 0.9709505944546686\
  removing Wind from \[\'Wind\'\]\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Wind @ 0\
  Pure Subset; Leaf Node created: Wind @ 0 -\> 1\
  \-\-\-\-\-\-\-\-\-\-\--\
  Calculations for Wind @ 1\
  Pure Subset; Leaf Node created: Wind @ 1 -\> 0

  ------------------------------------------------------------------------------------------------------------
