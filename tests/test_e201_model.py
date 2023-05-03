import trusspy as tp


def test_e201(filepath="tests/"):
    "Ex.201: 1 Truss with 1 DOF, linear elastic-plastic (isotropic hardening)"

    M = tp.Model(filepath + "e201_input.xlsx")
    M.Settings.nstatev = 2

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

    # history plot
    fig, ax = M.plot_history(nodes=[2, 2], X="Displacement X", Y="Force X")
    fig.savefig("history_node2_DispX-ForceX.pdf")


if __name__ == "__main__":
    test_e201(filepath="./")
