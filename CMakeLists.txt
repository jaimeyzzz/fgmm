cmake_minimum_required(VERSION 3.16)

# Set project name and version
project(fgmm VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Set global resource and output directories
add_compile_definitions(
    RESOURCES_DIR="${PROJECT_SOURCE_DIR}/resources/"
    OUTPUT_DIR="${PROJECT_SOURCE_DIR}/output/"
) 

# Add subdirectories
add_subdirectory(external/qiwu)
