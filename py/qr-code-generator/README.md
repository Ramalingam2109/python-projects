# 📱 QR Code Generator

A simple and efficient tool to generate QR codes from text or URLs. Perfect for creating QR codes for websites, contact information, or any text data.

## Features

- 🎨 Generate QR codes from any text or URL
- 💾 Automatic PNG format saving
- 📝 Custom file naming
- ✅ Input validation
- 🛡️ Error handling
- 📁 Shows file location after generation

## Requirements

- Python 3.6 or higher
- `qrcode` library
- `Pillow` (PIL) for image processing

## Installation

### Install Dependencies

**Option 1: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option 2: Manual installation**
```bash
pip install qrcode[pil]
```

Or install separately:

```bash
pip install qrcode pillow
```

## Usage

```bash
python qr_code_generator.py
```

### Example Usage

```
==================================================
QR Code Generator
==================================================

Enter the text or URL: https://github.com/yourusername
Enter the file name (without extension): my_qr_code
✅ QR code saved as 'my_qr_code.png'
📁 File location: D:\Downloads\py\qr-code-generator\my_qr_code.png
```

## What Can You Generate?

- **URLs**: `https://example.com`
- **Text**: `Hello, World!`
- **Contact Info**: `BEGIN:VCARD\nVERSION:3.0\nFN:John Doe\nEND:VCARD`
- **WiFi Credentials**: `WIFI:T:WPA;S:NetworkName;P:Password;;`
- **Email**: `mailto:example@email.com`
- **Phone**: `tel:+1234567890`
- **SMS**: `sms:+1234567890:Message`

## How It Works

1. Prompts for text or URL input
2. Prompts for filename (optional, defaults to "qrcode")
3. Generates QR code with error correction
4. Saves as PNG image file
5. Displays file location

## QR Code Settings

The generator uses:
- **Version**: 1 (auto-adjusts)
- **Box Size**: 10 pixels
- **Border**: 4 boxes
- **Error Correction**: Level L (Low - ~7% recovery)

## Code Structure

- `generate_qr_code(data, filename)`: Creates and saves QR code
- `main()`: Main program loop with user interaction

## Customization

You can modify the QR code settings in the code:

```python
qr = qrcode.QRCode(
    version=1,              # Size (1-40)
    box_size=10,           # Pixel size per box
    border=4,               # Border thickness
    error_correction=qrcode.constants.ERROR_CORRECT_L  # Error correction level
)
```

### Error Correction Levels

- `ERROR_CORRECT_L`: ~7% recovery
- `ERROR_CORRECT_M`: ~15% recovery
- `ERROR_CORRECT_Q`: ~25% recovery
- `ERROR_CORRECT_H`: ~30% recovery

## Use Cases

- **Business Cards**: Generate QR codes with contact information
- **Website Links**: Quick access to websites
- **WiFi Sharing**: Share WiFi credentials easily
- **Event Tickets**: Generate unique QR codes for events
- **Product Information**: Link to product pages
- **Social Media**: Link to profiles

## Error Handling

The program handles:
- Empty input
- Invalid file paths
- Permission errors
- Keyboard interrupts (Ctrl+C)

## Tips

- Use descriptive filenames to organize your QR codes
- Higher error correction levels create larger QR codes but are more durable
- Test QR codes with a scanner before printing
- For printing, use higher box_size values for better quality

## License

This project is open source and available for educational purposes.

---

**Generate QR codes easily! 📱**

