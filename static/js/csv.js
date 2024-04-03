const uploadBtn = document.getElementById('uploadBtn');
const modal = document.getElementById('modal');
const closeBtn = document.getElementById('closeBtn');
const analysisBtn = document.getElementById('analysisBtn');
const churnPredictionBtn = document.getElementById('churnPredictionBtn');

uploadBtn.addEventListener('click', () => {
  modal.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
  modal.style.display = 'none';
});

analysisBtn.addEventListener('click', () => {
  // Redirect to analysis page
  window.location.href = 'analysis.html';
});

churnPredictionBtn.addEventListener('click', () => {
  // Redirect to churn prediction page
  window.location.href = 'churn_prediction.html';
});
