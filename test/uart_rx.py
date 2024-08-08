# top=uart::uart_rx

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer

@cocotb.test()
async def normal_operation(dut):
    s = SpadeExt(dut)

    clk = dut.clk_i
    s.i.rx = "true"
    await cocotb.start(Clock(clk, 1, units='ns').start())

    await FallingEdge(clk)
    # 0b10010011
    
    # start bit
    s.i.rx = "false"
    await Timer(4, units='ns')

    s.i.rx = "true"
    await Timer(4, units='ns')
    s.i.rx = "true"
    await Timer(4, units='ns')
    s.i.rx = "false"
    await Timer(4, units='ns')
    s.i.rx = "false"
    await Timer(4, units='ns')
    s.i.rx = "true"
    await Timer(4, units='ns')
    s.i.rx = "false"
    await Timer(4, units='ns')
    s.i.rx = "false"
    await Timer(4, units='ns')
    s.i.rx = "true"
    await Timer(4, units='ns')
    # stop bit
    s.i.rx = "true"
    await Timer(4, units='ns')

    await Timer(10, units='ns')


    # s.o.assert_eq("OutputControl::Ret()")

