import tensorflow as tf
import os
import numpy as np
from PIL import Image
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

cnn_model = None

# This finds the exact directory where THIS processor.py file is sitting
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'weights.h5')

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(244,244,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1, activation='sigmoid')   
])

model.save(MODEL_PATH, save_format='h5')

if os.path.exists(MODEL_PATH):
    print(f"🔎 Found file at {MODEL_PATH}. Attempting to load...")
    try:
        cnn_model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        print("🚀 DONE: cnn_model is now loaded and ready!")
    except Exception as e:
        print(f"💀 LOAD FAILED: The file exists but Keras hates it. Error: {e}")
else:
    print(f"🚫 FILE NOT FOUND: Python looked at {MODEL_PATH} and saw nothing.")

def run_cnn_scan(image_path: str):

    global cnn_model
    
    if cnn_model is None:
        return "CNN Analysis skipped: Model file (weights.h5) is missing from the server."
    
    try:
        # Load and convert to 3-channel RGB (important for medical images)
        img = Image.open(image_path).convert('RGB').resize((244, 244))
        img_array = np.array(img) / 255.0
        
        # Expand to 4D: (1, 244, 244, 3) for Keras
        processed_img = np.expand_dims(img_array, axis=0)

        prediction = cnn_model.predict(processed_img)
        # Assuming binary classification: >0.5 is abnormal
        prob = prediction[0][0]
        return f"Abnormality probability: {prob:.2%}"
    except Exception as e:
        return f"Image processing error: {str(e)}"

# --- 4. LANGCHAIN PIPELINE ---
# Replace with your actual key or use os.environ
llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0, 
    openai_api_key="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" 
)

template = """You are a specialized Radiologist Assistant. 
Below is the raw data from a CNN analysis of a patient's X-ray.

CNN FINDINGS: {cnn_output}
PATIENT NAME: {patient_name}

Based on this data, write a professional medical summary. 
Mention the probability of abnormality and suggest that the doctor 
performs a clinical correlation. Do not provide a final diagnosis."""

prompt = ChatPromptTemplate.from_template(template)

# This is your final pipeline
chain = (
    {
        "cnn_output": lambda x: run_cnn_scan(x["image_path"]),
        "patient_name": lambda x: x["patient_name"]
    }
    | prompt
    | llm
    | StrOutputParser()
)