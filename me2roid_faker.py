from PIL import Image
import piexif
import sys
import os
from colorama import init, Fore

init(autoreset=True)

def print_info(msg, color=Fore.CYAN):
    print(f"{color}{msg}")

def convert_value_to_me2roid(value):
    """
    Convert the original EXIF tag value to a 'Me2roid' fake value
    with the same data type to avoid errors.
    """
    if isinstance(value, bytes):
        return b"Me2roid"
    elif isinstance(value, str):
        return "Me2roid"
    elif isinstance(value, int):
        return 1337  # Arbitrary integer value
    elif isinstance(value, tuple) and len(value) == 2 and all(isinstance(x, int) for x in value):
        return (13, 37)  # Rational number as tuple
    elif isinstance(value, list) and all(isinstance(x, tuple) for x in value):
        return [(13, 37) for _ in value]
    else:
        return value  # Return original if unknown type

def me2roidify_metadata(image_path, output_path):
    """
    Open the image, read its EXIF data if any,
    replace all EXIF tag values with 'Me2roid' (or suitable fake values),
    and save the image with the modified metadata.
    """
    try:
        img = Image.open(image_path)
        exif_bytes = img.info.get("exif")
        if exif_bytes:
            exif_dict = piexif.load(exif_bytes)
        else:
            # Create an empty EXIF dict if none exists
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "Interop": {}, "thumbnail": None}

        # Replace all EXIF tag values
        for ifd in exif_dict:
            if isinstance(exif_dict[ifd], dict):
                for tag in list(exif_dict[ifd]):
                    old_value = exif_dict[ifd][tag]
                    try:
                        exif_dict[ifd][tag] = convert_value_to_me2roid(old_value)
                    except Exception as e:
                        print_info(f"⛔ Could not replace tag {tag}: {e}", Fore.YELLOW)

        exif_bytes_new = piexif.dump(exif_dict)
        img.save(output_path, "jpeg", exif=exif_bytes_new)

        print_info(f"[✓] All metadata replaced with 'Me2roid' or fake values. File saved as: {output_path}", Fore.GREEN)

    except Exception as e:
        print_info(f"[!] Error: {e}", Fore.RED)

def main():
    if len(sys.argv) != 2:
        print_info("Usage:\n  python me2roid_faker.py image.jpg", Fore.YELLOW)
        return

    image_path = sys.argv[1]

    if not os.path.isfile(image_path):
        print_info("❌ File does not exist.", Fore.RED)
        return

    filename, ext = os.path.splitext(image_path)
    output_file = f"{filename}_me2roid{ext}"

    me2roidify_metadata(image_path, output_file)

if __name__ == "__main__":
    main()