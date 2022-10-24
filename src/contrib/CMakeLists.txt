
add_subdirectory(Pspline)
add_subdirectory(Ezcdf)
add_subdirectory(Lsode)
add_subdirectory(Linpack)

list (APPEND fieldlines_sources
	${CMAKE_CURRENT_SOURCE_DIR}/stel_constants.f
	${CMAKE_CURRENT_SOURCE_DIR}/stel_kinds.f
	${CMAKE_CURRENT_SOURCE_DIR}/safe_open_mod.f
	${CMAKE_CURRENT_SOURCE_DIR}/read_wout_mod.f
	${CMAKE_CURRENT_SOURCE_DIR}/wall_mod.f90
	${CMAKE_CURRENT_SOURCE_DIR}/mpi_inc.f
	${CMAKE_CURRENT_SOURCE_DIR}/mpi_params.f
	${CMAKE_CURRENT_SOURCE_DIR}/vmec_input.f
	${CMAKE_CURRENT_SOURCE_DIR}/vparams.f
	${CMAKE_CURRENT_SOURCE_DIR}/vsvd0.f
	${CMAKE_CURRENT_SOURCE_DIR}/mgrid_mod.f
	${CMAKE_CURRENT_SOURCE_DIR}/vessel_mod.f90
	${CMAKE_CURRENT_SOURCE_DIR}/v3_utilities.f
	${CMAKE_CURRENT_SOURCE_DIR}/system_mod.f
	${CMAKE_CURRENT_SOURCE_DIR}/biotsavart.f
	${CMAKE_CURRENT_SOURCE_DIR}/ez_hdf5.f90
	${CMAKE_CURRENT_SOURCE_DIR}/mgrid_field_mod.f90
	${CMAKE_CURRENT_SOURCE_DIR}/vmec_utils.f
	${CMAKE_CURRENT_SOURCE_DIR}/bsc_T.f
	${CMAKE_CURRENT_SOURCE_DIR}/virtual_casing_mod.f90
	${CMAKE_CURRENT_SOURCE_DIR}/tolower.f90
	${CMAKE_CURRENT_SOURCE_DIR}/init_random_seed.f90
	${CMAKE_CURRENT_SOURCE_DIR}/getcarg.f
	${CMAKE_CURRENT_SOURCE_DIR}/parse_extension.f
	${CMAKE_CURRENT_SOURCE_DIR}/vmec_getenv.f
	${CMAKE_CURRENT_SOURCE_DIR}/dcuhre.f
)
set (fieldlines_sources "${fieldlines_sources}" PARENT_SCOPE)

