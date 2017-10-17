from CipherFunctions import *

reading = ReadFromFile("tmp.txt")
print(len(reading.split()))
permuted = TakeInitialPermutationString(key_text=reading,key_combination="0246813579")
print(permuted)
print("Len of permuted {}".format(len(permuted)))
bin_dat = ConvertDataToBinaries(permuted)
print(bin_dat)
shift_bin = EightBitsRightShiftRotate(eight_data=bin_dat,shift_ratio=4)
print("---------------")
print(shift_bin)
# print(len(bin_dat))
# CipherText(text_binary=bin_dat,key="ka")