# Euler - LaTex Derivation Renderer

<p align="center">
    <image alt="Euler" src="./assets/images.jpeg">
</P>

<p align="center">
    <image alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <image alt="Python" src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white"/>

</p>

## An animation toolkit built on top of Manim

Please note that because euler is built on top of manim, please make sure you have a proper manim installation

Euler is a tool for rendering latex equations from a file line by line into a beautiful Manim animations

```latex
x^2 + y^2 = r^2 |
\frac{x^2}{r^2} + \frac{y^2}{r^2} = 1 | Divide by $r^2$
\left( \frac{x}{r} \right) ^2 + \left( \frac{y}{r} \right) ^2   = 1 | $\frac{x}{r} = \cos(\theta)$ and $\frac{y}{r} = \sin(\theta)$
\left( \cos\theta ) ^2 + \left( \sin\theta \right) ^2   = 1 |
\cos^2\theta + \sin^2\theta = 1 | 
```

![Rendered Scene](/assets/EquationScene(1).gif)

The topmost equation will be rendered and then transformed into the succeding lines.

Current use cases are mostly for rendering equation derivations, more features are coming soon (hopefully)

### Todos
- [x] Basic proof of concept
- [ ] A cli app for rendering
- [ ] More advanced positioning systems
- [ ] Publish to pypi