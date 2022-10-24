cmake_minimum_required(VERSION 3.15.0)

project(fieldlines LANGUAGES C CXX Fortran)

# Start Project and note the language used. The BLAS and LAPACK libraries for ifort require a working C and C++ compiler.
project (FIELDLINES Fortran C CXX)

set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH};${CMAKE_CURRENT_SOURCE_DIR}/cmake)
find_package (NetCDF MODULE REQUIRED)
find_package (MPI REQUIRED)
find_package (HDF5 REQUIRED COMPONENTS Fortran)
find_package (FFTW MODULE REQUIRED COMPONENTS DOUBLE_LIB)

set(CMAKE_VERBOSE_MAKEFILE ON CACHE BOOL "ON")

# Set a directories to build all binary files.
set (EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_BINARY_DIR}/bin)
set (LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_BINARY_DIR}/lib)

# Add extra compiler flags to various builds.
set (CMAKE_Fortran_FLAGS_RELEASE "${CMAKE_Fortran_FLAGS_RELEASE} ${EXTRA_RELEASE_FLAGS}")
set (CMAKE_Fortran_FLAGS_DEBUG "${CMAKE_Fortran_FLAGS_DEBUG} ${EXTRA_DEBUG_FLAGS}")
set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} ${EXTRA_FLAGS}")

# Fortran specific settings. The first setting tells the compiler to use the C preprocessor.
# The second places a common directory to place all of the module files.
set (CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -cpp -ffixed-line-length-none -ffree-line-length-none")
set (CMAKE_Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)

find_package (BLAS REQUIRED)
if (NOT ${BLA_VENDOR} MATCHES "^Intel")
    find_package (LAPACK REQUIRED)
endif()

# needed for ez_hdf5
if (HDF5_FOUND)
	message (STATUS "Using HDF5")
	add_definitions (-DLHDF5)

else ()
	message (FATAL_ERROR "Failed to find the required HDF5 libraries.")
endif ()

if (NetCDF_FOUND)
	message (STATUS "Using netcdf")
	add_definitions (-DNETCDF)
	include_directories (${NetCDF_INCLUDE_DIRS})

	list (APPEND NETCDF_LIBRARIES "${NetCDF_LIBRARIES}")
else ()
	message (FATAL_ERROR "Failed to find the required netcdf libraries.")
endif ()

if (FFTW_DOUBLE_LIB_FOUND)
	message (STATUS "Using fftw")
	include_directories (${FFTW_INCLUDE_DIRS})
else ()
	message (FATAL_ERROR "Failed to find the required fftw library.")
endif ()

set (fieldlines_sources "")
add_subdirectory(src)

add_library (fieldlines STATIC ${fieldlines_sources})
set_target_properties (fieldlines PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_Fortran_MODULE_DIRECTORY}/fieldlines)
target_include_directories(fieldlines PUBLIC ${CMAKE_Fortran_MODULE_DIRECTORY}/fieldlines)

target_link_libraries (fieldlines PUBLIC ${NETCDF_LIBRARIES})
target_link_libraries (fieldlines PUBLIC $<$<BOOL:${HDF5_FOUND}>:HDF5::HDF5>)
target_link_libraries (fieldlines PUBLIC ${FFTW_DOUBLE_LIB})

target_link_libraries (fieldlines PUBLIC $<$<BOOL:${MPI_Fortran_FOUND}>:MPI::MPI_Fortran> )

if (BLAS_FOUND)
	target_link_libraries (fieldlines PUBLIC ${BLAS_LIBRARIES})
endif ()
if (LAPACK_FOUND)
	target_link_libraries (fieldlines PUBLIC ${LAPACK_LIBRARIES})
endif ()

get_target_property(FIELDLINES_LINK_LIB fieldlines LINK_LIBRARIES)
message(STATUS "fieldlines linked libraries are ${FIELDLINES_LINK_LIB}")

# Define an executable and link all libraries.
add_executable (xfieldlines ${CMAKE_CURRENT_SOURCE_DIR}/src/fieldlines_main.f90)
target_link_libraries (xfieldlines fieldlines)
