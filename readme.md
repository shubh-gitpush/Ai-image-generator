<!--
  README.md with HTML inside Markdown
  Replace placeholders (YOUR-USERNAME, YOUR-REPO, etc.) before committing.
-->

<div align="center">

  <!-- Hero / Title -->
  <h1 style="margin-bottom:0.2rem;">🧠 AI Prompt Generator</h1>
  <p style="margin-top:0.2rem;">Django + Django REST Framework backend • React frontend — type a prompt and get AI-generated responses via API key</p>

  <!-- Badges (shields.io) -->
  <p>
    <img alt="Django" src="https://img.shields.io/badge/Django-3.2%2B-092E20?logo=django&logoColor=white" />
    <img alt="DRF" src="https://img.shields.io/badge/Django--REST--Framework-3.12-blue?logo=django" />
    <img alt="React" src="https://img.shields.io/badge/React-18-blue?logo=react&logoColor=white" />
    <img alt="License" src="https://img.shields.io/badge/License-MIT-green" />
    <img alt="Docker" src="https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white" />
  </p>
</div>

<hr />

<!-- Two-column style using HTML table for nicer layout -->
<table>
  <tr>
    <td width="65%" valign="top">

## ✨ Project Overview

This repository contains a full-stack application that wires a **React** frontend to a **Django + Django REST Framework** backend.  
Users enter free-text prompts in the frontend; the backend forwards the prompt to an external AI service using a secured API key and returns the generated response to the user.

**Primary goals**
- Quick, interactive prompt → AI response experience  
- Secure API key usage on server-side (never expose secret keys in the frontend)  
- Clean separation between frontend and backend for scaling and deployment  
- Container-ready with **Docker** for easy deployment anywhere

</td>
    <td width="35%" valign="top">

<!-- Screenshot placeholder (replace with your real screenshot) -->
<figure>
  <img src="img.png" alt="App screenshot" style="max-width:100%;border-radius:8px"max-height:100%;">
  
</figure>

</td>
  </tr>
</table>

---

## 🚀 Features

<ul>
  <li><strong>Prompt → Response</strong>: Type anything and get an AI-generated reply.</li>
  <li><strong>Secure Key Handling</strong>: API keys live on the backend; frontend only calls your DRF endpoints.</li>
  <li><strong>Modern Frontend</strong>: React with Hooks for a responsive UI.</li>
  <li><strong>Extensible Backend</strong>: Django + DRF endpoints to integrate other services later.</li>
  <li><strong>Configurable DB</strong>: SQLite by

