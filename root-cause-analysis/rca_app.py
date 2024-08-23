import os
import streamlit as st
import rca_lib as rcalib #reference to local lib script

motor_options = {
  "AC motor 6W 110-120VAC": "Transmotec-Datasheet-AI-006W.pdf",
  "RS PRO 3 Phase AC motor": "A700000006779781.pdf", 
  "AMA-IE2 90L2 2.2kW 2 Pole": "AMA-IE2 90L2 (B5).pdf"
}

fms = ['Bedrock Titan', 'Bedrock Claude Instant', 'Bedrock Claude 2']
default_model = fms.index('Bedrock Claude Instant')

default_values = {
  "img_summary": None,
  "motor_summary": None,
  "motor_contents": None, 
  "label_text": None,
  "generated_code": None,
  "selected_motor": None
}

def initialize_session_state():
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

def configure_sidebar():
    return st.sidebar.selectbox('Select a FM', options=fms, index=default_model)

def configure_page():
  st.set_page_config(
    page_title="GenAI IIoT Electric Motor Diagnosis", 
    page_icon="cloud_with_lightning"
  )

def add_header():
  st.title("GenAI IIoT Electric Motor Diagnosis")
  st.markdown("# :orange[Root Cause Analysis] of Electric Motors Using Manufacturer Specs")
  st.sidebar.header("GenAI IIoT Electric Motor Diagnosis")

def add_description():
  st.markdown("### With this demo you can:")

  st.write("1. Upload an electric motor datasheet in pdf format")
  st.markdown("- [RS PRO 3 Phase AC motor](https://docs.rs-online.com/7939/A700000006779781.pdf)")
  st.markdown("- [AMA-IE2 90L2 2.2kW 2 Pole](https://amtecs.co.uk/datasheet/6Gq4LEgn7OAWDRKvdJ53)")
  st.markdown("- [AC motor 6W 110-120VAC](https://transmotec.com/Download/Datasheets/Transmotec-Datasheet-AI-006W.pdf)")
  st.markdown('''
  <style>
  [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
  }
  </style>
  ''', unsafe_allow_html=True)

  st.write("2. Generate examples of IIoT sensor data representing anomalous and optiomal conditions based on motor specs.")
  st.write("3. Evaluate IIoT sensor data to determine anomalies and potential root causes.")

def select_motor():
  c1, c2 = st.columns(2)
  
  c1.subheader("Choose a Motor Spec")
  selected_motor = c1.selectbox("Select motor", list(motor_options.keys()))

  return motor_options[selected_motor]

def upload_file(selected_file, model):
  if selected_file is None or st.session_state['selected_motor'] == selected_file: return

  st.session_state["selected_motor"] = selected_file
  with st.spinner("Processing..."):
    file_path = os.path.join("../../data/root-cause-analysis", selected_file)
    motor_contents, motor_summary = rcalib.upload_file_get_summary(file_path, model)
    st.session_state["motor_contents"] = motor_contents
    if len(motor_summary) > 5:
        st.session_state["motor_summary"] = motor_summary  
        st.success("File uploaded and processed")

def generate_conditions(model):
  conditions = ['anomalous', 'optimal']
  tabs = st.tabs(conditions)
  for i in range(0, len(conditions)):
    with tabs[i]:
      code_text = 'Based on the motor specs that you provided, please write a JSON message with motor random SENSOR DATA for an ' + conditions[i] + '.\n'
      code = rcalib.call_bedrock(model, code_text)
      st.session_state.generated_code = code
      st.code(code,language=str(conditions[i]))

def display_motor_summary(model):
  st.markdown('**Motor Specs:** \n')
  st.write(str(st.session_state.motor_summary).replace("$","\$"))
  generate_conditions(model)
  
def display_prompt_snesor_data():
  st.markdown("---")  
  st.subheader("**Analyze IoT Sensor Data**\n")
  return st.text_area('**Paste a motor sensor JSON message here, or use one from the examples above.**', key='text')

def describe_sensor_data(model, input_text):
  if(not(input_text and input_text.strip())): return
  
  rca_prompt = "Please write a paragraph describing the following sensors data:\n" + input_text + "\n"
  rca = rcalib.call_bedrock(model, rca_prompt)

  st.subheader('**Interpretation of the IoT sensor data**\n')
  st.write(rca)
  return rca

def run_root_cause_analysis(model, rca):
    if rca is None: return
  
    rca_prompt = "Based on your observations:\n" + rca + "\n and based the motor specs below, TASK: please describe if there is any anomaly and the potential root cause(s):\n ** motor specs **" + st.session_state['motor_summary'] + "\n"
    rca = rcalib.call_bedrock(model, rca_prompt)

    st.subheader('**Root Cause Analysis**\n')
    st.write(rca)

def process_specs(model):
  if st.session_state.motor_summary and len(st.session_state.motor_summary) > 5: 
    display_motor_summary(selected_model)
    sensor_data = display_prompt_snesor_data()
    rca = describe_sensor_data(selected_model, sensor_data)
    run_root_cause_analysis(selected_model, rca)
                           
initialize_session_state()
configure_page()
add_header()  
st.markdown("---")
add_description()
st.markdown("---")

selected_model = configure_sidebar().lower()
selected_file = select_motor()

upload_file(selected_file, selected_model)
process_specs(selected_model)
