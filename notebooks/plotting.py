import numpy
from matplotlib import colors
import pymc3


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


def plot_density(*, ax, x, samples, percentiles=(5, 95), percentile_kwargs=None, **kwargs):
    assert samples.ndim == 2

    # Step-function mode draws horizontal density bands inbetween the x coordinates
    step_mode = samples.shape[1] == x.shape[0] - 1
    fill_kwargs = {}
    if step_mode:
        samples = numpy.hstack([
            samples,
            samples[:, -1][:, None]
        ])
        fill_kwargs["step"] = "post"

    # Plot the density band
    pymc3.gp.util.plot_gp_dist(
        ax=ax,
        x=x,
        samples=samples,
        fill_kwargs=fill_kwargs,
        **kwargs
    )

    # Add percentiles for orientation
    pkwargs = dict(
        linestyle="--",
        color="black",
    )
    pkwargs.update(percentile_kwargs or {})
    for p in percentiles:
        values = numpy.percentile(samples, p, axis=0)
        if step_mode:
            ax.stairs(values[:-1], x, baseline=None, **pkwargs)
        else:
            ax.plot(x, values, **pkwargs)
        pass

    return


