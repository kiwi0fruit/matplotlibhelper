# Matplotlib Helper

Matplotlib Helper is my custom helper to tune Matplotlib experience for [Pandoctools/Knitty](https://github.com/kiwi0fruit/pandoctools) (but it can be used by itself). I tuned fonts (that are shipped with this python package), please see default fonts and other options in default keyword arguments of [`ready()`](https://github.com/kiwi0fruit/matplotlibhelper/blob/master/matplotlibhelper/matplotlib_helper.py)). I made some tweaks to use it with [SugarTeX](https://github.com/kiwi0fruit/sugartex), some tweaks to automatically use interactive Qt5 plots in Atom/Hydrogen or non-jupyter Python. It can also export plots to SVG or PNG.

Works in Jupyter as well.


# Contents

* [Matplotlib Helper](#matplotlib-helper)
* [Contents](#contents)
* [Install](#install)
* [Usage example](#usage-example)
* [Hints](#hints)


# Install

Via conda:

```
conda install -c defaults -c conda-forge matplotlibhelper
```

Via pip:

```
pip install matplotlibhelper
```


Additionally you may need to install to use in Jupyter Lab:

```
conda install jupyterlab jupyterlab_server tk nodejs
pip install ipympl
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib
```
Instead of `pip install ipympl` you can also try:
```
conda update --all
conda install -c defaults -c conda-forge ipympl
conda update --all
```


## Usage example

Usage example that works both in Atom+Hydrogen and in Pandoctools+Knitty:

```py
from IPython.display import Markdown
import matplotlibhelper as mh
mh.ready(font_size=14)  # should be run before import matplotlib.pyplot
import matplotlib.pyplot as plt


plt.figure(figsize=mh.figsize(w=6))  # height is automatic via the golden ration
plt.plot([1, 2, 3, 4])
plt.ylabel(mh.stex('ˎ∇ ⋅ [ ⃗E]ˎ, V/m'))  # using SugarTeX

# this code in Knitty would be parsed by Pandoc,
# in Atom/Hydrogen or Jupyter it would be displayed:
Markdown(f'![My beautiful figure]({mh.img(plt)}){{#fig:1}}')
```

Qt backend gives [interactive plots in Atom/Hydrogen](https://nteract.gitbooks.io/hydrogen/docs/Usage/Examples.html#interactive-plots-using-matplotlib).


## Hints

1. Delete `fontList.cache`, `fontList.py3k.cache` or `fontList.json` from `%USERPROFILE%\.matplotlib` folder after installing a new font.
2. If font becomes bold without a reason try ([source](https://github.com/matplotlib/matplotlib/issues/5574)):

```py
from matplotlib import font_manager
if 'roman' in font_manager.weight_dict:
    del font_manager.weight_dict['roman']
    # noinspection PyProtectedMember
    font_manager._rebuild()
```

3. Install [Computer Modern Unicode](https://sourceforge.net/projects/cm-unicode/) for bold-italic unicode support: `"mathtext.sf": "CMU Serif:bold:italic"`. Sans-serif command `\mathsf{}` is reassigned because sans-serif font is rarely used in serif docs.
