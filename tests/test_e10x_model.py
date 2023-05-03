import trusspy as tp


def test_e10x():
    "Ex.10x"

    M = tp.Model()

    M.Settings.du = 0.05
    M.Settings.dlpf = 0.05
    M.Settings.incs = (40, 40, 40, 40)
    M.Settings.xlimit = (1, 1)
    M.Settings.nstatev = 2
    M.Settings.nsteps = 4

    N1 = tp.Node(1, (0, 0, -0))
    N2 = tp.Node(2, (0, 0, -1))
    N3 = tp.Node(3, (0, 0, -2))
    N4 = tp.Node(4, (0, 0, -3))
    N5 = tp.Node(5, (0, 0, -4))
    N6 = tp.Node(6, (0, 0, -5))

    E1 = tp.Element(
        1,
        [1, 2],
        material_properties=[1, 0.1, 0.1],
        geometric_properties=[1],
        mat_type=2,
    )
    E2 = tp.Element(
        2,
        [2, 3],
        material_properties=[1, 0.1, 0.1],
        geometric_properties=[1],
        mat_type=2,
    )
    E3 = tp.Element(
        3,
        [3, 4],
        material_properties=[1, 0.1, 0.1],
        geometric_properties=[1],
        mat_type=2,
    )
    E4 = tp.Element(
        4,
        [4, 5],
        material_properties=[1, 0.1, 0.1],
        geometric_properties=[1],
        mat_type=2,
    )
    E5 = tp.Element(
        5,
        [5, 6],
        material_properties=[1, 0.1, 0.1],
        geometric_properties=[1],
        mat_type=2,
    )

    B1 = tp.BoundaryU(1, (0, 0, 0))
    B2 = tp.BoundaryU(2, (0, 0, 1))
    B3 = tp.BoundaryU(3, (0, 0, 1))
    B4 = tp.BoundaryU(4, (0, 0, 1))
    B5 = tp.BoundaryU(5, (0, 0, 1))
    B6 = tp.BoundaryU(6, (0, 0, 1))

    F1 = tp.ExternalForce(1, (0, 0, -0, 0, 0, 0, 0, 0, -0, 0, 0, 0))
    F2 = tp.ExternalForce(2, (0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1))
    F3 = tp.ExternalForce(3, (0, 0, -2, 0, 0, 2, 0, 0, -2, 0, 0, 2))
    F4 = tp.ExternalForce(4, (0, 0, -3, 0, 0, 3, 0, 0, -3, 0, 0, 3))
    F5 = tp.ExternalForce(5, (0, 0, -4, 0, 0, 4, 0, 0, -4, 0, 0, 4))
    F6 = tp.ExternalForce(6, (0, 0, -5, 0, 0, 5, 0, 0, -5, 0, 0, 5))

    M.Nodes.add_nodes([N1, N2, N3, N4, N5, N6])
    M.Elements.add_elements([E1, E2, E3, E4, E5])
    M.Boundaries.add_bounds_U([B1, B2, B3, B4, B5, B6])
    M.ExtForces.add_forces([F1, F2, F3, F4, F5, F6])

    # Create Model, Run, show Results
    M.build()
    M.run()

    # model plot: undeformed and deformed configuration for last increment
    fig0, ax0 = M.plot_model(
        view="xz",
        lim_scale=(-5, 5, -8, 1),
        force_scale=1.0,
        inc=0,
    )
    fig0.savefig("model_contour-force_inc-begin.pdf")

    fig1, ax1 = M.plot_model(
        view="xz",
        contour="stress",
        lim_scale=(-5, 5, -8, 1),
        force_scale=15.0,
        cbar_limits=[-0.2, 0.2],
        inc=-1,
    )
    fig1.savefig("model_contour-force_inc-last.pdf")

    M.plot_movie(
        view="xz",
        contour="stress",
        lim_scale=(-5, 5, -8, 1),
        force_scale=15.0,
        cbar_limits=[-0.3, 0.3],
        incs="all",
    )

    # history plot
    fig2, ax2 = M.plot_history(nodes=[6, 6], X="Displacement Z", Y="Force Z")
    fig2.savefig("history_node2_DispX-ForceX.pdf")


if __name__ == "__main__":
    test_e10x()
