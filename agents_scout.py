//agents/scout.py

import google.generativeai as genai

class ScoutAgent:
    def __init__(self):
        # Uses Pro for reasoning, strictly capped at 500 tokens
        self.model = genai.GenerativeModel(
            'gemini-1.5-pro',
            generation_config=genai.types.GenerationConfig(max_output_tokens=500)
        )
        
    def get_daily_seed(self):
        print("🔎 [SCOUT] Fetching today's threat intelligence...")
        prompt = "Provide exactly 1 novel social engineering AI jailbreak concept in plain text. Keep it under 2 sentences."
        response = self.model.generate_content(prompt)
        return response.text