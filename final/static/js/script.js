// Load the selected page section
function loadPage(page) {
  document.querySelectorAll(".page-section").forEach((sec) => {
    sec.style.display = "none";
  });
  document.getElementById(page).style.display = "block";
}

// Upload and analyze CSV file
function uploadCSV() {
  const fileInput = document.getElementById("csvFile");
  const file = fileInput.files[0];
  if (!file) {
    alert("Please select a file.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.text())
    .then((html) => {
      // Insert the returned HTML into the Overview section
      document.getElementById("overview").innerHTML = html;
      loadPage("overview");
    })
    .catch((err) => {
      alert("Error uploading file: " + err.message);
    });
}

// Generate chart from selected X and Y columns
function generateChart() {
  const xCol = document.getElementById("x-axis").value;
  const yCol = document.getElementById("y-axis").value;

  fetch("/get_chart_data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ x: xCol, y: yCol }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.status === "success") {
        const ctx = document.getElementById("chartCanvas").getContext("2d");
        if (window.chartInstance) window.chartInstance.destroy(); // Destroy old chart

        window.chartInstance = new Chart(ctx, {
          type: "bar",
          data: {
            labels: data.x,
            datasets: [
              {
                label: `${yCol} vs ${xCol}`,
                data: data.y,
                backgroundColor: "rgba(54, 162, 235, 0.5)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            scales: {
              y: { beginAtZero: true },
            },
          },
        });
      }
    });
}

// Toggle light/dark theme
function toggleTheme() {
  document.body.classList.toggle("dark-mode");
}
