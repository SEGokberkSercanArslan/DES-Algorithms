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