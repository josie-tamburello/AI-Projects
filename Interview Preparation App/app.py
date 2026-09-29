import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Tuple

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.set_page_config(
    page_title="Legal Interview Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Main background - White */
    .stApp { background-color: #FFFFFF; }
    
        /* Sidebar - Pure white background, no gradients, with black border on all sides - FORCE VISIBLE */
    [data-testid="stSidebar"],
    section[data-testid="stSidebar"],
    .css-1d391kg {
        background-color: #FFFFFF !important;
        background-image: none !important;
        border: 2px solid #000000 !important;
        display: block !important;
        visibility: visible !important;
        width: 16rem !important;
        min-width: 16rem !important;
        max-width: 16rem !important;
        opacity: 1 !important;
        transform: none !important;
        position: relative !important;
    }
    
        /* Sidebar content - White */
    [data-testid="stSidebar"] > div {
        background-color: #FFFFFF !important;
    }
    
    
    /* Sidebar header - Bigger font */
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] .stHeader {
        font-size: 5rem !important;
        font-weight: bold !important;
    }
    
        /* Header - White background only */
    header[data-testid="stHeader"],
    [data-testid="stHeader"],
    .stApp > header,
    header {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }
    
        /* All text - Black */
    .stMarkdown, p, div, label, h1, h2, h3, span, .stTitle, .stSubheader {
        color: #000000 !important;
    }
    
    /* Main content area text - Black */
    .main .block-container,
    .main .block-container *,
    .element-container,
    .element-container * {
        color: #000000 !important;
    }
    
            /* Main content area text - Black */
    .main .block-container,
    .main .block-container *,
    .element-container,
    .element-container * {
        color: #000000 !important;
    }
    
    /* Input boxes - White with black borders */
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #FFFFFF !important;
        border: 1px solid #000000 !important;
        color: #000000 !important;
    }
    
    /* ALL Selectboxes/Dropdowns - White background with black text */
    .stSelectbox > div > div > div {
        background-color: #FFFFFF !important;
        border: 1px solid #000000 !important;
    }
    
    /* Dropdown selected value - Black text */
    .stSelectbox > div > div > div > div,
    .stSelectbox > div > div > div > div > div {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }
    
    /* Dropdown labels - Black */
    .stSelectbox label,
    .stSelectbox > label {
        color: #000000 !important;
    }
    
        /* Dropdown menu when open - White background, black text - ULTRA AGGRESSIVE */
    [data-baseweb="popover"],
    [data-baseweb="popover"] *,
    [data-baseweb="popover"] > div,
    [data-baseweb="popover"] > div > div,
    [data-baseweb="popover"] > div > div > div {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }
    
    [data-baseweb="select"] > div,
    [data-baseweb="select"] > div > div,
    [data-baseweb="select"] * {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Dropdown menu container - Force white on ALL elements */
    [data-baseweb="menu"],
    [data-baseweb="menu"] *,
    [data-baseweb="menu"] > div,
    [data-baseweb="menu"] > div > div,
    [data-baseweb="menu"] > div *,
    [data-baseweb="menu"] > ul,
    [data-baseweb="menu"] > ul > div,
    [data-baseweb="menu"] > ul * {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }
    
    /* All dropdown menu items - Force white background, black text */
    [data-baseweb="menu"] li,
    [data-baseweb="menu"] ul li,
    [data-baseweb="menu"] ul li,
    [data-baseweb="menu"] > div > div,
    [data-baseweb="menu"] > div,
    [data-baseweb="menu"] li > div,
    [data-baseweb="menu"] li > div > div,
    [data-baseweb="menu"] li > span,
    [data-baseweb="menu"] li > div > span,
    [data-baseweb="menu"] li * {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Dropdown option text - Force black on ALL text elements */
    [data-baseweb="menu"] li *,
    [data-baseweb="menu"] ul li *,
    [data-baseweb="menu"] span,
    [data-baseweb="menu"] p,
    [data-baseweb="menu"] div {
        color: #000000 !important;
    }
    
    /* Dropdown option text when hovered */
    [data-baseweb="menu"] li:hover,
    [data-baseweb="menu"] ul li:hover,
    [data-baseweb="menu"] li:hover *,
    [data-baseweb="menu"] li:hover > div,
    [data-baseweb="menu"] li:hover > span {
        background-color: #F3F4F6 !important;
        background: #F3F4F6 !important;
        color: #000000 !important;
    }
    
    /* Override ANY dark theme styles with universal selector */
    [data-baseweb="menu"] [style*="background"],
    [data-baseweb="popover"] [style*="background"],
    [data-baseweb="menu"] [style*="background-color"],
    [data-baseweb="popover"] [style*="background-color"] {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }
    
    /* Force white on any element with dark colors */
    [data-baseweb="menu"] [style*="#000"],
    [data-baseweb="menu"] [style*="rgb(0"],
    [data-baseweb="menu"] [style*="rgba(0"] {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }
    
    /* Button - Purple, no border - Only for main content area buttons (not sidebar) */
    .main .stButton > button[kind="primary"],
    .block-container .stButton > button[kind="primary"] {
        background-color: #6B46C1 !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
    }
    
    /* Force white text on all button text elements - Only for main content area */
    .main .stButton > button[kind="primary"] *,
    .main .stButton > button[kind="primary"] span,
    .main .stButton > button[kind="primary"] div,
    .main .stButton > button[kind="primary"] p,
    .block-container .stButton > button[kind="primary"] *,
    .block-container .stButton > button[kind="primary"] span,
    .block-container .stButton > button[kind="primary"] div,
    .block-container .stButton > button[kind="primary"] p {
        color: white !important;
    }
    
    .main .stButton > button[kind="primary"]:hover,
    .block-container .stButton > button[kind="primary"]:hover {
        background-color: #7C3AED !important;
        border: none !important;
    }
    
    /* Force white text on hover state - Only for main content area */
    .main .stButton > button[kind="primary"]:hover *,
    .main .stButton > button[kind="primary"]:hover span,
    .main .stButton > button[kind="primary"]:hover div,
    .main .stButton > button[kind="primary"]:hover p,
    .block-container .stButton > button[kind="primary"]:hover *,
    .block-container .stButton > button[kind="primary"]:hover span,
    .block-container .stButton > button[kind="primary"]:hover div,
    .block-container .stButton > button[kind="primary"]:hover p {
        color: white !important;
    }
    

    /* Slider value display - White background, black text, no borders */
    .stSlider > div > label,
    .stSlider label,
    .stSlider > div > div > label {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        padding: 2px 6px !important;
        border-radius: 3px !important;
        border: none !important;
    }
    
    /* Slider number input background - No borders */
    .stSlider input[type="number"],
    .stSlider > div > div > input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: none !important;
    }
    
        /* Slider number input background - No borders */
    .stSlider input[type="number"],
    .stSlider > div > div > input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: none !important;
    }
    
    
    /* Remove borders only on the slider container, not all spans */
.stSlider [data-baseweb="slider"] {
  border-top: none !important;
  border-bottom: none !important;
}

    
    /* ===== Slider: remove the little end tick lines but keep min/max labels ===== */

/* Hide ONLY tiny decorative tick bars (they're divs; labels are spans) */
.stSlider [data-baseweb="slider"] div[style*="height: 4px"],
.stSlider [data-baseweb="slider"] div[style*="height:4px"],
.stSlider [data-baseweb="slider"] div[style*="height: 5px"],
.stSlider [data-baseweb="slider"] div[style*="height:5px"],
.stSlider [data-baseweb="slider"] div[style*="height: 6px"],
.stSlider [data-baseweb="slider"] div[style*="height:6px"] {
  display: none !important;
}

/* In some builds the tick bars are borders instead of blocks */
.stSlider [data-baseweb="slider"] div {
  border-top: none !important;
  border-bottom: none !important;
}

/* Ensure the min/max text always stays visible */
.stSlider [data-baseweb="slider"] span {
  visibility: visible !important;
}

/* ===== Catch the end-ticks (usually 2–3px tall) without hiding the main rail ===== */

/* Hide the tick/mark bars, but do NOT affect the rail */
.stSlider [data-baseweb="slider"] div[style*="height: 2px"],
.stSlider [data-baseweb="slider"] div[style*="height:2px"],
.stSlider [data-baseweb="slider"] div[style*="height: 3px"],
.stSlider [data-baseweb="slider"] div[style*="height:3px"] {
  opacity: 0 !important;     /* safer than display:none (keeps layout/labels stable) */
}

/* ========= Slider (BaseWeb) ========= */

/* main rail (the long middle line only) */
.stSlider [data-baseweb="slider"] > div:first-child > div {
  background: #000000 !important;
  height: 3px !important;
  border-radius: 2px !important;
}

/* thumb */
.stSlider [role="slider"] {
  background-color: #000000 !important;
  border-color: #000000 !important;
}

/* remove tick marks / short end lines */
.stSlider [data-baseweb="slider"] div[class*="tick"],
.stSlider [data-baseweb="slider"] div[class*="Tick"],
.stSlider [data-baseweb="slider"] [aria-hidden="true"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

/* keep min/max labels visible */
.stSlider [data-baseweb="slider"] span {
  visibility: visible !important;
  opacity: 1 !important;
}

    /* ===== Sidebar "Settings" heading ===== */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2 {
  font-size: 2.2rem !important;
  font-weight: 700 !important;
  margin-bottom: 0.5rem !important;
}


        /* Header - Keep visible but clean (needed for sidebar toggle to work) */
    header[data-testid="stHeader"],
    [data-testid="stHeader"],
    .stApp > header,
    header {
        background: #FFFFFF !important;
        height: 3.25rem !important;
        visibility: visible !important;
        display: block !important;
    }
    
    /* Hide Deploy button and menu button (three dots) */
    [data-testid="stHeader"] button[kind="header"],
    [data-testid="stHeader"] button[title="Deploy"],
    [data-testid="stHeader"] button[aria-label*="Deploy"],
    [data-testid="stHeader"] button[aria-label*="Menu"],
    [data-testid="stHeader"] button[title="Menu"],
    button[kind="header"],
    #MainMenu,
    [data-testid="stDecoration"],
    [data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }
    
          /* All text - Black */
     .stMarkdown, p, div, label, h1, h2, h3, span, .stTitle, .stSubheader {
        color: #000000 !important;
    }
    
    /* Reduce font size of response output */
    .main .stMarkdown,
    .main .stMarkdown p,
    .main .stMarkdown div,
    .main .element-container .stMarkdown {
        font-size: 14px !important;
        line-height: 1.5 !important;
    }
    
    /* Make headers in response smaller */
    .main .stMarkdown h1 {
        font-size: 1.5rem !important;
    }
    .main .stMarkdown h2 {
        font-size: 1.3rem !important;
    }
    .main .stMarkdown h3 {
        font-size: 1.1rem !important;
    }
    
    /* Sidebar toggle button - Fixed position, always visible */
    .sidebar-toggle-btn {
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 999 !important;
        background-color: #6B46C1 !important;
        color: white !important;
        border: 1px solid #000000 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 0.5rem !important;
        cursor: pointer !important;
    }
    
    /* Chat message styling - User messages (light gray background for visibility) */
    [data-testid="stChatMessage"] [data-testid="stChatMessageUser"],
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageUser"]) {
        background-color: #F3F4F6 !important;
        padding: 1rem !important;
        border-radius: 0.5rem !important;
        border: 1px solid #D1D5DB !important;
        margin-bottom: 1rem !important;
    }
    
    [data-testid="stChatMessage"] [data-testid="stChatMessageUser"] *,
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageUser"]) * {
        color: #000000 !important;
    }
    
    /* Chat message styling - Assistant messages (white background) */
    [data-testid="stChatMessage"] [data-testid="stChatMessageAssistant"],
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAssistant"]) {
        background-color: #FFFFFF !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    [data-testid="stChatMessage"] [data-testid="stChatMessageAssistant"] *,
    div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAssistant"]) * {
        color: #000000 !important;
    }
    
    /* General chat message container styling */
    div[data-testid="stChatMessage"] {
        margin-bottom: 1rem !important;
    }
    
    /* Ensure user message content is visible */
    .stChatMessage [data-testid="stChatMessageUser"] p,
    .stChatMessage [data-testid="stChatMessageUser"] div,
    .stChatMessage [data-testid="stChatMessageUser"] span {
        color: #000000 !important;
        background-color: transparent !important;
    }
    
    /* Chat input field - Clean single border, white background, black text */
    [data-testid="stChatInput"] {
        background-color: #FFFFFF !important;
    }
    
    /* Remove all borders from container divs */
    [data-testid="stChatInput"] > div,
    [data-testid="stChatInput"] > div > div,
    [data-testid="stChatInput"] > div > div > div {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        background-color: #FFFFFF !important;
    }
    
    /* Style only the textarea/input with a single clean border */
    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #000000 !important;
        border-radius: 0.5rem !important;
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Remove focus borders that might overlap */
    [data-testid="stChatInput"] textarea:focus,
    [data-testid="stChatInput"] input:focus {
        border: 1px solid #000000 !important;
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Chat input placeholder text */
    [data-testid="stChatInput"] textarea::placeholder,
    [data-testid="stChatInput"] input::placeholder,
    [data-testid="stChatInput"] textarea::-webkit-input-placeholder,
    [data-testid="stChatInput"] input::-webkit-input-placeholder {
        color: #666666 !important;
        opacity: 0.7 !important;
    }
    
    /* Chat input text color - force black */
    [data-testid="stChatInput"] textarea,
    [data-testid="stChatInput"] input,
    [data-testid="stChatInput"] * {
        color: #000000 !important;
    }
    
    /* Chat input send button */
    [data-testid="stChatInput"] button,
    .stChatInput button,
    [data-testid="stChatInput"] button[type="submit"] {
        background-color: #6B46C1 !important;
        color: #FFFFFF !important;
    }
    
    /* Make columns equal height for alignment */
    .row-widget.stHorizontal {
        display: flex !important;
        align-items: stretch !important;
    }
    
    .row-widget.stHorizontal > div {
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* Style custom chat input in mock interview */
    input[placeholder="Type your answer here..."] {
        border-radius: 0.5rem !important;
        padding: 0.75rem !important;
    }
    
    /* Make columns equal height for alignment */
    .row-widget.stHorizontal {
        display: flex !important;
        align-items: stretch !important;
    }
    
    </style>
    """, unsafe_allow_html=True)


PROMPT_STRATEGIES = {
    "Zero-shot": """

You are an expert interview coach helping a candidate prepare for a Paralegal role interview.

The user will provide their job description and CV in the following message.

Your task is to generate a set of interview questions and model answers tailored to both the job description and the candidate's CV. Work with the information provided and generate the best possible questions based on what is available. For each question:
- Base the question on specific requirements from the job description
- Reference relevant experience from the candidate's CV where applicable
- Provide a model answer that demonstrates how the candidate's experience aligns with the role requirements
- Include brief feedback on what makes the answer strong

Paralegal interviews typically focus on:
- Document management and legal research skills
- Attention to detail and organizational abilities
- Understanding of legal terminology and procedures
- Ability to work under supervision and support solicitors
- Time management and multitasking in a legal environment
- Familiarity with legal software and case management systems

Generate 5 interview questions with corresponding model answers that connect the job description requirements to the candidate's CV experience.
""",

    "Few-shot": """
Few-Shot Prompting: In this approach, the model is guided by providing one or more examples within the prompt, helping it generate more accurate or contextually relevant interview questions and answers.

You are an experienced in-house legal counsel coaching a candidate for an In-House Legal Counsel role.

The user will provide their job description and CV/resume in the following message.

Here are two examples of how to structure questions and answers that connect job requirements to CV experience:

Example 1 - Question: "How do you balance legal risk with business objectives?"
Model Answer (based on CV showing 3 years in-house experience): "Based on my three years as in-house counsel at [Company], I start by understanding the business goal and the commercial context. Then I assess the legal risks on a spectrum - from low to high severity. For low-risk items, I provide clear guidance and let the business proceed. For high-risk items, I work collaboratively to find alternative solutions that meet the business objective while mitigating legal exposure. I always explain the 'why' behind my recommendations so stakeholders understand the reasoning."

Example 2 - Question: "Describe how you would handle a contract negotiation with a key supplier."
Model Answer (referencing CV experience): "Drawing from my experience managing vendor contracts at [Previous Role], I'd first review our standard terms and identify our must-haves versus nice-to-haves. I'd understand the supplier's key concerns by asking questions early. Then I'd prepare a negotiation strategy prioritizing our critical terms while being flexible on less important points. Throughout, I'd maintain clear communication with our procurement team and ensure alignment on commercial terms before finalizing legal language."

Now, generate 5 interview questions for the user based on their job description and CV. For each question, provide a model answer that references specific experiences from their CV and aligns with the job description requirements.
""",

    "Chain-of-Thought": """
Chain-of-Thought Prompting: This technique involves instructing the model to break interview preparation into logical steps, enhancing its ability to reason through complex legal scenarios and provide structured feedback.

You are a legal interview coach for a Legal Engineer role position.

The user will provide their job description and CV/resume in the following message.

Legal Engineer interviews focus on:
- Technical skills (programming, legal tech tools, automation)
- Understanding of legal processes and workflows
- Problem-solving using technology
- Ability to bridge legal and technical domains
- System design and implementation
- Data analysis and legal analytics

To generate tailored questions and answers, follow this reasoning framework:

Step 1: Analyze the job description - Identify key technical and legal competencies required
Step 2: Review the CV - Extract relevant technical skills, legal experience, and projects
Step 3: Match competencies - Connect job requirements to CV experiences
Step 4: Formulate questions - Create questions that test both technical and legal knowledge
Step 5: Structure answers - Provide model answers that demonstrate how the candidate's CV experience addresses the job requirements
Step 6: Add reasoning - Explain the thought process behind each answer

Generate 5 interview questions with step-by-step model answers that show how the candidate's CV experience (technical skills, legal projects, relevant work) directly addresses the job description requirements.
""",

    "Least-to-Most Prompting": """
Least-to-Most Prompting: Similar to chain of thought, this technique breaks interview preparation into sequential steps, asking the model to solve each in order to arrive at a comprehensive interview strategy.

You are a senior partner at a prestigious City law firm conducting an interview for a City Firm Lawyer position.

The user will provide their job description and CV/resume in the following message.

Your interview style is:
- Direct and challenging, testing how candidates think under pressure
- Focused on commercial awareness and client relationship skills
- Interested in how candidates handle ambiguity and complex legal scenarios
- Looking for candidates who can balance legal rigor with practical business solutions
- Testing knowledge of recent case law, regulatory developments, and market trends
- Evaluating ability to work in high-pressure, billable-hour environments

Start by identifying five key competencies from the job description (e.g., technical legal knowledge, commercial awareness, client management, research skills, resilience). Next, review the candidate's CV to find relevant experiences for each competency. Then, for each competency, formulate two challenging interview questions that test both the job requirements and reference the candidate's background. Finally, provide model answers that demonstrate how the candidate's CV experience positions them for this role.

Generate 5 challenging interview questions with model answers that connect the job description requirements to the candidate's CV, written from a senior partner's perspective.
""",

    "Self-Refinement": """
Self-Refinement: This method involves analyzing a job description and CV, generating 5 interview questions and responses, and then refining it to ensure it's comprehensive, targeted, and covers all aspects of the role.

You are a legal career coach specializing in helping candidates prepare for Legal Operations Specialist roles.

The user will provide their job description and CV/resume in the following message.

Legal Operations Specialist interviews focus on:
- Process optimization and workflow improvement
- Legal technology implementation and management
- Budget management and vendor relationships
- Data analytics and reporting for legal departments
- Project management skills
- Understanding of legal department operations and metrics

Initial Analysis: Analyze the job description and CV to identify:
- Key operational competencies required in the job description
- Specific legal tech tools or systems mentioned
- Process improvement skills emphasized
- Metrics and KPIs the role will manage
- Relevant experiences from the CV that match these requirements

Refined Output: Generate a comprehensive set of 8-10 interview questions with model answers that:
- Are highly specific to the job description requirements
- Reference and leverage the candidate's CV experience
- Cover legal operations concepts (e.g., matter management, e-billing, contract lifecycle management)
- Include technical skills demonstrations from the CV
- Use STAR method (Situation, Task, Action, Result) examples from the candidate's background
- Provide questions the candidate should ask the interviewer

Revise and refine your questions and answers to ensure they create a strong connection between the job description and the candidate's CV, making the candidate's experience directly relevant to the role.
"""
}

PERSONAS = {
    "Paralegal": "Zero-shot",
    "City Firm Lawyer": "Least-to-Most Prompting",
    "In-House Legal Counsel": "Few-shot",
    "Legal Engineer": "Chain-of-Thought",
    "Legal Operations Specialist": "Self-Refinement"
}


from typing import Tuple

def security_guard(user_input: str) -> Tuple[bool, str]:
    if not user_input or not user_input.strip():
        return False, "Please provide some input."
    
    inappropriate_keywords = [
        "hack", "exploit", "bypass", "illegal", "unethical",
        "harmful", "dangerous", "violence", "threat"
    ]
    input_lower = user_input.lower()
    for keyword in inappropriate_keywords:
        if keyword in input_lower:
            if not any(legal_term in input_lower for legal_term in ["legal", "law", "regulation", "compliance", "ethics"]):
                return False, f"Input contains potentially inappropriate content. Please focus on legal interview preparation."
    words = user_input.split()
    if len(words) > 0:
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        max_repetition = max(word_counts.values())
        if max_repetition > len(words) * 0.3:  
            return False, "Input appears to contain excessive repetition. Please provide a more varied query."
    
    return True, ""



def calculate_cost(prompt_tokens: int, completion_tokens: int, model: str) -> float:
    """
    Calculate the cost of an API call based on token usage.
    Pricing for GPT-4o and GPT-4o-mini (as of 2024)
    """
    
    pricing = {
        "gpt-4o": {"input": 0.0025, "output": 0.010}, 
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},  
    }
    
    if model not in pricing:
        return 0.0
    
    input_cost = (prompt_tokens / 1000) * pricing[model]["input"]
    output_cost = (completion_tokens / 1000) * pricing[model]["output"]
    return input_cost + output_cost


def main():
    st.title("Legal Interview Assistant")
    
  
    st.markdown("""
    <script>
    setTimeout(function() {
        var sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            sidebar.style.cssText = 'display: block !important; visibility: visible !important; width: 16rem !important; min-width: 16rem !important; max-width: 16rem !important; opacity: 1 !important;';
        }
    }, 100);
    </script>
    """, unsafe_allow_html=True)
    
   
    if "mock_interview_messages" not in st.session_state:
        st.session_state.mock_interview_messages = []
    if "mock_interview_context" not in st.session_state:
        st.session_state.mock_interview_context = None
    
    with st.sidebar:
        st.header("Settings")
        
        model = st.selectbox(
            "Select Model",
            ["gpt-4o", "gpt-4o-mini"],
            index=1,  
            help="GPT-4o: Higher quality, higher cost. GPT-4o-mini: Good balance of quality and cost."
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1,
            help="Lower (0.0-0.5): More focused, factual responses. Higher (0.7-2.0): More creative, varied responses. Recommended: 0.5-0.7 for legal interview prep."
        )
        
        top_p = st.slider(
            "Top-p",
            min_value=0.0,
            max_value=1.0,
            value=0.9,
            step=0.05,
            help="Controls diversity via nucleus sampling. 0.9 is a good default."
        )
        
        max_tokens = st.slider(
            "Max Response Length",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100,
            help="Maximum tokens in the response"
        )
        
        difficulty = st.selectbox(
            "Question Difficulty",
            ["Low", "Medium", "Hard"],
            index=1,
            help="Low: Core concepts and basic questions. Medium: Standard interview level. Hard: Complex case law and detailed procedure."
        )
        
        response_style = st.selectbox(
            "Response Style",
            ["Concise", "Standard", "Long"],
            index=1,
            help="Concise: Quick reference format. Standard: Balanced responses. Long: Comprehensive detailed answers."
        )
    

    tab1, tab2 = st.tabs(["Interview Prep Generator", "Mock Interview"])
    
    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Interview Details")
            
            selected_persona = st.selectbox(
                "Interview Persona",
                list(PERSONAS.keys()),
                help="Choose the legal role persona for your interview preparation"
            )
            
            prompt_strategy = PERSONAS[selected_persona]
        
            if prompt_strategy == "JD-Focused Prep Plan":
                job_description = st.text_area(
                    "Job Description",
                    height=200,
                    max_chars=3000,
                    help="Paste the job description here. Maximum 3000 characters.",
                    placeholder="Paste the full job description for this role..."
                )
            else:
                job_description = st.text_area(
                    "Summarise your job description",
                    height=150,
                    max_chars=3000,
                    help="Paste or summarize the job description here. Maximum 3000 characters."
                )
            
            cv_input = st.text_area(
                "Your CV",
                height=150,
                max_chars=2000,
                help="Paste your CV or resume here.",
                placeholder="Paste your CV or resume..."
            )
            
            if job_description and cv_input:
                user_query = f"Job Description:\n{job_description}\n\nCV/Resume:\n{cv_input}"
            elif job_description:
                user_query = f"Job Description:\n{job_description}"
            else:
                user_query = ""
            
            if user_query:
                char_count = len(user_query)
                max_chars = 5000 if prompt_strategy == "JD-Focused Prep Plan" else 5000
                st.caption(f"Characters: {char_count}/{max_chars}")
            
            submit_button = st.button("Generate Interview Prep", type="primary", use_container_width=True)
        
        with col2:
            st.subheader("Preparation")
            response_container = st.container()
            
            
            with response_container:
                if "last_prep_response" not in st.session_state or not st.session_state.get("last_prep_response"):
                    st.info("Enter your job description and CV, then click 'Generate Interview Prep' to begin!")
        
        if submit_button:
            if not job_description or not job_description.strip():
                st.error("Please provide a job description. The AI needs this information to generate relevant interview questions.")
                return
            
            if not cv_input or not cv_input.strip():
                st.error("Please provide your CV. The AI needs this information to tailor questions and answers to your experience.")
                return
            
            if len(job_description.strip()) < 50:
                st.error("Job description is too short. Please provide at least 50 characters of information about the role.")
                return
            
            if len(cv_input.strip()) < 50:
                st.error("CV is too short. Please provide at least 50 characters of information about your experience.")
                return
            
          
            if not user_query or not user_query.strip():
                st.error("Please provide some input before submitting.")
                return
            
            is_valid, error_msg = security_guard(user_query)
            if not is_valid:
                st.error(f"Security Check Failed: {error_msg}")
                return
            
            with response_container:
                with st.spinner("Generating your interview preparation..."):
                    try:
                        system_prompt = PROMPT_STRATEGIES[prompt_strategy]
                        
                        system_prompt += f"\n\nThe candidate is preparing for a {selected_persona} position."
                        
                
                        if difficulty == "Low":
                            system_prompt += "\n\nIMPORTANT: Generate questions at a LOW difficulty level. Focus on fundamental concepts, basic legal terminology, and entry-level competencies. Questions should test foundational knowledge that a junior candidate would be expected to know."
                        elif difficulty == "Medium":
                            system_prompt += "\n\nIMPORTANT: Generate questions at a MEDIUM difficulty level. These should be standard interview questions that test practical knowledge, common scenarios, and typical competencies expected for this role."
                        elif difficulty == "Hard":
                            system_prompt += "\n\nIMPORTANT: Generate questions at a HARD difficulty level. Include complex legal scenarios, advanced case law references, detailed procedural questions, and challenging situations that test deep expertise and analytical thinking."
                        
                      
                        if response_style == "Concise":
                            system_prompt += "\n\nIMPORTANT: Provide CONCISE responses. Each model answer must be exactly 2 sentences. Focus on key points only. Use bullet points where appropriate. Avoid lengthy explanations."
                        elif response_style == "Standard":
                            system_prompt += "\n\nIMPORTANT: Provide STANDARD length responses. Each model answer must be exactly 5 sentences. Provide context and examples where relevant, but remain focused."
                        elif response_style == "Long":
                            system_prompt += "\n\nIMPORTANT: Provide LONG, comprehensive responses. Each model answer must be exactly 8 sentences. Include multiple examples, thorough analysis, and extensive context. Be thorough and exhaustive in your model answers."
                        
                    
                        system_prompt += "\n\nIMPORTANT: Start directly with the interview questions and answers. Do not include any introductory text, thank you messages, or explanations. Begin immediately with 'Question 1:' followed by the question and model answer."
                        
                 
                        system_prompt += "\n\nIMPORTANT: Do not provide legal advice. This is interview preparation only, not legal counsel. If asked for legal advice, respond with: 'I cannot provide legal advice. This tool is for interview preparation only.'"
                        
        
                        try:
                            response = client.chat.completions.create(
                                model=model,
                                messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": user_query}
                                ],
                                temperature=temperature,
                                top_p=top_p,
                                max_tokens=max_tokens
                            )
                        except Exception as api_error:
                            st.error(f"API Call Failed: {str(api_error)}")
                            if "api_key" in str(api_error).lower() or "authentication" in str(api_error).lower():
                                st.warning("This might be an API key issue. Check your `.env` file.")
                            raise
                        
                       
                        response_text = response.choices[0].message.content
                        
                       
                        st.session_state.last_prep_response = response_text
                        
                    
                        prompt_tokens = response.usage.prompt_tokens
                        completion_tokens = response.usage.completion_tokens
                        total_tokens = response.usage.total_tokens
                        cost = calculate_cost(prompt_tokens, completion_tokens, model)
                        
                      
                        with response_container:
                            st.markdown(response_text)
                        
                 
                        st.divider()
                        with st.expander("Request Details"):
                            col_meta1, col_meta2, col_meta3 = st.columns(3)
                            with col_meta1:
                                st.metric("Prompt Tokens", f"{prompt_tokens:,}")
                            with col_meta2:
                                st.metric("Completion Tokens", f"{completion_tokens:,}")
                            with col_meta3:
                                st.metric("Total Tokens", f"{total_tokens:,}")
                            
                            st.metric("💰 Estimated Cost", f"${cost:.4f}")
                            st.caption(f"Model: {model} | Temperature: {temperature} | Top-p: {top_p}")
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                        st.info("Please check your API key in the .env file and ensure you have sufficient credits.")
    
    
    with tab2:
        col_mock1, col_mock2 = st.columns([1, 1])
        
        with col_mock1:
            st.subheader("Interview Details")
            
            mock_persona = st.selectbox(
                "Interviewer Persona",
                list(PERSONAS.keys()),
                help="Choose the type of interviewer persona"
            )
            
            mock_job_desc = st.text_area(
                "Job Description (for Mock Interview)",
                height=150,
                max_chars=3000,
                help="Paste the job description for the role you're interviewing for.",
                placeholder="Paste the job description here..."
            )
            
            mock_cv = st.text_area(
                "Your CV (for Mock Interview)",
                height=150,
                max_chars=2000,
                help="Paste your CV/resume.",
                placeholder="Paste your CV here..."
            )
            
            if st.button("Start Mock Interview", type="primary", use_container_width=True):
                if mock_job_desc and mock_cv:
                    st.session_state.mock_interview_messages = []
                    st.session_state.mock_interview_context = {
                        "job_description": mock_job_desc,
                        "cv": mock_cv,
                        "persona": mock_persona
                    }
                
                    with st.spinner("Preparing interview questions..."):
                        try:
                            system_prompt = f"""You are an experienced interviewer conducting a mock interview for a {mock_persona} position.

The candidate's job description:
{mock_job_desc}

The candidate's CV/resume:
{mock_cv}

Your role:
- Ask relevant interview questions based on the job description and candidate's CV
- Ask one question at a time
- Be professional but conversational
- After the candidate answers, provide brief constructive feedback (1-2 sentences) and then ask the next question
- Ask 5-7 questions total, covering different aspects of the role
- Focus on behavioral questions, technical skills, and role-specific scenarios
- Keep questions appropriate for a {mock_persona} position

Start by greeting the candidate and asking your first question. Do not ask multiple questions at once."""
                            
                            response = client.chat.completions.create(
                                model=model,
                                messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": "Hello, I'm ready to begin the interview."}
                                ],
                                temperature=temperature,
                                top_p=top_p,
                                max_tokens=max_tokens
                            )
                            
                            first_question = response.choices[0].message.content
                            st.session_state.mock_interview_messages = [
                                {"role": "assistant", "content": first_question}
                            ]
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error starting interview: {str(e)}")
                else:
                    st.warning("Please provide both job description and CV to start the mock interview.")
        
        with col_mock2:
            st.subheader("Interview Conversation")
            
           
            messages_container = st.container(height=500)
            
            with messages_container:
                if len(st.session_state.mock_interview_messages) == 0:
                    st.info("Enter your job description and CV, then click 'Start Mock Interview' to begin!")
                else:
                    for message in st.session_state.mock_interview_messages:
                        with st.chat_message(message["role"]):
                            st.markdown(message["content"])
            
            
            if len(st.session_state.mock_interview_messages) > 0 and st.session_state.mock_interview_context:
                user_response = st.chat_input("Type your answer here...")
                
                if user_response:
                    st.session_state.mock_interview_messages.append({"role": "user", "content": user_response})
                    
                    with messages_container:
                        with st.chat_message("user"):
                            st.markdown(user_response)
                        
                        with st.chat_message("assistant"):
                            with st.spinner("Interviewer is thinking..."):
                                try:
                                    messages_for_api = [
                                        {
                                            "role": "system",
                                            "content": f"""You are an experienced interviewer conducting a mock interview for a {st.session_state.mock_interview_context['persona']} position.

The candidate's job description:
{st.session_state.mock_interview_context['job_description']}

The candidate's CV/resume:
{st.session_state.mock_interview_context['cv']}

Your role:
- Ask relevant interview questions based on the job description and candidate's CV
- Ask one question at a time
- Be professional but conversational
- After the candidate answers, provide brief constructive feedback (1-2 sentences) and then ask the next question
- Ask 5-7 questions total, covering different aspects of the role
- Focus on behavioral questions, technical skills, and role-specific scenarios
- Keep questions appropriate for a {st.session_state.mock_interview_context['persona']} position
- If you've asked enough questions (5-7), wrap up the interview professionally"""
                                        }
                                    ]
                                    
                                    
                                    for msg in st.session_state.mock_interview_messages:
                                        messages_for_api.append({
                                            "role": msg["role"],
                                            "content": msg["content"]
                                        })
                                    
                                    response = client.chat.completions.create(
                                        model=model,
                                        messages=messages_for_api,
                                        temperature=temperature,
                                        top_p=top_p,
                                        max_tokens=max_tokens
                                    )
                                    
                                    interviewer_response = response.choices[0].message.content
                                    st.session_state.mock_interview_messages.append({"role": "assistant", "content": interviewer_response})
                                    st.markdown(interviewer_response)
                                    st.rerun()
                                    
                                except Exception as e:
                                    st.error(f"Error: {str(e)}")
                                    st.info("Please check your API key in the .env file and ensure you have sufficient credits.")
    
    


if __name__ == "__main__":
    if not os.getenv('OPENAI_API_KEY'):
        st.error("⚠️ OpenAI API key not found. Please create a `.env` file with your `OPENAI_API_KEY`.")
        st.info("See `.env.example` for the format.")
    else:
        main()

