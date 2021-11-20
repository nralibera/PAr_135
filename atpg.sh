read_netlist ./CORE65GPSVT_tmax.v -library
read_netlist ./c7552_65n.v 
run_build_model c7552
run_drc
set_faults -model stuck
add_faults -all
run_atpg -auto_compression -ndetects 1
report_faults -all > c7552.fault
write_patterns c7552.stil -internal -format stil -cycle_count -nopatinfo -parallel 0 -cellnames parallel
