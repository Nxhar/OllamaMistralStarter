# Mistral-7B-Instruct v0.3 Local Run Starter

This repo is a starter to pull and install the **mistral-7b-instruct v0.3** model.

## Prerequisites

- [Ollama](https://ollama.com/) installed on your system
- Python 3.9+ (for running the example script)
- Python packages installed from requirements.txt

## Step 1: Clone this Repository

```sh
git clone https://github.com/Nxhar/OllamaMistralStarter.git
cd OllamaMistralStarter
```

## Step 2: Build the Model from the Modelfile

```sh
ollama create local-mistral -f Modelfile
```

This command will build the model named `local-mistral` using the provided `Modelfile`.

## Step 3: Verify the Model

List your local models to confirm:

```sh
ollama list
```

You should see `local-mistral` in the list.

## Step 4: Install Python Dependencies

```sh
pip install -r requirements.txt # You can add more requirements if you want to run langgraph
```

## Step 5: Run the Example Script

```sh
python ollamarun.py
```

This will stream a response from the model using the prompt defined in `ollamarun.py`.

---

**Note:**  
- You can modify the prompt or input in `ollamarun.py` as needed.
- For more information - [Ollama Documentation](https://ollama.com/docs).