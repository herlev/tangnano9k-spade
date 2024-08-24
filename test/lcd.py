# top=lcd::lcd

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer, RisingEdge

@cocotb.test()
async def normal_operation(dut):
    s = SpadeExt(dut)
    clk = dut.clk_i

    s.i.rst = "true"


    await cocotb.start(Clock(clk, 1, units='ns').start())

    await RisingEdge(clk)
    s.i.rst = "false"

    await Timer(5, units='us')
