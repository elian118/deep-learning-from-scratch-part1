from ch02.and_gate import AND
from ch02.nand_gate import NAND
from ch02.or_gate import OR
from ch02.utils import inputs

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y

for [x1, x2] in inputs:
    print(f"{x1}, {x2} → XOR → {XOR(x1, x2)}")