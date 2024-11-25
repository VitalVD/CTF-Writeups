# Challenge Name:- Too Many Bits

**Category:** Warmups    
**CTF Event:** Huntress CTF 2024    
**Points:** 50 Points


## Challenge Description
Don't believe everything you see on the Internet!

Anyway, have you heard this intro soundtrack from Half-Life 3?


## Solve 

This challenge had a download attachment that was Half-Life_3_OST.mp3. So the flag is hidden in this .mp3 file. 

I tried writing a python code to solve this challenge and it worked. 

**Python Code:-**
```
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import os

def check_mp3_metadata(file_path):
    try:
        # Load the MP3 file and read its metadata (ID3 tags)
        audio = MP3(file_path, ID3=ID3)
        metadata = {}

        # Extract metadata (ID3 tags) if available
        for tag in audio.tags.values():
            metadata[tag.FrameID] = tag.text

        if metadata:
            print("Metadata found in the MP3 file:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("No metadata found in the MP3 file.")
        return metadata
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None

def inspect_file_signature(file_path):
    try:
        # Open the file in binary mode to inspect its raw content
        with open(file_path, 'rb') as file:
            file_content = file.read()

        # Check the first few bytes (file signature/magic bytes)
        file_signature = file_content[:8]
        return file_signature, file_content
    except Exception as e:
        print(f"Error reading file signature: {e}")
        return None, None

def extract_png_from_mp3(file_content, output_path):
    try:
        # Save the raw PNG data to a new file
        with open(output_path, 'wb') as png_file:
            png_file.write(file_content)
        print(f"PNG file extracted and saved to: {output_path}")
    except Exception as e:
        print(f"Error saving PNG file: {e}")

def main():
    # Path to the MP3 file provided by the user
    mp3_file_path = "Half-Life_3_OST.mp3"
    
    # Step 1: Check MP3 metadata
    print("Checking MP3 metadata...")
    metadata = check_mp3_metadata(mp3_file_path)

    # Step 2: Inspect file signature
    print("\nInspecting file signature...")
    file_signature, file_content = inspect_file_signature(mp3_file_path)

    if file_signature:
        print(f"File signature: {file_signature}")
        
        # Step 3: Check if the file is actually a PNG based on the signature
        if file_signature.startswith(b'\x89PNG'):
            print("File is a PNG image disguised as an MP3.")
            
            # Define the path for the extracted PNG
            extracted_png_path = "extracted_image.png"
            
            # Step 4: Extract the PNG image from the MP3 file
            extract_png_from_mp3(file_content, extracted_png_path)
        else:
            print("File is not a PNG image.")
    else:
        print("Could not inspect file signature.")

if __name__ == "__main__":
    main()
```


**Output:-** 

```
python solve.py
Checking MP3 metadata...
Error reading metadata: can't sync to MPEG frame

Inspecting file signature...
File signature: b'\x89PNG\r\n\x1a\n'
File is a PNG image disguised as an MP3.
Error saving PNG file: [Errno 2] No such file or directory: '/mnt/data/extracted_image.png'

H:\solve>python solve.py
Checking MP3 metadata...
Error reading metadata: can't sync to MPEG frame

Inspecting file signature...
File signature: b'\x89PNG\r\n\x1a\n'
File is a PNG image disguised as an MP3.
PNG file extracted and saved to: extracted_image.png
```


**The flag that I found inside extracted_image.png was:-** flag{a85466991f0a8dc3d9837a5c32fa0c91}


Thus, the flag is:- 

**flag{a85466991f0a8dc3d9837a5c32fa0c91}**



