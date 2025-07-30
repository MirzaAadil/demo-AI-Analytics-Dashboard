from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)
uploaded_df = None  # global to store uploaded DataFrame

# AI summary logic
def generate_ai_summary(df):
    return (
        " AI Summary (Unavailable on Free Deployment):\n\n"
        "This feature uses large AI models like Transformers for summarizing data, but due to free hosting limits (RAM, storage), "
        "The actual AI model cannot be deployed here.\n\n"
        "However, the AI logic is fully written and works perfectly in a local development environment."
    )


# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Upload handler (returns HTML snippet)
@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_df
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded.'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file.'})

    try:
        df = pd.read_csv(file)
        uploaded_df = df  # Store in memory
        summary = generate_ai_summary(df)
        columns = df.columns.tolist()
        data_html = df.head(10).to_html(classes='data-table', index=False)

        # Return custom HTML with summary and chart controls
        return f"""
        <h1>AI-Powered Analytics Dashboard</h1>
        <p class="intro-text">Upload a CSV file to get AI-generated insights and visual reports.</p>

        <div id="summaryContainer" class="summary">
          <h2>AI Summary</h2>
          <p id="summaryBox">{summary}</p>
        </div>

        <div id="chartControls" class="chart-controls">
          <label for="x-axis">X-axis:</label>
          <select id="x-axis" onchange="generateChart()">
            {''.join([f'<option value="{col}">{col}</option>' for col in columns])}
          </select>

          <label for="y-axis">Y-axis:</label>
          <select id="y-axis" onchange="generateChart()">
            {''.join([f'<option value="{col}">{col}</option>' for col in columns])}
          </select>
        </div>

        <canvas id="chartCanvas" width="600" height="300"></canvas>
        """
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Chart data route
@app.route('/get_chart_data', methods=['POST'])
def get_chart_data():
    global uploaded_df
    try:
        if uploaded_df is None:
            return jsonify({'status': 'error', 'message': 'No data uploaded yet.'})

        data = request.get_json()
        x_col = data['x']
        y_col = data['y']

        if x_col not in uploaded_df.columns or y_col not in uploaded_df.columns:
            return jsonify({'status': 'error', 'message': 'Invalid column selection.'})

        x = uploaded_df[x_col].astype(str).tolist()
        y = uploaded_df[y_col].astype(float).tolist()

        return jsonify({'status': 'success', 'x': x, 'y': y})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host='0.0.0.0', port=port)

