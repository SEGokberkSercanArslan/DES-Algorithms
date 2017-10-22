from CipherFunctions import EightBitsLeftShiftRotate,EightBitsRightShiftRotate

binary= "11010011"
print(binary)
lsr = EightBitsLeftShiftRotate(binary,3,1)
print(lsr)
rsr = EightBitsRightShiftRotate(lsr,3,1)
print(rsr)