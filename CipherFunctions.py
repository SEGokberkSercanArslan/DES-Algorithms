from WordBinaries import *


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
# if iteration = None it tooks lenght of array else it iterates declared number.
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
    print("Stage 5 : Cipher plain binary text file")
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
    print("First XOR operations are complete !")
    print("Left nibble {}".format(left_nibble))
    print("Right nibble {}".format(right_nibble))


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
    print("Second XOR operations are complete !")
    print("Left nibble {}".format(left_nibble))
    print("Right nibble {}".format(right_nibble))
    print("XOR operations complete...")

    #re-produce text togather

    right_counter = 0
    left_counter = 0
    for i in range(len(left_nibble)+len(right_nibble)):
        if i % 2 == 1:
            union_text.append(left_nibble[left_counter])
            left_counter += 1
        else:
            union_text.append(right_nibble[right_counter])
            right_counter += 1
        #union_text.append(right_nibble[i])
        #union_text.append(left_nibble[i])
    print("Reproduction of cipher binary text complete")
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

def TakeInitialPermutationBinaryKey(binary_text=[],key_combination_first="",key_combination_last=""):
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
    print("Stage 1 : Read plain text from file")
    print(plain_text)
    #Call Stage 2
    permuted_plain_text = TakeInitialPermutationString(key_text=plain_text,key_combination="0246813579")
    print("Stage 2 : Take initial Permutation of text for 10 character")
    print(permuted_plain_text)
    #Call Stage 3
    binary_plain_text_data_permuted = ConvertDataToBinaries(data=permuted_plain_text)
    print("Stage 3 : Convert plain text to binary format")
    print(binary_plain_text_data_permuted)
    #Call Stage 4
    binary_plain_text_shifted = EightBitsRightShiftRotate(eight_data=binary_plain_text_data_permuted,shift_ratio=4)
    print("Stage 4 : Perform 8 bit right shift rotate operation for plain binary text")
    print(binary_plain_text_shifted)
    #Call Stage 5
    cipher_text = CipherSequence(shifted_array=binary_plain_text_shifted,cipher_key=key)

    return cipher_text

def DecodeCipher(binary_cipher = [],key = "ru"):
    "Stage 1: Preparing reverse stages"
    print("Preparing required keys and varribles for decipher operation")
    binary_key = ConvertCharacterToBinaries(key=key)
    binary_permuted_key = TakeInitialPermutationBinaryKey(binary_key, "02561374", "01346275")
    binary_permuted_key[0] = EightBitsLeftShiftRotate(binary_permuted_key[0], 3, 1)
    binary_permuted_key[1] = EightBitsRightShiftRotate(binary_permuted_key[1], 5, 1)

    left_nibble = []
    right_nibble= []
    Stage1= TakeInitialPermutationBinaryCipherArray(binary_cipher,"0246813579")
    print("Stage 1 : Initial permutation operations completed !")

    "Separate Nibbles"
    for i in range(len(Stage1)):
        if i %2 == 1:
            left_nibble.append(Stage1[i])
        else :
            right_nibble.append(Stage1[i])
    print("Left and Right nibbles created")

    "Stage 2, Reverse Stages"
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
    print("Stage 2 : Fist reverse XOR operations completed !")

    binary_permuted_key[0]=EightBitsRightShiftRotate(binary_permuted_key[0],3,1)
    binary_permuted_key[1]=EightBitsLeftShiftRotate(binary_permuted_key[1],5,1)
    print("Reverse keys Generated !")

    "Use normal permuted keys now"
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
    print("Stage 3 : Second reverse XOR operations completed !")
    "ReUnion nibbles in a list"
    print("Right nibble :".format(right_nibble))
    print("Left nibble :".format(right_nibble))
    union_nible = []
    right_counter = 0
    left_counter = 0
    for i in range(len(right_nibble+left_nibble)):
        if i % 2 == 1:
            union_nible.append(left_nibble[left_counter])
            left_counter+=1
        else:
            union_nible.append(right_nibble[right_counter])
            right_counter+=1
    print("Stage 4 : List re-created !")
    "Reverse shift operation"
    union_nible = EightBitsLeftShiftRotate(union_nible,4)
    print("Stage 5 : Reverse shift binary operations completed !")
    "Convert binary to characters"
    for i in range(len(union_nible)):
        union_nible[i] = reverse_word_binaries[union_nible[i]]
    "Reverse permutation and deciphered text"
    deciphered_text = ""
    union_string = ""
    for i in range(len(union_nible)):
        union_string += union_nible[i]
    deciphered_text = TakeInitialPermutationString(union_string,"0516273849")
    print("Reverse permutation and binary to character conversation completed !")
    return deciphered_text