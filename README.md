# Journal Vetting Assistant

This Python application helps research labs process and evaluate academic journals. It:

* **Reads** PDF files from a `resources/` folder
* **Summarizes** each journal to reduce verbosity
* **Splits** text into chunks for embedding
* **Prompts** a language model (via LangChain) to recommend journals based on user-defined criteria

> **Note:** Only PDF files are supported. Place your PDFs into the `project/resources/` directory before running.

---

## Features

* Extract raw text from PDFs using PyMuPDF
* Interactive metadata template creation via console prompts
* Text splitting into \~50-token chunks using LangChain's `TokenTextSplitter`
* Summarization of each journal to keep prompts concise
* Querying an OpenAI Chat model (GPT-4.1) through LangChain to recommend journals

---

## Prerequisites

* Python 3.8 or newer
* A valid OpenAI API key

---

## Installation

1. **Clone this repository**

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**

   ```bash
   pip install langchain openai python-dotenv pymupdf
   ```

---

## Configuration

1. **Environment Variables**

   Create a `.env` file at the project root (adjacent to your script) with:

   ```text
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Resource Folder**

   Place all your journal PDF files in:

   ```
   ```

project/project/resources/

````
   The script will automatically load every `.pdf` found there.

---

## Usage

Run the main script:

```bash
python run_journal_vetting.py
````

1. The app will **read** all PDFs in `resources/`.
2. It will **summarize** each journal.
3. You’ll be prompted to **define metadata keys and values** (e.g., `field: computational modeling`, `impact_factor: >5`).
4. Finally, the app will **query GPT-4.1** to recommend the best-fit journal(s) and print the result.

---

## Project Structure

```
project/
├── resources/       # Place your .pdf journal files here
├── run_journal_vetting.py  # Main application script
├── requirements.txt # (Optional) dependencies list
├── .env             # OpenAI API key
└── README.md        # This file
```

---

## Customization

* **Chunk size**: Adjust `chunk_size` and `chunk_overlap` in `createembeddings()`.
* **Model settings**: Modify `model_name`, `temperature`, and `max_tokens` in the `ChatOpenAI` constructor.
* **Prompt templates**: Tweak the wording in `buildquery()` or `compressjournals()` to fit your vetting criteria.

---

## Contributing

Feel free to open issues or pull requests for additional features, bug fixes, or enhancements.

---
