from CipherFunctions import *

print("Cipher Text Started")
sec2 = CipherTextNew(file_name="mailm.txt",key="rm")
print("Final Inverse Permutation Cipher Text Under the Line")
inv_per = TakeInitialPermutationBinaryCipherArray(sec2,"0516273849")
print(inv_per)
print("Cipher Text Finished")

print("Decode started")
decode_stage = DecodeCipher(inv_per,"rm")
print(decode_stage)

#print("Last stage inverse permutation started..")
#print(inv_per)
#inv_per = TakeInitialPermutationBinaryCipherArray(inv_per,"0246813579")
#print("Final Inverse permutation Complete !!")
#decoded_cipher = DecodeCipher(inv_per,"rm")
#print(decoded_cipher)