# Answers to Problem Set V

*Prepared by* Christian Y. Cahig

## Problem No. 4

Find a basis of solutions for the following ODE.
Try to identify the series as expansions of known functions.

$$
x^{2} y^{\prime \prime} + 2 x^{3} y^{\prime} + \left(x^{2} - 2\right) y = 0
$$ (4.0)

Note that (4.0) can be rewritten as

$$
\left(x - \alpha\right)^{2} A \left(x\right) y^{\prime \prime}
+
\left(x - \alpha\right) B \left(x\right) y^{\prime}
+
C \left(x\right) y
= 0
$$ (4.1)
where $\alpha = 0$, $A \left(x\right) = 1$,
$B \left(x\right) = 2x^{2}$, and
$C \left(x\right) = x^{2} - 2$.
With $A \left(\alpha\right) \neq 0$,
$x = \alpha = 0$ is a regular singular point of (4.0).
The indicial equation would then be

$$
r^{2} +
\left(\frac{B \left(\alpha\right)}{A \left(\alpha\right)} - 1\right) r
+
\frac{C \left(\alpha\right)}{A \left(\alpha\right)}
= 0
\Longrightarrow
r^{2} - r -2 = 0
$$ (4.2)
whose roots are $r_{1} = 2$ and $r_{2} = -1$.
Since $r_{1} - r_{2} = R = 3 \in \mathbb{Z}^{+}$,
we look for two solutions $y_{1}$ and $y_{2}$ of the forms

$$
y_{1} = x^{r_{1}} \sum_{k=0}^{\infty} a_{k} x^{k} = \sum_{k=0}^{\infty} a_{k} x^{k+2}
$$ (4.3a)
$$
y_{2} = c y_{1} \ln x + x^{r_{2}} \sum_{k=0}^{\infty} b_{k} x^{k}
= c y_{1} \ln x + \sum_{k=0}^{\infty} b_{k} x^{k-1}
$$ (4.3b)
where $a_{k}$, $b_{k}$, and $c$ are constants.

We first look for $y_{1}$. Differentiating with respect to $x$,

$$
y_{1}^{\prime} = \sum_{k=0}^{\infty} \left(k+2\right) a_{k} x^{k+1};
\quad
y_{1}^{\prime \prime} = \sum_{k=0}^{\infty} \left(k+1\right) \left(k+2\right) a_{k} x^{k}
$$ (4.4)
Substituting (4.3a) and (4.4) to (4.0), and collecting like terms,

$$
\sum_{k=0}^{\infty} \left[
    \left(k+1\right) \left(k+2\right) - 2
\right] a_{k} x^{k+2}
+
\sum_{k=0}^{\infty} \left(2k+5\right) a_{k} x^{k+4}
= 0
$$ (4.5a)
Explicitly writing the first two terms of the first series
(*i.e.*, $k=0,1$),

$$
0 \cdot a_{0} \cdot x^{2}
+
4 \cdot a_{1} \cdot x^{3}
+
\sum_{k=2}^{\infty} \left[
    \left(k+1\right) \left(k+2\right) - 2
\right] a_{k} x^{k+2}
+
\sum_{k=0}^{\infty} \left(2k+5\right) a_{k} x^{k+4}
= 0
$$ (4.5b)
That the multiplier for $a_{0}$ is $0$ because it is just the indicial equation in disguise.
Because the ODE is homogeneous, the coefficient of each power of $x$ must be zero.
Then, by

$$
0 \cdot a_{0} = 0,
\quad \quad 4 \cdot a_{1} \cdot x^{3} = 0
$$
we deduce that $a_{0}$ must be set by the user and $a_{1} = 0$.
Moreover, we can rewrite the series involving $x^{k+2}$
in terms of $x^{k+4}$ with $k \geq 0$:

$$
\sum_{k=2}^{\infty} \left[
    \left(k+1\right) \left(k+2\right) - 2
\right] a_{k} x^{k+2}
=
\sum_{k=0}^{\infty} \left[
    \left(k+3\right) \left(k+4\right) - 2
\right] a_{k+2} x^{k+4}
$$
Since the terms involving $x^{2}$ and $x^{3}$ are zero,
(4.5b) can now be expressed as a single series in $x^{k+4}$ with $k \geq 0$:

$$
\sum_{k=0}^{\infty} \left\{
    \left[\left(k+3\right) \left(k+4\right) - 2\right] a_{k+2}
    +
    \left(2k + 5\right) a_{k}
\right\} x^{k+4}
= 0
$$ (4.5c)
Due to homogeneity, the coefficient of $x^{k+4}$ must vanish,
giving us a recurrence relation:

$$
a_{k+2} = - \frac{2k + 5}{k^{2} + 7k + 10} a_{k},
\quad k = 0, 1, 2, \ldots
$$ (4.6a)
Having already established that $a_{1} = 0$, we get $a_{k} = 0$ for all odd $k$.
We can thus rewrite (4.6a) to explicitly exclude the odd terms:

$$
a_{2k} = \left(-1\right)^{k} a_{0}
\prod_{j=0}^{k-1} \frac{2j + 5}{j^{2} + 7j + 10},
\quad k = 0, 1, 2, \ldots
$$ (4.6b)
Hence, the first solution $y_{1}$ is

$$
y_{1} = \sum_{k=0}^{\infty} P \left(k\right) a_{0} x^{k+2},
\quad
P \left(k\right) = \left(-1\right)^{k} \prod_{j=0}^{k-1} \frac{2j + 5}{j^{2} + 7j + 10}
$$ (4.7)
where $a_{0}$ is a constant.

Now, from (4.3b),

$$
y_{2} = c y_{1} \ln x + D,
\quad
D = \sum_{k=0}^{\infty} b_{k} x^{k-1}
$$ (4.8a)
$$
y_{2}^{\prime} = c x^{-1} y_{1} + c y_{1}^{\prime} \ln x + D^{\prime},
\quad
D^{\prime} = \sum_{k=0}^{\infty} \left(k-1\right) b_{k} x^{k-2}
$$ (4.8b)
$$
y_{2}^{\prime \prime} = -c x^{-2} y_{1} + 2c x^{-1} y_{1}^{\prime} + c y_{1}^{\prime \prime} \ln x + D^{\prime \prime},
\quad
D^{\prime \prime} = \sum_{k=0}^{\infty} \left(k-1\right) \left(k-2\right) b_{k} x^{k-3}
$$ (4.8c)
Substituting (4.8) to (4.0),

$$
-cy_{1} + 2cxy_{1} + cx^{2} y_{1}^{\prime \prime} \ln x + x^{2} D^{\prime \prime}
+ 2cx^{2} y_{1} + 2cx^{3} y_{1}^{\prime} \ln x + 2x^{3} D^{\prime}
+ \left(x^{2} - 2\right) cy_{1} \ln x + \left(x^{2} - 2\right) D = 0
$$ (4.9a)
Rearranging the ugly mess that is (4.9a),

$$
\left(2x^{2}-1\right) cy_{1} + 2cxy_{1}^{\prime}
+
\left[
    x^{2} y_{1}^{\prime \prime} + 2x^{3} y_{1}^{\prime} + \left(x^{2} - 2\right) y_{1}
\right] c \ln x
+
\left[
    x^{2} D^{\prime \prime} + 2x^{3} D^{\prime} + \left(x^{2} - 2\right) D
\right]
= 0
$$ (4.9b)
Observe that the quantity inside the first bracket in (4.9b)
is just applying $y_{1}$ onto (4.0)&mdash;it is equal to zero:

$$
\left(2x^{2}-1\right) cy_{1} + 2cxy_{1}^{\prime} +
\left[
    x^{2} D^{\prime \prime} + 2x^{3} D^{\prime} + \left(x^{2} - 2\right) D
\right] = 0
$$ (4.9c)
We can rewrite (4.9c) as a "matching" of series:

$$
x^{2} D^{\prime \prime} + 2x^{3} D^{\prime} + \left(x^{2} - 2\right) D
= -2cxy_{1}^{\prime} + \left(1 - 2x^{2}\right) cy_{1}
$$ (4.10)
Using the definitions for $D$ and its derivatives in (4.8),
we can list out the first few terms in the left hand side of (4.10):

$$
0\cdot b_{0} x^{-1} - 2b_{1} x^{0} - \left(2b_{2} - b_{0}\right) x^{1}
+ \left(0\cdot b_{3} + b_{1}\right) x^{2} + \cdots
$$ (4.11)
In series form, the right hand side of (4.10) is

$$
- \sum_{k=0}^{\infty} c\left(2k+3\right) P\left(k\right) a_{0} x^{k+2}
- \sum_{k=0}^{\infty} 2c P\left(k\right) a_{0} x^{k+4}
=
- 3 ca_{0} x^{2} + \frac{5}{2} ca_{0} x^{3} + \cdots
$$ (4.12)
Comparing the $x^{-1}$ and $x^{0}$ terms in (4.11) and (4.12),
we can deduce information for $b_{0}$ and $b_{1}$:

- $0\cdot b_{0} = 0$ suggests that $b_{0}$ is a constant to be set by the user.
- $-2b_{1} = 0$ means $b_{1} = 0$.
- $-2b_{2} - b_{0} = 0$ means $b_{2} = -\frac{1}{2} b_{0}$.

Comparing the $x^{2}$ terms in (4.11) and (4.12),

$$
0\cdot b_{3} + b_{1} = -3ca_{0} \Longrightarrow ca_{0} = 0
$$ (4.13)
which means that we can set $c=0$ regardless of $a_{0}$.
As such $y_{2}$ is rid of the logarithm term:

$$
y_{2} = \sum_{k=0}^{\infty} b_{k} x^{k-1}
= b_{0} x^{-1} + b_{1} + b_{2} x^{1} +
b_{3} x^{2} + b_{4} x^{3} + b_{5} x^{4} + \cdots
$$
Moreover, notice that
$b_{3} x^{2} + b_{4} x^{3} + b_{5} x^{4} + \cdots$
is just a linear transformation of
$y_{1} = P_{0} a_{0} x^{2} + P_{1} a_{1} x^{3} + P_{2} a_{2} x^{4} + \cdots$,
and hence must be excluded from being a distinct solution.
The second solution now reduces to a polynomial

$$
y_{2} = b_{0} x^{-1} + b_{1} + b_{2} x^{1}
$$
Differentiating $y_{2}$ with respect to $x$,

$$
y_{2}^{\prime}= -b_{0} x^{-2} + b_{2},
\quad
y_{2}^{\prime \prime} = 2b_{0} x^{-3}
$$
and substituting onto (4.0) yields

$$
-\left(b_{0} + 2b_{2}\right) x + b_{1} x^{2} + 3b_{2} x^{3} - 2b_{1} = 0
$$
whence we derive the same information earlier presented in (4.12), namely
$b_{1} = 0$ and $b_{2} = -\frac{1}{2} b_{0}$.
We also know from the $x^{3}$ term that $b_{2} = 0$, and thus $b_{0} = 0$.
The second solution, after all the analyses, turns out to be trivial:

$$
y_{2} = 0
$$ (4.14)
Therefore, the basis of solutions to (4.0) consists of
a non-trivial Frobenius series $y_{1}$
and a trivial $y_{2} = 0$:

$$
y = y_{1} + y_{2} =
\sum_{k=0}^{\infty} P \left(k\right) a_{0} x^{k+2},
\quad
P \left(k\right) = \left(-1\right)^{k} \prod_{j=0}^{k-1} \frac{2j + 5}{j^{2} + 7j + 10}
$$ (4.15)
where $a_{0}$ is a constant.
