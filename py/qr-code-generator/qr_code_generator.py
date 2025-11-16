"""
QR Code Generator
A simple tool to generate QR codes from text or URLs.
"""

import qrcode
import os


def generate_qr_code(data, filename):
    """Generate a QR code from the given data and save it to a file."""
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
            error_correction=qrcode.constants.ERROR_CORRECT_L
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        image = qr.make_image(fill_color="black", back_color="white")
        
        # Ensure filename has .png extension
        if not filename.lower().endswith('.png'):
            filename += '.png'
        
        image.save(filename)
        print(f"✅ QR code saved as '{filename}'")
        return True
    except Exception as e:
        print(f"❌ Error generating QR code: {e}")
        return False


def main():
    """Main function to run the QR code generator."""
    print("=" * 50)
    print("QR Code Generator")
    print("=" * 50)
    
    data = input("\nEnter the text or URL: ").strip()
    if not data:
        print("❌ Error: No input provided.")
        return
    
    filename = input("Enter the file name (without extension): ").strip()
    if not filename:
        filename = "qrcode"
    
    if generate_qr_code(data, filename):
        # Check if file exists and show its location
        if os.path.exists(filename if filename.endswith('.png') else f"{filename}.png"):
            file_path = os.path.abspath(filename if filename.endswith('.png') else f"{filename}.png")
            print(f"📁 File location: {file_path}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
