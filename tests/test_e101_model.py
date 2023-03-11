import trusspy as tp


def test_e101(filepath="tests/"):
    "Ex.101: 1 Truss with 1 DOF, linear elastic"

    M = tp.Model(filepath + "e101_input.xlsx", logfile=False)

    # Create Model, Run, show Results
    M.build()
    M.run()

    # model plot: undeformed and deformed configuration for last increment
    fig, ax = M.plot_model(
        config=["undeformed", "deformed"],
        view="xz",
        contour="force",
        lim_scale=2,
        force_scale=0.2,
        inc=-1,
    )
    fig.savefig("model_contour-force_inc-last.pdf")

    # history plot
    fig, ax = M.plot_history(nodes=[2, 2], X="Displacement X", Y="Force X")
    fig.savefig("history_node2_DispX-ForceX.pdf")


if __name__ == "__main__":
    test_e101(filepath="./")
