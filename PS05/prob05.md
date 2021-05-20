# Answers to Problem Set V

*Prepared by* Christian Y. Cahig

## Problem No. 5

Find the general solution
(in terms of $J_{\textsf{v}}$ and $Y_{\textsf{v}}$)
to the following ODE
by using $12 \sqrt{x} = z$:

$$
x y^{\prime \prime} + y^{\prime} + 36y = 0
$$ (5.0)

For some quantities $a$ and $b$,
let $a_{b}$ and $a_{bb}$ denote the first and second derivatives of $a$ with respect to $b$,
respectively, assuming that such derivatives exist.
From the given substitution scheme:

$$
z = 12 \sqrt{x}
\quad \Longrightarrow \quad
z_{x} = 6 x^{-\frac{1}{2}}
\quad \Longrightarrow \quad
z_{xx} = -3 x^{-\frac{3}{2}}
$$ (5.1)
Assume that $y$ is a composition of $z$ and $x$, so that by the chain rule,

$$
y^{\prime} = y_{x} = y_{z} z_{x} = 6 x^{-\frac{1}{2}} y_{z}
\quad \Longrightarrow \quad
y^{\prime \prime} = y_{z} z_{xx} + \left(z_{x}\right)^{2} y_{zz}
= -3x^{\frac{3}{2}} y_{z} + 6x^{-1} y_{zz}
$$ (5.2)
Substituting (5.2) to (5.0),

$$
x \left[-3x^{\frac{3}{2}} y_{z} + 6x^{-1} y_{zz}\right]
+ 6x^{-\frac{1}{2}} y_{z} + 36y = 0
\quad \Longrightarrow \quad
12x^{\frac{1}{2}} y_{zz} + y_{z} + 12x^{\frac{1}{2}} y = 0
$$
and invoking the substitution scheme,

$$
z y_{zz} + y_{z} + zy = 0
\quad \Longrightarrow \quad
z^{2} y_{zz} + z y_{z} + \left(z^{2} - \nu^{2}\right) y = 0,
\quad \nu = 0
$$ (5.3)

In other words, the transformation $z = 12\sqrt{x}$
allows the reformulation of an Euler-Cauchy ODE (5.0)
into a Bessel equation of order $\nu = 0$.
This eventually leads to two solutions
$J_{0} \left(z\right)$ and $Y_{0} \left(z\right)$.
The first solution is a Bessel function of the first kind of order zero:

$$
J_{0} \left(z\right) = \sum_{k=0}^{\infty}
\frac{\left(-1\right)^{k}}{
    2^{2k} \left[\Gamma \left(k+1\right)\right]^{2}
} z^{2k}
= \sum_{k=0}^{\infty}
\frac{\left(-1\right)^{k}}{
    2^{2k} \left(k!\right)^{2}
} z^{2k}
$$ (5.4a)
The second solution is a Bessel function of the second kind of order zero:

$$
Y_{0} \left(z\right) = \frac{2}{\pi}
\left[
    \left(\ln \frac{z}{2} + \gamma \right) J_{0} \left(z\right) +
    \sum_{k=0}^{\infty} \frac{
        \left(-1\right)^{k} H \left(k+1\right)
    }{
        2^{2k} \left(k!\right)^{2}
    }z^{2k}
\right]
$$ (5.4b)
where $\gamma$ is the Euler-Mascheroni constant
and $H \left(k\right)$ is the harmonic series:

$$
\gamma = \lim_{n \rightarrow +\infty}
\left(-\ln n + \sum_{k=1}^{n} \frac{1}{k} \right)
\approx 0.57722, \quad
H \left(k\right) = 1 + \frac{1}{2} + \frac{1}{3}
+ \cdots + \frac{1}{k}
$$ (5.4c)
The general solution to the Bessel equation (5.3) is

$$
y \left(z\right) = C_{J} J_{0} \left(z\right) + C_{Y} Y_{0} \left(z\right)
$$
where $C_{J}$ and $C_{Y}$ are constants.
Expressing back in terms of $x$ by substituting $z = 12\sqrt{x}$,
the general solution to the given Euler-Cauchy ODE (5.0) is

$$
J_{0} \left(x\right) = \sum_{k=0}^{\infty}
\frac{\left(-144\right)^{k}}{
    2^{2k} \left(k!\right)^{2}
} x^{k}
$$ (5.5a)
$$
Y_{0} \left(x\right) = \frac{2}{\pi}
\left[
    \left(\ln \frac{z}{2} + \gamma \right) J_{0} \left(x\right) +
    \sum_{k=0}^{\infty} \frac{
        \left(-144\right)^{k} H \left(k+1\right)
    }{
        2^{2k} \left(k!\right)^{2}
    }x^{k}
\right]
$$ (5.5b)
$$
y \left(x\right) = C_{J} J_{0} \left(x\right) + C_{Y} Y_{0} \left(x\right)
$$ (5.5c)
where $C_{J}$ and $C_{Y}$ are constants.
