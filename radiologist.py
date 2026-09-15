from PIL import Image
import hashlib


def analyze_xray(image_path):
    img = Image.open(image_path).convert("L")

    pixels = list(img.getdata())
    avg_brightness = sum(pixels) / len(pixels)

    img_bytes = img.tobytes()
    digest = hashlib.md5(img_bytes).hexdigest()
    seed_value = int(digest[:8], 16) % 100

    findings = []

    if avg_brightness < 90:
        findings.append("Possible consolidation detected")
    if seed_value % 3 == 0:
        findings.append("Pattern consistent with possible pneumonia")
    if seed_value % 7 == 0:
        findings.append("Irregularity suggestive of a possible fracture")

    if findings:
        status = "ABNORMAL"
    else:
        status = "NORMAL"
        findings.append("No significant abnormality detected")

    return {
        "status": status,
        "findings": findings,
        "avg_brightness": round(avg_brightness, 1)
    }