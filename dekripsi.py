def text_to_binary(text):
    binary_text = ""
    for char in text:
        binary_char = format(ord(char), '08b')  # Mengonversi karakter menjadi bilangan biner 8-bit
        binary_text += binary_char
    return binary_text

def binary_to_text(binary_text):
    text = ""
    for i in range(0, len(binary_text), 8):
        binary_char = binary_text[i:i+8]
        char = chr(int(binary_char, 2))  # Mengonversi bilangan biner 8-bit menjadi karakter
        text += char
    return text

def decrypt(binary_text, key):
    binary_key = text_to_binary(key)
    
    # Pastikan panjang kunci sama dengan panjang teks terenkripsi
    if len(binary_key) < len(binary_text):
        raise ValueError("Panjang kunci harus sama dengan atau lebih panjang dari panjang teks terenkripsi")
    
    # Dekripsi menggunakan XOR
    decrypted_text = ''.join(['1' if binary_text[i] != binary_key[i] else '0' for i in range(len(binary_text))])
    
    return binary_to_text(decrypted_text)

if __name__ == "__main__":
    # Membaca teks terenkripsi dari file .txt
    with open("cipher_text.txt", "r") as file:
        cipher_text = file.read()
    
    access_key = input("Masukkan kunci akses (panjangnya harus sama dengan teks terenkripsi): ")
    
    decrypted_text = decrypt(cipher_text, access_key)
    print("Teks Terdekripsi: ", decrypted_text)
