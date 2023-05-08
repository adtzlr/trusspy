import trusspy as tp


def create_model():
    """Create a TrussPy-Model and return the Model instance."""
    M = tp.Model(log=0)

    with M.Nodes as MN:
        MN.add_node(1, coord=(0, 0, 0))
        MN.add_node(2, coord=(1, 0, 1))
        MN.add_node(3, coord=(2, 0, 0))

    with M.Elements as ME:
        ME.add_element(1, conn=(1, 2), gprop=[1])
        ME.add_element(2, conn=(2, 3), gprop=[1])
        ME.assign_material("all", [1])

    with M.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (0, 0, 1))
        MB.add_bound_U(3, (0, 0, 0))

    with M.ExtForces as MF:
        MF.add_force(2, (0, 0, -1))

    M.Settings.incs = 1
    return M


def stiffness(list_of_areas):
    """Calculate the stiffness matrix as a function of elemental
    cross-section areas (passed as list)."""

    M = create_model()
    M.Elements.assign_geometries("all", list_of_areas)

    M.build()
    M.run()

    R0 = M.Results.R[1]
    # return K (full system), Kred (only active DOF)
    # or Kmod (see Documentation)
    return R0.Kred


def test_stiffness_function():
    list_of_areas = [2, 3]
    K = stiffness(list_of_areas)


if __name__ == "__main__":
    test_stiffness_function()
