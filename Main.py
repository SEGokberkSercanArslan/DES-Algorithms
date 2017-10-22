from CipherFunctions import *

print("Cipher Text Started")
sec2 = CipherTextNew(file_name="mailm.txt",key="rm")

print("Final Inverse Permutation Cipher Text Under the Line")
inv_per = TakeInitialPermutationBinaryCipherArray(sec2,"0516273849")
cipher_file = open("cipher.txt","w")
cipher_file.writelines(inv_per)
cipher_file.close()
print(inv_per)
print("Cipher Text Finished")



"Decode Section"
print("Decode started")
decode_stage = DecodeCipher(inv_per,"rm")
decoded_txt = open("decoded.txt","w")
decoded_txt.write(decode_stage)
decoded_txt.close()
print(decode_stage)