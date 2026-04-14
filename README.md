# 🛡️ Project Marubozu: The Autonomous AI Red Team

![Status](https://img.shields.io/badge/Status-Prototype-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)
![Event](https://img.shields.io/badge/Evolve_Hack-2026-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

**The machine that guards the machine.** Project Marubozu is an Agent-Oriented Software (AOS) designed to continuously red-team and evaluate Generative AI applications directly within the CI/CD pipeline. 

## 🚨 The Problem: "Unwinnable Math"
In the era of Agentic AI, manual Trust & Safety reviews are an operational bottleneck. Human red teams cannot manually simulate the infinite, evolving landscape of toxic and adversarial (jailbreak) prompts. Companies are forced to choose between bottlenecking innovation with 5-day manual reviews or risking catastrophic zero-day vulnerabilities in production. 

## 💡 The Solution: Continuous Automated Red Teaming (CART)
Marubozu shifts Trust & Safety from a qualitative manual review to a high-speed engineering discipline. We codified complex legal and safety policies into a precise **"AI Constitution."** Using a swarm of autonomous AI agents, Marubozu automatically generates thousands of mutated cyber-attacks against your candidate AI model and blocks unsafe code merges in milliseconds.

### 🔑 Key Innovations
1. **The 500-Token Efficiency Limit:** To prevent API cost-bloat, Marubozu uses exactly 500 tokens a day to fetch a "Threat Seed" of novel vulnerabilities. 
2. **Token-Free Mutation:** It uses local algorithmic wrappers (Base64, Persona Adoption, Developer Mode) to multiply that seed into thousands of complex payloads for free.
3. **The AI Judge:** A zero-temperature evaluator objectively scores the target's defense against the Constitution.
4. **Live Threat Dashboard:** A professional Purple Team visualizer to watch the grammar of adversarial attacks unfold in real-time.

---

## 🧠 Architecture: The Agent Swarm

Project Marubozu utilizes a Multi-Agent System (MAS) to achieve autonomous governance:

* 🕵️ **The Scout (Agent 1):** Wakes up daily. Uses 500 tokens via a frontier API to gather the latest zero-day LLM jailbreak topologies.
* 🗡️ **The Red Teamer (Agent 2):** The mutation engine. It takes the Scout's seed and applies algorithmic wrappers to create highly deceptive adversarial payloads.
* 🎯 **The Target (Agent 3):** Your candidate LLM application undergoing the security audit.
* ⚖️ **The Judge (Agent 4):** Evaluates the Target's responses against the AI Constitution, outputting strict `PASS/FAIL` JSON.
* 🛡️ **The Gatekeeper (Agent 5):** The DevSecOps python orchestrator that bridges the swarm with GitHub/GitLab, blocking unsafe Pull Requests.

---

## 🚀 Quickstart & Installation

### Prerequisites
* Python 3.11+
* Google Gemini API Key (AI Studio)

### 1. Clone & Install
```bash
git clone [https://github.com/yourusername/marubozu-aos.git](https://github.com/yourusername/marubozu-aos.git)
cd marubozu-aos
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Setup
Create a `.env` file in the root directory and add your API key:
```env
GEMINI_API_KEY="your_api_key_here"
```

### 3. Run the CI/CD Orchestrator (Backend)
Run the automated pipeline to watch the swarm fetch intel, attack the target, and judge the interaction:
```bash
python orchestrator.py
```

### 4. Launch the Threat Engine Dashboard (Frontend)
To visualize the mutation logic and the threat matrix:
* Simply double-click `marubozu_threat_engine.html` to open it in your browser.
* *Or*, if using the Streamlit visualizer:
```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```text
marubozu-aos/
├── .github/workflows/       # GitHub Actions CI/CD pipelines
├── agents/                  # Autonomous Agent Logic
│   ├── scout.py             # Threat Intel Fetcher
│   ├── red_teamer.py        # Algorithmic Payload Mutator
│   ├── target.py            # Simulated Vulnerable App
│   └── judge.py             # Constitutional Evaluator
├── data/                    
│   ├── constitution.txt     # The AI Rules of Engagement
│   └── threat_seeds.json    # Local DB populated by the Scout
├── app.py                   # Streamlit Visualizer Dashboard
├── marubozu_threat_engine.html # Advanced HTML Threat Matrix UI
├── orchestrator.py          # The Gatekeeper execution script
└── requirements.txt         # Dependencies
```

---

## 🛣️ Project Roadmap

- [x] **Phase 1: Proof of Concept.** Develop core Red Teamer, Target, and Judge logic using API-driven models.
- [x] **Phase 2: Purple Workflow UI.** Build the Threat & Mutation Engine visualizer.
- [ ] **Phase 3: CI/CD Integration.** Embed the Gatekeeper agent directly into GitHub Actions as a mandatory PR check.
- [ ] **Phase 4: Local SLM Migration.** Move Red Teamer and Judge to local, token-free Small Language Models (e.g., Llama-3-8B) to scale testing at zero cost.
- [ ] **Phase 5: Auto-Remediation.** Enable the system to automatically suggest the exact code/prompt fix to the developer via GitHub comments.

---
Learning Festival Contest-2026-GlobalLogic
