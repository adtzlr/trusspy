import trusspy as tp


def test_e103_python():
    "Ex.103-Python: 2 Trusses with 1 DOF, linear elastic"

    M1 = tp.Model(logfile=False)

    with M1.Nodes as MN:
        MN.add_node(1, coord=(0, 0, 0))
        MN.add_node(2, coord=(1, 0, 3))
        MN.add_node(3, coord=(2, 0, 0))

    with M1.Elements as ME:
        ME.add_element(1, conn=(1, 2), gprop=[1])
        ME.add_element(2, conn=(2, 3), gprop=[1])

        E = 1  # elastic modulus
        ME.assign_material("all", [E])

    with M1.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (0, 0, 1))
        MB.add_bound_U(3, (0, 0, 0))

    with M1.ExtForces as MF:
        MF.add_force(2, (0, 0, -1))

    M1.Settings.incs = 150
    M1.Settings.du = 0.01
    M1.Settings.dlpf = 0.01
    M1.Settings.xlimit = (1, 10)
    M1.Settings.dlpf
    M1.Settings.stepcontrol = True
    M1.Settings.maxfac = 10

    # Create Model, Run, show Results
    M1.build()
    M1.run()

    fig, ax = M1.plot_model(inc=0)
    fig.savefig("model1_undeformed.png")
    fig.savefig("model1_undeformed.pdf")

    # model plot: last increment
    fig, ax = M1.plot_model(
        view="xz",
        contour="force",
        force_scale=2,
        inc=20,
    )
    fig.savefig("model1_deformed.png")
    fig.savefig("model1_deformed.pdf")

    # history plot
    fig1, ax1 = M1.plot_history(nodes=[2, 2], X="Displacement X", Y="Displacement Z")
    fig2, ax2 = M1.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF")

    # re-run with imperfection
    M2 = tp.Model(logfile=False)

    with M2.Nodes as MN:
        MN.add_node(1, coord=(0, 0, 0))
        MN.add_node(2, coord=(1.1, 0, 3))
        MN.add_node(3, coord=(2, 0, 0))

    with M2.Elements as ME:
        ME.add_element(1, conn=(1, 2), gprop=[1])
        ME.add_element(2, conn=(2, 3), gprop=[1])

        E = 1  # elastic modulus
        ME.assign_material("all", [E])

    with M2.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (1, 0, 1))
        MB.add_bound_U(3, (0, 0, 0))

    with M2.ExtForces as MF:
        MF.add_force(2, (0, 0, -1))

    M2.Settings.incs = 150
    M2.Settings.du = 0.01
    M2.Settings.dlpf = 0.01
    M2.Settings.xlimit = (2, 10)
    M2.Settings.dlpf
    M2.Settings.stepcontrol = True
    M2.Settings.maxfac = 10

    # Create Model, Run, show Results
    M2.build()
    M2.run()

    fig, ax = M2.plot_model(lim_scale=(-1, 4, -1, 4), inc=0)
    fig.savefig("model2_undeformed.png")
    fig.savefig("model2_undeformed.pdf")

    # model plot: last increment
    fig, ax = M2.plot_model(
        view="xz",
        contour="force",
        lim_scale=(-1, 4, -1, 4),
        force_scale=10,
        inc=40,
    )
    fig.savefig("model2_deformed.png")
    fig.savefig("model2_deformed.pdf")

    fig2, ax2 = M2.plot_history(
        nodes=[2, 2], X="Displacement Z", Y="LPF", fig=fig2, ax=ax2
    )
    ax2.legend(["Node 2: basic model (nDOF=1)", "Node 2: imperfection (nDOF=2)"])
    fig2.savefig("history_node2_DispZ-LPF.png")
    fig2.savefig("history_node2_DispZ-LPF.pdf")

    fig1, ax1 = M2.plot_history(
        nodes=[2, 2], X="Displacement X", Y="Displacement Z", fig=fig1, ax=ax1
    )
    ax1.legend(["Node 2: basic model (nDOF=1)", "Node 2: imperfection (nDOF=2)"])
    fig1.savefig("history_node2_DispX-DispZ.png")
    fig1.savefig("history_node2_DispX-DispZ.pdf")

    M2.plot_movie(
        view="xz",
        contour="force",
        lim_scale=(-4.5, 5, -6, 3.5),
        force_scale=10,
        cbar_limits=[-1, 1],
        incs=range(1, 130, 10),
    )


if __name__ == "__main__":
    test_e103_python()
