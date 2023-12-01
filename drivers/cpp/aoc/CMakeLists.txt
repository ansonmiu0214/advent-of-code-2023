# One executable per solution
file(GLOB solutions CONFIGURE_DEPENDS "*.cpp")
foreach(filename ${solutions})
    get_filename_component(executable ${filename} NAME_WE)
    message(STATUS "Registering executable: ${executable}")

    add_executable(${executable} ${filename})
    target_include_directories(${executable} PRIVATE "${CMAKE_SOURCE_DIR}/lib")

    target_link_libraries(${executable} PRIVATE aoc)
endforeach()