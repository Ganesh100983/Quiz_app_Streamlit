# 🧠 General Knowledge Quiz App

A beautiful and interactive general knowledge quiz application built with Streamlit. Test your knowledge across multiple categories including Science, Geography, History, Arts, Sports, and Technology!

## ✨ Features

- **Multiple Categories**: Questions spanning 6 different knowledge areas
- **Interactive UI**: Modern, responsive design with custom styling
- **Progress Tracking**: Real-time progress bar and timer
- **Instant Feedback**: Immediate feedback on answers with correct/incorrect indicators
- **Detailed Results**: Comprehensive score breakdown and category-wise performance
- **Answer Review**: Complete review of all questions with your answers vs correct answers
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Installation

### Prerequisites
- Python 3.14 or higher
- pip (Python package installer)

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -e .
   ```
   Or install Streamlit directly:
   ```bash
   pip install streamlit
   ```

## 🎮 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Open your browser to the URL shown (usually `http://localhost:8501`)
3. Click "Start Quiz" to begin
4. Answer each question by clicking on your chosen option
5. View your results and detailed breakdown at the end
6. Click "Play Again" to take the quiz again with different questions

## 📋 Requirements

- Python 3.14+
- Streamlit 1.55.0+

Dependencies are defined in `pyproject.toml`.

## 🏗️ Project Structure

```
quiz-app/
├── main.py          # Main application file
├── pyproject.toml   # Project configuration and dependencies
├── README.md        # This file
└── uv.lock          # Lock file for uv package manager
```

## 🎯 How It Works

- The app randomly selects 10 questions from a pool of 30 across 6 categories
- Each quiz session is unique with different question combinations
- Progress is tracked in real-time with a visual progress bar
- Timer shows elapsed time for the entire session
- Score is calculated as percentage correct
- Detailed category breakdown shows performance in each knowledge area
- Answer review table allows users to learn from mistakes

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding more questions to the question bank
- Improving the UI/UX design
- Adding new features or categories
- Fixing bugs or optimizing performance

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Enjoy testing your knowledge! 🧠✨**