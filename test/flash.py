# top=flash::flash

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer, RisingEdge

@cocotb.test()
async def normal_operation(dut):
    s = SpadeExt(dut)
    clk = dut.clk_i

    s.i.rst = "true"
    s.i.cmd = "None"


    await cocotb.start(Clock(clk, 1, units='ns').start())

    await RisingEdge(clk)
    s.i.rst = "false"

    await Timer(12, units='ns')
    await RisingEdge(clk)
    s.i.cmd = "Some(Command::start_read(0x00))"
    await RisingEdge(clk)
    s.i.cmd = "None"

    await Timer(100, units='ns')

    await RisingEdge(clk)
    s.i.cmd = "Some(Command::read_next)"
    await RisingEdge(clk)
    s.i.cmd = "None"

    await Timer(20, units='ns')
    await RisingEdge(clk)
    s.i.cmd = "Some(Command::stop_read)"
    await RisingEdge(clk)
    s.i.cmd = "None"

    await Timer(300, units='ns')
