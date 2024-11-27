def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp = phi
    while e > 0:
        temp1, temp2 = divmod(temp, e)
        temp, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp == 1:
        return d + phi

def gen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while gcd(e, phi) != 1:
        e += 1
    d = modinv(e, phi)
    return ((e, n), (d, n))

def enc(pk, pt):
    key, n = pk
    cipher = [pow(ord(c), key, n) for c in pt]  # Encrypt character by character
    return cipher

def dec(pk, ct):
    key, n = pk
    plain = [chr(pow(c, key, n)) for c in ct]  # Decrypt and convert back to character
    return "".join(plain)

if __name__ == "__main__":
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    public, private = gen(p, q)
    print("Public Key:", public)
    print("Private Key:", private)
    msg = input("Message: ")
    encc = enc(public, msg)
    print("Encrypted Message:", encc)
    decc = dec(private, encc)
    print("Decrypted Message:", decc)
