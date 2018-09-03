#Test the min max function


from pymtl      import *
from RegIncr     import RegIncr

def test_basic( dump_vcd ):
   model = MaxMinUnit()
   model.vcd_file = dump_vcd
   model.elaborate()

   sim = SimulationTool(model)
   sim.rest()
   print ""

   def t( in0, in1, out_min, out_max):
     model.in0.value = in0
     model.in1.value = in1 
     
     sim.eval_combinational()

     sim.print_line_trace()

     if (out_min != '?'):
       assert model.out_min == out_min

     if (out_max != '?'):
       assert model.out_max == out_max

     sim.cycle()
 
#test
   t(1, 2, 1, 2)
   t(3, 1, 1, 3)
   t(0, 2, 0, 2) 
