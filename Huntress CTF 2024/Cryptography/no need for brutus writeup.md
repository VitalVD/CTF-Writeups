# Challenge Name: No Need for Brutus

**Category:** Cryptography  
**CTF Event:** Huntress CTF 2024    
**Points:** 50 Points

## Challenge Description
A simple message for you to decipher:

squiqhyiiycfbudeduutvehrhkjki

Submit the original plaintext hashed with MD5, wrapped between the usual flag format: flag{}

Ex: If the deciphered text is "hello world", the MD5 hash would be 5eb63bbbe01eeed093cb22bb8f5acdc3, and the flag would be flag{5eb63bbbe01eeed093cb22bb8f5acdc3}.

## Solve

 Python script that will try all possible Caesar cipher shifts (0 to 25) on the given ciphertext and print out all the possible results. This way, you can easily see which shift produces the meaningful plaintext.

 **Python Script:**
```
# Function to apply Caesar cipher decryption
def caesar_decrypt(cipher_text, shift):
    decrypted = []
    for char in cipher_text:
        if char.isalpha():
            # Decrypt character with the given shift and wrap around the alphabet
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted.append(shifted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Cipher text provided
cipher_text = "squiqhyiiycfbudeduutvehrhkjki"

# Trying all possible shifts (0 to 25)
for shift in range(26):
    decrypted_text = caesar_decrypt(cipher_text, shift)
    print(f"Shift {shift}: {decrypted_text}")
```



**Output:**
```
Shift 0: squiqhyiiycfbudeduutvehrhkjki
Shift 1: rpthpgxhhxbeatcdcttsudgqgjijh
Shift 2: qosgofwggwadzsbcbssrtcfpfihig
Shift 3: pnrfnevffvzcyrabarrqsbeoehghf
Shift 4: omqemdueeuybxqzazqqpradndgfge
Shift 5: nlpdlctddtxawpyzyppoqzcmcfefd
Shift 6: mkockbsccswzvoxyxoonpyblbedec
Shift 7: ljnbjarbbrvyunwxwnnmoxakadcdb
Shift 8: kimaizqaaquxtmvwvmmlnwzjzcbca
Shift 9: jhlzhypzzptwsluvullkmvyiybabz
Shift 10: igkygxoyyosvrktutkkjluxhxazay
Shift 11: hfjxfwnxxnruqjstsjjiktwgwzyzx
Shift 12: geiwevmwwmqtpirsriihjsvfvyxyw
Shift 13: fdhvdulvvlpsohqrqhhgirueuxwxv
Shift 14: ecguctkuukorngpqpggfhqtdtwvwu
Shift 15: dbftbsjttjnqmfopoffegpscsvuvt
Shift 16: caesarissimplenoneedforbrutus
Shift 17: bzdrzqhrrhlokdmnmddcenqaqtstr
Shift 18: aycqypgqqgknjclmlccbdmpzpsrsq
Shift 19: zxbpxofppfjmibklkbbacloyorqrp
Shift 20: ywaowneooeilhajkjaazbknxnqpqo
Shift 21: xvznvmdnndhkgzijizzyajmwmpopn
Shift 22: wuymulcmmcgjfyhihyyxzilvlonom
Shift 23: vtxltkbllbfiexghgxxwyhkuknmnl
Shift 24: uswksjakkaehdwfgfwwvxgjtjmlmk
Shift 25: trvjrizjjzdgcvefevvuwfisilklj
```


**Shift 16: caesarissimplenoneedforbrutus**


Once we deciphered the text to "caesarissimplenoneedforbrutus", it became clear that this was a reference to Julius Caesar, the namesake of the Caesar cipher. The phrase humorously suggests that the Caesar cipher is so simple that no betrayal by "Brutus" is needed.


### Generating the MD5 Hash

```
import hashlib
plaintext = "caesarissimplenoneedforbrutus"
hashed = hashlib.md5(plaintext.encode()).hexdigest()
print(f"flag{{{hashed}}}")
```


**Output: flag{c945bb2173e7da5a292527bbbc825d3f}**


Thus the flag is:-

**flag{c945bb2173e7da5a292527bbbc825d3f}**
