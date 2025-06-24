# 🕵️‍♂️ Me2roid Metadata Faker

**Me2roid Metadata Faker** is a Python-based CLI tool that doesn't just remove metadata from JPEG images — it *replaces all EXIF values with a custom marker: `Me2roid`*. This approach ensures that no traceable or personal information remains, while still preserving the structure of a valid EXIF block.

Whether you're protecting your privacy, testing forensic systems, or adding a digital signature to your work — this tool is a simple, powerful solution.

---

## 🔥 Why Replace Instead of Remove?

Most tools simply **delete** metadata, which can be suspicious in certain use cases (e.g., forensic analysis).  
Me2roid Faker replaces every EXIF tag value with a fake equivalent (like `"Me2roid"`, `1337`, or `(13, 37)`) depending on the data type.

This means:

✅ The image stays valid.  
✅ Metadata appears to exist, but is fake.  
✅ Your signature (`Me2roid`) is embedded across all tags.

---

## ✨ Features

- ✅ Replaces **every EXIF tag** with the string `Me2roid` or matching dummy values.
- ✅ Keeps the **image visually identical**.
- ✅ Avoids errors by **preserving data types** (e.g. bytes, strings, integers, rationals).
- ✅ Outputs cleanly named file with `_me2roid` suffix.
- ✅ Simple CLI, cross-platform, no external tools needed.
- ✅ MIT licensed.

---

## 📦 Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)
- [piexif](https://pypi.org/project/piexif/)
- [colorama](https://pypi.org/project/colorama/)

Install dependencies via:

```bash
pip install pillow piexif colorama
```

---

## 🛠️ Usage

```bash
python me2roid_faker.py image.jpg
```

📂 This will create a new file named:  
`image_me2roid.jpg`

Example:

```bash
python me2roid_faker.py vacation.jpeg
```

Output:

```
[✓] All metadata replaced with 'Me2roid' or fake values. Saved file: vacation_me2roid.jpg
```

---

## 🧠 What Happens Internally?

For each EXIF tag:
- If the value is a string or byte string → it becomes `"Me2roid"`.
- If it's an integer → it becomes `1337`.
- If it's a rational (like shutter speed) → it becomes `(13, 37)`.
- If it's a list of values → all are replaced with fakes.

This ensures:
- The file is not corrupted.
- Fake metadata appears normal to standard readers.
- A fingerprint of `"Me2roid"` is left inside every field.

---

## ✅ Use Cases

- Scrubbing personal data from images before publishing online.
- Creating training datasets for forensic software.
- Embedding a stealthy watermark/fingerprint.
- Sharing photos without leaking location or device info.

---

## 🪪 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it — but all copies must retain the original license.

---

## 🏴 Signature


```
                                        ┏┓    • ┓
                                   ┏┳┓┏┓┏┛┏┓┏┓┓┏┫
                                   ┛┗┗┗ ┗━┛ ┗┛┗┗┻

                        created & powered by >>>  ME2ROID  <<<

```

**Protect your pixels. Leave no trace. Fake like a pro. — Me2roid**
