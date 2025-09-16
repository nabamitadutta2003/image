from PIL import Image, ImageDraw, ImageFont

# Open your image (make sure example.jpg is in the same folder)
img = Image.open("example.jpg")

# Create a drawing object
draw = ImageDraw.Draw(img)

# Load a font (you can change size)
try:
    font = ImageFont.truetype("arial.ttf", 60)  # Use Arial if available
except:
    font = ImageFont.load_default()  # fallback if Arial not found

# Text and position
text = "Happy Birthday 🎉"
position = (0, 0)  # (x, y) from top-left corner

# Add text to image (white text with black outline for visibility)
draw.text(position, text, font=font, fill="white", stroke_width=2, stroke_fill="black")

# Save and show result
img.save("birthday_card.jpg")
img.show()