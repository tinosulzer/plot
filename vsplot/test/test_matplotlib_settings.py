import vsplot


def test_get_rcParams():
    rcparams = vsplot.matplotlib_settings.get_rcParams()
    assert isinstance(rcparams, dict)
