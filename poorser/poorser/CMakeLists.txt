add_library(poorser poorser.hpp poorser.cpp)

add_executable(poorser_demo poorser_demo.cpp)
target_link_libraries(poorser_demo poorser)