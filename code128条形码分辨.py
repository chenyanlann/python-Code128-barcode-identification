from PIL import Image

import numpy as np

import matplotlib.pyplot as plt

image_path = "10.png"

img = Image.open(image_path)

width, height = img.size

basewidth = 121 * width

img = img.resize((basewidth, height))

data = np.asarray(img, dtype="int32")[0]

flag = 0

line = -1

line_temp = 0

plt.plot(data)

plt.show()

bit = ''
while True:
    line += 1
    number = data[line][0]
    if flag == 0 and number > 128:
        temp = line % 242
        if temp >= 0 or temp <=10 :
            for n in range(0,int((line - line_temp) / 242)):
                bit += '1'
        elif temp > 232 :
            for n in range(0,int((line - line_temp)/242)+1):
                bit += '1'
        flag = 1
        line_temp = line
    if flag == 1 and number < 128:
        temp = (line - line_temp) % 242
        if temp >= 0 or temp <=10 :
            for n in range(0,int((line - line_temp)/242)):
                bit += '0'
        elif temp > 232 :
            for n in range(0,int((line - line_temp)/242)+1):
                bit += '0'
        flag = 0
        line_temp = line
    if line == basewidth - 1:
        break

print(bit)

CODE128_CHART = """
        0   _   _   00  32   11011001100 212222
        1   !   !   01  33   11001101100 222122
        2   "   "   02  34   11001100110 222221
        3   #   #   03  35   10010011000 121223
        4   $   $   04  36   10010001100 121322
        5   %   %   05  37   10001001100 131222
        6   &   &   06  38   10011001000 122213
        7   ‘   ‘   07  39   10011000100 122312
        8   (   (   08  40   10001100100 132212
        9   )   )   09  41   11001001000 221213
        10  *   *   10  42   11001000100 221312
        11  +   +   11  43   11000100100 231212
        12  ,   ,   12  44   10110011100 112232
        13  -   -   13  45   10011011100 122132
        14  .	.   14  46   10011001110 122231
        15  /	/   15  47   10111001100 113222
        16  0	0   16  48   10011101100 123122
        17  1	1   17  49   10011100110 123221
        18  2	2   18  50   11001110010 223211
        19  3	3   19  51   11001011100 221132
        20  4	4   20  52   11001001110 221231
        21  5	5   21  53   11011100100 213212
        22  6	6   22  54   11001110100 223112
        23  7	7   23  55   11101101110 312131
        24  8	8   24  56   11101001100 311222
        25  9   9   25  57   11100101100 321122
        26  :	:   26  58   11100100110 321221
        27  ;	;   27  59   11101100100 312212
        28  <	<   28  60   11100110100 322112
        29  =	=   29  61   11100110010 322211
        30  >	>   30  62   11011011000 212123
        31  ?	?   31  63   11011000110 212321
        32  @	@   32  64   11000110110 232121
        33  A	A   33  65   10100011000 111323
        34  B	B   34  66   10001011000 131123
        35  C	C   35  67   10001000110 131321
        36  D	D   36  68   10110001000 112313
        37  E	E   37  69   10001101000 132113
        38  F	F   38  70   10001100010 132311
        39  G	G   39  71   11010001000 211313
        40  H	H   40  72   11000101000 231113
        41  I	I   41  73   11000100010 231311
        42  J	J   42  74   10110111000 112133
        43  K	K   43  75   10110001110 112331
        44  L	L   44  76   10001101110 132131
        45  M	M   45  77   10111011000 113123
        46  N	N   46  78   10111000110 113321
        47  O	O   47  79   10001110110 133121
        48  P	P   48  80   11101110110 313121
        49  Q	Q   49  81   11010001110 211331
        50  R	R   50  82   11000101110 231131
        51  S	S   51  83   11011101000 213113
        52  T	T   52  84   11011100010 213311
        53  U	U   53  85   11011101110 213131
        54  V	V   54  86   11101011000 311123
        55  W	W   55  87   11101000110 311321
        56  X	X   56  88   11100010110 331121
        57  Y	Y   57  89   11101101000 312113
        58  Z	Z   58  90   11101100010 312311
        59  [	[   59  91   11100011010 332111
        60  \\	\\   60  92  11101111010 314111
        61  ]	]   61  93   11001000010 221411
        62  ^	^   62  94   11110001010 431111
        63  _	_   63  95   10100110000 111224
        64  NUL	`   64  96   10100001100 111422
        65  SOH	a   65  97   10010110000 121124
        66  STX	b   66  98   10010000110 121421
        67  ETX	c   67  99   10000101100 141122
        68  EOT	d   68  100  10000100110 141221
        69  ENQ	e   69  101  10110010000 112214
        70  ACK	f   70  102  10110000100 112412
        71  BEL	g   71  103  10011010000 122114
        72  BS	h   72  104  10011000010 122411
        73  HT	i   73  105  10000110100 142112
        74  LF	j   74  106  10000110010 142211
        75  VT	k   75  107  11000010010 241211
        76  FF	i   76  108  11001010000 221114
        77  CR	m   77  109  11110111010 413111
        78  SO	n   78  110  11000010100 241112
        79  SI	o   79  111  10001111010 134111
        80  DLE	p   80  112  10100111100 111242
        81  DC1	q   81  113  10010111100 121142
        82  DC2	r   82  114  10010011110 121241
        83  DC3	s   83  115  10111100100 114212
        84  DC4	t   84  116  10011110100 124112
        85  NAK	u   85  117  10011110010 124211
        86  SYN	v   86  118  11110100100 411212
        87  ETB	w   87  119  11110010100 421112
        88  CAN	x   88  120  11110010010 421211
        89  EM	y   89  121  11011011110 212141
        90  SUB	z   90  122  11011110110 214121
        91  ESC	{   91  123  11110110110 412121
        92  FS	|   92  124  10101111000 111143
        93  GS  }   93  125  10100011110 111341
        94  RS  ~   94  126  10001011110 131141
        95  US  DEL 95  127  10111101000 114113
        96  FNC3 FNC3 96 128 10111100010 114311
        97  FNC2 FNC2 97 129 11110101000 411113
        98  SHIFT SHIFT 98 130 11110100010 411311
        99  CODEC CODEC 99 131 10111011110 113141
        100 CODEB FNC4 CODEB 132 10111101110 114131
        101 FNC4 CODEA CODEA 133 11101011110 311141
        102 FNC1 FNC1 FNC1 134 11110101110 411131
        103 Start Start A   208 11010000100 211412
        104 Start Start B   209 11010010000 211214
        105 Start Start C   210 11010011100 211232
        106 Stop Stop   -   -   11000111010 233111""".split()#把字符串变成列表，每个元素以换行或者空格为界

SYMBOLS = [value for value in CODE128_CHART[5::7]]

VALUESC = [value for value in CODE128_CHART[3::7]]
VALUESB = [value for value in CODE128_CHART[2::7]]
VALUESA = [value for value in CODE128_CHART[1::7]]

CODE128C = dict(zip(SYMBOLS, VALUESC))
CODE128B = dict(zip(SYMBOLS, VALUESB))
CODE128A = dict(zip(SYMBOLS, VALUESA))

sym_len = 11

symbols = [bit[i:i+sym_len] for i in range(0, len(bit), sym_len)]

print(symbols)

str_out = ""


print(bit[0:11])

for sym in symbols:

    if bit[0:11] == '11010000100':
        flag_type = 'A'
        if sym != symbols[-2]:
            str_out += CODE128A[sym]
        print("  ", sym, CODE128A[sym])
        continue

    elif bit[0:11] == '11010010000':
        flag_type = 'B'
        if sym != symbols[-2]:
            str_out += CODE128B[sym]
        print("  ", sym, CODE128B[sym])
        continue

    elif bit[0:11] == '11010011100':
        flag_type = "C"
        if sym != symbols[-2]:
            str_out += CODE128C[sym]
        print("  ", sym, CODE128C[sym])
        continue

    if CODE128A[sym] == 'Stop' or CODE128B[sym] == 'Stop' or CODE128A[sym] == '-':

        break

print('数据类型是:CODE128%s'%flag_type)

if flag_type == 'A' or flag_type == 'B':
    print('数据是:' + str_out[5:-6])
elif flag_type == 'C':
    print("数据是:"+ str_out[1:-1])






