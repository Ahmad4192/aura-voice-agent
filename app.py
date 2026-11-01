import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AURA // CORE - Realtime Voice Agent",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden !important;}
    div.block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
        height: 100vh !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_CODE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AURA Realtime Agent</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #07090e;
      --card-bg: rgba(13, 17, 26, 0.9);
      --card-border: #1a2233;
      --cyan: #00f2fe;
      --purple: #bd93f9;
      --green: #00ffaa;
      --text-main: #e6edf3;
      --text-muted: #8b949e;
      --font-mono: 'Consolas', monospace;
      --font-urdu: 'Noto Sans Arabic', 'Segoe UI', Tahoma, sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    body {
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(circle at 50% 10%, rgba(0, 242, 254, 0.05), transparent 40%),
        linear-gradient(rgba(0, 242, 254, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 242, 254, 0.02) 1px, transparent 1px);
      background-size: 100% 100%, 30px 30px, 30px 30px;
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      height: 62px;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--card-border);
      background: rgba(7, 9, 14, 0.95);
    }

    .brand { display: flex; align-items: center; gap: 12px; }
    .brand-icon {
      width: 36px; height: 36px; border-radius: 8px;
      background: rgba(0, 242, 254, 0.1); border: 1px solid rgba(0, 242, 254, 0.3);
      display: flex; align-items: center; justify-content: center;
      color: var(--cyan); box-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
    }
    .brand-title { font-size: 15px; font-weight: 700; letter-spacing: 1.5px; font-family: var(--font-mono); }
    .brand-title span.version {
      font-size: 11px; background: rgba(0, 242, 254, 0.15); color: var(--cyan);
      padding: 2px 6px; border-radius: 4px; margin-left: 6px;
    }

    .header-center {
      display: flex; align-items: center; gap: 18px;
      background: rgba(13, 17, 26, 0.9); padding: 6px 16px; border-radius: 20px;
      border: 1px solid var(--card-border); font-family: var(--font-mono); font-size: 12px;
    }
    .status-dot {
      width: 7px; height: 7px; border-radius: 50%; background: var(--green);
      display: inline-block; margin-right: 6px; box-shadow: 0 0 8px var(--green);
    }

    .header-actions { display: flex; align-items: center; gap: 10px; }
    .lang-switcher {
      background: #111827; border: 1px solid var(--cyan); color: var(--cyan);
      padding: 6px 10px; border-radius: 6px; font-family: var(--font-mono);
      font-size: 12px; font-weight: 700; cursor: pointer; outline: none;
    }
    .icon-btn {
      background: #111827; border: 1px solid var(--card-border); color: var(--text-main);
      padding: 7px 14px; border-radius: 6px; font-size: 12px; font-family: var(--font-mono);
      display: flex; align-items: center; gap: 7px; cursor: pointer;
    }
    .icon-btn:hover { border-color: var(--cyan); color: var(--cyan); }

    .dashboard-container {
      flex: 1; display: grid; grid-template-columns: 1fr 1.35fr; gap: 18px;
      padding: 18px 24px; max-width: 1700px; margin: 0 auto; width: 100%;
    }

    .panel {
      background: var(--card-bg); border: 1px solid var(--card-border);
      border-radius: 12px; display: flex; flex-direction: column; overflow: hidden;
    }
    .panel-header {
      padding: 14px 18px; border-bottom: 1px solid var(--card-border);
      display: flex; align-items: center; justify-content: space-between;
      font-family: var(--font-mono); font-size: 12px; font-weight: 600;
    }
    .flush-btn { background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-size: 11px; }

    .transcript-scroll {
      flex: 1; padding: 18px; overflow-y: auto; display: flex; flex-direction: column; gap: 14px; max-height: 520px;
    }
    .msg-card { border-radius: 8px; padding: 14px; font-size: 13.5px; line-height: 1.6; }
    .msg-agent { background: rgba(189, 147, 249, 0.08); border-left: 3px solid var(--purple); }
    .msg-user { background: rgba(0, 242, 254, 0.08); border-left: 3px solid var(--cyan); }
    .msg-meta {
      display: flex; justify-content: space-between; align-items: center;
      font-family: var(--font-mono); font-size: 10px; margin-bottom: 6px; color: var(--text-muted);
    }
    .urdu-text { font-family: var(--font-urdu); direction: rtl; text-align: right; font-size: 15px; }

    .quick-prompts {
      padding: 8px 18px; display: flex; gap: 8px; flex-wrap: wrap;
      background: rgba(9, 12, 18, 0.6); border-top: 1px solid var(--card-border);
    }
    .prompt-chip {
      background: #111827; border: 1px solid var(--card-border); padding: 4px 10px;
      border-radius: 4px; font-size: 11px; color: var(--text-muted); cursor: pointer; font-family: var(--font-mono);
    }
    .prompt-chip.urdu { font-family: var(--font-urdu); direction: rtl; font-size: 12px; }

    .chat-input-row {
      padding: 12px 18px; display: flex; gap: 10px;
      background: rgba(7, 9, 14, 0.9); border-top: 1px solid var(--card-border);
    }
    .chat-input {
      flex: 1; background: #111827; border: 1px solid var(--card-border);
      border-radius: 6px; padding: 10px 14px; color: #fff; font-size: 13px; outline: none;
    }
    .send-btn {
      background: var(--cyan); border: none; color: #000; width: 40px;
      border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 700;
    }

    .right-stack { display: flex; flex-direction: column; gap: 16px; }
    .orb-panel { padding: 24px; display: flex; flex-direction: column; align-items: center; position: relative; }
    .orb-header { width: 100%; display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 11px; margin-bottom: 20px; }

    .visualizer-wrapper {
      position: relative; width: 260px; height: 260px;
      display: flex; align-items: center; justify-content: center; margin: 10px 0;
    }
    #orbCanvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; }

    .center-mic-node {
      position: relative; z-index: 10; width: 80px; height: 80px; border-radius: 50%;
      background: radial-gradient(circle, #081a2e 0%, #030811 100%);
      border: 2px solid rgba(0, 242, 254, 0.6); display: flex; flex-direction: column;
      align-items: center; justify-content: center; cursor: pointer;
      box-shadow: 0 0 25px rgba(0, 242, 254, 0.3); transition: all 0.3s ease;
    }
    .center-mic-node:hover { transform: scale(1.06); }
    .center-mic-node i { color: var(--cyan); font-size: 24px; }
    .center-mic-node span { font-size: 8px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 4px; }

    .action-controls { display: flex; gap: 14px; margin-top: 25px; }
    .btn-primary-listen {
      background: linear-gradient(90deg, #00d2ff, #00f2fe); color: #020617;
      border: none; padding: 12px 28px; border-radius: 25px; font-family: var(--font-mono);
      font-size: 13px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
    }
    .btn-secondary-test {
      background: #111827; border: 1px solid var(--card-border); color: var(--text-main);
      padding: 12px 22px; border-radius: 25px; font-family: var(--font-mono);
      font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 8px;
    }

    .telemetry-row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
    .gauge-card {
      background: var(--card-bg); border: 1px solid var(--card-border);
      border-radius: 10px; padding: 16px; display: flex; flex-direction: column; gap: 12px;
    }
    .meter-item { display: flex; flex-direction: column; gap: 6px; }
    .meter-label-row { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); }
    .meter-track { width: 100%; height: 6px; background: #151b27; border-radius: 3px; overflow: hidden; }
    .meter-fill-cyan { height: 100%; width: 12%; background: var(--cyan); box-shadow: 0 0 8px var(--cyan); }
    .meter-fill-purple { height: 100%; width: 8%; background: var(--purple); box-shadow: 0 0 8px var(--purple); }

    .telemetry-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-family: var(--font-mono); font-size: 11px; }
    .telem-unit { color: var(--text-muted); }
    .telem-val { color: var(--cyan); font-weight: 600; margin-top: 2px; }

    .bottom-runtime-bar {
      background: var(--card-bg); border: 1px solid var(--card-border);
      border-radius: 10px; padding: 12px 18px; display: flex; align-items: center;
      justify-content: space-between; font-family: var(--font-mono); font-size: 11px;
    }

    .modal-overlay {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(0,0,0,0.7); backdrop-filter: blur(5px); z-index: 1000;
      display: none; align-items: center; justify-content: center;
    }
    .modal-box {
      background: #0d121d; border: 1px solid var(--cyan); border-radius: 12px;
      width: 480px; padding: 24px; box-shadow: 0 0 35px rgba(0, 242, 254, 0.2);
    }
    .modal-box h3 { font-family: var(--font-mono); color: var(--cyan); margin-bottom: 15px; font-size: 16px; }
    .modal-box label { display: block; font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin: 10px 0 5px; }
    .modal-box input, .modal-box select {
      width: 100%; background: #151b27; border: 1px solid var(--card-border);
      color: #fff; padding: 9px 12px; border-radius: 6px; font-size: 13px; outline: none;
    }
    .modal-btns { margin-top: 20px; display: flex; justify-content: flex-end; gap: 10px; }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <div class="brand-icon"><i class="fa-solid fa-robot"></i></div>
      <div>
        <div class="brand-title">AURA // CORE <span class="version">v2.4 REALTIME</span></div>
        <div class="brand-subtitle">High-Definition Female Voice Agent</div>
      </div>
    </div>

    <div class="header-center">
      <div><span class="status-dot"></span>FEMALE VOICE ACTIVE</div>
      <div style="color: var(--text-muted);">|</div>
      <div style="color: var(--cyan);"><i class="fa-solid fa-bolt"></i> <span id="latencyDisplay">Fast</span></div>
      <div style="color: var(--text-muted);">|</div>
      <div><i class="fa-regular fa-clock"></i> <span id="sessionTimer">00:00</span></div>
    </div>

    <div class="header-actions">
      <select class="lang-switcher" id="languageSelector" onchange="switchLanguage(this.value)">
        <option value="ur-PK" selected>🇵🇰 اردو (Urdu)</option>
        <option value="en-US">🇬🇧 English</option>
      </select>
      <button class="icon-btn" id="muteBtn" onclick="toggleMute()"><i class="fa-solid fa-microphone"></i></button>
      <button class="icon-btn" onclick="openConfigModal()"><i class="fa-solid fa-sliders"></i> CONFIG</button>
    </div>
  </header>

  <div class="dashboard-container">
    <div class="panel">
      <div class="panel-header">
        <span><i class="fa-solid fa-terminal" style="color: var(--cyan); margin-right: 8px;"></i> LIVE TRANSCRIPT</span>
        <button class="flush-btn" onclick="flushTranscript()"><i class="fa-solid fa-trash-can"></i> FLUSH</button>
      </div>

      <div class="transcript-scroll" id="transcriptContainer">
        <div class="msg-card msg-agent">
          <div class="msg-meta">
            <span class="tag"><i class="fa-solid fa-sparkles"></i> AURA // AGENT</span>
            <span>READY</span>
          </div>
          <div class="urdu-text">السلام علیکم! میں آپ کی وائس اسسٹنٹ ہوں۔ مائیک کا بٹن دبائیں اور مجھ سے بات کریں۔</div>
        </div>
      </div>

      <div class="quick-prompts">
        <span style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted);">QUICK:</span>
        <div class="prompt-chip urdu" onclick="usePrompt('گاڑی کی چابی پروگرامنگ کیسے ہوتی ہے؟')">"گاڑی کی چابی پروگرامنگ"</div>
        <div class="prompt-chip urdu" onclick="usePrompt('اپنا تعارف کروائیں اور آپ کیا کر سکتی ہیں؟')">"آپ کیا کر سکتی ہیں؟"</div>
      </div>

      <div class="chat-input-row">
        <input type="text" id="customInput" class="chat-input" placeholder="اردو یا انگلش میں لکھیں یا بولیں..." onkeydown="handleInputKey(event)">
        <button class="send-btn" onclick="sendTextMessage()"><i class="fa-solid fa-paper-plane"></i></button>
      </div>
    </div>

    <div class="right-stack">
      <div class="panel orb-panel">
        <div class="orb-header">
          <div style="color: var(--cyan); font-weight:700;"><span class="status-dot"></span><span id="agentStateText">IDLE // STANDBY</span></div>
          <div style="color: var(--text-muted);">AUDIO ENGINE: <span style="color: var(--green); font-weight:600;">Nova (Female HD)</span></div>
        </div>

        <div class="visualizer-wrapper">
          <canvas id="orbCanvas" width="260" height="260"></canvas>
          <div class="center-mic-node" id="orbCenterBtn" onclick="toggleListening()">
            <i class="fa-solid fa-microphone" id="orbMicIcon"></i>
            <span id="orbMicLabel">TAP MIC</span>
          </div>
        </div>

        <div class="action-controls">
          <button class="btn-primary-listen" id="mainListenBtn" onclick="toggleListening()">
            <i class="fa-solid fa-microphone"></i> بولنا شروع کریں
          </button>
          <button class="btn-secondary-test" onclick="testVoiceSynthesis()">
            <i class="fa-solid fa-volume-high"></i> آواز سنیں
          </button>
        </div>

        <div style="font-size: 11px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 15px;">
          مائیک دبا کر بات کریں۔ اگر میں بول رہی ہوں اور آپ بولیں گے تو میں فوراً رک جاؤں گی۔
        </div>
      </div>

      <div class="telemetry-row">
        <div class="gauge-card">
          <div class="meter-item">
            <div class="meter-label-row">
              <span><i class="fa-solid fa-microphone-lines"></i> MIC INPUT</span>
              <span id="micDbVal" style="color: var(--cyan);">-48 dB</span>
            </div>
            <div class="meter-track">
              <div class="meter-fill-cyan" id="micMeterFill"></div>
            </div>
          </div>
          <div class="meter-item">
            <div class="meter-label-row">
              <span><i class="fa-solid fa-volume-low"></i> AGENT AUDIO</span>
              <span id="outDbVal" style="color: var(--purple);">-68 dB</span>
            </div>
            <div class="meter-track">
              <div class="meter-fill-purple" id="outMeterFill"></div>
            </div>
          </div>
        </div>

        <div class="gauge-card">
          <div style="display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:11px;">
            <span>TELEMETRY</span>
            <span style="color:var(--green);">● ACTIVE</span>
          </div>
          <div class="telemetry-grid">
            <div>
              <div class="telem-unit">LANGUAGE</div>
              <div class="telem-val" id="telemLang">Urdu (ur-PK)</div>
            </div>
            <div>
              <div class="telem-unit">VOICE PERSONA</div>
              <div class="telem-val" id="voiceDisplay" style="color: var(--green);">nova (Female HD)</div>
            </div>
            <div>
              <div class="telem-unit">INTELLIGENCE</div>
              <div class="telem-val">gpt-4o-mini</div>
            </div>
            <div>
              <div class="telem-unit">BARGE-IN</div>
              <div class="telem-val" style="color: var(--purple);">Instant Cutoff</div>
            </div>
          </div>
        </div>
      </div>

      <div class="bottom-runtime-bar">
        <div style="font-weight:700;"><i class="fa-solid fa-microchip" style="color: var(--cyan); margin-right: 6px;"></i> FEMALE NEURAL PIPELINE</div>
        <div style="display:flex; gap:20px;">
          <div>PERSONA: <span style="color:var(--green);">Nova Active</span></div>
          <div>STREAM: <span style="color:var(--cyan);">Ready</span></div>
        </div>
      </div>
    </div>
  </div>

  <div class="modal-overlay" id="configModal">
    <div class="modal-box">
      <h3><i class="fa-solid fa-key"></i> SYSTEM CONFIGURATION</h3>
      <label>OPENAI API KEY</label>
      <input type="password" id="modalApiKey" placeholder="sk-proj-...">

      <label>VOICE PERSONA</label>
      <select id="modalVoiceSelect">
        <option value="nova" selected>nova (خاتون - پُرجوش، قدرتی اور سریلی)</option>
        <option value="shimmer">shimmer (خاتون - نرم اور واضح)</option>
        <option value="alloy">alloy (نیوٹرل / متوازن)</option>
        <option value="echo">echo (مردانہ - بھاری)</option>
        <option value="onyx">onyx (مردانہ - سنجیدہ)</option>
      </select>

      <label>SYSTEM INSTRUCTIONS</label>
      <input type="text" id="modalInstructions" value="You are AURA, a friendly female voice assistant and automotive locksmith expert. If the user speaks Urdu, respond politely in sweet, natural Urdu. If English, respond in English. Always keep answers concise in 1 to 2 sentences max.">

      <div class="modal-btns">
        <button class="icon-btn" onclick="closeConfigModal()">Cancel</button>
        <button class="icon-btn" style="background: var(--cyan); color:#000; font-weight:700;" onclick="saveConfig()">Save</button>
      </div>
    </div>
  </div>

  <script>
    let currentLang = 'ur-PK';
    let apiKey = localStorage.getItem('aura_api_key') || '';
    // مستقل طور پر لڑکی کی آواز nova کو ڈیفالٹ بنا دیا گیا ہے
    let voice = localStorage.getItem('aura_voice') || 'nova';
    let instructions = localStorage.getItem('aura_inst') || 'You are AURA, a friendly female voice assistant and automotive locksmith expert. If the user speaks Urdu, respond politely in sweet, natural Urdu. If English, respond in English. Always keep answers concise in 1 to 2 sentences max.';
    let isListening = false;
    let isSpeaking = false;
    let isMuted = false;
    let recognition = null;
    let secondsElapsed = 0;
    let abortController = null;
    let currentAudio = null;

    setInterval(() => {
      secondsElapsed++;
      const mins = String(Math.floor(secondsElapsed / 60)).padStart(2, '0');
      const secs = String(secondsElapsed % 60).padStart(2, '0');
      document.getElementById('sessionTimer').innerText = `${mins}:${secs}`;
    }, 1000);

    function switchLanguage(langCode) {
      currentLang = langCode;
      document.getElementById('telemLang').innerText = (langCode === 'ur-PK') ? 'Urdu (ur-PK)' : 'English (en-US)';
      const listenBtn = document.getElementById('mainListenBtn');
      if (langCode === 'ur-PK') {
        listenBtn.innerHTML = '<i class="fa-solid fa-microphone"></i> بولنا شروع کریں';
        document.getElementById('customInput').placeholder = 'اردو یا انگلش میں لکھیں یا بولیں...';
      } else {
        listenBtn.innerHTML = '<i class="fa-solid fa-microphone"></i> START LISTENING';
        document.getElementById('customInput').placeholder = 'Speak or type here...';
      }
      if (recognition) recognition.lang = langCode;
    }

    function openConfigModal() {
      document.getElementById('modalApiKey').value = apiKey;
      document.getElementById('modalVoiceSelect').value = voice;
      document.getElementById('modalInstructions').value = instructions;
      document.getElementById('configModal').style.display = 'flex';
    }

    function closeConfigModal() {
      document.getElementById('configModal').style.display = 'none';
    }

    function saveConfig() {
      apiKey = document.getElementById('modalApiKey').value.trim();
      voice = document.getElementById('modalVoiceSelect').value;
      instructions = document.getElementById('modalInstructions').value;
      localStorage.setItem('aura_api_key', apiKey);
      localStorage.setItem('aura_voice', voice);
      localStorage.setItem('aura_inst', instructions);
      document.getElementById('voiceDisplay').innerText = voice + ' (Female HD)';
      closeConfigModal();
      addLogMessage('System', 'ترتیبات محفوظ ہو گئیں۔');
    }

    function toggleMute() {
      isMuted = !isMuted;
      document.getElementById('muteBtn').innerHTML = isMuted 
        ? '<i class="fa-solid fa-microphone-slash" style="color:#ff5555;"></i>' 
        : '<i class="fa-solid fa-microphone"></i>';
      if (isMuted) stopSpeakingImmediately();
    }

    // Stop speaking immediately (Barge-in / Interrupt)
    function stopSpeakingImmediately() {
      if (currentAudio) {
        currentAudio.pause();
        currentAudio = null;
      }
      if (window.speechSynthesis) window.speechSynthesis.cancel();
      if (abortController) {
        abortController.abort();
        abortController = null;
      }
      isSpeaking = false;
      updateStateUI();
    }

    // Visualizer Orb Canvas
    const canvas = document.getElementById('orbCanvas');
    const ctx = canvas.getContext('2d');
    let angle = 0;

    function renderOrb() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2;
      const cy = canvas.height / 2;
      angle += 0.02;

      let baseRadius = 85;
      let wave = Math.sin(angle * 2) * 4;

      if (isListening) {
        wave = Math.sin(angle * 6) * 12;
        baseRadius = 90;
      } else if (isSpeaking) {
        wave = Math.sin(angle * 8) * 16;
        baseRadius = 94;
      }

      ctx.beginPath();
      ctx.arc(cx, cy, baseRadius + wave, 0, Math.PI * 2);
      ctx.strokeStyle = isListening ? 'rgba(0, 242, 254, 0.7)' : (isSpeaking ? 'rgba(189, 147, 249, 0.8)' : 'rgba(0, 242, 254, 0.2)');
      ctx.lineWidth = 2;
      ctx.stroke();

      for (let i = 0; i < 42; i++) {
        let pAngle = (i / 42) * Math.PI * 2 + angle;
        let pDist = baseRadius + Math.sin(angle * 3 + i) * 10;
        let px = cx + Math.cos(pAngle) * pDist;
        let py = cy + Math.sin(pAngle) * pDist;

        ctx.beginPath();
        ctx.arc(px, py, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = (i % 2 === 0) ? '#00f2fe' : '#bd93f9';
        ctx.fill();
      }
      requestAnimationFrame(renderOrb);
    }
    renderOrb();

    // Volume Meters Simulator
    setInterval(() => {
      const micMeter = document.getElementById('micMeterFill');
      const micDb = document.getElementById('micDbVal');
      const outMeter = document.getElementById('outMeterFill');
      const outDb = document.getElementById('outDbVal');

      if (isListening) {
        let val = Math.floor(Math.random() * 45) + 35;
        micMeter.style.width = val + '%';
        micDb.innerText = `-${60 - val} dB`;
      } else {
        micMeter.style.width = '10%';
        micDb.innerText = '-48 dB';
      }

      if (isSpeaking) {
        let outVal = Math.floor(Math.random() * 55) + 30;
        outMeter.style.width = outVal + '%';
        outDb.innerText = `-${70 - outVal} dB`;
      } else {
        outMeter.style.width = '6%';
        outDb.innerText = '-68 dB';
      }
    }, 120);

    // Browser Speech-to-Text
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    function initSpeech() {
      if (!SpeechRecognition) {
        addLogMessage('System', 'Google Chrome استعمال کریں تاکہ آواز اور مائیک کی پرمیشن مکمل مل سکے۔');
        return;
      }
      recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = currentLang;

      recognition.onstart = () => {
        isListening = true;
        stopSpeakingImmediately();
        updateStateUI();
      };

      recognition.onresult = (e) => {
        stopSpeakingImmediately();
        const transcript = e.results[0][0].transcript.trim();
        if (transcript) {
          addLogMessage('آپ (User)', transcript);
          processWithAgent(transcript);
        }
      };

      recognition.onerror = (e) => {
        console.error("Mic error:", e);
        isListening = false;
        updateStateUI();
      };

      recognition.onend = () => {
        isListening = false;
        updateStateUI();
      };
    }
    initSpeech();

    function toggleListening() {
      if (isMuted) return;
      if (!recognition) initSpeech();
      if (!recognition) return;

      recognition.lang = currentLang;

      if (!isListening) {
        stopSpeakingImmediately();
        try {
          recognition.start();
        } catch(e) {}
      } else {
        try { recognition.stop(); } catch(e) {}
      }
    }

    function updateStateUI() {
      const stateText = document.getElementById('agentStateText');
      const listenBtn = document.getElementById('mainListenBtn');
      const micIcon = document.getElementById('orbMicIcon');
      const micLabel = document.getElementById('orbMicLabel');

      if (isListening) {
        stateText.innerText = (currentLang === 'ur-PK') ? 'سن رہی ہوں // LISTENING' : 'LISTENING // ACTIVE';
        stateText.style.color = '#00f2fe';
        listenBtn.innerHTML = '<i class="fa-solid fa-stop"></i> مائیک بند کریں';
        micLabel.innerText = 'LISTENING';
        micIcon.style.color = '#00ffaa';
      } else if (isSpeaking) {
        stateText.innerText = (currentLang === 'ur-PK') ? 'جواب دے رہی ہوں // TALKING' : 'SPEAKING...';
        stateText.style.color = '#bd93f9';
        listenBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i> بات کاٹیں (Stop)';
        micLabel.innerText = 'TALKING';
      } else {
        stateText.innerText = 'IDLE // STANDBY';
        stateText.style.color = '#00f2fe';
        listenBtn.innerHTML = (currentLang === 'ur-PK') ? '<i class="fa-solid fa-microphone"></i> بولنا شروع کریں' : '<i class="fa-solid fa-microphone"></i> START LISTENING';
        micLabel.innerText = 'TAP MIC';
        micIcon.style.color = '#00f2fe';
      }
    }

    // Call OpenAI API (Text) then Call OpenAI TTS (Female Audio)
    async function processWithAgent(userText) {
      if (!apiKey) {
        addLogMessage('AURA // AGENT', '🔑 OpenAI API Key موجود نہیں ہے۔ ٹاپ دائیں طرف CONFIG پر کلک کر کے کی درج کریں۔');
        openConfigModal();
        return;
      }

      abortController = new AbortController();
      const startTime = performance.now();
      isSpeaking = true;
      updateStateUI();

      try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
          },
          signal: abortController.signal,
          body: JSON.stringify({
            model: 'gpt-4o-mini',
            messages: [
              { role: 'system', content: instructions },
              { role: 'user', content: userText }
            ],
            max_tokens: 140,
            temperature: 0.6
          })
        });

        const data = await response.json();
        const latency = Math.round(performance.now() - startTime);
        document.getElementById('latencyDisplay').innerText = `${latency} ms`;

        if (data.choices && data.choices[0]) {
          const reply = data.choices[0].message.content.trim();
          addLogMessage('AURA // AGENT', reply);
          await playOpenAIAudio(reply);
        } else if (data.error) {
          addLogMessage('System Error', data.error.message);
          isSpeaking = false;
          updateStateUI();
        }
      } catch (err) {
        if (err.name !== 'AbortError') {
          addLogMessage('System Error', err.message);
        }
        isSpeaking = false;
        updateStateUI();
      }
    }

    // Female Audio Generation using OpenAI TTS
    async function playOpenAIAudio(text) {
      if (!apiKey) return;
      try {
        const ttsResponse = await fetch('https://api.openai.com/v1/audio/speech', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
          },
          signal: abortController ? abortController.signal : null,
          body: JSON.stringify({
            model: 'tts-1',
            voice: voice,
            input: text
          })
        });

        if (!ttsResponse.ok) throw new Error('TTS API failed');

        const audioBlob = await ttsResponse.blob();
        const audioUrl = URL.createObjectURL(audioBlob);

        if (currentAudio) currentAudio.pause();

        currentAudio = new Audio(audioUrl);
        currentAudio.onplay = () => {
          isSpeaking = true;
          updateStateUI();
        };
        currentAudio.onended = () => {
          isSpeaking = false;
          updateStateUI();
        };
        currentAudio.onerror = () => {
          isSpeaking = false;
          updateStateUI();
        };

        await currentAudio.play();
      } catch (err) {
        if (err.name !== 'AbortError') {
          console.warn("TTS Error, fallback to native speech:", err);
          fallbackNativeSpeech(text);
        }
      }
    }

    function fallbackNativeSpeech(text) {
      if (!window.speechSynthesis) return;
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = /[\u0600-\u06FF]/.test(text) ? 'ur-PK' : 'en-US';
      utterance.onstart = () => { isSpeaking = true; updateStateUI(); };
      utterance.onend = () => { isSpeaking = false; updateStateUI(); };
      window.speechSynthesis.speak(utterance);
    }

    function testVoiceSynthesis() {
      const isUrdu = (currentLang === 'ur-PK');
      const testMsg = isUrdu ? 'السلام علیکم! میں آپ کی وائس اسسٹنٹ ہوں اور میری آواز بالکل ٹھیک چل رہی ہے۔' : 'Speech synthesis is online with female HD persona.';
      addLogMessage('AURA // AGENT', testMsg);
      playOpenAIAudio(testMsg);
    }

    function addLogMessage(sender, text) {
      const container = document.getElementById('transcriptContainer');
      const isAgent = sender.includes('AURA') || sender.includes('System');
      const isUrdu = /[\u0600-\u06FF]/.test(text);

      const card = document.createElement('div');
      card.className = `msg-card ${isAgent ? 'msg-agent' : 'msg-user'}`;
      card.innerHTML = `
        <div class="msg-meta">
          <span style="color: ${isAgent ? 'var(--purple)' : 'var(--cyan)'}; font-weight:700;">
            <i class="fa-solid ${isAgent ? 'fa-sparkles' : 'fa-user'}"></i> ${sender}
          </span>
          <span>${new Date().toLocaleTimeString()}</span>
        </div>
        <div class="${isUrdu ? 'urdu-text' : ''}">${text}</div>
      `;
      container.appendChild(card);
      container.scrollTop = container.scrollHeight;
    }

    function flushTranscript() {
      document.getElementById('transcriptContainer').innerHTML = '';
      addLogMessage('System', 'ٹرانسکرپٹ صاف کر دیا گیا ہے۔');
    }

    function usePrompt(text) {
      document.getElementById('customInput').value = text;
      sendTextMessage();
    }

    function handleInputKey(e) {
      if (e.key === 'Enter') sendTextMessage();
    }

    function sendTextMessage() {
      const input = document.getElementById('customInput');
      const val = input.value.trim();
      if (!val) return;
      input.value = '';
      stopSpeakingImmediately();
      addLogMessage('آپ (User)', val);
      processWithAgent(val);
    }
  </script>
</body>
</html>"""

components.html(HTML_CODE, height=920, scrolling=False)