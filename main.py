import streamlit as st
import random
import time

# ─────────────────────────────────────────────────────────
# 🧠  Simple General Knowledge Quiz App
# ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="🧠 General Knowledge Quiz",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* Global */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }

    /* Hero title */
    .hero-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #f9d423, #ff4e50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        padding-top: 1rem;
    }
    .hero-sub {
        text-align: center;
        color: #b0b0cc;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Question card */
    .question-card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(18px);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    }
    .question-text {
        font-size: 1.35rem;
        font-weight: 600;
        color: #eee;
        margin-bottom: 0.4rem;
    }
    .question-meta {
        font-size: 0.85rem;
        color: #9a8fc2;
        margin-bottom: 0;
    }

    /* Progress bar */
    .progress-container {
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        height: 10px;
        margin-bottom: 1.8rem;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #f9d423, #ff4e50);
        transition: width 0.5s ease;
    }

    /* Stats row */
    .stats-row {
        display: flex;
        justify-content: center;
        gap: 1.4rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    .stat-badge {
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 14px;
        padding: 0.6rem 1.3rem;
        color: #d8d4f0;
        font-weight: 600;
        font-size: 0.95rem;
        text-align: center;
        min-width: 120px;
    }

    /* Result card */
    .result-card {
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(18px);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 24px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        margin-top: 1rem;
    }
    .result-score {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #f9d423, #ff4e50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .result-label {
        color: #b0b0cc;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    .result-msg {
        font-size: 1.3rem;
        font-weight: 700;
        color: #eee;
        margin-bottom: 0.5rem;
    }

    /* Correct / Wrong feedback */
    .feedback-correct {
        background: rgba(0,200,83,0.12);
        border: 1px solid rgba(0,200,83,0.35);
        border-radius: 14px;
        padding: 1rem 1.4rem;
        color: #69f0ae;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .feedback-wrong {
        background: rgba(255,23,68,0.12);
        border: 1px solid rgba(255,23,68,0.35);
        border-radius: 14px;
        padding: 1rem 1.4rem;
        color: #ff5252;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Review table */
    .review-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 0.5rem;
    }
    .review-table th {
        color: #9a8fc2;
        font-weight: 600;
        text-align: left;
        padding: 0.5rem 0.8rem;
        font-size: 0.85rem;
    }
    .review-table td {
        background: rgba(255,255,255,0.04);
        color: #d8d4f0;
        padding: 0.7rem 0.8rem;
        font-size: 0.9rem;
    }
    .review-table tr td:first-child { border-radius: 10px 0 0 10px; }
    .review-table tr td:last-child  { border-radius: 0 10px 10px 0; }

    /* Button overrides */
    .stButton>button {
        border-radius: 14px;
        font-weight: 600;
        padding: 0.6rem 2rem;
        border: none;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(249,212,35,0.25);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# ── Question Bank ────────────────────────────────────────
QUESTIONS = [
    # Science
    {"q": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Fe", "Go"], "answer": "Au", "category": "Science"},
    {"q": "How many bones are in the adult human body?", "options": ["196", "206", "216", "186"], "answer": "206", "category": "Science"},
    {"q": "What planet is known as the Red Planet?", "options": ["Venus", "Jupiter", "Mars", "Saturn"], "answer": "Mars", "category": "Science"},
    {"q": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide", "category": "Science"},
    {"q": "What is the speed of light in km/s (approximately)?", "options": ["150,000", "300,000", "450,000", "600,000"], "answer": "300,000", "category": "Science"},

    # Geography
    {"q": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": "Canberra", "category": "Geography"},
    {"q": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile", "category": "Geography"},
    {"q": "Which country has the most natural lakes?", "options": ["USA", "Brazil", "Canada", "Russia"], "answer": "Canada", "category": "Geography"},
    {"q": "Mount Everest is located on the border of which two countries?", "options": ["India & China", "Nepal & China", "Nepal & India", "Bhutan & China"], "answer": "Nepal & China", "category": "Geography"},
    {"q": "What is the smallest country in the world by area?", "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "answer": "Vatican City", "category": "Geography"},

    # History
    {"q": "In which year did World War II end?", "options": ["1943", "1944", "1945", "1946"], "answer": "1945", "category": "History"},
    {"q": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"], "answer": "George Washington", "category": "History"},
    {"q": "The ancient city of Rome was built on how many hills?", "options": ["5", "6", "7", "8"], "answer": "7", "category": "History"},
    {"q": "Which civilization built Machu Picchu?", "options": ["Aztec", "Maya", "Inca", "Olmec"], "answer": "Inca", "category": "History"},
    {"q": "In which year did the Titanic sink?", "options": ["1910", "1911", "1912", "1913"], "answer": "1912", "category": "History"},

    # Arts & Literature
    {"q": "Who painted the Mona Lisa?", "options": ["Michelangelo", "Raphael", "Leonardo da Vinci", "Donatello"], "answer": "Leonardo da Vinci", "category": "Arts"},
    {"q": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "answer": "William Shakespeare", "category": "Arts"},
    {"q": "Which novel begins with 'Call me Ishmael'?", "options": ["Moby-Dick", "The Old Man and the Sea", "Treasure Island", "Robinson Crusoe"], "answer": "Moby-Dick", "category": "Arts"},
    {"q": "What art movement is Salvador Dalí associated with?", "options": ["Cubism", "Impressionism", "Surrealism", "Pop Art"], "answer": "Surrealism", "category": "Arts"},
    {"q": "How many symphonies did Beethoven compose?", "options": ["7", "8", "9", "10"], "answer": "9", "category": "Arts"},

    # Sports
    {"q": "In which sport is the term 'love' used to indicate zero?", "options": ["Badminton", "Cricket", "Tennis", "Golf"], "answer": "Tennis", "category": "Sports"},
    {"q": "How many players are on a standard soccer team on the field?", "options": ["9", "10", "11", "12"], "answer": "11", "category": "Sports"},
    {"q": "Which country hosted the 2016 Summer Olympics?", "options": ["China", "UK", "Brazil", "Japan"], "answer": "Brazil", "category": "Sports"},
    {"q": "What is the national sport of Japan?", "options": ["Karate", "Judo", "Sumo Wrestling", "Kendo"], "answer": "Sumo Wrestling", "category": "Sports"},
    {"q": "In cricket, how many runs is a maximum hit (six)?", "options": ["4", "5", "6", "8"], "answer": "6", "category": "Sports"},

    # Technology
    {"q": "Who is known as the father of the computer?", "options": ["Alan Turing", "Charles Babbage", "John von Neumann", "Tim Berners-Lee"], "answer": "Charles Babbage", "category": "Technology"},
    {"q": "What does 'HTTP' stand for?", "options": ["HyperText Transfer Protocol", "High Tech Transfer Program", "HyperText Transmission Protocol", "Home Tool Transfer Protocol"], "answer": "HyperText Transfer Protocol", "category": "Technology"},
    {"q": "In what year was the first iPhone released?", "options": ["2005", "2006", "2007", "2008"], "answer": "2007", "category": "Technology"},
    {"q": "What programming language is known as the 'language of the web'?", "options": ["Python", "Java", "JavaScript", "C++"], "answer": "JavaScript", "category": "Technology"},
    {"q": "What does 'AI' stand for?", "options": ["Automated Intelligence", "Artificial Intelligence", "Applied Integration", "Algorithmic Inference"], "answer": "Artificial Intelligence", "category": "Technology"},
]

NUM_QUESTIONS = 10  # Questions per quiz session


# ── Helper Functions ─────────────────────────────────────
def init_session():
    """Initialize / reset the quiz session state."""
    selected = random.sample(QUESTIONS, NUM_QUESTIONS)
    st.session_state.update({
        "questions": selected,
        "current_q": 0,
        "score": 0,
        "answers": [],          # list of dicts with user answer & correctness
        "quiz_active": True,
        "answered": False,      # has current question been answered?
        "selected_option": None,
        "start_time": time.time(),
    })


def category_emoji(cat: str) -> str:
    return {
        "Science": "🔬", "Geography": "🌍", "History": "📜",
        "Arts": "🎨", "Sports": "⚽", "Technology": "💻",
    }.get(cat, "❓")


def grade_label(pct: float) -> tuple[str, str]:
    if pct >= 90: return "🏆 Outstanding!", "You're a quiz master!"
    if pct >= 70: return "🌟 Great Job!", "Very impressive knowledge!"
    if pct >= 50: return "👍 Good Effort!", "You know your stuff — keep going!"
    if pct >= 30: return "📖 Keep Learning!", "A little more practice and you'll shine!"
    return "💪 Don't Give Up!", "Every expert was once a beginner!"


# ── Initialize State ─────────────────────────────────────
if "quiz_active" not in st.session_state:
    init_session()


# ── HEADER ───────────────────────────────────────────────
st.markdown('<h1 class="hero-title">🧠 General Knowledge Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Test your knowledge across Science, Geography, History, Arts, Sports & Tech</p>', unsafe_allow_html=True)


# ── QUIZ IN PROGRESS ─────────────────────────────────────
if st.session_state.quiz_active:
    idx = st.session_state.current_q
    total = len(st.session_state.questions)
    q_data = st.session_state.questions[idx]

    # Progress bar
    pct = int((idx / total) * 100)
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-fill" style="width:{pct}%"></div>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    elapsed = int(time.time() - st.session_state.start_time)
    mins, secs = divmod(elapsed, 60)
    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-badge">📋 Question {idx + 1} / {total}</div>
        <div class="stat-badge">✅ Score: {st.session_state.score}</div>
        <div class="stat-badge">⏱️ {mins:02d}:{secs:02d}</div>
        <div class="stat-badge">{category_emoji(q_data["category"])} {q_data["category"]}</div>
    </div>
    """, unsafe_allow_html=True)

    # Question card
    st.markdown(f"""
    <div class="question-card">
        <p class="question-text">{q_data["q"]}</p>
        <p class="question-meta">{category_emoji(q_data["category"])} {q_data["category"]}  •  Question {idx + 1} of {total}</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Answer phase ──
    if not st.session_state.answered:
        cols = st.columns(2)
        for i, opt in enumerate(q_data["options"]):
            with cols[i % 2]:
                if st.button(opt, key=f"opt_{idx}_{i}", use_container_width=True):
                    is_correct = (opt == q_data["answer"])
                    if is_correct:
                        st.session_state.score += 1
                    st.session_state.answers.append({
                        "question": q_data["q"],
                        "your_answer": opt,
                        "correct_answer": q_data["answer"],
                        "is_correct": is_correct,
                        "category": q_data["category"],
                    })
                    st.session_state.selected_option = opt
                    st.session_state.answered = True
                    st.rerun()
    else:
        # Show feedback
        selected = st.session_state.selected_option
        correct = q_data["answer"]
        if selected == correct:
            st.markdown(f'<div class="feedback-correct">✅ Correct! The answer is <strong>{correct}</strong>.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="feedback-wrong">❌ Wrong! You chose <strong>{selected}</strong>. The correct answer is <strong>{correct}</strong>.</div>', unsafe_allow_html=True)

        # Next / Finish button
        if idx + 1 < total:
            if st.button("Next Question ➡️", use_container_width=True):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.session_state.selected_option = None
                st.rerun()
        else:
            if st.button("🏁 See Results", use_container_width=True):
                st.session_state.quiz_active = False
                st.rerun()


# ── RESULTS SCREEN ────────────────────────────────────────
else:
    score = st.session_state.score
    total = len(st.session_state.questions)
    pct = int((score / total) * 100)
    elapsed = int(time.time() - st.session_state.start_time)
    mins, secs = divmod(elapsed, 60)
    title, subtitle = grade_label(pct)

    st.markdown(f"""
    <div class="result-card">
        <div class="result-score">{score} / {total}</div>
        <p class="result-label">You scored {pct}% in {mins:02d}:{secs:02d}</p>
        <p class="result-msg">{title}</p>
        <p class="result-label">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Category breakdown
    st.markdown("### 📊 Category Breakdown")
    cats = {}
    for a in st.session_state.answers:
        c = a["category"]
        if c not in cats:
            cats[c] = {"correct": 0, "total": 0}
        cats[c]["total"] += 1
        if a["is_correct"]:
            cats[c]["correct"] += 1

    cols = st.columns(min(len(cats), 3))
    for i, (cat, data) in enumerate(cats.items()):
        with cols[i % 3]:
            cat_pct = int((data["correct"] / data["total"]) * 100)
            st.markdown(f"""
            <div class="stat-badge" style="margin-bottom:0.8rem;width:100%">
                {category_emoji(cat)} {cat}<br>
                <span style="font-size:1.3rem">{data['correct']}/{data['total']}</span>
                <span style="font-size:0.8rem;color:#9a8fc2">({cat_pct}%)</span>
            </div>
            """, unsafe_allow_html=True)

    # Review table
    st.markdown("### 📝 Answer Review")
    rows = ""
    for i, a in enumerate(st.session_state.answers, 1):
        icon = "✅" if a["is_correct"] else "❌"
        rows += f"""<tr>
            <td>{i}</td>
            <td>{a['question']}</td>
            <td>{a['your_answer']}</td>
            <td>{a['correct_answer']}</td>
            <td>{icon}</td>
        </tr>"""

    st.markdown(f"""
    <table class="review-table">
        <thead><tr>
            <th>#</th><th>Question</th><th>Your Answer</th><th>Correct Answer</th><th></th>
        </tr></thead>
        <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("")
    if st.button("🔄 Play Again", use_container_width=True):
        init_session()
        st.rerun()
