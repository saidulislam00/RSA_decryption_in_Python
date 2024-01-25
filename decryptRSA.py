#functions to calculate private key
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

#get the values
e = int(input("Enter public exponent: "))
phi = int(input("Enter phi value: "))
p= int(input("Enter the first prime number P: "))
message = int(input("Enter the cipher text: "))

# Calculate private key d, second prime num. q and n
d = modinv(e, phi)
q = (phi // (p - 1)) + 1
n = p * q

#find the decrypted message
decrypted_message = pow(message, d, n)

# integer to text convertion
def int_to_bytes(integer):
    byte_array = integer.to_bytes((integer.bit_length() + 7) // 8, 'big')
    return byte_array
text_result = int_to_bytes(decrypted_message).decode('utf-8')
print("\nDecrypted Message (Text):", text_result)