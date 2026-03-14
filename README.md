
# 🩻 AI X-Ray Disease Detection System using CNN, LangChain & Gemini API

## 📌 Project Overview

The **AI X-Ray Disease Detection System** is an intelligent medical analysis application that detects abnormalities in chest X-ray images using **Deep Learning (CNN)** and provides AI-generated medical explanations using **LangChain with Gemini API**.

The system combines **computer vision and generative AI** to assist healthcare professionals by automatically analyzing X-ray images and generating detailed medical insights.

This project demonstrates how **deep learning models and large language models (LLMs)** can be integrated to build intelligent healthcare diagnostic systems.

---

# 🧠 System Architecture

The system consists of two main components:

1️⃣ **CNN-based Image Classification Model**

A **Convolutional Neural Network (CNN)** analyzes chest X-ray images to detect potential diseases such as:

* Pneumonia
* Lung infection
* Abnormal lung patterns

The CNN extracts image features and predicts the probability of disease presence.

---

2️⃣ **Generative AI Explanation Engine**

After the CNN produces a prediction, the result is passed to a **LangChain-powered pipeline** that communicates with the **Gemini API**.

The AI model generates:

* Medical explanation of the prediction
* Possible causes
* General healthcare insights
* Patient-friendly explanation

This makes the system **more interpretable and useful for telemedicine and clinical support systems**.

---

# ⚙️ Workflow

1️⃣ User uploads a **Chest X-Ray Image**

2️⃣ The image is processed and passed into the **CNN model**

3️⃣ The model predicts the **presence or absence of disease**

4️⃣ The prediction result is sent to **LangChain**

5️⃣ LangChain queries the **Gemini API**

6️⃣ Gemini generates a **medical explanation of the prediction**

7️⃣ The system displays:

* Prediction result
* Confidence score
* AI-generated explanation

---

# 🧠 Key Features

### 🩻 Automated X-Ray Analysis

Uses **CNN-based deep learning** to analyze chest X-ray images.

---

### 🤖 AI Medical Explanation

Uses **Generative AI (Gemini)** to generate understandable medical insights.

---

### 🔗 LangChain Integration

LangChain connects the CNN prediction pipeline with the **Gemini LLM** to create intelligent responses.

---

### 📊 AI-Assisted Diagnosis

Provides support for **medical analysis and clinical decision-making**.

---

### ⚡ Fast Image Processing

The system processes medical images quickly and provides instant results.

---

# 🛠 Tools & Technologies

### 🤖 Artificial Intelligence & Deep Learning

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge\&logo=TensorFlow\&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge\&logo=Keras\&logoColor=white)

---

### 🧠 Generative AI & LLM

![LangChain](https://img.shields.io/badge/LangChain-AI%20Framework-green?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-LLM-blueviolet?style=for-the-badge\&logo=google)

---

### 📊 Data Processing & Visualization

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge\&logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge\&logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=for-the-badge)

---
# 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone (https://github.com/Hari-23-cpu/Xray-Detector-using-Langchain-CNN)
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add Gemini API Key

Create an environment variable:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```
python app.py
```

---

# 📊 Model Evaluation

The CNN model is evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **Confusion Matrix**

These metrics help determine the model's effectiveness in detecting lung diseases.

---

# ⚠️ Disclaimer

This system is designed for **educational and research purposes only**.

The predictions and AI-generated explanations **should not be used as a substitute for professional medical diagnosis**. Always consult a qualified healthcare professional for medical advice.

---



