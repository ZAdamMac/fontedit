##
##    This file is part of Fontedit.
##    Copyright 2010-2020 Nathan Dumont
##
##    Fontedit is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    Fontedit is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Fontedit.  If not, see <http://www.gnu.org/licenses/>.
##

asc_char = ['?'] * 256
for i in range(32, 128):
  asc_char[i] = chr(i)

asc_desc = ['NULL'] * 256

asc_desc[0] = "Null"
asc_desc[1] = "Start of header"
asc_desc[2] = "Start of text"
asc_desc[3] = "End of text"
asc_desc[4] = "End of transmission"
asc_desc[5] = "Enquiry"
asc_desc[6] = "Acknowledgement"
asc_desc[7] = "Bell"
asc_desc[8] = "Backspace"
asc_desc[9] = "Tab"
asc_desc[10] = "Line feed"
asc_desc[11] = "Vertical tab"
asc_desc[12] = "Form feed"
asc_desc[13] = "Carriage return"
asc_desc[14] = "Shift out"
asc_desc[15] = "Shift in"
asc_desc[16] = "Sata link escape"
asc_desc[17] = "XON"
asc_desc[18] = "Device control 2"
asc_desc[19] = "XOFF"
asc_desc[20] = "Device control 4"
asc_desc[21] = "Negative acknowledge"
asc_desc[22] = "Synchronous idle"
asc_desc[23] = "End of transmission block"
asc_desc[24] = "Cancel"
asc_desc[25] = "End of medium"
asc_desc[26] = "Substitute"
asc_desc[27] = "Escape"
asc_desc[28] = "File separator"
asc_desc[29] = "Group separator"
asc_desc[30] = "Record separator"
asc_desc[31] = "Unit separator"
asc_desc[32] = "Space" #  
asc_desc[33] = "Exclamation mark" # !
asc_desc[34] = "Double quote" # "
asc_desc[35] = "Octalthorpe" # #
asc_desc[36] = "Dollar" # $
asc_desc[37] = "Percent" # %
asc_desc[38] = "Ampersand" # &
asc_desc[39] = "Single quote" # '
asc_desc[40] = "Open bracket" # (
asc_desc[41] = "Close bracket" # )
asc_desc[42] = "Star" # *
asc_desc[43] = "Plus" # +
asc_desc[44] = "Comma" # ,
asc_desc[45] = "Dash" # -
asc_desc[46] = "Full stop" # .
asc_desc[47] = "Forward slash" # /
asc_desc[48] = "Zero" # 0
asc_desc[49] = "One" # 1
asc_desc[50] = "Two" # 2
asc_desc[51] = "Three" # 3
asc_desc[52] = "Four" # 4
asc_desc[53] = "Five" # 5
asc_desc[54] = "Six" # 6
asc_desc[55] = "Seven" # 7
asc_desc[56] = "Eight" # 8
asc_desc[57] = "Nine" # 9
asc_desc[58] = "Colon" # :
asc_desc[59] = "Semi-colon" # ;
asc_desc[60] = "Less than" # <
asc_desc[61] = "Equals" # =
asc_desc[62] = "Greater than" # >
asc_desc[63] = "Question mark" # ?
asc_desc[64] = "At" # @
asc_desc[65] = "" # A
asc_desc[66] = "" # B
asc_desc[67] = "" # C
asc_desc[68] = "" # D
asc_desc[69] = "" # E
asc_desc[70] = "" # F
asc_desc[71] = "" # G
asc_desc[72] = "" # H
asc_desc[73] = "" # I
asc_desc[74] = "" # J
asc_desc[75] = "" # K
asc_desc[76] = "" # L
asc_desc[77] = "" # M
asc_desc[78] = "" # N
asc_desc[79] = "" # O
asc_desc[80] = "" # P
asc_desc[81] = "" # Q
asc_desc[82] = "" # R
asc_desc[83] = "" # S
asc_desc[84] = "" # T
asc_desc[85] = "" # U
asc_desc[86] = "" # V
asc_desc[87] = "" # W
asc_desc[88] = "" # X
asc_desc[89] = "" # Y
asc_desc[90] = "" # Z
asc_desc[91] = "Open square bracket" # [
asc_desc[92] = "Backslash" # \
asc_desc[93] = "Close square bracket" # ]
asc_desc[94] = "Carret" # ^
asc_desc[95] = "Underscore" # _
asc_desc[96] = "Angled single quote" # `
asc_desc[97] = "" # a
asc_desc[98] = "" # b
asc_desc[99] = "" # c
asc_desc[100] = "" # d
asc_desc[101] = "" # e
asc_desc[102] = "" # f
asc_desc[103] = "" # g
asc_desc[104] = "" # h
asc_desc[105] = "" # i
asc_desc[106] = "" # j
asc_desc[107] = "" # k
asc_desc[108] = "" # l
asc_desc[109] = "" # m
asc_desc[110] = "" # n
asc_desc[111] = "" # o
asc_desc[112] = "" # p
asc_desc[113] = "" # q
asc_desc[114] = "" # r
asc_desc[115] = "" # s
asc_desc[116] = "" # t
asc_desc[117] = "" # u
asc_desc[118] = "" # v
asc_desc[119] = "" # w
asc_desc[120] = "" # x
asc_desc[121] = "" # y
asc_desc[122] = "" # z
asc_desc[123] = "Open brace" # {
asc_desc[124] = "Pipe" # |
asc_desc[125] = "Close brace" # }
asc_desc[126] = "Tilde" # ~
asc_desc[127] = "Delete"
asc_desc[128] = ""
asc_desc[129] = ""
asc_desc[130] = ""
asc_desc[131] = ""
asc_desc[132] = ""
asc_desc[133] = ""
asc_desc[134] = ""
asc_desc[135] = ""
asc_desc[136] = ""
asc_desc[137] = ""
asc_desc[138] = ""
asc_desc[139] = ""
asc_desc[140] = ""
asc_desc[141] = ""
asc_desc[142] = ""
asc_desc[143] = ""
asc_desc[144] = ""
asc_desc[145] = ""
asc_desc[146] = ""
asc_desc[147] = ""
asc_desc[148] = ""
asc_desc[149] = ""
asc_desc[150] = ""
asc_desc[151] = ""
asc_desc[152] = ""
asc_desc[153] = ""
asc_desc[154] = ""
asc_desc[155] = ""
asc_desc[156] = ""
asc_desc[157] = ""
asc_desc[158] = ""
asc_desc[159] = ""
asc_desc[160] = ""
asc_desc[161] = ""
asc_desc[162] = ""
asc_desc[163] = ""
asc_desc[164] = ""
asc_desc[165] = ""
asc_desc[166] = ""
asc_desc[167] = ""
asc_desc[168] = ""
asc_desc[169] = ""
asc_desc[170] = ""
asc_desc[171] = ""
asc_desc[172] = ""
asc_desc[173] = ""
asc_desc[174] = ""
asc_desc[175] = ""
asc_desc[176] = ""
asc_desc[177] = ""
asc_desc[178] = ""
asc_desc[179] = ""
asc_desc[180] = ""
asc_desc[181] = ""
asc_desc[182] = ""
asc_desc[183] = ""
asc_desc[184] = ""
asc_desc[185] = ""
asc_desc[186] = ""
asc_desc[187] = ""
asc_desc[188] = ""
asc_desc[189] = ""
asc_desc[190] = ""
asc_desc[191] = ""
asc_desc[192] = ""
asc_desc[193] = ""
asc_desc[194] = ""
asc_desc[195] = ""
asc_desc[196] = ""
asc_desc[197] = ""
asc_desc[198] = ""
asc_desc[199] = ""
asc_desc[200] = ""
asc_desc[201] = ""
asc_desc[202] = ""
asc_desc[203] = ""
asc_desc[204] = ""
asc_desc[205] = ""
asc_desc[206] = ""
asc_desc[207] = ""
asc_desc[208] = ""
asc_desc[209] = ""
asc_desc[210] = ""
asc_desc[211] = ""
asc_desc[212] = ""
asc_desc[213] = ""
asc_desc[214] = ""
asc_desc[215] = ""
asc_desc[216] = ""
asc_desc[217] = ""
asc_desc[218] = ""
asc_desc[219] = ""
asc_desc[220] = ""
asc_desc[221] = ""
asc_desc[222] = ""
asc_desc[223] = ""
asc_desc[224] = ""
asc_desc[225] = ""
asc_desc[226] = ""
asc_desc[227] = ""
asc_desc[228] = ""
asc_desc[229] = ""
asc_desc[230] = ""
asc_desc[231] = ""
asc_desc[232] = ""
asc_desc[233] = ""
asc_desc[234] = ""
asc_desc[235] = ""
asc_desc[236] = ""
asc_desc[237] = ""
asc_desc[238] = ""
asc_desc[239] = ""
asc_desc[240] = ""
asc_desc[241] = ""
asc_desc[242] = ""
asc_desc[243] = ""
asc_desc[244] = ""
asc_desc[245] = ""
asc_desc[246] = ""
asc_desc[247] = ""
asc_desc[248] = ""
asc_desc[249] = ""
asc_desc[250] = ""
asc_desc[251] = ""
asc_desc[252] = ""
asc_desc[253] = ""
asc_desc[254] = ""
asc_desc[255] = ""


if __name__ == "__main__":
  for i in range(256):
    print(asc_char[i], end='')
    print(asc_desc[i])
