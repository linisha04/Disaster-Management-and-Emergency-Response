# Infosys-Disaster-Management_Response-System

# **From Alt Text to Real Context Using AI**
### *Disaster Management and Advisory System*

## 📌 **Project Overview**
This AI-powered disaster response system analyzes images of disaster scenes, classifies disaster types, and provides emergency response advisories. It leverages state-of-the-art deep learning models to enhance situational awareness and guide responders with actionable insights.

---
## 🚀 **Key Features**
- **AI-Based Object Detection**: Identifies crucial elements in disaster scenes (e.g., water, fire, rubble)
- **Image Captioning**: Generates a textual description of the disaster scenario
- **Disaster Type Classification**: Categorizes the disaster as **Flood, Fire, or Earthquake**
- **Emergency Advisory Generation**: Provides instant, AI-generated response recommendations
- **User-Friendly Web Interface**: Developed using **Streamlit** for ease of use

---
## 🔧 **Technologies & Tools Used**
- **Programming Language**: Python 🐍
- **Framework**: Streamlit (for UI)
- **AI Models**:
  - Object Detection: `DETR (Facebook)`
  - Image Captioning: `BLIP (Salesforce)`
  - Disaster Type Classification: Custom AI logic
  - AI Advisory Generation: `Meta Llama 3B`
- **Libraries Used**:
  - `Requests` (API calls)
  - `PIL` (Image Processing)
  - `LangChain` (AI-powered prompt engineering)
  - `Hugging Face API`

---
## 📊 **How It Works?**
1️⃣ **User Uploads an Image**: Disaster scene is uploaded to the system
2️⃣ **AI Performs Object Detection**: Key elements are identified
3️⃣ **Image Captioning is Generated**: Describes the scenario
4️⃣ **Disaster Type is Classified**: Flood, Fire, or Earthquake
5️⃣ **AI Generates an Advisory**: Emergency response guidelines are provided

---
## 🏗️ **Installation & Setup**
### 🔹 **Prerequisites**
Ensure you have **Python 3.8+** installed along with the required libraries:

```bash
pip install streamlit requests pillow langchain_huggingface
```

### 🔹 **Running the Application**
```bash
streamlit run app.py
```
This will launch the web interface where users can upload images for analysis.

---
## 📌 **Example Use Case**
**Scenario**: A responder uploads an image showing collapsed buildings with smoke.
- 🔍 AI detects **rubble, fire, smoke**
- 🏷️ Classifies disaster as **Earthquake**
- 📋 Advisory suggests **search and rescue operations, medical assistance, and safety measures**

---
## 🚀 **Future Enhancements**
- 📹 **Real-Time Video Analysis**: Support for live disaster scene monitoring
- 🌍 **Multilingual Advisory Support**: Expanding to different languages
- 📡 **Geolocation & Weather Data Integration**: Enhancing response accuracy
- 📊 **Crowdsourced Data for Model Training**: Improving model accuracy with real-world data


