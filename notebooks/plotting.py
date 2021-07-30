import numpy
from matplotlib import colors


def transparentify(cmap: colors.Colormap) -> colors.ListedColormap:
    """Creates a transparent->color version from a standard colormap.
    
    Adapted from https://stackoverflow.com/a/37334212/4473230
    
    Testing
    -------
    The following code block can be used to plot a (trasparent) colormap in a way that one
    can check if the transparency actually works. This is not trivial because the background
    is often white already.
    Check the thread under https://github.com/matplotlib/matplotlib/pull/17888#issuecomment-845253158
    for updates about automatic cmap representation in notebooks that could make this snippet obsolete.

    x = numpy.arange(256)
    fig, ax = pyplot.subplots(figsize=(12,1))
    ax.scatter(x, numpy.ones_like(x) - 0.01, s=100, c=[
        cm.Reds(v)
        for v in x
    ])
    ax.scatter(x, numpy.ones_like(x) + 0.01, s=100, c=[
        redsT(v)
        for v in x
    ])
    ax.set_ylim(0.9, 1.1)
    pyplot.show()
    """
    # Get the colormap colors
    cm_new = numpy.array(cmap(numpy.arange(cmap.N)))
    cm_new[:, 3] = numpy.linspace(0, 1, cmap.N)
    return colors.ListedColormap(cm_new)
