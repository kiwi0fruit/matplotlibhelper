# Matplotlib Helper

Matplotlib Helper is my custom helper to tune Matplotlib experience for [Pandoctools/Knitty](https://github.com/kiwi0fruit/pandoctools). I tuned fonts (that are shipped with this python package, see default fonts in default keyword arguments of [`ready()`](https://github.com/kiwi0fruit/matplotlibhelper/blob/master/matplotlibhelper/matplotlib_helper.py)), made some tweaks to use it with [SugarTeX](https://github.com/kiwi0fruit/sugartex), some tweaks to automatically use interactive Qt5 plots in Atom/Hydrogen or non-jupyter python. It can export plots to SVG or PNG.


# Contents

* [Matplotlib Helper](#matplotlib-helper)
* [Contents](#contents)
* [Install](#install)
* [Usage example](#usage-example)
* [Hints](#hints)


# Install

Via conda (should be `"pip>=10.0.1"`):

```
conda install numpy pandas ipython matplotlib pandoc pyyaml future shutilwhich
pip install panflute sugartex matplotlibhelper
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

# this code in knitty would be parsed by pandoc:
Markdown(f'![My beautiful figure]({mh.img(plt)}){{#fig:1}}')
```

Qt backend gives [interactive plots in Atom/Hydrogen](https://nteract.gitbooks.io/hydrogen/docs/Usage/Examples.html#interactive-plots-using-matplotlib).


## Hints

1. [MJ fonts](https://github.com/kiwi0fruit/open-fonts/tree/master/Fonts/MJ/oft).
2. Delete `fontList.cache`, `fontList.py3k.cache` or `fontList.json` from `%USERPROFILE%\.matplotlib` folder after installing a new font.
3. If font becomes bold without a reason try ([source](https://github.com/matplotlib/matplotlib/issues/5574)):

```py
from matplotlib import font_manager
if 'roman' in font_manager.weight_dict:
    del font_manager.weight_dict['roman']
    # noinspection PyProtectedMember
    font_manager._rebuild()
```

4. Install [Computer Modern Unicode](https://sourceforge.net/projects/cm-unicode/) for bold-italic unicode support: `"mathtext.sf": "CMU Serif:bold:italic"`. Sans-serif command `\mathsf{}` is reassigned because sans-serif font is rarely used in serif docs.
