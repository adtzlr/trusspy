import trusspy as tp


def test_adv_a_python():
    """Ex.ADV(A)
    * 3D truss system
    * linear elastic
    * source: https://www.scielo.br/pdf/tema/v19n1/2179-8451-tema-19-01-161.pdf
    """

    # init Model
    M = tp.Model(logfile=True)

    # add Nodes
    with M.Nodes as MN:
        MN.add_node(1, coord=(-1.697, -1, 0))
        MN.add_node(2, coord=(0.000, -1, 0))
        MN.add_node(3, coord=(1.697, -1, 0))

        MN.add_node(4, coord=(-1.697, 1, 0))
        MN.add_node(5, coord=(0.000, 1, 0))
        MN.add_node(6, coord=(1.697, 1, 0))

        MN.add_node(7, coord=(-1.414, 0, 1))
        MN.add_node(8, coord=(0.000, 0, 1))
        MN.add_node(9, coord=(1.414, 0, 1))

    # add Elements
    with M.Elements as ME:
        ME.add_element(1, conn=(1, 7), gprop=[1.0])
        ME.add_element(2, conn=(4, 7), gprop=[1.0])
        ME.add_element(3, conn=(2, 8), gprop=[1.0])
        ME.add_element(4, conn=(5, 8), gprop=[1.0])
        ME.add_element(5, conn=(3, 9), gprop=[1.0])
        ME.add_element(6, conn=(6, 9), gprop=[1.0])
        ME.add_element(7, conn=(7, 8), gprop=[1.0])
        ME.add_element(8, conn=(8, 9), gprop=[1.0])
        ME.add_element(9, conn=(1, 8), gprop=[1.0])
        ME.add_element(10, conn=(4, 8), gprop=[1.0])
        ME.add_element(11, conn=(3, 8), gprop=[1.0])
        ME.add_element(12, conn=(6, 8), gprop=[1.0])

        ME.assign_material("all", [1.0])

    # add Fixed Constraints
    with M.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (0, 0, 0))
        MB.add_bound_U(3, (0, 0, 0))
        MB.add_bound_U(4, (0, 0, 0))
        MB.add_bound_U(5, (0, 0, 0))
        MB.add_bound_U(6, (0, 0, 0))

    # add External Forces
    with M.ExtForces as MF:
        MF.add_force(7, (0, 0, -1.5))
        MF.add_force(8, (0, 0, -1.0))
        MF.add_force(9, (0, 0, -1.5))

    # set solution parameters
    M.Settings.dlpf = 0.05
    M.Settings.du = 0.05

    # set max. number of Increments (stepcontrol disabled)
    M.Settings.incs = 132
    # M.Settings.stepcontrol = True
    # M.Settings.maxfac = 8

    ## Create Model, Run, show Results
    M.build()
    M.run()

    ## model plot: with external loads
    fig, ax = M.plot_model(
        view="3d",
        contour="force",
        lim_scale=(-3, 3, -3, 3, -2, 3),
        force_scale=2.0,
        inc=0,
    )
    fig.savefig("model_undeformed_inc0_3d.pdf")

    # history plot
    Disp = "Displacement Z"
    fig, ax = M.plot_history(nodes=[7, 7], X=Disp, Y="LPF")
    ax.invert_xaxis()
    fig.savefig("history_node7_Disp" + Disp[-1] + "-LPF.pdf")


if __name__ == "__main__":
    test_adv_a_python()
