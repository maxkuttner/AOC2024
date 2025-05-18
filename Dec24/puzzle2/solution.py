file = open("data.txt")

# these wire values we already know
known = {}

# formulas which ought to be applied to the wires
formulas = {}


for line in file:
    if line.isspace(): break
    x, y = line.strip().split(":")
    known[x] = int(y)


for line in file:
    x, op, y, z = line.replace(" -> ", " ").strip().split()
    formulas[z] = (op, x, y)


operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}


def pp(wire, depth=0):
    if wire[0] in ["x", "y"]:
        return "  " * depth + wire
    op, x, y = formulas[wire]
    return (
            "  " * depth + op + " (" + wire + "):\n"
            + pp(x, depth + 1)
            + "\n"
            + pp(y, depth + 1)
    )

print(pp("z00"))
# print(pp("z01"))
# print(pp("z02"))


def verify_z(wire, num):
    print("vz", wire, num)
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    if num == 0:
        # if we are checking the first wire z00 -> it should
        # just be a xor connection between wires x00 and y00
        return sorted([x, y]) == ["x00", "y00"]

    # ... else (i.e. for higher wires z01, z02, ... -> the operation must be a
    # a XOR : for a valid xor (intermediate) and a valid carry
    return (
            verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or
            verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

def get_wire(char, num):
    # ... construct the wire in the given notation z[0].\d
    return char + str(num).rjust(2, "0")

def verify_intermediate_xor(wire, num):
    print("vx", wire, num)
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if op != "XOR":
        return False
    return sorted([x, y]) == [get_wire("x", num), get_wire("y", num)]

def verify_carry_bit(wire, num):
    print("vc", wire, num)
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]
    if num == 1:
        # For bit 1: carry is x00 AND y00
        if op != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]

    # .. for higher bits it must be an or ...
    if op != "OR":
        return False
    # ... of ...
    # *) a direct carry: xN AND yN
    # *) and a re-carry: (xN XOR yN) AND previous carry
    # For reference look at the graph of "full adder" where you have
    # the ANDs connecting with an OR gate
    return (
            verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or
            verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)
    )

def verify_direct_carry(wire, num):
    print("vd", wire, num)
    if wire not in formulas:
        return False
    op, x, y = formulas[wire]

    if op != "AND":
        return False
    # a direct carry is just the AND connection between the two bits x and y
    return sorted([x, y]) == [
        get_wire("x", num),
        get_wire("y", num),
    ]

def verify_recarry(wire, num):
    print("vr", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "AND":
        return False
    # the verify recarry is seen in the "full adder" graph where there is
    # an AND connection between the top xor and the input carry bit
    # we just need to check if either of the two wires x and y comes from the
    # combination XOR and valid Carry ... does not matter which so that is why
    # we apply it to either blabla(x) and blublub(y)
    # or blabla(y) and blublub(x)
    return (
            verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or
            verify_intermediate_xor(y, num) and verify_carry_bit(x, num)
    )

def verify(num):
    return verify_z(get_wire("z", num), num)

i = 0

while True:
    if not verify(i):
        break
    i += 1

print("failed on", get_wire("z", i))

# now we need to fiddle around and see which ones we need to change
# in order to arrive at 45
# 45 is expected to fail becuase technically it is the carry from the
# previous addition

# shj <-> z07
# tpk <-> wkb
# z23 <-> pfn
# kcd <-> z27


# result: kcd,pfn,shj,tpk,wkb,z07,z23,z27
# credits: hyperneutrino ... for this approach



