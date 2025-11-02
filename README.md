# arjun-loop-ai

With modern AI, machine learning, and digital tools, arjun-loop-ai aims to address major challenges in healthcare such as organizing scattered medical records, making sense of complex medical reports, enabling faster clinical decisions, simplifying healthcare operations, and bringing care closer to people in every corner of the country.

## Project Description

This project provides an interface for diagnosis interaction between patients and doctors where both preventive and diagnostic tasks can be performed efficiently. It includes:

- A medical image analysis system that generates advanced pathological markings and biomarkers to assist doctors in diagnosis.
- Easy-to-understand medical report summaries for patients.
- Support for patients to upload medical images or X-rays for analysis.
- Record aggregation and natural language summaries to transform scattered medical records, test results, and advice into clear, connected, and readily accessible information.

## Documentation, Presentation, and Demo

- [Project Demo](https://drive.google.com/drive/folders/1CakqPv7cl8xOErp2dOA4wmXBsC_gV6Xd)
- [Project Presentation](https://drive.google.com/file/d/1iqHzcnoB-TKL35KIFvqmkFZUPd2KQBg_/view?usp=drive_link)  
- [Project Documentation](https://github.com/viren711/arjun-loop-ai)


## Folder Structure

```
/arjun-loop-ai
├── backend/               # Backend server code and APIs
├── model_training/        # Scripts and notebooks for training AI models
├── data/                  # Sample datasets and medical images
└── README.md              
```

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (see `requirements.txt` in backend folder)

### Running the Backend

1. Clone this repository:
   ```
   git clone https://github.com/viren711/arjun-loop-ai.git
   cd arjun-loop-ai/backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Launch the backend server:
   ```
   python flask_app.py
   ```

   The backend will expose APIs for image upload, diagnosis requests, and record processing.

### Model Training

1. Navigate to the model training folder:
   ```
   cd ../model_training
   ```

2. Prepare your training data and configuration as needed.

3. Run the training scripts or notebooks to train/update models that generate pathological markings and biomarkers.
