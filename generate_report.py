import subprocess
import os

REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEX_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab3.tex")
PDF_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab3.pdf")

# --- IMAGE PATHS (update these to point to your saved plot files) ---
FIGURE_1 = "figures/PLACEHOLDER.png"
FIGURE_2 = "figures/PLACEHOLDER.png"
FIGURE_3 = "figures/PLACEHOLDER.png"

tex_content = r"""
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{parskip}
\usepackage{float}

\titleformat{\section}{\large\bfseries}{}{0em}{}
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}

\title{Lab 3: Monte Carlo Methods}
\author{Morgan Cooper \\ MSDS 684 --- Reinforcement Learning}
\date{\today}

\begin{document}
\maketitle

\section{Section 1: Project Overview}

% 400-500 words
% Required content:
%   - Problem/Question: What RL problem are you investigating?
%   - Core Concepts: What RL concepts from Sutton & Barto (Chapter 5) are you exploring?
%   - Theoretical Grounding: How does this connect to theory from the readings?
%   - Environment Description:
%       - State space (discrete/continuous, dimensions)
%       - Action space (discrete/continuous, number of actions)
%       - Reward structure
%       - Episode termination conditions
%   - Expected Behavior: What do you hypothesize will happen and why?
%
% This is NOT a code walkthrough, methods section, or summary of results.
% Purpose: Demonstrate conceptual understanding before diving into implementation.
%
% Environment: Gymnasium's Blackjack-v1
% Topics: MC prediction, MC control with exploring starts, on-policy MC control
%         (epsilon-soft policies), off-policy learning and importance sampling,
%         episode-based learning, first-visit vs every-visit MC methods
% Reading: Sutton & Barto Chapter 5 (Monte Carlo Methods)

[PLACEHOLDER: Write your project overview here]


\section{Section 2: Deliverables}

\subsection{GitHub Repository}
\begin{verbatim}
GitHub Repository: https://github.com/cooper-rm/monte-carlo-methods
\end{verbatim}

\subsection{Implementation Summary}

% 100-150 words
% What you implemented (algorithms, environments)
% Experimental setup (e.g., "500,000 episodes, epsilon values, decay schedules")
% Key hyperparameters chosen
% NOT detailed pseudocode or line-by-line methods
%
% Lab assignment: First-visit MC control for Blackjack-v1 using on-policy
% MC control with epsilon-soft policies. Train for at least 500,000 episodes.
% Experiment with different epsilon values and decay schedules.

[PLACEHOLDER: Write your implementation summary here]


\subsection{Key Results \& Analysis}

% 400-600 words + 2-4 visualizations
% CRITICAL RULES: NO raw code listings in PDF, NO console output dumps
% Include 2-4 key visualizations (PNG/JPG) with detailed interpretive captions
% Discussion must address:
%   - What do results show about algorithm behavior?
%   - How do they relate to theory from Sutton & Barto? (cite chapters/sections)
%   - What didn't work as expected? Why?
%   - How did hyperparameters affect performance?
%   - What does this teach you about the RL concept?
%
% Expected visualizations:
%   - 3D surface plots of learned value function (player sum vs dealer showing card)
%     for both usable and non-usable ace cases (Matplotlib mplot3d)
%   - Comparison of learned policies with basic Blackjack strategy
%   - Learning curves showing average returns over episodes (with smoothing)
%   - Results from different epsilon values and decay schedules

[PLACEHOLDER: Write your key results and analysis here]

% Uncomment and update figures as you generate them:
%
% \begin{figure}[H]
% \centering
% \includegraphics[width=0.85\textwidth]{""" + FIGURE_1 + r"""}
% \caption{[PLACEHOLDER: Interpretive caption for figure 1]}
% \label{fig:figure1}
% \end{figure}
%
% \begin{figure}[H]
% \centering
% \includegraphics[width=0.85\textwidth]{""" + FIGURE_2 + r"""}
% \caption{[PLACEHOLDER: Interpretive caption for figure 2]}
% \label{fig:figure2}
% \end{figure}
%
% \begin{figure}[H]
% \centering
% \includegraphics[width=0.85\textwidth]{""" + FIGURE_3 + r"""}
% \caption{[PLACEHOLDER: Interpretive caption for figure 3]}
% \label{fig:figure3}
% \end{figure}


\section{Section 3: AI Use Reflection}

% 250-350 words total

\subsection{Initial Interaction}

% 50-75 words
% What did you ask the AI to help you with?
% What was your initial prompt?
% What code/explanation did it provide?

[PLACEHOLDER: Write your initial interaction here]


\subsection{Iteration Cycle}

% 150-200 words --- MOST IMPORTANT
% Describe at least 2-3 concrete debugging cycles with:
%   - The error/problem you encountered
%   - Your follow-up prompt to AI
%   - AI's response
%   - Whether it worked or needed more iteration

\textbf{Iteration 1: [PLACEHOLDER: Title]}

[PLACEHOLDER: Describe the first debugging cycle]

\textbf{Iteration 2: [PLACEHOLDER: Title]}

[PLACEHOLDER: Describe the second debugging cycle]

\textbf{Iteration 3: [PLACEHOLDER: Title]}

[PLACEHOLDER: Describe the third debugging cycle]

\subsection{Critical Evaluation}

% 50-75 words
% Did you catch any mistakes the AI made?
% Did you test alternative approaches?
% How did you verify the final solution was correct?

[PLACEHOLDER: Write your critical evaluation here]

\subsection{Learning Reflection}

% 50-75 words
% What did you learn about the RL algorithm through debugging?
% What did you learn about working with AI tools?
% What would you do differently next time?

[PLACEHOLDER: Write your learning reflection here]

\section{Section 4: Speaker Notes}

% ~5 minutes / 5-7 bullets
% Covering:
%   - Problem statement and motivation
%   - Method and key algorithmic choices
%   - Important design decision or challenge you faced
%   - Main result or finding
%   - Key insight or learning
%   - (Optional) Connection to future weeks or real-world applications

\begin{itemize}
  \item \textbf{Problem:} [PLACEHOLDER]
  \item \textbf{Method:} [PLACEHOLDER]
  \item \textbf{Design choice:} [PLACEHOLDER]
  \item \textbf{Key result:} [PLACEHOLDER]
  \item \textbf{Insight:} [PLACEHOLDER]
  \item \textbf{Challenge:} [PLACEHOLDER]
  \item \textbf{Connection:} [PLACEHOLDER]
\end{itemize}

\section{References}

\begin{enumerate}
  \item Sutton, R. S., \& Barto, A. G. (2018). \textit{Reinforcement learning: An introduction} (2nd ed.). MIT Press.
  \item Anthropic. (2025). Claude Code [Large language model CLI tool]. \texttt{https://claude.ai}
  \item OpenAI. (2025). ChatGPT (GPT-4o) [Large language model]. \texttt{https://chat.openai.com}
\end{enumerate}

\end{document}
"""

def main():

    # Write temporary .tex file
    with open(TEX_FILE, "w") as f:
        f.write(tex_content)

    # Compile to PDF (run twice to resolve cross-references)
    for pass_num in (1, 2):
        print(f"Compiling to PDF (pass {pass_num})...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEX_FILE],
            cwd=REPORT_DIR,
            capture_output=True,
            text=True,
        )

    if result.returncode == 0:
        print(f"PDF generated: {PDF_FILE}")
    else:
        print("pdflatex encountered issues:")
        print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)

    # Clean up all LaTeX artifacts (keep only the PDF)
    for ext in [".tex", ".aux", ".log", ".out"]:
        artifact = os.path.join(REPORT_DIR, f"Cooper_Morgan_Lab3{ext}")
        if os.path.exists(artifact):
            os.remove(artifact)


if __name__ == "__main__":
    main()
