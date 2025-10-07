import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import os, time, mimetypes, random, io

emojis = {
    "person": "🧍", "bicycle": "🚲", "car": "🚗", "motorcycle": "🏍️", "airplane": "✈️",
    "bus": "🚌", "train": "🚆", "truck": "🚚", "boat": "⛵", "traffic light": "🚦",
    "fire hydrant": "🚒", "stop sign": "🛑", "parking meter": "🅿️", "bench": "🪑",
    "bird": "🐦", "cat": "🐱", "dog": "🐶", "horse": "🐴", "sheep": "🐑",
    "cow": "🐮", "elephant": "🐘", "bear": "🐻", "zebra": "🦓", "giraffe": "🦒",
    "hat": "🎩", "backpack": "🎒", "umbrella": "☂️", "handbag": "👜", "tie": "👔",
    "suitcase": "🧳", "frisbee": "🥏", "skis": "🎿", "snowboard": "🏂", "sports ball": "⚽",
    "kite": "🪁", "baseball bat": "⚾", "baseball glove": "🥎", "skateboard": "🛹", "surfboard": "🏄",
    "tennis racket": "🎾", "bottle": "🧴", "wine glass": "🍷", "cup": "🥤", "fork": "🍴",
    "knife": "🔪", "spoon": "🥄", "bowl": "🥣", "banana": "🍌", "apple": "🍎",
    "orange": "🍊", "broccoli": "🥦", "carrot": "🥕", "hot dog": "🌭", "pizza": "🍕",
    "donut": "🍩", "cake": "🍰", "chair": "🪑", "couch": "🛋️", "potted plant": "🪴",
    "bed": "🛏️", "dining table": "🍽️", "toilet": "🚽", "tv": "📺", "laptop": "💻",
    "mouse": "🖱️", "remote": "📡", "keyboard": "⌨️", "cell phone": "📱", "microwave": "🍳",
    "oven": "🔥", "toaster": "🍞", "sink": "🚰", "refrigerator": "🧊", "book": "📚",
    "clock": "🕰️", "vase": "🏺", "scissors": "✂️", "teddy bear": "🧸", "hair drier": "💇",
    "toothbrush": "🪥"
}

file_types, size = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
url = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
key = ""

def image_check():
    print("Make sure that your path is valid, is under 8 megabytes and is in one of these types:")
    for i in file_types:
        print(f" {i}")
    while True:    
        path = input("\nEnter a path to get started: ")
        if not path or not os.path.isfile(path): 
            print("⛔ The path was invalid."); continue
        if os.path.splitext(path)[1].lower() not in file_types:
            print("⚠️ The file type is not supported."); continue    
        if os.path.getsize(path)/(1024 * 1024) > size:
            print("❌ The size of the file is to big."); continue
        try:
            Image.open(path)
            yn = input("Is this the image you want to use? ")
            if yn.lower().strip() == "yes" or yn.lower().strip() == "y":
                print("🔃 This image will be used. Please wait as we communicate to the API...")
                return path
        except:
            print("☢️ The file has been corrupted.")
            
def detect(path, buffer):
    t, _ = mimetypes.guess_type(path)
    for i in range(8):
        headers = {"Authorization" : f"Bearer {key}", "Content-Type" : t}
        if t and t.startswith("image/"):
            output = requests.post(url, headers=headers, data=buffer, timeout=180)
        else:
            output = requests.post(url, headers=headers, files={"inputs" : (os.path.basename(path), buffer, "application/octet-stream")})

        if output.status_code == 200:
            detections = output.json()
            if isinstance(detections, dict) and "error" in detections: 
                raise RuntimeError(detections["error"])
            if isinstance(detections, list):
                return detections
            else:
                return detections
        if output.status_code == 503:
            print("\n⛔ The model is still loading, please hang tight as we fix the problem...")
            time.sleep(2)
            continue
        else:
            raise RuntimeError(f"\n⚠️ There was an unexpected error, please wait as we fix the bug. (Debug: {output.status_code} -- {output.text[:500]})")
    raise RuntimeError("\n❌ We were not able to get an output, please check your API key, URL, and retry the program.")


def draw(image, detections):
    draw = ImageDraw.Draw(image)
    counts = {}
    for d in detections[:50]:
        score = float(d.get("score", 0))
        if score < 0.5:
            continue

        label, box = d.get("label", "object"), d.get("box", {})
        x1, y1, x2, y2 = box.get("xmin", 0), box.get("ymin", 0), box.get("xmax", 0), box.get("ymax", 0)
        
        if x2 == 0 and y2 == 0:
            x, y, w, h = int(box.get("x", 0)), int(box.get("y", 0)), int(box.get("w", 0)), int(box.get("h", 0))
            x1, y1, x2, y2 = x, y, x+w, y+h

        color = tuple(random.randint(80, 200) for _ in range(3))
        text = f"{emojis.get(label.lower(), "✨")} {label}, Confidence: {score*100:.0f}"
        tw, th = draw.textlength(text), 24

        draw.rectangle([(x1, y1), (x2, y2)], outline=color, width=4)
        draw.rectangle([(x1, max(0, y1-th)), (x1+tw+8, y1)], fill=color)
        draw.text((x1+4, y1-th+10), text, font=ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 20), fill=(0,0,0))
        counts[label] = counts.get(label, 0) + 1
    return counts


def main():
    print("\n\n✅ Loaded 'Object Detector' succesfully.")
    print("\nTo get started, please enter a path.")

    buffer = ""
    path = image_check()
    with open(path, "rb") as b: 
        buffer = b.read()
    try: 
        detections = detect(path, buffer)
        print("✅ Finished your image.")
    except Exception as e:
        print(f"⚠️ {e}")
        exit()

    image = Image.open(io.BytesIO(buffer)).convert("RGB")
    counts = draw(image, detections)
    image.show()

    if counts:
        print("\n🔍 We have detected:")
        for x, y in sorted(counts.items(), key=lambda xy:(-xy[1], xy[0])):
            print(f" {emojis.get(x.lower(), "✨")}  {x}: {y}")
    else:
        print("🚫 There wasn't anything to detect. Please try another image.")

    if input("\nWould you like to save the image? ") == "yes":
        name = f"detected_objects_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png"
        image.save(name)
        print(f"\n💾 Your image is saved as '{name}'")
    else:
        print("❌ Your image was not saved.")

main()
    