# Legal Interview Preparation Assistant

An AI-powered Streamlit application to help candidates prepare for legal role interviews using advanced prompt engineering techniques and a mock interview chatbot.

## Features

### Interview Prep Generator
- **5 Prompt Engineering Strategies** mapped to legal roles:
  - **Zero-shot** (Paralegal) - Direct questions without examples
  - **Few-shot** (In-House Legal Counsel) - Example-based guidance
  - **Chain-of-Thought** (Legal Engineer) - Structured reasoning framework
  - **Least-to-Most** (City Firm Lawyer) - Sequential competency analysis
  - **Self-Refinement** (Legal Operations Specialist) - Comprehensive refinement approach

- **Customizable Settings**:
  - Model selection (GPT-4o or GPT-4o-mini)
  - Temperature tuning (0.0-2.0)
  - Top-p tuning (0.0-1.0)
  - Max response length (100-2000 tokens)
  - Question difficulty levels (Low/Medium/Hard)
  - Response styles (Concise/Standard/Long)

### Security Features
- Input validation and spam detection
- Character limits on user inputs (Job Description: 3000 chars, CV: 2000 chars)

### Cost Tracking
- Real-time calculation of API usage costs
- Token usage metrics (prompt, completion, total)
- Model-specific pricing display

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Get your API key from: https://platform.openai.com/api-keys

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Docker Setup (Optional)

1. **Build the Docker image**:
   ```bash
   docker build -t legal-interview-prep .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY=your_api_key_here legal-interview-prep
   ```
   Or use an environment file:
   ```bash
   docker run -p 8501:8501 --env-file .env legal-interview-prep
   ```

3. **Access the app**: Open your browser to `http://localhost:8501`

