# top=uart::uart_tx

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer

@cocotb.test()
async def normal_operation(dut):
    s = SpadeExt(dut)

    clk = dut.clk_i
    s.i.tx_en = "false"
    s.i.tx_byte = "0b11001001"
    await cocotb.start(Clock(clk, 37, units='ns').start())

    await FallingEdge(clk)
    s.i.tx_en = "true"

    await Timer(10, units='ms')

    # s.o.assert_eq("OutputControl::Ret()")

