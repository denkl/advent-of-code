#!/usr/bin/env python
HEADER_N_BITS = 6
VERSION_N_BITS = 3
PACKET_MODE_ID = 6
GROUP_N_BITS = 5
LITERAL_TYPE_ID = 4
TOTAL_LENGTH_IN_BITS = 15
SUBPACKETS_NUM_IN_BITS = 11


def read_input():
    with open("./inputs/day16") as f:
        return f.readline().strip()


def to_bin(hexs):
    return "".join([bin(int(c, base=16)).split("b")[1].zfill(4) for c in hexs])


def part1():
    BITS = read_input()
    bits_ptr = 0
    versions = []

    def at_least_n_bits(n, head=""):
        nonlocal bits_ptr
        n -= len(head)
        n_hex = (n // 4) or 1
        n_hex += 1 if n > 4 and n % 4 else 0
        hexs = BITS[bits_ptr : bits_ptr + n_hex]
        bits_ptr += n_hex
        bits = to_bin(hexs)
        return f"{head}{bits}"

    packet = ""
    while bits_ptr < len(BITS) - 1:
        packet = at_least_n_bits(HEADER_N_BITS + 1, packet)
        version = int(packet[:VERSION_N_BITS], base=2)
        type_id = int(packet[VERSION_N_BITS:HEADER_N_BITS], base=2)
        packet_ptr = HEADER_N_BITS
        versions.append(version)

        if type_id == LITERAL_TYPE_ID:
            number = ""
            while True:
                bits = at_least_n_bits(GROUP_N_BITS, packet[packet_ptr:])
                group = bits[:GROUP_N_BITS]
                group_prefix, group_bits = group[0], group[1:]
                number = f"{number}{group_bits}"
                packet = "".join((packet[:packet_ptr], bits))
                packet_ptr += len(group)
                if group_prefix == "0":
                    packet = packet[packet_ptr:]
                    break
        else:
            mode = packet[PACKET_MODE_ID]
            packet_ptr += 1
            if mode == "0":
                bits = at_least_n_bits(TOTAL_LENGTH_IN_BITS, packet[packet_ptr:])
                packet = bits[TOTAL_LENGTH_IN_BITS:]
            else:
                bits = at_least_n_bits(SUBPACKETS_NUM_IN_BITS, packet[packet_ptr:])
                packet = bits[SUBPACKETS_NUM_IN_BITS:]

    print(f"#1: {sum(versions)}")


if __name__ == "__main__":
    part1()
