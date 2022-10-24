
list (APPEND fieldlines_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/xerrwv.f
    ${CMAKE_CURRENT_SOURCE_DIR}/cfode.f
    ${CMAKE_CURRENT_SOURCE_DIR}/ewset.f
    ${CMAKE_CURRENT_SOURCE_DIR}/intdy.f
    ${CMAKE_CURRENT_SOURCE_DIR}/lsode.f
    ${CMAKE_CURRENT_SOURCE_DIR}/prepj.f
    ${CMAKE_CURRENT_SOURCE_DIR}/solsy.f
    ${CMAKE_CURRENT_SOURCE_DIR}/stode.f
    ${CMAKE_CURRENT_SOURCE_DIR}/vnorm.f
)
set (fieldlines_sources "${fieldlines_sources}" PARENT_SCOPE)

