set(PROGS example)
foreach(name ${PROGS})
  add_executable(${name} ${name}.cc)
  target_link_libraries(${name} mptensor)
endforeach(name ${PROGS})
