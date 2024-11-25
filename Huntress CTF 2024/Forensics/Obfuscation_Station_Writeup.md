
# Obfuscation Station - CTF Write-up

## Challenge Name: Obfuscation Station  
**Category:** Forensics

---

### Description:
You've reached the Obfuscation Station!
Can you decode this PowerShell to find the flag?
Archive password: infected-station

---

## Step-by-Step Solution:

### 1. Understanding the Obfuscated PowerShell Script:
The provided PowerShell script uses a combination of Base64 encoding, compression, and string manipulation to hide the flag. Here’s the original script:

```powershell
(nEW-objECt  SYstem.iO.COMPreSsIon.deFlaTEStREAm( 
[IO.mEmORYstreAM][coNVERt]::FROMBAse64sTRING( 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA') ,
[io.COmPREssioN.coMpreSSioNmODE]::DeCoMpReSS) | 
%{ nEW-objECt  sYStEm.Io.StREAMrEADeR($_,[TeXT.encodiNG]::AsCii)} | 
%{ $_.READTOENd()}) | & ( $eNV:cOmSPEc[4,15,25]-JOin'')
```

---

### 2. Analyzing the Script:

- **`[convert]::FromBase64String`**: This method decodes the given Base64 string.
- **`System.IO.Compression.DeflateStream`**: This decompresses the data using the Deflate algorithm.
- **`System.IO.StreamReader`**: The decompressed data is then read as a string in ASCII format.

The key part of the script is the Base64 string `'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'`. We need to decode and decompress this string to get the hidden flag.

---

### 3. Base64 Decoding and Decompression:

- The first step is to **Base64 decode** the string. This will convert it to binary data.
- The second step is to **decompress** the binary data using the Deflate algorithm. In PowerShell, this is done using `DeflateStream`. In Python, we can achieve the same result using the `zlib` module with the `MAX_WBITS` flag set to `-15`, which handles raw deflate data.

---

### 4. Python Script:

To solve this challenge, we used the following Python script to automate the process of decoding and decompressing the data.

```python
import base64
import zlib

# Base64 encoded string from the PowerShell script
base64_string = 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'

# Step 1: Base64 decode
compressed_data = base64.b64decode(base64_string)

# Step 2: Decompress the data using zlib
# Since DeflateStream is used in the PowerShell script, we use -zlib.MAX_WBITS to decompress
decompressed_data = zlib.decompress(compressed_data, -zlib.MAX_WBITS)

# Step 3: Convert the decompressed data to readable ASCII
result = decompressed_data.decode('ascii')

# Step 4: Print the result, which contains the flag
print(result)
```

---

### 5. Extracting the Flag:
After running the script, the output reveals the flag:

```
$5GMLW = "flag{3ed675ef0343149723749c34fa910ae4}"
```

Thus, the flag is:

**flag{3ed675ef0343149723749c34fa910ae4}**

---

