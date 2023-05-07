import trusspy as tp


def test_nta_a_python():
    """Ex.NTA(A)
    * 3D truss system
    * linear elastic
    """

    M = tp.Model(logfile=True)

    with M.Nodes as MN:
        MN.add_node(1, coord=(2.5, 0, 0))
        MN.add_node(2, coord=(-1.25, 1.25, 0))
        MN.add_node(3, coord=(1, 2, 0))
        MN.add_node(4, coord=(-0.5, 1.5, 1.5))
        MN.add_node(5, coord=(-2.5, 4.5, 2.5))

    with M.Elements as ME:
        ME.add_element(1, conn=(1, 4), gprop=[0.75])
        ME.add_element(2, conn=(2, 4), gprop=[1])
        ME.add_element(3, conn=(3, 4), gprop=[0.5])
        ME.add_element(4, conn=(3, 5), gprop=[0.75])
        ME.add_element(5, conn=(2, 5), gprop=[1])
        ME.add_element(6, conn=(4, 5), gprop=[1])

        ME.assign_etype("all", 1)
        ME.assign_mtype("all", 1)
        ME.assign_material("all", [1.0])

    with M.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (0, 0, 0))
        MB.add_bound_U(3, (0, 0, 0))
        MB.add_bound_U(5, (1, 0, 1))

    with M.ExtForces as MF:
        MF.add_force(4, (1, 1, -1))
        MF.add_force(5, (-2, 0, -2))

    M.Settings.dlpf = 0.005
    M.Settings.du = 0.05

    M.Settings.incs = 163

    M.Settings.stepcontrol = True
    M.Settings.maxfac = 4

    M.Settings.ftol = 8
    M.Settings.xtol = 8
    M.Settings.nfev = 8

    M.Settings.dxtol = 1.25

    ## lim_scale < 1: fixed value for all axis (good for videos)
    ## lim_scale > 1: scale factor for min/max values
    ## forces:        1 N = "force_scale" L

    ## Create Model, Run, show Results
    M.build()
    M.run()

    ## model plot: undeformed and deformed configuration for last increment
    fig, ax = M.plot_model(
        view="3d",
        contour="force",
        lim_scale=(-3, 2, 0, 5, -1, 4),
        force_scale=2.0,
        inc=0,
    )
    fig.savefig("model_undeformed_inc0_3d.pdf")
    fig.savefig("model_undeformed_inc0_3d.png")

    fig, ax = M.plot_model(
        view="xz",
        contour="force",
        lim_scale=1.4,
        force_scale=2.0,
        inc=0,
    )
    fig.savefig("model_undeformed_inc0_xz.pdf")
    fig.savefig("model_undeformed_inc0_xz.png")

    fig, ax = M.plot_model(
        view="yz",
        contour="force",
        lim_scale=1.4,
        force_scale=2.0,
        inc=0,
    )
    fig.savefig("model_undeformed_inc0_yz.pdf")
    fig.savefig("model_undeformed_inc0_yz.png")

    fig, ax = M.plot_model(
        view="xy",
        contour="force",
        lim_scale=1.4,
        force_scale=2.0,
        inc=0,
    )
    fig.savefig("model_undeformed_inc0_xy.pdf")
    fig.savefig("model_undeformed_inc0_xy.png")

    pinc = 40  # 105
    fig, ax = M.plot_model(
        view="xz",
        contour="force",
        # lim_scale=(-4,4,-2,6,-1,5),
        lim_scale=1.3,
        force_scale=500.0,
        inc=pinc,
    )
    fig.savefig("model_contour-force_inc40_xz.pdf")
    fig.savefig("model_contour-force_inc40_xz.png")

    fig, ax = M.plot_model(
        view="yz",
        contour="force",
        # lim_scale=(-4,4,-2,6,-1,5),
        lim_scale=1.3,
        force_scale=500.0,
        inc=pinc,
    )
    fig.savefig("model_contour-force_inc40_yz.pdf")
    fig.savefig("model_contour-force_inc40_yz.png")

    fig, ax = M.plot_model(
        view="xy",
        contour="force",
        # lim_scale=(-4,4,-2,6,-1,5),
        lim_scale=1.3,
        force_scale=500.0,
        inc=pinc,
    )
    fig.savefig("model_contour-force_inc40_xy.pdf")
    fig.savefig("model_contour-force_inc40_xy.png")

    fig, ax = M.plot_model(
        view="3d",
        contour="force",
        lim_scale=(-3, 2, 0, 5, -2, 3),
        # lim_scale=1.2,
        force_scale=500.0,
        inc=pinc,
    )
    fig.savefig("model_contour-force_inc40_3d.pdf")
    fig.savefig("model_contour-force_inc40_3d.png")

    # M.plot_movie(
    #     view="3d",
    #     contour="force",
    #     lim_scale=(-3, 2, 0, 5, -2, 3),  # 3D
    #     # lim_scale=-5, #XZ
    #     # lim_scale=(-4,4,-2,6), #XY
    #     # lim_scale=(-2,6,-2,6), #YZ
    #     cbar_limits=[-0.3, 0.3],
    #     force_scale=50.0,
    #     incs=range(0, M.Settings.incs, 1),
    # )

    ## history plot
    Disp = "Displacement X"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    fig, ax = M.plot_history(nodes=[5, 5], X=Disp, Y="LPF", fig=fig, ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.png")

    Disp = "Displacement Y"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    # fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.png")

    Disp = "Displacement Z"
    fig, ax = M.plot_history(nodes=[4, 4], X=Disp, Y="LPF")
    fig, ax = M.plot_history(nodes=[5, 5], X=Disp, Y="LPF", fig=fig, ax=ax)
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.pdf")
    fig.savefig("history_node45_Disp" + Disp[-1] + "-LPF.png")


if __name__ == "__main__":
    test_nta_a_python()
