from PIL import Image

# XOR encryption/decryption
def xor_encrypt_decrypt(image, key):
    pixels = image.load()  # Load the image pixels
    width, height = image.size  # Get the dimensions of the image
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Get the RGB values of the pixel
            
            # XOR the RGB values with the key
            r = r ^ key
            g = g ^ key
            b = b ^ key
            
            # Set the new XORed RGB values back to the pixel
            pixels[i, j] = (r, g, b)
    
    return image

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    
    # Encrypt the image using XOR encryption
    encrypted_image = xor_encrypt_decrypt(image, key)
    
    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved at {output_image_path}")

# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    
    # Decrypt the image using XOR decryption (same as encryption)
    decrypted_image = xor_encrypt_decrypt(image, key)
    
    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved at {output_image_path}")

# Main program
if __name__ == "__main__":
    # User input for image path, output path, and XOR key
    input_image_path = input("Enter the path of the image to encrypt: ")
    output_encrypted_image_path = input("Enter the path to save the encrypted image: ")
    output_decrypted_image_path = input("Enter the path to save the decrypted image: ")
    key = int(input("Enter the XOR key (integer): "))
    
    # Encrypt the image
    encrypt_image(input_image_path, output_encrypted_image_path, key)
    
    # Decrypt the image (using the same key)
    decrypt_image(output_encrypted_image_path, output_decrypted_image_path, key)
