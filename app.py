from flask import Flask, render_template, request, send_file
import torch
from torchvision import transforms
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

def transform_image(image):
    """Applies Ghibli-style transformation (placeholder, replace with AI model)"""
    transform = transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x * 0.5 + 0.5),
        transforms.ToPILImage()
    ])
    return transform(image)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return "No image uploaded", 400
    
    file = request.files['image']
    image = Image.open(file.stream).convert("RGB")
    transformed_image = transform_image(image)
    
    img_io = io.BytesIO()
    transformed_image.save(img_io, format='PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
