
let questionsData = [];

// Fetch the JSON questions file
fetch("python_mcq_questions_100.json")
    .then(response => response.json())
    .then(data => {
        questionsData = data;
        init(); // Call quiz initializer after data is loaded
    })
    .catch(error => {
        console.error("Failed to load questions:", error);
        alert("Unable to load questions. Please make sure 'python_mcq_questions_100.json' is in the same directory.");
    });

// All your quiz logic (copied from previous <script> section in HTML, but wrapped to be triggered after fetch)

// Application state
let currentState = {
    username: '',
    questionCount: 10,
    currentQuestionIndex: 0,
    userAnswers: [],
    quizStarted: false,
    startTime: null,
    endTime: null,
    timerInterval: null,
    timeRemaining: 60
};

// DOM Elements
const userInfoSection = document.getElementById('user-info-section');
const quizSection = document.getElementById('quiz-section');
const resultsSection = document.getElementById('results-section');
const usernameInput = document.getElementById('username');
const questionCountSelect = document.getElementById('question-count');
const startBtn = document.getElementById('start-btn');
const quizContainer = document.getElementById('quiz-container');
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const submitBtn = document.getElementById('submit-btn');
const progressBar = document.getElementById('progress-bar');
const progressText = document.getElementById('progress-text');
const totalQuestionsSpan = document.getElementById('total-questions');
const timerElement = document.getElementById('timer');
const reviewContainer = document.getElementById('review-container');
const resultUsername = document.getElementById('result-username');
const scoreSpan = document.getElementById('score');
const totalSpan = document.getElementById('total');
const correctAnswersSpan = document.getElementById('correct-answers');
const percentageSpan = document.getElementById('percentage');
const timeTakenSpan = document.getElementById('time-taken');
const resultMessage = document.getElementById('result-message');
const restartBtn = document.getElementById('restart-btn');
const resultChart = document.getElementById('result-chart');

startBtn.addEventListener('click', startQuiz);
prevBtn.addEventListener('click', showPreviousQuestion);
nextBtn.addEventListener('click', showNextQuestion);
submitBtn.addEventListener('click', showResults);
restartBtn.addEventListener('click', restartQuiz);

function init() {
    currentState.userAnswers = Array(questionsData.length).fill(null);
}

function startQuiz() {
    const username = usernameInput.value.trim();
    const count = parseInt(questionCountSelect.value);
    if (!username) {
        alert('Please enter your name');
        return;
    }

    const available = Math.min(count, questionsData.length);
    const shuffled = [...questionsData].sort(() => 0.5 - Math.random());
    questionsData = shuffled.slice(0, available);

    currentState.username = username;
    currentState.questionCount = available;
    currentState.currentQuestionIndex = 0;
    currentState.quizStarted = true;
    currentState.startTime = new Date();
    currentState.timeRemaining = 60;
    currentState.userAnswers = Array(available).fill(null);

    userInfoSection.classList.add('hidden');
    quizSection.classList.remove('hidden');

    totalQuestionsSpan.textContent = available;
    updateProgressBar();
    startTimer();
    showQuestion(0);
}

function showQuestion(index) {
    const question = questionsData[index];

    prevBtn.disabled = (index === 0);
    nextBtn.disabled = (index === currentState.questionCount - 1);
    submitBtn.classList.toggle('hidden', index !== currentState.questionCount - 1);

    progressText.textContent = `Question ${index + 1} of ${currentState.questionCount}`;
    questionText.textContent = question.question;
    optionsContainer.innerHTML = '';

    question.options.forEach((option, i) => {
        const optionElement = document.createElement('div');
        optionElement.classList.add('option');
        if (currentState.userAnswers[index] === i) optionElement.classList.add('selected');

        optionElement.innerHTML = `
            <div class="option-prefix">${String.fromCharCode(65 + i)}</div>
            <div class="option-text">${option}</div>
        `;

        optionElement.addEventListener('click', () => {
            document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
            optionElement.classList.add('selected');
            currentState.userAnswers[index] = i;
            updateProgressBar();
        });

        optionsContainer.appendChild(optionElement);
    });

    updateProgressBar();
}

function startTimer() {
    clearInterval(currentState.timerInterval);
    currentState.timerInterval = setInterval(() => {
        currentState.timeRemaining--;
        timerElement.textContent = `${currentState.timeRemaining}s`;
        if (currentState.timeRemaining <= 0) {
            clearInterval(currentState.timerInterval);
            if (currentState.currentQuestionIndex < currentState.questionCount - 1) {
                showNextQuestion();
            } else {
                showResults();
            }
        }
    }, 1000);
}

function updateProgressBar() {
    const answered = currentState.userAnswers.filter(a => a !== null).length;
    const percentage = (answered / currentState.questionCount) * 100;
    progressBar.style.width = `${percentage}%`;
}

function showPreviousQuestion() {
    if (currentState.currentQuestionIndex > 0) {
        currentState.currentQuestionIndex--;
        currentState.timeRemaining = 60;
        showQuestion(currentState.currentQuestionIndex);
        startTimer();
    }
}

function showNextQuestion() {
    if (currentState.currentQuestionIndex < currentState.questionCount - 1) {
        currentState.currentQuestionIndex++;
        currentState.timeRemaining = 60;
        showQuestion(currentState.currentQuestionIndex);
        startTimer();
    }
}

function showResults() {
    clearInterval(currentState.timerInterval);
    currentState.endTime = new Date();

    const timeTaken = Math.floor((currentState.endTime - currentState.startTime) / 1000);
    let score = 0;

    for (let i = 0; i < currentState.questionCount; i++) {
        const question = questionsData[i];
        if (currentState.userAnswers[i] === question.answer) score++;
    }

    quizSection.classList.add('hidden');
    resultsSection.classList.remove('hidden');

    resultUsername.textContent = currentState.username;
    scoreSpan.textContent = score;
    totalSpan.textContent = currentState.questionCount;
    correctAnswersSpan.textContent = score;
    percentageSpan.textContent = Math.round((score / currentState.questionCount) * 100) + '%';
    timeTakenSpan.textContent = timeTaken + 's';

    const percent = (score / currentState.questionCount) * 100;
    resultMessage.textContent = percent >= 90 ? "Excellent! You're a Python Master!" :
                                percent >= 70 ? "Great job! You have strong Python knowledge!" :
                                percent >= 50 ? "Good effort! Keep learning and practicing!" :
                                "Keep practicing! Review the concepts and try again!";

    createResultChart(score, currentState.questionCount - score);

    let reviewHTML = '';
    for (let i = 0; i < currentState.questionCount; i++) {
        const question = questionsData[i];
        const userAnswerIndex = currentState.userAnswers[i];
        const isCorrect = userAnswerIndex === question.answer;
        reviewHTML += `
            <div class="review-item ${isCorrect ? 'correct' : 'incorrect'}">
                <div class="question-text">${i + 1}. ${question.question}</div>
                <p><strong>Your answer:</strong> ${userAnswerIndex !== null ? 
                    String.fromCharCode(65 + userAnswerIndex) + '. ' + question.options[userAnswerIndex] : 
                    'No answer'}</p>
                <p><strong>Correct answer:</strong> ${String.fromCharCode(65 + question.answer)}. ${question.options[question.answer]}</p>
                <div class="explanation">${question.explanation}</div>
            </div>
        `;
    }

    reviewContainer.innerHTML = reviewHTML;
}

function createResultChart(correct, incorrect) {
    const ctx = resultChart.getContext('2d');
    if (window.resultChartInstance) window.resultChartInstance.destroy();

    window.resultChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Correct', 'Incorrect'],
            datasets: [{
                data: [correct, incorrect],
                backgroundColor: ['rgba(72, 187, 120, 0.8)', 'rgba(229, 62, 62, 0.8)'],
                borderColor: ['rgba(72, 187, 120, 1)', 'rgba(229, 62, 62, 1)'],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { color: 'white', font: { size: 14 } }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.7)',
                    titleFont: { size: 16 },
                    bodyFont: { size: 14 }
                }
            },
            cutout: '65%',
            animation: { animateRotate: true, animateScale: true }
        }
    });
}

function restartQuiz() {
    resultsSection.classList.add('hidden');
    userInfoSection.classList.remove('hidden');
    currentState = {
        username: '',
        questionCount: 10,
        currentQuestionIndex: 0,
        userAnswers: [],
        quizStarted: false,
        timeRemaining: 60
    };
    usernameInput.value = '';
    questionCountSelect.value = '10';
}
