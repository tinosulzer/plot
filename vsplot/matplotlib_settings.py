fs = 12


def get_rcParams():
    from cycler import cycler

    rcParams = {}

    rcParams["axes.prop_cycle"] = cycler(
        "color",
        [
            "#1f77b4",
            "#ff7f0e",
            "k",
            "#d62728",
            "#2ca02c",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        ],
    )

    # Set fonts
    rcParams["text.usetex"] = False
    rcParams["font.size"] = fs
    rcParams["legend.fontsize"] = fs
    rcParams["axes.labelsize"] = fs
    rcParams["axes.titlesize"] = fs
    rcParams["xtick.labelsize"] = fs - 1
    rcParams["ytick.labelsize"] = fs - 1

    # Set x axis
    rcParams["xtick.direction"] = "in"
    rcParams["xtick.major.size"] = 3
    rcParams["xtick.major.width"] = 0.5
    rcParams["xtick.minor.size"] = 1.5
    rcParams["xtick.minor.width"] = 0.5
    # rcParams["xtick.minor.visible"] = True
    rcParams["xtick.top"] = True

    # Set y axis
    rcParams["ytick.direction"] = "in"
    rcParams["ytick.major.size"] = 3
    rcParams["ytick.major.width"] = 0.5
    rcParams["ytick.minor.size"] = 1.5
    rcParams["ytick.minor.width"] = 0.5
    # rcParams["ytick.minor.visible"] = True
    rcParams["ytick.right"] = True

    # Set line widths
    rcParams["axes.linewidth"] = 0.5
    rcParams["grid.linewidth"] = 0.5
    rcParams["lines.linewidth"] = 1.8
    rcParams["lines.markersize"] = 5

    # Remove legend frame
    rcParams["legend.frameon"] = False

    # Always save as 'tight'
    rcParams["savefig.bbox"] = "tight"
    rcParams["savefig.pad_inches"] = 0.05

    # Use serif fonts
    # font.serif : Times
    # rcParams["font.family"] = "serif"
    # rcParams["mathtext.fontset"] = "dejavuserif"

    return rcParams