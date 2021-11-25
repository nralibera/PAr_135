read_netlist CORE65GPSVT_tmax.v -library
read_netlist c17_65n.v
run_build_model c7552
run_drc
set_faults -model stuck
add_faults -all
set_patterns -external c7552.stil -sensitive
run_simulation -pin { N1 1 } > datalog_SA1_N1.txt
quit