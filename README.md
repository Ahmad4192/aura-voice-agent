# AURA // CORE - Realtime Dual-Language Voice Agent

A low-latency AI voice agent built with a cyberpunk HUD interface, supporting real-time conversational intelligence in both Urdu and English.

Powered by Streamlit, JavaScript Web Audio, and OpenAI models (gpt-4o-mini and tts-1).

---

## Features

- Dual-Language Support: Speech recognition and generation for both Urdu (ur-PK) and English (en-US).
- Instant Barge-In (Interruptibility): Speaking while the agent is talking cuts off audio output immediately to process the new input without delay.
- Neural Voice Synthesis: Clear voice output generated via OpenAI tts-1 using the nova persona.
- Privacy-First Client Architecture: API keys are stored strictly in the browser local storage, avoiding server-side key exposure.
- Realtime Telemetry: Microphone and speaker decibel tracking, canvas visualizer, and round-trip response latency indicators.

---

## Tech Stack

- Frontend Framework: Python, Streamlit, HTML5 Canvas, CSS
- Audio and Speech Pipeline: Web Speech API, Web Audio API, OpenAI TTS-1
- LLM Reasoning: OpenAI GPT-4o-mini

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- OpenAI API Key

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Ahmad4192/aura-voice-agent.git](https://github.com/Ahmad4192/aura-voice-agent.git)
   cd aura-voice-agent
