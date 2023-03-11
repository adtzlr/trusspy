import trusspy as tp


def test_e10xx():
    "Ex.10xx"

    nnodes = 2

    M = tp.Model()

    M.Settings.du = 0.1
    M.Settings.dlpf = 0.05
    M.Settings.incs = (20, 20, 20, 20)
    M.Settings.xlimit = (1, 1)
    M.Settings.nsteps = 4
    M.Settings.stepcontrol = False

    NN = []
    for i in range(1, nnodes + 1):
        N = tp.Node(i, (0, 0, -(i - 1) / (nnodes - 1)))
        NN.append(N)

    EE = []
    for i in range(1, nnodes):
        E = tp.Element(
            i,
            [i, i + 1],
            material_properties=[100, 80, 1],
            geometric_properties=[1],
            mat_type=2,
        )
        EE.append(E)

    BB = [tp.BoundaryU(1, (0, 0, 0))]
    for i in range(2, nnodes + 1):
        B = tp.BoundaryU(i, (0, 0, 1))
        BB.append(B)

    FF = []
    for i in range(1, nnodes):  # +1):
        F = tp.ExternalForce(i, (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        # F = tp.ExternalForce( i, (0,0,-(i-1)/(nnodes-1), 0,0, (i-1)/(nnodes-1), 0,0,-(i-1)/(nnodes-1), 0,0,0) )
        FF.append(F)
    F = tp.ExternalForce(nnodes, (0, 0, -1.2, 0, 0, 2.45, 0, 0, -2.6, 0, 0, 2.85))
    FF.append(F)

    M.Nodes.add_nodes(NN)
    M.Elements.add_elements(EE)
    M.Boundaries.add_bounds_U(BB)
    M.ExtForces.add_forces(FF)

    # Create Model, Run, show Results
    M.build()
    M.run()

    # model plot: undeformed and deformed configuration for last increment
    fig0, ax0 = M.plot_model(
        config=["undeformed"],
        view="xz",
        lim_scale=(-1, 1, -1.5, 0.5),
        force_scale=0.5,
        inc=0,
    )
    fig0.savefig("model_contour-force_inc-begin.pdf")

    fig1, ax1 = M.plot_model(
        config=["deformed"],
        view="xz",
        contour="stress",
        lim_scale=(-1, 1, -1.5, 0.5),
        force_scale=0.5,
        cbar_limits="auto",
        inc=-1,
    )
    fig1.savefig("model_contour-force_inc-last.pdf")

    # M.plot_movie(config=['deformed'],
    #             view='xz',
    #             contour='stress',
    #             lim_scale=(-5,5,-8,1),
    #             force_scale=15.0,
    #             cbar_limits=[-0.3,0.3],
    #             incs='all')

    # history plot
    M.plot_history(nodes=[nnodes, nnodes], X="Increments", Y="LPF")
    fig2, ax2 = M.plot_history(nodes=[nnodes, nnodes], X="Displacement Z", Y="Force Z")
    fig2.savefig("history_node2_DispX-ForceX.pdf")

    # path plot
    fig3, ax3 = M.plot_path(
        nodepath=range(1, nnodes + 1), increment=-1, Y="Displacement Z"
    )
    fig3, ax3 = M.plot_path(
        nodepath=range(1, nnodes + 1),
        increment=-2,
        Y="Displacement Z",
        fig=fig3,
        ax=ax3,
    )
    fig3.savefig("path_nodes_DispZ.pdf")


if __name__ == "__main__":
    test_e10xx()
