#  AI-Powered Analytics Dashboard

This project is a fully responsive, modern AI-powered analytics dashboard built using **Flask**, **HTML/CSS/JavaScript**, and **Chart.js** — with advanced AI summarization and dynamic charting capabilities.

---

##  What It Does

- 📂 Upload your own **CSV** file
- 🤖 Get a **natural-language AI summary** of your data
- 📊 View **interactive charts** by selecting X and Y columns
- 🌙 Toggle between **light and dark themes**
- 🎨 Enjoy a **beautiful, responsive UI** made for clarity

---

## 🛠 Built with the Help of AI

This project was built with **extensive assistance from modern AI coding tools** for planning, coding, design, and debugging.

## ⚠️ Note on AI Performance
  
> This project uses **free-tier AI services** like Hugging Face's public summarization models. As a result:
>
> - ⏳ **AI-generated summaries may take a few seconds to process**, depending on server load.  
> - 🌐 **Internet connectivity and model availability** can affect response time.
>
>  Please be **patient** while your data is being analyzed — it’s all part of working with open, free AI APIs!



###  AI Tools Used:

| 🛠 Tool |  Purpose & Usage |
|--------|--------------------|
| **ChatGPT (OpenAI)** | Brainstormed the project idea, guided backend architecture, generated Flask routing logic, built Jinja-based templates, improved UI/UX layout, and assisted in writing frontend JS/CSS logic. |
| **GitHub Copilot** | Used for auto-completing code, reducing boilerplate typing, and offering context-aware suggestions within VS Code for both Python and JavaScript. |
| **OpenAI GPT-3.5 API** | Initially used to generate AI-powered summaries for uploaded CSV data. Produced clean, human-like insights from tabular datasets. |
| **Hugging Face Transformers** (`facebook/bart-large-cnn`) | Final method for AI summarization after OpenAI API credits ran out. Seamlessly integrated for extracting meaningful summaries from dataframes. |
| **Hugging Face Spaces & Datasets** | Tested summarization models and benchmarking with public datasets before final integration into the app. |
| **Chart.js** | Client-side JavaScript library used to visualize uploaded data dynamically. Fully responsive and customizable chart output. |
| **Google Gemini (experimental)** | Consulted for alternate UI/UX layout strategies and improved design responsiveness across screen sizes. |
| **Claude AI / Bard** | Occasionally referenced for alternative approaches to frontend logic and summarization fallback flows when OpenAI/Hugging Face were not accessible. |

>  I extensively used a combination of AI tools throughout the entire development process – from planning to coding and debugging. This project is a true testament to building with modern AI-first workflows.

>  I initially used OpenAI's GPT-based API for generating AI summaries. However, due to limited API credits, I later switched to **Hugging Face's `facebook/bart-large-cnn` model** for summarizing uploaded CSV data.  
>  Overall, I used **many AI tools** throughout the development process — from generating HTML/CSS code to writing Python logic and improving UI design.

---

## 📁 Project Structure

```
AI-Powered-Analytics-Dashboard/
├── app.py                 # Flask backend: routes, file upload, AI summary, chart data
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css          # Responsive UI design with light/dark mode
│   └── script.js          # Navigation, file upload, Chart.js logic
├── templates/
│   └── index.html         # Main dashboard layout (Overview, Reports, Settings)
├── uploads/               # (Optional) Temp storage for uploaded CSVs
├── README.md              # Project overview + AI usage report
```
