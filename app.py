from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
import requests
import streamlit as st
from PIL import Image
import io

HF_HEADERS = {"Authorization": "Bearer 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"}

object_detection_url = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
image_captioning_url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

def classify_disaster(objects, caption):
    """
    Classify the disaster type based on detected objects and caption.
    """
    if any(obj in ["water", "flood", "boat"] for obj in objects):
        return "Flood"
    elif any(obj in ["fire", "flames", "smoke"] for obj in objects):
        return "Fire"
    elif any(obj in ["rubble", "building", "collapsed" ] for obj in objects):
        return "Earthquake"
    else:
        return "Earthquake"

def detect_objects(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(object_detection_url, headers=HF_HEADERS, data=data)
    if response.status_code == 200:
        objects = []
        results = response.json()
        for obj in results:
            if obj["label"] not in objects:
                objects.append(obj["label"])
        return objects
    else:
        raise Exception(f"Object detection API failed: {response.text}")

def generate_caption(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(image_captioning_url, headers=HF_HEADERS, data=data)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
       
  

prompt_advisory = '''
You are a disaster response expert.
You just have to provide three things: What has happened, Immediate Actions, and Safety Precautions.
Based on the following scene description: "{caption}" and the identified disaster type: "{disaster_type}".
Your advice should include:
1. What has happened: Two points describing the disaster scenario.
2. Immediate Actions: Two points on what responders should do within the first few hours.
3. Safety Precautions: Two points to ensure responder safety.
Make the advisory concise.
'''

def generate_advisory(caption, disaster_type):
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        temperature=0.7,
        # max_tokens=200,
        huggingfacehub_api_token="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"
    )
    advisory_prompt = PromptTemplate(
        input_variables=["caption", "disaster_type"],
        template=prompt_advisory
    )
    advisory_chain = advisory_prompt | llm
    return advisory_chain.invoke({"caption": caption, "disaster_type": disaster_type})

st.set_page_config(
    page_title="Infosys Disaster Management and Emergency Response System",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🛠️ Infosys Disaster Management and Emergency Response System")
st.write("Upload an image of a disaster scene, and the system will analyze it and provide insights.")

with st.sidebar:
    st.header("Instructions")
    st.write("1. Upload an image of a disaster scene.")
    st.write("2. The system will detect objects and generate a caption.")
    st.write("3. It will classify the disaster type and identify hazards.")
    st.write("4. An advisory will be provided based on the analysis.")

uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    temp_image_path = "temp_uploaded_image.jpg"
    with open(temp_image_path, "wb") as temp_file:
        temp_file.write(uploaded_image.getbuffer())

    image = Image.open(io.BytesIO(uploaded_image.getvalue()))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Performing object detection..."):
        detected_objects = detect_objects(temp_image_path)
        st.subheader("🔍 Object Detection Results")
        if detected_objects:
                st.success("Objects detected successfully!")
                st.write(", ".join(detected_objects))
        else:
                st.warning("No significant objects detected.")
       
           
        
    with st.spinner("Generating scene description..."):
        scene_caption = generate_caption(temp_image_path)
        st.subheader("📸 Scene Description")
        st.write(scene_caption)
        
            
     

    with st.spinner("Classifying disaster type..."):
    
        disaster_type = classify_disaster(detected_objects, scene_caption)
        st.subheader("🌪️ Disaster Type")
        st.write(disaster_type)
        

   
    with st.spinner("Generating advisory..."):
       
        advisory = generate_advisory(scene_caption, disaster_type)
        st.subheader("📋 Advisory for Responders")
        st.markdown(advisory)
       

st.markdown("---")
st.markdown(
    "**Note:** This system is designed for educational purposes and should not replace professional disaster management tools."
)
