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
- Python 3.11 or higher
- UV package manager (install from [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv))

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies and create virtual environment:
   ```bash
   uv sync
   ```
   This will automatically create a virtual environment and install all required packages.

4. Activate the virtual environment (if needed for manual commands):
   ```bash
   uv run --no-sync streamlit run main.py
   ```
   Or use UV to run commands directly without activation.

## 🎮 Usage

1. Run the Streamlit app:
   ```bash
   uv run streamlit run main.py
   ```
   Or if you prefer to activate the environment first:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   streamlit run main.py
   ```
2. Open your browser to the URL shown (usually `http://localhost:8501`)
3. Click "Start Quiz" to begin
4. Answer each question by clicking on your chosen option
5. View your results and detailed breakdown at the end
6. Click "Play Again" to take the quiz again with different questions

## 📋 Requirements

- Python 3.11+
- UV package manager
- Streamlit 1.55.0+

Dependencies are defined in `pyproject.toml` and locked in `uv.lock`.

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



**Enjoy testing your knowledge! 🧠✨**