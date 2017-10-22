from WordBinaries import *

#Notları bu kısıma al ve çalışmaya hazır hale getir
#Stage 1 Reading data düz string olarak veriyi çıkarıyor arada boşluklar var array değil
#DefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefaultDefault Default  Default
#Stage 2 text permüte edilmiş durumda ve düz string formunda hala
#Stage 3 de artık 8 bit uzunluğunda her bir elemanı olan array çıkıyor
#Stage 4 her bir elemanı 8 bit uzunluğunda ve shiftlenmiş olarak duruyor
#


# Return string of reading elements
# Stage 1
def ReadFromFile(file_name="default.txt"):
    data = ""
    full_str = ""
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
        data = list(filter(None,data))
        for i in range(len(data)):
            data[i] = data[i].split()
        for i in range(len(data)):
            for i2 in range(len(data[i])):
                full_str += data[i][i2]
    print("Reading data from file completed\n")
    return full_str

# Return String which contain permutation
# Stage 2
def TakeInitialPermutationString(key_text="", key_combination="0123456789"):
    Number_of_iterations = len(key_text)
    permuted_text = []

    if Number_of_iterations%10 == 0 :
        for i in range(Number_of_iterations//10):
            for i2 in range(10):
                position = int(key_combination[i2])
                permuted_text.append(key_text[10 * i + position])
        print("10 Block Character data permuted \n")

    else :
        lenght_text = (10-(len(key_text)%10))
        key_text += backup_words[0:lenght_text]
        for i in range((Number_of_iterations//10)+1):
            for i2 in range(10):
                position = int(key_combination[i2])
                permuted_text.append(key_text[(10 * i) + position])

    print("10 Block Character data permuted \n")

    return "".join(permuted_text)

def TakeInitialPermutationBinaryCipherArray(cipher_array=[],key_combination="0123456789"):
    permuted_cipher_text = []
    for i in range(len(cipher_array)//10):
        for i2 in range(10):
            permuted_cipher_text.append(cipher_array[int(key_combination[i2])+(i*10)])
    return permuted_cipher_text

# Returns array of binary_data
#Düz string için değil array için düzenlenmiş revizyona git
# Stage 3
def ConvertDataToBinaries(data=""):
    binary_data =[]
    for i in range(len(data)):
        try:
            binary_data.append(word_binaries[data[i]])
        except:
            binary_data.append(capital_word_binaries[data[i]])
    print("Character data converted to binary format\n")
    return binary_data

# Right Shift rotate 8 bit binaries
# Stage 4
def EightBitsRightShiftRotate(eight_data=[],shift_ratio=None,iteration=None):
    shift_list = []
    if iteration == None:
        for i in range (len(eight_data)):
            eight_bit_string = ""
            for i2 in range(8):
                eight_bit_string += "".join(str(eight_data[i][((i2+shift_ratio))%8]))
            shift_list.append(eight_bit_string)
        print("Right Shift Rotate Complete")
        return shift_list
    else: #True, only if shift key attribute
        for i in range(iteration):
            eight_bit_string = ""
            for i2 in range(8):
                eight_bit_string += "".join(str(eight_data[((i2 + shift_ratio)) % 8]))
        print("Right Shift Rotate Complete")
        return eight_bit_string


#Left shift rotate 8 bit binaries
#Düzeltildi
def EightBitsLeftShiftRotate(eight_data=[],shift_ratio=None,iteration=None):
    shift_list = []
    if iteration == None:
        for i in range(len(eight_data)):
            eight_bit_string = ""
            for i2 in range(8):
                eight_bit_string += "".join(str(eight_data[i][((i2 - shift_ratio)) % 8]))
            shift_list.append(eight_bit_string)
        print("Left Shift Rotate Complete")
        return shift_list
    else: #True, only if shift key attribute
        for i in range(iteration):
            eight_bit_string = ""
            for i2 in range(8):
                eight_bit_string += "".join(str(eight_data[((i2 - shift_ratio)) % 8]))
        print("Left Shift Rotate Complete")
        return eight_bit_string

# Stage 5
def CipherSequence(shifted_array=[],cipher_key=""):
    left_nibble  = []
    right_nibble = []
    union_text = []
    binary_key = ""
    #Even right odd left
    for i in range (len(shifted_array)):
        if i % 2 == 1:
            left_nibble.append(shifted_array[i])
        else :
            right_nibble.append(shifted_array[i])
    binary_key = ConvertCharacterToBinaries(key=cipher_key)
    binary_permuted_key = TakeInitialPermutationBinaryKey(binary_key,"02561374","01346275")
    #First XOR step
    for i in range(len(left_nibble)):
        xor_bit = ""
        for i2 in range(8):
            xor_bit += str(int(left_nibble[i][i2])^int(binary_permuted_key[1][i2]))
        left_nibble[i] = xor_bit
    for i in range(len(right_nibble)):
        xor_bit = ""
        for i2 in range(8):
            xor_bit += str(int(right_nibble[i][i2])^int(binary_permuted_key[0][i2]))
        right_nibble[i] = xor_bit

    print("New key generations started ")
    binary_permuted_key[0] = EightBitsLeftShiftRotate(binary_permuted_key[0],3,1)
    binary_permuted_key[1] = EightBitsRightShiftRotate(binary_permuted_key[1],5,1)
    print("New key generations complete !")

    #Second XOR operations
    for i in range(len(left_nibble)):
        xor_bit = ""
        for i2 in range(8):
            xor_bit += str(int(left_nibble[i][i2]) ^ int(binary_permuted_key[0][i2]))
        left_nibble[i] = xor_bit
    for i in range(len(right_nibble)):
        xor_bit = ""
        for i2 in range(8):
            xor_bit += str(int(right_nibble[i][i2]) ^ int(binary_permuted_key[1][i2]))
        right_nibble[i] = xor_bit
    print("XOR operations complete...")
    #re-produce text togather
    for i in range(len(left_nibble)):
        union_text.append(right_nibble[i])
        union_text.append(left_nibble[i])
    print(union_text)
    return union_text


#Returns Array which has two elements, each elements contain 8 bit data of key
#['00010101', '00011001']
def ConvertCharacterToBinaries(key=""):
    binary_data = []
    for i in range(len(key)):

        try:
            binary_data.append(word_binaries[key[i]])

        except:
            binary_data.append(capital_word_binaries[key[i]])

    print("2 Character key converted binary format\n")
    return binary_data

def TakeInitialPermutationBinaryKey(binary_text=[],key_combination_first="02461357",key_combination_last="13570246"):
    permutation_array = []
    for i in range(2):
        permutation_string = ""
        for i2 in range(8):
            if i == 0 :
                position = int(key_combination_first[i2])
                permutation_string += binary_text[i][position]
            else:
                position = int(key_combination_last[i2])
                permutation_string += binary_text[i][position]
        permutation_array.append(permutation_string)
    return permutation_array

"Main Cipher Functions"
def CipherTextNew(file_name = "Default.txt",key="ru",):
    "String Var"
    plain_text = ""
    permuted_plain_text = ""
    cipher_text = ""
    "Array Var"
    binary_plain_text_data_permuted = []
    binary_plain_text_shifted = []


    #Call Stage 1
    plain_text = ReadFromFile(file_name=file_name)

    #Call Stage 2
    permuted_plain_text = TakeInitialPermutationString(key_text=plain_text,key_combination="0246813579")

    #Call Stage 3
    binary_plain_text_data_permuted = ConvertDataToBinaries(data=permuted_plain_text)

    #Call Stage 4
    binary_plain_text_shifted = EightBitsRightShiftRotate(eight_data=binary_plain_text_data_permuted,shift_ratio=4)

    #Call Stage 5
    cipher_text = CipherSequence(shifted_array=binary_plain_text_shifted,cipher_key=key)

    return cipher_text

def DecodeCipher(binary_cipher = [],key = "ru"):
    "Stage 1: Preparing reverse stages"
    key = ConvertCharacterToBinaries(key)
    key_permuted = TakeInitialPermutationBinaryKey(key,key_combination_first="02461357",key_combination_last="13570246")
    key_1_left   = key_permuted[0]
    key_2_right  = key_permuted[1]
    key_1_left_shifted =EightBitsLeftShiftRotate(key_1_left,3,1)
    key_2_right_shifted=EightBitsRightShiftRotate(key_2_right,5,1)
    left_nible = []
    right_nible= []
    Stage1= TakeInitialPermutationBinaryCipherArray(binary_cipher,"0246813579")
    for i in range(len(Stage1)):
        if i %2 == 1:
            left_nible.append(Stage1[i])
        else :
            right_nible.append(Stage1[i])
    "Stage 2, Reverse Stages"



    return Stage1