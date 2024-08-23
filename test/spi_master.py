# top=spi::spi_master

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer, Edge

async def rising_edge(pin, clk):
    while pin.is_eq("true"):
        await Edge(clk)
    while pin.is_eq("false"):
        await Edge(clk)

async def falling_edge(pin, clk):
    while pin.is_eq("false"):
        await Edge(clk)
    while pin.is_eq("true"):
        await Edge(clk)

@cocotb.test()
async def normal_operation(dut):
    s = SpadeExt(dut)

    clk = dut.clk_i
    sclk = s.o.sclk
    mosi = s.o.mosi
    rx_byte = s.o.byte

    s.i.tx_byte = "None"
    s.i.miso = "false"
    await cocotb.start(Clock(clk, 1, units='ns').start())

    await RisingEdge(clk)
    await RisingEdge(clk)
    tx_bits = "11001001"
    rx_bits = "01101010"
    s.i.tx_byte = f"Some(0b{tx_bits})"
    await RisingEdge(clk)
    s.i.tx_byte = "None"

    for i in range(8):
        await falling_edge(sclk, clk)
        s.i.miso = "true" if rx_bits[i] == "1" else "false"
        await rising_edge(sclk, clk)
        mosi.assert_eq("true" if tx_bits[i] == "1" else "false")

    rx_byte.assert_eq(f"Some(0b{rx_bits})")

    await Timer(5, units='ns')
