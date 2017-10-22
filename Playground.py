from CipherFunctions import EightBitsLeftShiftRotate,EightBitsRightShiftRotate

binary= "011010011"
print("First Binary = {}".format(binary))
binaryl = EightBitsLeftShiftRotate(binary,3,1)
print("Left Shift 3:{}".format(binary))
for i in range(8):
    binaryr = EightBitsRightShiftRotate(binaryl,i,1)
    if binaryr == binary:
        print("Matched combination : {}".format(i))