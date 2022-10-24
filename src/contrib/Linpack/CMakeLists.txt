
list (APPEND fieldlines_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/li_gbfa.f
    ${CMAKE_CURRENT_SOURCE_DIR}/li_gbsl.f
    ${CMAKE_CURRENT_SOURCE_DIR}/li_gefa.f
    ${CMAKE_CURRENT_SOURCE_DIR}/li_gesl.f
    ${CMAKE_CURRENT_SOURCE_DIR}/liprec.f
)
set (fieldlines_sources "${fieldlines_sources}" PARENT_SCOPE)
