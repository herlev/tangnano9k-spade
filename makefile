main.fs: main_pnr.json
	gowin_pack -d GW1N-9C -o main.fs main_pnr.json

main_pnr.json: build/hardware.json
	nextpnr-himbaechel --json build/hardware.json --write main_pnr.json --device GW1NR-LV9QN88PC6/I5 --vopt family=GW1N-9C --vopt cst=pins.cst --vopt top=main

build/hardware.json: src/main.spade src/uart.spade
	swim synth
