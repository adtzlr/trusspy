import trusspy as tp


def test_e202(filepath="tests/"):
    "Ex.202: 2 Trusses with 1 DOF, linear elastic-plastic (isotropic hardening)"

    M = tp.Model(filepath + "e202_input.xlsx")
    M.Settings.nstatev = 2

    M.Settings.incs = 100

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
    fig, ax = M.plot_history(nodes=[2, 2], X="Displacement Z", Y="LPF")
    fig.savefig("history_node2_DispZ-LPF.pdf")


if __name__ == "__main__":
    test_e202(filepath="./")
