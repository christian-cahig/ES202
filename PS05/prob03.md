# Answers to Problem Set V

*Prepared by* Christian Y. Cahig

## Problem No. 3

Find a basis of solutions for the following ODE.
Try to identify the series as expansions of known functions.

$$
2 x y^{\prime \prime} + \left(3 - 4x\right) y^{\prime} + \left(2x - 3\right) y = 0
$$ (3.0)

The given ODE can be rewritten as

$$
\left(x - \alpha\right)^{2} A\left(x\right) y^{\prime \prime}
+
\left(x - \alpha\right) B\left(x\right) y^{\prime}
+
C\left(x\right) y = 0,
\quad \alpha = 0,\ A\left(x\right) = \frac{2}{x},\ 
B\left(x\right) = \frac{3-4x}{x},\ C\left(x\right) = 2x-3
$$
$x = \alpha = 0$ is a regular singular point of (3.0).
The indicial equation is

$$
r^{2} + \left[
    \frac{B\left(\alpha\right)}{A\left(\alpha\right)} - 1
\right] r
+ \frac{C\left(\alpha\right)}{A\left(\alpha\right)}
= 0 \quad \Longrightarrow \quad
r^{2} + \frac{1}{2}r = 0
$$ (3.1)
whose roots are $r_{1} = 0$ and $r_{2} = -\frac{1}{2}$.
Since $r_{1} - r_{2} = \frac{1}{2} \notin \mathbb{Z}^{+}$,
we look for two solutions $y_{1}$ and $y_{2}$ of the forms:

$$
y_{1} = x^{r_{1}} \sum_{k=0}^{\infty} a_{k} x^{k}
= \sum_{k=0}^{\infty} a_{k} x^{k}
$$ (3.2a)
$$
y_{2} = x^{r_{2}} \sum_{k=0}^{\infty} b_{k} x^{k}
= x^{-\frac{1}{2}} \sum_{k=0}^{\infty} b_{k} x^{k}
$$ (3.2b)
where $a_{k}$ and $b_{k}$ are constants.

Due to the nature of the roots of (3.1),
$y_{1}$ and $y_{2}$ can be represented by a generic series

$$
y = x^{r} \sum_{k=0}^{\infty} a_{k} x^{k} = \sum_{k=0}^{\infty} a_{k} x^{k+r}
$$ (3.3)
Differentiating with respect to $x$,

$$
y^{\prime} = \sum_{k=0}^{\infty}
\left(k+r\right) a_{k} x^{k+r-1},
\quad
y^{\prime \prime} = \sum_{k=0}^{\infty}
\left(k+r-1\right) \left(k+r\right) a_{k} x^{k+r-2}
$$ (3.4)
Substituting (3.3) and (3.4) onto (3.0) and combining like terms,

$$
\sum_{k=0}^{\infty} \left(2k+2r+1\right) \left(k+r\right) a_{k} x^{k+r-1}
- \sum_{k=0}^{\infty} \left[
    4 \left(k+r\right) + 3
\right] a_{k} x^{k+r}
+ \sum_{k=0}^{\infty} 2 a_{k} x^{k+r+1}
= 0
$$ (3.5a)
Writing down the terms uncommon in all three series,

$$
\left(2r+1\right) ra_{0} x^{r-1} + \left(2r+3\right) \left(r+1\right) a_{1} x^{r}
+ \sum_{k=2}^{\infty} \left(2k+2r+1\right) \left(k+r\right) a_{k} x^{k+r-1}
- \left(4r+3\right) a_{0} x^{r}
- \sum_{k=1}^{\infty} \left[
    4 \left(k+r\right) + 3
\right] a_{k} x^{k+r}
+ \sum_{k=0}^{\infty} 2 a_{k} x^{k+r+1}
= 0
$$ (3.5b)
We can rewrite the three series to be of similar form:

$$
\sum_{k=2}^{\infty} \left(2k+2r+1\right) \left(k+r\right) a_{k} x^{k+r-1}
=
\sum_{n=1}^{\infty} \left[2 \left(n+1\right) + 2r + 1\right]
\left(n+r+1\right) a_{n+1} x^{n+r}
$$
$$
\sum_{k=1}^{\infty} \left[4 \left(k+r\right) + 3\right] a_{k} x^{k+r}
=
\sum_{n=1}^{\infty} \left[4 \left(n+r\right) +3\right] a_{n} x^{n+r}
$$
$$
\sum_{k=0}^{\infty} 2 a_{k} x^{k+r+1}
=
\sum_{n=1}^{\infty} 2 a_{n-1} x^{n+r}
$$
so that the ODE becomes
$$
\left(2r+1\right) ra_{0} x^{r-1} +
\left[
    \left(2r+3\right) \left(r+1\right) a_{1} - \left(4r+3\right) a_{0}
\right] x^{r} +
\sum_{n=1}^{\infty} \left\{
    \left[2\left(n+r\right) + 3\right] \left(n+r+1\right) a_{n+1} -
    \left[4\left(n+r\right) + 3\right] a_{n} +
    2 a_{n-1}
\right\} x^{n+r} = 0
$$ (3.5c)
Owing to homogeneity, the coefficient of any power of $x$ equals zero:

$$
\left(2r+1\right) ra_{0} = 0
$$ (3.6a)
$$
\left(2r+3\right) \left(r+1\right) a_{1} - \left(4r+3\right) a_{0} = 0
\quad \Longrightarrow \quad
a_{1} = \frac{4r+3}{\left(2r+3\right) \left(r+1\right)} a_{0}
$$ (3.6b)
$$
\left[2\left(n+r\right) + 3\right] \left(n+r+1\right) a_{n+1} -
\left[4\left(n+r\right) + 3\right] a_{n} +
2 a_{n-1} = 0
\quad \Longrightarrow \quad
a_{n+1} = \frac{
    \left[4\left(n+r\right) + 3\right] a_{n} - 2 a_{n-1}
}{\left[2\left(n+r\right) + 3\right] \left(n+r+1\right)},
\quad n = 1,2,3,\ldots
$$ (3.6c)
Note that the expression multiplied by $a_{0}$ in (3.6a) is the indicial equation,
*i.e.*, (3.6a) is an identity and $a_{0}$ can be an arbitrary constant.
The recurrence relations (3.6b)-(3.6c) hold for both $r_{1}$ and $r_{2}$.

With $r=r_{1}=0$,

$$
a_{1} = a_{0}; \quad \quad
a_{n+1} = \frac{
    \left[4\left(n+r\right) + 3\right] a_{n} - 2a_{n-1}
}{\left[2\left(n+r\right) + 3\right] \left(n+r+1\right)},
\quad n = 1,2,3,\ldots
$$ (3.7)
where $a_{0}$ is a constant.
Evaluating for a few $n > 1$,

$$
a_{2} = \frac{a_{0}}{2},\quad
a_{3} = \frac{a_{0}}{6},\quad
a_{4} = \frac{a_{0}}{24},\quad
a_{5} = \frac{a_{0}}{120},\quad
a_{6} = \frac{a_{0}}{720}
$$
Hence, the first solution is

$$
y_{1} = \sum_{k=0}^{\infty} a_{k} x^{k}
= a_{0} + a_{0} x + \frac{a_{0}}{2} x^{2} + \frac{a_{0}}{6} x^{3} +
\frac{a_{0}}{24} x^{4} + \frac{a_{0}}{120} x^{5} +
\frac{a_{0}}{720} x^{6} + \cdots
= \sum_{k=0}^{\infty} \frac{a_{0}}{k!} x^{k}
= a_{0} \exp \left(x\right)
$$ (3.8)
where $a_{0}$ is a constant.

With $r=r_{2}=-\frac{1}{2}$, and a harmless substitution of $a$ with $b$,

$$
b_{1} = b_{0}; \quad \quad
b_{n+1} = \frac{
    \left(4n+1\right) b_{n} - 2b_{n-1}
}{\left(n+1\right)\left(2n+1\right)},
\quad n = 1,2,3,\ldots
$$ (3.9)
where $b_{0}$ is a constant. Evaluating for a few $n>1$,

$$
b_{2} = \frac{b_{0}}{2},\quad
b_{3} = \frac{b_{0}}{6},\quad
b_{4} = \frac{b_{0}}{24},\quad
b_{5} = \frac{b_{0}}{120},\quad
b_{6} = \frac{b_{0}}{720}
$$
Hence, the second solution is

$$
y_{2} = x^{-\frac{1}{2}} \sum_{k=0}^{\infty} b_{k} x^{k}
= x^{-\frac{1}{2}} \left[
    b_{0} + b_{0} x + \frac{b_{0}}{2} x^{2} + \frac{b_{0}}{6} x^{3} +
    \frac{b_{0}}{24} x^{4} + \frac{b_{0}}{120} x^{5} +
    \frac{b_{0}}{720} x^{6} + \cdots
\right]
= x^{-\frac{1}{2}} \sum_{k=0}^{\infty} \frac{b_{0}}{k!} x^{k}
= b_{0} x^{-\frac{1}{2}} \exp \left(x\right)
$$ (3.10)
where $b_{0}$ is a constant.

Therefore, since $y_{1}$ and $y_{2}$ are linearly independent,
they constitute a basis of solutions for (3.0).
