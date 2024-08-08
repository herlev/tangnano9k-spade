# Tang Nano 9K Spade

## Getting started

This repository contains the code I develop while working through the [Tang Nano 9K Series](https://learn.lushaylabs.com/tang-nano-series/), but written in [Spade](https://spade-lang.org/) instead of Verilog.

### Install tools
- install [`swim`](https://gitlab.com/spade-lang/swim) and [`surfer`](https://gitlab.com/surfer-project/surfer)
  - ```
    cargo install --git https://gitlab.com/spade-lang/swim
    cargo install --git https://gitlab.com/surfer-project/surfer surfer
    ```
- install a version of [oss-cad-suite](https://github.com/YosysHQ/oss-cad-suite-build) that is compatible with swim
  - `swim install-tools`
- install [`tio`](https://github.com/tio/tio)
  - `paru -S tio`
- install [`openFPGALoader`](https://github.com/trabucayre/openFPGALoader) and [`just`](https://github.com/casey/just)
  - `pacman -S openfpgaloader just`

### Editor setup
#### [Helix](https://helix-editor.com/)
- install [`spade-language-server`](https://gitlab.com/spade-lang/spade-language-server)
  - `cargo install --git https://gitlab.com/spade-lang/spade-language-server`
- Add the following to `~/.config/helix/languages.toml`
    ```toml
    [[language]]
    name = "spade"
    scope = "source.spade"
    roots = ["swim.toml"]
    file-types = ['spade']
    comment-token = "//"
    language-servers = ["spade-language-server"]

    [[grammar]]
    name = "spade"
    source = {git = "https://gitlab.com/spade-lang/tree-sitter-spade", rev = "977dbc6ec98d409374a990e7a3b1fdb33a3459aa"}
    
    [language-server.spade-language-server]
    command="spade-language-server"
    ```
- Create the file [highlights.scm](https://gitlab.com/spade-lang/spade-vim/-/blob/master/queries/spade/highlights.scm) inside the directory `~/.config/helix/runtime/queries/spade/`
- `hx --grammar fetch && hx --grammar build`

### Building, flashing and testing

List available commands using `just --list`

## Resources

**Tutorials**

- [Tang Nano 9K Series by Lushay Labs](https://learn.lushaylabs.com/tang-nano-series/)
- [Introduction to FPGA by Digikey](https://www.youtube.com/watch?v=lLg1AgA2Xoo&list=PLEBQazB0HUyT1WmMONxRZn9NmQ_9CIKhb&index=2)

**Examples**

- [Sipeed Tang Nano 9K examples](https://github.com/sipeed/TangNano-9K-example)
- [Lushay Labs Tang Nano 9K Series examples](https://github.com/lushaylabs/tangnano9k-series-examples)

**Datasheets**

- [ST7789VW LCD driver](http://www.lcdwiki.com/res/MSP1141/ST7789VW_datasheet.pdf)
- [Tang Nano 9K schematic](https://learn.lushaylabs.com/content/files/2022/08/Tang_Nano_9K_3672_schematic.pdf)
