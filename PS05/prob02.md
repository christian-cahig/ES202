# Answers to Problem Set V

*Prepared by* Christian Y. Cahig

## Problem No. 2

Find the power series solution (in $x$) of the following ODE:

$$
y^{\prime \prime} - 4 x y^{\prime} + \left(4 x^{2} - 2\right) y = 0
$$ (2.0)

We assume that the solution $y$ is a power series solution:

$$
y = \sum_{m=0}^{\infty} a_{m} x^{m}
$$ (2.1)
where the $a_{n}$ terms are constant coefficients.
Differentiating $y$ with respect to $x$,

$$
y^{\prime} = \sum_{m=1}^{\infty} m a_{m} x^{m-1}
\\
y^{\prime \prime} = \sum_{m=2}^{\infty} m \left(m - 1\right) a_{m} x^{m-2}
$$ (2.2)
Substituting (2.2) onto (2.0),

$$
\sum_{m=2}^{\infty} m \left(m - 1\right) a_{m} x^{m-2}
- 4 \sum_{m=1}^{\infty} m a_{m} x^{m}
+ 4 \sum_{m=0}^{\infty} m a_{m} x^{m+2}
- 2 \sum_{m=0}^{\infty} m a_{m} x^{m}
= 0
$$ (2.1a)

Expressing all series terms (2.1a) in $x^{m}$,

$$
\sum_{m=0}^{\infty} \left(m + 2\right) \left(m + 1\right) a_{m+2} x^{m}
- 4 \sum_{m=0}^{\infty} m a_{m} x^{m}
+ 4 \sum_{m=2}^{\infty} a_{m-2} x^{m}
- 2 \sum_{m=0}^{\infty} a_{m} x^{m}
= 0
$$ (2.1b)
Note that

$$
\sum_{m=0}^{\infty} \left(m + 2\right) \left(m + 1\right) a_{m+2} x^{m}
= 2 a_{2} + 6 a_{3} x
+ \sum_{m=2}^{\infty} \left(m + 2\right) \left(m + 1\right) a_{m+2} x^{m}
$$

$$
\sum_{m=0}^{\infty} m a_{m} x^{m}
= a_{1} x + \sum_{m=2}^{\infty} m a_{m} x^{m}
$$

$$
\sum_{m=0}^{\infty} a_{m} x^{m}
= a_{0} + a_{1} x + \sum_{m=2}^{\infty} a_{m} x^{m}
$$
Hence, we can rewrite the series terms in (2.1b) to have indices starting at $m=2$:

$$
2a_{2} + 6a_{3}x - 6a_{1}x - 2a_{0}
+ \sum_{m=2}^{\infty}
\left[ \left(m+2\right)\left(m+1\right) a_{m+2} - \left(4m+2\right) a_{m} + 4 a_{m-2} \right]
x^{m} = 0
$$ (2.1c)

Since (2.0) is homogenous, it follows from (2.1c) that

$$
2a_{2} - 2a_{0} = 0 \Longrightarrow a_{2} = a_{0}
$$ (2.2a)
$$
6a_{3} - 6a_{1} = 0 \Longrightarrow a_{3} = a_{1}
$$ (2.2b)
$$
\left(m+2\right)\left(m+1\right) a_{m+2} - \left(4m+2\right) a_{m} + 4 a_{m-2} = 0
\Longrightarrow
a_{m+2} = \frac{\left(4m+2\right) a_{m} - 4 a_{m-2}}{\left(m+1\right)\left(m+2\right)}
$$ (2.2c)
Now, with $m=2,3,4,5,6,7,9$,

$$
a_{4} = \frac{a_{0}}{2},\ 
a_{6} = \frac{a_{0}}{6},\ 
a_{8} = \frac{a_{0}}{24};
\quad
a_{5} = \frac{a_{1}}{2},\ 
a_{7} = \frac{a_{1}}{6},\ 
a_{9} = \frac{a_{1}}{24}
$$
This suggests two patterns for when even and odd $m$'s:

$$
a_{0},\ a_{2} = a_{0},\ a_{4} = \frac{a_{0}}{2},\ a_{6} = \frac{a_{0}}{6},\ 
a_{8} = \frac{a_{0}}{24},\ 
\cdots\ \Longrightarrow\ 
a_{2k} = \frac{a_{0}}{k!},
\quad k=0,1,2,\ldots
\ \ \ \ \ \ \ 
$$

$$
a_{1},\ a_{3} = a_{1},\  a_{5} = \frac{a_{1}}{2},\  a_{7} = \frac{a_{1}}{6},\ 
a_{9} = \frac{a_{1}}{24},\ 
\cdots\ \Longrightarrow\ 
a_{2k+1} = \frac{a_{1}}{k!},
\quad k=0,1,2,\ldots
$$
Notice that any $a_{m}$ is dependent on either $a_{0}$ or $a_{1}$,
but $a_{0}$ and $a_{1}$ cannot be determined solely from the recurrence relations.
We can treat $a_{0}$ and $a_{1}$ as yet unknown constants
whereupon the coeffiecents of two different power series are based.
Therefore, the power series solution to (2.0) is

$$
y =
\sum_{m=0}^{\infty} \frac{a_{0}}{m!} x^{2m}
+
\sum_{m=0}^{\infty} \frac{a_{1}}{m!} x^{2m+1}
= a_{0} \exp \left(x^{2}\right) + a_{1} x \exp \left(x^{2}\right)
$$ (2.3)
where $a_{0}$ and $a_{1}$ are constants.
