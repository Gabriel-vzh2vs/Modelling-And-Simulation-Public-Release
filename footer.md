% This defines the footer of the site, and is not parsed as a regular "page"
% We point to it with the following in `myst.yml`:
% site:
% parts:
% footer: footer.md

% Here we use `grid` to add a basic grid structure to the HTML,
% but the formatting column sizes are defined manually in css/footer.css
% see the `grid-template-columns` line.
:::::{grid} 3 3 5 5
:class: outer-grid col-screen

<!-- Project description -->

::::{div}

# Modelling and Simulation

```{image} https://jupyterbook.org/en/stable/_images/logo-square.svg
:width: 50px
:align: left
```

© 2026, Henning Mortveit and Gabriel Lawrence
::::

<!-- Spacer between project description and links columns -->

::::{div}
::::

<!-- Link columns -->

% This a _second_ grid embedded within the first one, to create nicer
% responsive design experience. This grid will have a single column on narrow screens,
% and fan out into three columns on wide screens. However, it always remains within
% its parent grid column.
::::{grid} 1 1 3 3

:::{div}

- [Homepage](https://gabriel-vzh2vs.github.io/Modelling-And-Simulation-Public-Release/)
- [Index](https://gabriel-vzh2vs.github.io/Modelling-And-Simulation-Public-Release/index-2/)
- [Report Issues or Errors](https://github.com/Gabriel-vzh2vs/Modelling-And-Simulation-Public-Release/issues)
  :::

:::{div}

- This book is a work in progress!
- We welcome contributions via GitHub or Email: GabeL@virginia.edu
  :::

:::{div}

- This is a Jupyter Book Project. Learn more here: [Jupyterbook](https://jupyterbook.org/)
  :::

::::

:::::
