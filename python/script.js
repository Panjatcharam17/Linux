// script.js
let questions = [];       // Full pool of questions from JSON
let selectedQs = [];      // Selected subset for this quiz attempt
let answers = [];         // User answers array (index of chosen option)
let currentPage = 0;      // Current page index (0-based)
let userName = '';
let numQuestionsWanted = 0;

// Load questions from JSON file on page load
fetch('questions.json')
  .then(response => response.json())
  .then(data => { questions = data; })
  .catch(error => { console.error('Error loading questions:', error); });

// Start button listener
document.getElementById('start-btn').addEventListener('click', startQuiz);

function startQuiz() {
    userName = document.getElementById('username').value.trim();
    numQuestionsWanted = parseInt(document.getElementById('numQuestions').value);
    if (!userName || !numQuestionsWanted || numQuestionsWanted < 1) {
        alert('Please enter your name and a valid number of questions.');
        return;
    }
    // Shuffle questions pool and pick requested number
    let pool = questions.slice();
    shuffleArray(pool);
    // Limit to available questions
    numQuestionsWanted = Math.min(numQuestionsWanted, pool.length);
    selectedQs = pool.slice(0, numQuestionsWanted);
    answers = Array(numQuestionsWanted).fill(null);

    // Hide start screen, show quiz
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('quiz-container').classList.remove('hidden');
    currentPage = 0;
    showPage(0);
}

function showPage(page) {
    currentPage = page;
    const container = document.getElementById('quiz-container');
    container.innerHTML = '';

    // Calculate question indices for this page
    const startIdx = page * 10;
    const endIdx = Math.min(startIdx + 10, selectedQs.length);

    // Render each question on this page
    for (let i = startIdx; i < endIdx; i++) {
        const q = selectedQs[i];
        // Question text
        const qDiv = document.createElement('div');
        qDiv.className = 'question';
        const qTitle = document.createElement('p');
        qTitle.textContent = `Q${i+1}. ${q.question}`;
        qDiv.appendChild(qTitle);

        // Options as radio buttons
        const optDiv = document.createElement('div');
        optDiv.className = 'options';
        q.options.forEach((opt, idx) => {
            const label = document.createElement('label');
            const radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = 'q' + i;
            radio.value = idx;
            // Check if user already answered this question
            if (answers[i] === idx) {
                radio.checked = true;
            }
            // Update answer on change
            radio.addEventListener('change', () => {
                answers[i] = idx;
            });
            label.appendChild(radio);
            label.appendChild(document.createTextNode(' ' + opt));
            optDiv.appendChild(label);
        });
        qDiv.appendChild(optDiv);
        container.appendChild(qDiv);
    }

    // Navigation buttons
    const nav = document.createElement('nav');
    // Previous button
    if (page > 0) {
        const prevBtn = document.createElement('button');
        prevBtn.textContent = 'Previous';
        prevBtn.addEventListener('click', () => showPage(page - 1));
        nav.appendChild(prevBtn);
    }
    // Next or Submit
    if (endIdx < selectedQs.length) {
        const nextBtn = document.createElement('button');
        nextBtn.textContent = 'Next';
        nextBtn.addEventListener('click', () => showPage(page + 1));
        nav.appendChild(nextBtn);
    } else {
        const submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit';
        submitBtn.addEventListener('click', submitQuiz);
        nav.appendChild(submitBtn);
    }
    container.appendChild(nav);
}

// Fisher-Yates shuffle for randomization
function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}

function submitQuiz() {
    // Calculate score
    let score = 0;
    selectedQs.forEach((q, idx) => {
        if (answers[idx] === q.answer) {
            score++;
        }
    });

    // Hide quiz, show results
    document.getElementById('quiz-container').classList.add('hidden');
    const resultDiv = document.getElementById('result-container');
    resultDiv.classList.remove('hidden');
    resultDiv.innerHTML = `<h2>${userName}, your score is ${score} out of ${selectedQs.length}.</h2>`;

    // Show each question with correct answer
    const breakdown = document.createElement('div');
    selectedQs.forEach((q, idx) => {
        const p = document.createElement('p');
        const userAnsIdx = answers[idx];
        const correctAnsIdx = q.answer;
        const userText = userAnsIdx != null ? q.options[userAnsIdx] : '<em>No answer</em>';
        const correctText = q.options[correctAnsIdx];
        p.innerHTML = `<strong>Q${idx+1}:</strong> ${q.question}<br>
                       Your answer: ${userText}<br>
                       Correct answer: ${correctText}`;
        breakdown.appendChild(p);
    });
    resultDiv.appendChild(breakdown);
}
