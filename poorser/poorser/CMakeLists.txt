add_library(poorser poorser.hpp poorser.cpp)

add_executable(poorser_test poorser_test.cpp)
target_link_libraries(poorser_test poorser)