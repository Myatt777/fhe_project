from Pyfhel import Pyfhel


HE = Pyfhel()
HE.contextGen(p=65537, m=4096)  # Generate context with specific parameters
HE.keyGen()  # Generate key pair


plain_num = 123
encrypted_num = HE.encryptFrac(plain_num)


encrypted_result = encrypted_num + encrypted_num


decrypted_result = HE.decryptFrac(encrypted_result)
print(f"Original: {plain_num}, Decrypted Result: {decrypted_result}")
