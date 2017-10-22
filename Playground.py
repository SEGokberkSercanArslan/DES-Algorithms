from CipherFunctions import EightBitsLeftShiftRotate,EightBitsRightShiftRotate

binary= "11010011"
binary1 = EightBitsRightShiftRotate(binary,4,1)
print(binary1)
binary2 = EightBitsLeftShiftRotate(binary1,4,1)
print(binary2)
print("Main binary")
print(binary)