# Job Experience Translator

A Python-based tool that converts non-traditional work experience into professional, resume-ready language using AI-powered translation.

**Version:** 1.0.0 (Mock Implementation)  
**Author:** Abdul Haseeb
**Date:** February 2026  
**Status:** Technical Test Submission

---

## Project Overview

The **Job Experience Translator** helps job seekers with non-traditional backgrounds (warehouse workers, service industry, gig economy, etc.) present their experience professionally on resumes.

### The Problem
Many capable workers struggle to translate their valuable real-world experience into language that resonates with hiring managers and ATS systems.

### The Solution
This tool takes raw, informal descriptions of work experience and transforms them into polished bullet points that emphasize **transferable skills**—the universal competencies that matter across industries.

---

## Project Structure

```
Resume/
├── prompt.md          # Contains the carefully engineered prompts that guide the AI to produce consistent, high-quality output
├── translator.py      # Main module with `translate_experience()` function; currently returns mock data
├── example.py         # Runnable demo showing input/output transformation
└── README.md          # Project documentation and integration guide
```

## Quick Start

### Run the Demo

```bash
cd Resume
python example.py
```

### Expected Output

```
============================================================
JOB EXPERIENCE TRANSLATOR - DEMO
============================================================

RAW INPUT:
----------------------------------------
I worked on the yard crew at a lumber yard for about 2 years...

TRANSLATED OUTPUT:
----------------------------------------
• Maintained accountability of tools, materials, and equipment...
• Coordinated with team members to complete time-sensitive projects...
```

---

## Prompt Strategy

### Why "Transferable Skills" Focus?

Transferable skills are competencies that apply across industries and roles. By focusing on these, we help non-traditional candidates compete for positions outside their original field.

| Raw Experience | Transferable Skill | Professional Framing |
|----------------|-------------------|---------------------|
| "Moved heavy stuff" | Operations & Logistics | "Executed material handling operations" |
| "Showed up on time" | Reliability | "Demonstrated consistent attendance" |
| "Made sure nothing got stolen" | Accountability | "Maintained inventory integrity" |
| "Trained new guys" | Leadership | "Onboarded and mentored new team members" |

### Why "Neutral Tone"?

Corporate buzzwords like "synergized," "leveraged," and "spearheaded" can:
1. Sound inauthentic for blue-collar roles
2. Trigger skepticism from experienced hiring managers
3. Create a mismatch between resume language and interview presence

Our neutral, direct approach builds trust and accurately represents the candidate.

### Prompt Design Principles

1. **Constraint-Based Instructions** — Clear rules prevent AI hallucination
2. **Output Format Specification** — Ensures consistent, parseable responses
3. **Example-Driven Context** — Shows the AI exactly what success looks like
4. **Negative Instructions** — Explicitly states what to avoid (buzzwords, exaggeration)

---

## Integration Path

### Current State: Mock Implementation

The `translate_experience()` function currently returns a static string for testing purposes. This allows:
- Frontend/integration development without API costs
- Unit testing with predictable outputs
- Demo presentations without live dependencies

### Future State: Claude API Integration

To connect to the real Claude 3.5 Sonnet API, modify `translator.py`:

```python
import anthropic
from typing import str

# Load prompt from prompt.md or define inline
SYSTEM_PROMPT = """You are an expert resume writer..."""

def translate_experience(raw_text: str) -> str:
    """
    Translate raw work experience using Claude 3.5 Sonnet.
    """
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=256,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Please translate this experience:\n\n{raw_text}"
            }
        ]
    )

    return message.content[0].text
```

### Flask MVP Integration

When ready to build the web API:

```python
# app.py (Future Flask Implementation)
from flask import Flask, request, jsonify
from translator import translate_experience

app = Flask(__name__)

@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json()
    raw_text = data.get("experience", "")

    result = translate_experience(raw_text)

    return jsonify({
        "success": True,
        "translated": result
    })
```
