"Agent-as-Coder" Challenge: Bank Statement Parser Agent
This project contains an autonomous AI agent designed to automatically generate Python parsers for bank statement PDFs. Given a sample PDF and a corresponding CSV with the expected output, the agent writes, tests, and self-corrects Python code until it produces a working parser.

How the Agent Works
The agent is built as a cyclical graph or state machine using LangGraph. It follows a "Plan, Generate, Test, Refine" loop. First, the Planner node reads the sample PDF and CSV to create a detailed, context-rich prompt for the LLM. The Generator (the LLM) then writes the Python parser code. Next, the Executor node saves this code and runs a test harness against it, comparing the parser's output to the sample CSV. A Decision node then checks the test result: if it passes, the process ends successfully. If it fails and attempts remain, the process moves to a Refiner node, which sends the broken code and the error message back to the LLM to be fixed, and the cycle repeats.

![Untitled](https://github.com/user-attachments/assets/d8242b85-1a63-4bdb-9c9f-7f46f3164e86)

How to Run the Project (5 Steps)
Follow these steps to set up and run the agent on your local machine.

Step 1: Set Up the Environment
First, clone the repository and create a Python virtual environment.

# Clone the repository
git clone https://github.com/AdityaPokhriyal/ai-agent-challenge-karbon.git
cd https://github.com/AdityaPokhriyal/ai-agent-challenge-karbon.git

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Step 2: Install Dependencies
The agent relies on camelot for PDF parsing, which has a system-level dependency on Ghostscript.

Install Ghostscript:

Windows: Download and run the installer from the official Ghostscript website.

macOS: Use Homebrew: brew install ghostscript

Linux (Debian/Ubuntu): sudo apt-get install python3-tk ghostscript

Install Python Packages:
Install all required Python libraries from the requirements.txt file.

python -m pip install -r requirements.txt

Step 3: Configure Your API Key
The agent uses the Google Gemini API. You need to provide your API key in an environment file.

Create a new file named .env in the root of the project directory.

Add your API key to this file:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Step 4: Run the Agent
Execute the agent from your terminal, specifying the target bank using the --target flag. The data for icici is already included.

python agent.py --target icici

The agent will begin its process, and you will see status updates printed to the console.

Step 5: Verify the Output
A successful run will end with a success message in your terminal. You can then find the final, working parser file in the custom_parsers directory.

Generated File: custom_parsers/icici_parser.py

To run the agent for a new bank (e.g., "sbi"), simply create a new folder data/sbi/ containing "sbi sample.pdf" and "result.csv", and run the agent with python agent.py --target sbi.
