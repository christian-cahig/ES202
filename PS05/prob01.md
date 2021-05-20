# Answers to Problem Set V

*Prepared by* Christian Y. Cahig

## Problem No. 1

Find the power series solution (in $x$) of the following ODE:

$$
y^{\prime \prime} + 2 x y^{\prime} + y = 0
$$ (1.0)

We assume that the solution $y$ is a power series solution:

$$
y = \sum_{m=0}^{\infty} a_{m} x^{m}
$$ (1.1)
where the $a_{n}$ terms are constant coefficients.
Differentiating $y$ with respect to $x$,

$$
y^{\prime} = \sum_{m=1}^{\infty} m a_{m} x^{m-1}
\\
y^{\prime \prime} = \sum_{m=2}^{\infty} m \left(m - 1\right) a_{m} x^{m-2}
$$ (1.2)
Substituting (1.2) onto (1.0),

$$
\sum_{m=2}^{\infty} m \left(m - 1\right) a_{m} x^{m-2}
+
2 \sum_{m=1}^{\infty} m a_{m} x^{m}
+
\sum_{m=0}^{\infty} a_{m} x^{m}
= 0
$$
The first series can be re-written
in terms of $x^{m}$, *i.e.*,

$$
\sum_{m=2}^{\infty} m \left(m - 1\right) a_{m} x^{m-2}
=
\sum_{m=0}^{\infty} \left(m + 2\right) \left(m + 1\right) a_{m+2} x^{m}
$$
Moreover, notice that the index of second series in (1.3) can start at $m = 0$:

$$
\sum_{m=1}^{\infty} m a_{m} x^{m}
=
0 \cdot a_{0} x^{0} + 1 \cdot a_{1} x^{1} + 2 \cdot a_{2} x^{2} + \cdots
=
\sum_{m=0}^{\infty} m a_{m} x^{m}
$$
The series equivalent of the given ODE can now be expressed
in terms of $x^{m}$ and with indices starting at 0:

$$
\sum_{m=0}^{\infty}
\left[\left(m + 2\right) \left(m + 1\right) a_{m+2} + \left(2m + 1\right) a_{m}\right]
x^{m} =0
$$ (1.3)
The homogeneity of the given ODE means that the corresponding coefficient
of $x^{m}$ in (1.3) is zero, that is,

$$
a_{m+2} = -
\frac{2m + 1}{\left(m + 1\right) \left(m + 2\right)}
a_{m},
\quad m = 0,1,2,\ldots
$$ (1.4a)
Note that $a_{0}$ and $a_{1}$ cannot be determined from the recurrence relation alone,
and hence in the present treatment will be as arbitrary constants
derived from additional information (*e.g.*, initial conditions).
Moreover, the recurrence relation can be "split" into odd and even terms:

$$
a_{2k} = \left(-1\right)^{k} a_{0}
\prod_{j=0}^{k-1} \frac{4j + 1}{\left(2j + 1\right) \left(2j + 2\right)},
\quad k = 1,2,3,\ldots
$$ (1.4b)
$$
a_{2k+1} = \left(-1\right)^{k} a_{1}
\prod_{j=0}^{k-1} \frac{4j + 3}{\left(2j + 2\right) \left(2j + 3\right)},
\quad k = 1,2,3,\ldots
$$ (1.4c)
Therefore, we can write the series solution to (1.0) as

$$
y =
a_{0} \left[
    1 + \sum_{k=1}^{\infty} \left(-1\right)^{k}
    \prod_{j=0}^{k-1} \frac{4j + 1}{\left(2j + 1\right) \left(2j + 2\right)} x^{2k}
\right]
+
a_{1} \left[
    x + \sum_{k=1}^{\infty} \left(-1\right)^{k}
    \prod_{j=0}^{k-1} \frac{4j + 3}{\left(2j + 2\right) \left(2j + 3\right)} x^{2k+1}
\right]
$$ (1.5)
where $a_{0}$ and $a_{1}$ are constants.
