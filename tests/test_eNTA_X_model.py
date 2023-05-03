import trusspy as tp


def test_nta_x(filepath="tests/"):
    """Ex.NTA(X)
    * 3D truss system
    * linear elastic
    """

    M = tp.Model(filepath + "eNTA_X_input.xlsx", logfile=True)

    M.Settings.dlpf = 0.005
    M.Settings.du = 0.05

    M.Settings.incs = 180

    M.Settings.stepcontrol = True
    M.Settings.maxfac = 1

    M.Settings.ftol = 8
    M.Settings.xtol = 8
    M.Settings.nfev = 8

    M.Settings.dxtol = 1.25

    # lim_scale < 1: fixed value for all axis (good for videos)
    # lim_scale > 1: scale factor for min/max values
    # forces:        1 N = "force_scale" L

    # Create Model, Run, show Results
    M.build()
    M.run()

    # model plot: last increment
    fig, ax = M.plot_model(
        view="xz",
        contour="force",
        lim_scale=2,
        force_scale=0.2,
        inc=-1,
    )
    fig.savefig("model_contour-force_inc-last.pdf")

    # M.plot_movie(view='xz',
    #             contour='stretch',
    #             lim_scale=-1.5,
    #             force_scale=10.0,
    #             incs='all')

    # history plot
    Disp = "Displacement X"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    fig, ax = M.plot_history(nodes=[5, 5], X=Disp, Y="LPF", fig=fig, ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")

    Disp = "Displacement Y"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    fig, ax = M.plot_history(nodes=[5, 5], X=Disp, Y="LPF", fig=fig, ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")

    Disp = "Displacement Z"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    fig, ax = M.plot_history(nodes=[5, 5], X=Disp, Y="LPF", fig=fig, ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")


if __name__ == "__main__":
    test_nta_x(filepath="./")
