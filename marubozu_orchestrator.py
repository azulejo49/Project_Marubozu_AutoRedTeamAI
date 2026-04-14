//marubozu_orchestrator.py

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
# Import autonomous agents
//from agents.scout import ScoutAgent
//from agents.red_teamer import RedTeamerAgent
//from agents.target import TargetAgent
//from agents.judge import JudgeAgent
from agents.judge_agent import JudgeAgent
from agents.red_teamer_agent import RedTeamerAgent
from target_app.main_app import TargetApp

load_dotenv()

def run_marubozu_pipeline():
    print("🛡️ Marubozu Gatekeeper Initialized...")
    
    # 1. Load the Threat Seeds
    with open('data/threat_seeds.json', 'r') as f:
        threat_seeds = json.load(f)
    
    # 2. Red Teamer generates payloads
    red_teamer = RedTeamerAgent()
    payloads = red_teamer.mutate_seeds(threat_seeds)
    print(f"🗡️ Red Teamer generated {len(payloads)} toxic payloads.")

    # 3. Target attempts to defend
    target = TargetApp()
    judge = JudgeAgent(api_key=os.getenv("GEMINI_API_KEY"))
    
    # 4. Evaluation Loop
    for payload in payloads:
        response = target.generate_response(payload)
        verdict_data = judge.evaluate(payload, response)
        
        if verdict_data['verdict'] == 'FAIL':
            print(f"🚨 BREACH DETECTED! Blocking CI/CD Pipeline.")
            print(f"Reason: {verdict_data['reason']}")
            exit(1) # This exit code fails the GitHub Action
            
    print("✅ All tests passed. CI/CD Pipeline Approved.")
    exit(0)

if __name__ == "__main__":
    run_marubozu_pipeline()