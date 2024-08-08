synth:
	swim synth

build:
	make main.fs

load: build
	openFPGALoader -b tangnano9k main.fs

flash: build
	openFPGALoader -b tangnano9k main.fs -f

test TEST:
	swim test {{TEST}}
