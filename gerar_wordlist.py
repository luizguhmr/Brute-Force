from itertools import product

tudo = ["a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
"ç",
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V",
"W",
"X",
"Y",
"Z",
"Ç",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9"]

permsList1 = [''.join(x) for x in product(tudo, repeat=1)]
permsList2 = [''.join(x) for x in product(tudo, repeat=2)]
permsList3 = [''.join(x) for x in product(tudo, repeat=3)]

arquivo = open("wordlist.txt", "a")
for x in range(len(permsList1)):
    arquivo.write(str(permsList1[x]) + str("\n"))
for x in range(len(permsList2)):
    arquivo.write(str(permsList2[x]) + str("\n"))
for x in range(len(permsList3)):
    arquivo.write(str(permsList3[x]) + str("\n"))

print("Wordlist gerada.")