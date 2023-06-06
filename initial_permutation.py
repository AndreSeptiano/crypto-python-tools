import sys

def init():
    hex_table = {
        '0':'0000','1':'0001','2':'0010','3':'0011',
        '4':'0100','5':'0101','6':'0110','7':'0111',
        '8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111',
    }

    # Kolom pertama = [58, 60, 62, 64, 57, 59, 61, 63]
    init_gen = [57, 59, 61, 63, 56, 58, 60, 62]
    ip_table = []
    for i in init_gen:
        while i >= 0:
            ip_table.append(i)
            i -= 8
    return ip_table, hex_table

def reverse_hex(hex_table):
    reverse_hex_table = {}
    for key, value in hex_table.items():
        reverse_hex_table[value] = key
    return reverse_hex_table

def main(input_hex='ABABCDCDEFEF0202'):
    assert len(input_hex) == 16, "The length of hex string must be equal to 16."

    ip_table, hex_table = init()
    to_bin    = ''.join([hex_table[char] for char in input_hex])
    permute   = [to_bin[ip_table[i]] for i in range(64)]
    
    reverse_hex_table = reverse_hex(hex_table)
    permute_to_hex = [reverse_hex_table[''.join(permute[i:i+4])] for i in range(0,64,4)]

    print('Before:',end=' ')
    for i in range(0,16,2):
        print(f'{input_hex[i]}{input_hex[i+1]}', end= ' ')
    print('\nAfter: ',end=' ')
    for i in range(0,16,2):
        print(f'{permute_to_hex[i]}{permute_to_hex[i+1]}', end= ' ')


if __name__=='__main__':
    n = len(sys.argv)
    if n > 2:
        raise TypeError("Incorrect number of arguments! (Less than three are needed).")
    try:
        if len(sys.argv) == 1:
            main()
        else:
            main(sys.argv[1].upper())
    except KeyError as e:
        raise e("Inputs are not Hexadecimal!")