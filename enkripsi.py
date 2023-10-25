def text_to_binary(text):
    binary_text = ""
    for char in text:
        binary_char = format(ord(char), '08b')  # Mengonversi karakter menjadi bilangan biner 8-bit
        binary_text += binary_char
    return binary_text

def encrypt(text, key):
    binary_text = text_to_binary(text)
    binary_key = text_to_binary(key)
    
    # Pastikan panjang kunci sama dengan panjang teks
    if len(binary_key) < len(binary_text):
        raise ValueError("Panjang kunci harus sama dengan atau lebih panjang dari panjang teks")
    
    # Enkripsi menggunakan XOR
    encrypted_text = ''.join(['1' if binary_text[i] != binary_key[i] else '0' for i in range(len(binary_text))])
    
    return encrypted_text

if __name__ == "__main__":
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    access_key = input("Masukkan kunci akses (panjangnya harus sama dengan teks): ")
    
    cipher_text = encrypt(plain_text, access_key)
    print("Teks Terenkripsi (dalam biner): ", cipher_text)
    
    # Simpan teks terenkripsi ke dalam file .txt
    with open("cipher_text.txt", "w") as file:
        file.write(cipher_text)

    print("Teks Terenkripsi telah disimpan dalam 'cipher_text.txt'.")
