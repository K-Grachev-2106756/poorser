cmake_minimum_required(VERSION 3.15)

project(poorser_demo)

include_directories(poorser)

add_subdirectory(poorser)

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX "${CMAKE_CURRENT_BINARY_DIR}/install" CACHE PATH "..." FORCE)
endif()

set(sources get_ids.py)
set(sources get_prices.py)
set(sources get_products.py)
set(sources sort.py)
set(sources sort1.py)
set(sources sort2.py)
set(sources show.py)

set(EXECUTABLE_OUTPUT PATH ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

install(TARGETS poorser_demo DESTINATION poorser)
install(FILES scripts/get_ids.py DESTINATION poorser)
install(FILES scripts/get_prices.py DESTINATION poorser)
install(FILES scripts/get_products.py DESTINATION poorser)
install(FILES scripts/sort.py DESTINATION poorser)
install(FILES scripts/sort1.py DESTINATION poorser)
install(FILES scripts/sort2.py DESTINATION poorser)
install(FILES scripts/show.py DESTINATION poorser)