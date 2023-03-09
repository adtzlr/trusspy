import trusspy as tp


def test_e102_python():
    "Ex.102-Python: 2 Trusses with 1 DOF, linear elastic"

    M = tp.Model(logfile=False)

    with M.Nodes as MN:
        MN.add_node(1, coord=(0, 0, 0))
        MN.add_node(2, coord=(1, 0, 1))
        MN.add_node(3, coord=(2, 0, 0))

    with M.Elements as ME:
        ME.add_element(1, conn=(1, 2), gprop=[1])
        ME.add_element(2, conn=(2, 3), gprop=[1])

        E = 1  # elastic modulus
        ME.assign_material("all", [E])

    with M.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (0, 0, 1))
        MB.add_bound_U(3, (0, 0, 0))

    with M.ExtForces as MF:
        MF.add_force(2, (0, 0, -1))

    M.Settings.incs = 100
    M.Settings.xlimit = (2, 0.5)
    M.Settings.dlpf
    M.Settings.stepcontrol = True
    M.Settings.maxfac = 4

    # Create Model, Run, show Results
    M.build()
    M.run()

    fig, ax = M.plot_model(config=["undeformed"], inc=0)
    fig.savefig("model_undeformed.png")
    fig.savefig("model_undeformed.pdf")

    # model plot: undeformed and deformed configuration for last increment
    fig, ax = M.plot_model(
        config=["undeformed", "deformed"],
        view="xz",
        contour="force",
        lim_scale=(-1, 3, -2.5, 1.5),
    )
    fig.savefig("model_deformed.png")
    fig.savefig("model_deformed.pdf")

    # history plot
    fig, ax = M.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF")

    # re-run with plasticity
    with M.Elements as ME:
        K = 0.1  # plastic modulus
        Sy = 0.1  # initial yield stress

        ME.assign_mtype("all", 2)
        ME.assign_material("all", [E, K, Sy])

    # Create Model, Run, show Results
    M.build()
    M.run()

    fig, ax = M.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF", fig=fig, ax=ax)
    ax.legend(
        ["Node 2: linear elastic", "Node 2: elastic-plastic (isotropic hardening)"]
    )
    fig.savefig("history_node2_DispZ-LPF.png")
    fig.savefig("history_node2_DispZ-LPF.pdf")


if __name__ == "__main__":
    test_e102_python()
