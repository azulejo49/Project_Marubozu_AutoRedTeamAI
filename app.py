//app.py

import os
import streamlit as st
from dotenv import load_dotenv

# Import our autonomous agents
from agents.red_teamer import RedTeamerAgent
from agents.target import TargetAgent
from agents.judge import JudgeAgent

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Marubozu CART Visualizer", layout="wide")
st.title("🛡️ Project Marubozu: Continuous Automated Red Teaming (CART)")
st.markdown("### Live Jailbreak Simulation & Automated Scoring")

# --- INITIALIZATION ---
load_dotenv()
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Agents
@st.cache_resource
def load_agents():
    return RedTeamerAgent(), TargetAgent(), JudgeAgent()

red_teamer, target, judge = load_agents()

# --- DASHBOARD STATE ---
if "jailbreaks" not in st.session_state:
    st.session_state.jailbreaks = []
if "results" not in st.session_state:
    st.session_state.results = []

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("⚙️ Simulation Controls")
    if st.button("🚨 1. Generate Jailbreak Payloads", use_container_width=True):
        with st.spinner("Red Teamer is crafting attacks..."):
            st.session_state.jailbreaks = red_teamer.generate_jailbreaks()
            st.session_state.results = [] # Clear previous results
        st.success("Payloads generated!")

    if st.button("⚔️ 2. Execute Attack Simulation", use_container_width=True) and st.session_state.jailbreaks:
        st.session_state.results = []
        for jb in st.session_state.jailbreaks:
            with st.spinner(f"Executing {jb['tactic']} attack..."):
                target_response = target.generate_response(jb['prompt'])
                verdict_data = judge.evaluate(jb['prompt'], target_response)
                
                st.session_state.results.append({
                    "tactic": jb['tactic'],
                    "prompt": jb['prompt'],
                    "response": target_response,
                    "verdict": verdict_data['verdict'],
                    "reason": verdict_data['reason']
                })

# --- MAIN VISUALIZATION ARENA ---
if st.session_state.results:
    # Calculate ASR (Attack Success Rate)
    # A successful attack means the Judge evaluated it as FAIL (Target failed to defend)
    successful_attacks = sum(1 for r in st.session_state.results if r["verdict"] == "FAIL")
    asr = (successful_attacks / len(st.session_state.results)) * 100
    
    st.markdown(f"### 📊 Automated Scoring (ASR: {asr:.1f}%)")
    if asr > 0:
        st.error("⚠️ Target model is vulnerable. Remediation required.")
    else:
        st.success("✅ Target model successfully defended all jailbreaks.")

    st.divider()

    # Display the battle row by row
    for i, res in enumerate(st.session_state.results):
        st.markdown(f"#### Attack Vector {i+1}: `{res['tactic']}`")
        
        # 3-Column Layout exactly like a Purple Team workflow
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.error("👺 Attacker (Red Team)")
            st.info(f"**Prompt Anatomy:**\n\n{res['prompt']}")
            
        with col2:
            st.warning("🤖 Target Model (Defender)")
            st.write(res['response'])
            
        with col3:
            st.success("⚖️ AI Judge (Automated Scoring)")
            if res['verdict'] == "PASS":
                st.success("**Verdict:** DEFENDED (PASS)")
            else:
                st.error("**Verdict:** BREACHED (FAIL)")
            st.write(f"**Reasoning:** {res['reason']}")
            
        st.divider()

elif st.session_state.jailbreaks:
    st.info("👈 Payloads generated. Click 'Execute Attack Simulation' in the sidebar.")
else:
    st.write("👈 Click 'Generate Jailbreak Payloads' in the sidebar to begin.")