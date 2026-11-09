# COMP 311 — Lab 4: Build a RISC-V CPU

Follow the course Lab 4 write-up for the tasks and submission requirements.
This starter is deliberately incomplete: you build the control unit and connect
an ALU and register file to the supplied PC and instruction memory.

## Start here

1. Open `cpu.dig` in Digital. Keep all custom circuit files in this folder.
2. Copy your completed Fall Lab 3 `alu.dig` and all of its dependencies here,
   plus your completed in-class `register-file.dig`.
3. Test those components separately before connecting the CPU. `alu-test.txt`
   contains the Fall ALU check cases in Digital test-block format.
4. Complete `control-signals.csv`, build `control-unit.dig`, and wire the
   datapath as described in the write-up. Preserve the supplied pin names.
5. Load `basic-tests.csv` into instruction memory starting at address 0.
   Copy the CSV cells (not the file path) into Digital's ROM editor.
6. Copy `basic.txt` into the green CPU test block and run it after completing
   the wiring. Restart simulation before each fresh run.

## Files and interfaces

- `cpu.dig`: PC starting at 0, PC+4, 1024-word instruction ROM, `clk`, and
  unconnected 32-bit outputs `ReadData1` and `ReadData2`.
- `control-signals.csv`: eleven instruction rows; `add` is the worked example.
- `basic-tests.s`: a starting program exercising addi, andi, and slti.
- `basic-tests.mem`: that program as one 32-bit hexadecimal instruction per line.
- `basic-tests.csv`: the same program in Digital's eight-cell-per-row format,
  with unused ROM entries cleared to zero.
- `basic.txt`: expected read-port values for that program. A `C` row checks
  the instruction selected AFTER the clock pulse, not the prior destination.
- `format.py`: converts a `.mem` file into ROM CSV. Python 3; no packages needed.
- `alu-test.txt`: component checks; A is the value and B[4:0] the shift amount.

ALU inputs: `A` (32), `B` (32), `ALUOp` (4).
ALU outputs: `Result` (32), `FlagZ` (1).
Control-unit inputs: `opcode` (7), `funct3` (3), `funct7` (7).
Control-unit outputs: `RegWrite` (1), `ALUSrc` (1), `ImmSrc` (2), `ALUOp` (4).
Use the same rising-edge clock for the PC and register file. The PC uses
bits 11–2 to index the ROM. Unsupported instructions must not write registers.

## Changing the program

Assemble your changes as RV32I (no compressed instructions), exporting one
hexadecimal instruction word per line. Then run:

```sh
python3 format.py basic-tests.mem basic-tests.csv
```

Reload the CSV into the ROM and update the expected output rows to match.
The formatter is not an assembler: editing `.s` alone does not update `.mem`.
The provided program is not comprehensive. Add tests for the remaining
instructions, shifts, signed boundaries, dependencies, and writes to x0.
