# AI-Powered Analytics Dashboard (Free Version)

This is the free-to-deploy version of my **AI-Powered Analytics Dashboard** project. The original full version uses advanced AI models (`transformers`, `torch`, etc.) to generate real-time data insights, but unfortunately, deploying that setup requires more than 4 GB of storage and compute resources — which exceeds the limits of free hosting platforms like Railway, Render, and Replit.

##  Why This Version?

Due to limitations on free hosting platforms:

- **Disk quotas** and **build size limits** made it impossible to deploy the original AI-powered version.
- Running local models like `transformers` and `torch` requires heavy dependencies.
- Many platforms restrict memory to **1 GB** and image sizes to **4 GB max**, which isn't enough for AI inference workloads.

### So what’s included in this version?

✅ Fully working frontend  
✅ Upload CSVs and view basic data previews  
✅ Static AI-like summary as a **placeholder**  
✅ Charts and visual insights  
❌ No live AI model inference (due to resource limits)

##  What does the full version have?

In the full version (not deployed due to cost constraints), the backend uses:

- Hugging Face Transformers (BERT/GPT models)
- Torch for inference
- Pandas for CSV processing
- OpenAI/LLM integration (optional)

If deployed on a paid plan or a local server, it will provide **real AI-generated insights** from the uploaded data.

##  Future Plans

- Host the full version on a cloud VM or paid container service
- Switch to Hugging Face APIs (hosted models) to reduce dependency size
- Optimize dependencies to fit within free-tier quotas

##  Note for Reviewers or Clients

> This version is meant **only for demo/portfolio purposes.** The real AI logic is implemented in code, but it is not deployed here due to the free-tier limitations.  
> Please refer to the source code to review AI implementation, or reach out for a local setup demo.
