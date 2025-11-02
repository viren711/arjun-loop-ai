from flask import Flask, request, render_template, jsonify
from ultralytics import YOLO
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def get_yolo_model():
    model = YOLO("yolov8n.pt") 
    return model

yolo_model = get_yolo_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image selected'}), 400
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    results = process_image(filepath)
    
    result_filename = f"{timestamp}_result_{file.filename}"
    result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
    
    result = results[0]
    result.save(result_path)
    
    detected_classes = []
    for box in result.boxes:
        class_id = int(box.cls[0].item())
        class_name = result.names[class_id]
        confidence = box.conf[0].item()
        detected_classes.append({
            'name': class_name,
            'confidence': round(confidence, 2)
        })
    
    return render_template('result.html', 
                          original_image=filepath,
                          result_image=result_path,
                          detected_classes=detected_classes)

def process_image(image_path):
    results = yolo_model(image_path)
    return results

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
