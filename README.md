# Journal Vetting Assistant

A CLI tool and Python library for vetting scientific journals via LLM-based summaries and scoring.

## Features

- **PDF ingestion**: Read and process local PDF files.  
- **Config-driven**: Central YAML config merges with CLI overrides.  
- **LLM summaries**: Condense full-text into focused summaries (methods, data, etc.).  
- **Fit scoring**: Assign a 0–10 score against user-defined criteria.  
- **Single recommendation**: Outputs “Recommended Journal: …” with rationale (CLI) or a single title (Library).  
- **Clean workspace**: Auto-clears your `resources/` folder each run.  

## Installation

```bash
pip install journal-vetter
```
## Or for local development:

```bash
git clone https://github.com/YourName/JournalAnalyzer.git
cd JournalAnalyzer
pip install -e .
```

## Quickstart

   - **Prepare your config (config.yaml at repo root):**
   ```
      criteria:
         field: "cancer research"
         impact_factor: ">5"
         cell_line: "MCF10A"
         model_type: "Mechanistic"

      model:
         name: gpt-4.1
         temperature: 0.0
         max_tokens: 512

      paths:
         resources_dir: resources
         output_file:  output/recommendations.txt

      - **Run the CLI with one or more PDFs**
   ```

   ## Example CLI usage (2 journals)
   
   ```journal-vetter \
   --config config.yaml \
   --download "/path/to/JournalA.pdf" \
   --download "/path/to/JournalB.pdf" \
   --field "oncology"
  ```

  ## Library Usage

```
   from journalvetter import load_config, do_vet_journals
   from pathlib import Path

   cfg = load_config("config.yaml")
   root = Path(".")

   do_vet_journals(
   cfg,
   root / "config.yaml",
   root / "resources",
   root / "output/recommendations.txt",
   field="oncology",
   impact_factor=">5",
   cell_line="MCF10A",
   model_type="Mechanistic",
   )
```

## CLI Options

Usage: journal-vetter [OPTIONS]

```
Options:
   --config TEXT           Path to YAML config file (default: config.yaml)
   --download PATH         Path to local PDF (repeatable)
   --field TEXT            Override research field
   --impact-factor TEXT    Override impact-factor criteria
   --cell-line TEXT        Override cell-line criteria
   --model-type TEXT       Override model-type criteria
   --help                  Show this message and exit.
```


