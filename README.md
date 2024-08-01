# Meeting Summarizer and Speech Analyzer

This project provides tools for transcribing and summarizing audio content, particularly useful for meeting recordings or speech analysis.

## 🚀 Key Features

- **Speech-to-Text Transcription**: Utilizes OpenAI's Whisper model for accurate audio transcription.
- **Text Summarization**: Employs a BART-based language model to extract key points from transcribed text.
- **User-Friendly Interface**: Integrates Gradio for an easy-to-use web interface.
- **GPU Acceleration**: Supports CUDA for faster processing on compatible hardware.

## 📁 Main Components

1. `Meeting Summarizer.ipynb`: Jupyter notebook containing the full pipeline implementation using model from HuggingFace.
2. `Speech Analyzer.py`: Python script version of the summarizer, using IBM Watson Machine Learning for LLM integration.

![Demo Screenshot](https://github.com/axiom19/AI-Meeting-Summarizer/blob/main/demos/demo%20img.png)
[Watch the Demo Video](https://github.com/axiom19/AI-Meeting-Summarizer/blob/main/demos/Demo%20Video.mp4)


## 🛠️ Technologies Used

- PyTorch
- Transformers (Hugging Face)
- Langchain
- Gradio
- IBM Watson Machine Learning (for `Speech Analyzer.py`)

## 📊 How It Works

1. **Audio Input**: Users upload an audio file (preferably .mp3) through the Gradio interface.
2. **Transcription**: The OpenAI Whisper model converts speech to text.
3. **Summarization**: The transcribed text is processed by a BART-based language model to extract key points.
4. **Output**: A concise summary of the audio content is presented to the user.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- GPU support (optional, but recommended for faster processing)

### Installation

1. Clone the repository: git clone [https://github.com/axiom19/meeting-summarizer.git]
2. Install required packages

### Demo
- **Screenshot**: A static image showing the user interface and output of the Speech Analyzer.
- **Screen Recording**: A video demonstration of the Speech Analyzer in action, from audio input to summarized output.

![Demo Screenshot](path/to/screenshot.png)

[Watch the Demo Video](link/to/your/video)


### Usage

1. For Jupyter Notebook:
- Open `Meeting Summarizer.ipynb` in a Jupyter environment.
- Run all cells to start the Gradio interface.

2. For Python Script:
- Run `python Speech Analyzer.py` to launch the application.

## 📝 Note

- The project includes additional scripts (`Simple LLM.py` and `Speech to Text App.py`) for standalone LLM testing and speech-to-text conversion.
- Ensure you have the necessary API keys and credentials set up for IBM Watson services when using `Speech Analyzer.py`.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## 📄 License

This project is licensed under the [MIT License](link-to-your-license-file).
