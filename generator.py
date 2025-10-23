from textwrap import dedent

DOK_DEFS = {
    1: "Recall & reproduction; execute a simple procedure; locate/identify.",
    2: "Skills & concepts; classify, organize, compare; multi-step with some decision-making.",
    3: "Strategic thinking; justify with evidence; analyze across parts or sources.",
    4: "Extended reasoning; investigate, synthesize, or create over time."
}

def dok_verbs(level: int):
    return {
        1: ["identify", "define", "recall", "compute", "list", "locate"],
        2: ["classify", "organize", "compare", "explain", "summarize", "predict"],
        3: ["analyze", "justify", "evaluate", "revise", "argue", "synthesize"],
        4: ["design", "investigate", "synthesize", "construct", "model", "defend"]
    }.get(level, [])

def make_assessments(standard: str, subject: str, grade: str, dok: int):
    v = dok_verbs(dok)
    items = []

    if dok == 1:
        items = [
            {
                "type": "Selected Response",
                "text": f"Which option best {v[0]}s a key element of the standard? (Based on: {standard})",
                "answer": "A (key element stated in the stem).",
                "rationale": "Single-step recall; identification with minimal reasoning.",
                "success": "Chooses accurate option; matches standard language precisely."
            },
            {
                "type": "Short Answer",
                "text": f"{v[1].capitalize()} two terms central to this standard and give a short definition.",
                "answer": "Two correct terms + definitions.",
                "rationale": "Recall/define core terms; no strategic reasoning.",
                "success": "Correct terms; definitions align with grade-appropriate wording."
            }
        ]
    elif dok == 2:
        items = [
            {
                "type": "Constructed Response",
                "text": f"{v[1].capitalize()} the parts of a sample task aligned to this standard and {v[2]} how each part supports the learning goal.",
                "answer": "Names parts correctly; explains role of each part.",
                "rationale": "Organizing + explaining relationships among parts.",
                "success": "Accurate parts; clear links; grade-appropriate vocabulary."
            },
            {
                "type": "Selected Response",
                "text": f"Which choice best {v[3]}s the relationship between two features required by the standard?",
                "answer": "Correct option describing the relationship.",
                "rationale": "Conceptual link; beyond recall.",
                "success": "Chooses option showing correct relationship using standard terms."
            }
        ]
    elif dok == 3:
        items = [
            {
                "type": "Constructed Response",
                "text": f"{v[0].capitalize()} how evidence demonstrates mastery of this standard and {v[1]} your claim with two pieces of textual/data evidence.",
                "answer": "Claim + two pieces of relevant evidence + explanation.",
                "rationale": "Strategic reasoning with justification.",
                "success": "Clear claim; strong evidence; logical explanation."
            },
            {
                "type": "Performance Task",
                "text": f"{v[2].capitalize()} two approaches to meeting the standard and {v[3]} which is more effective for a given context.",
                "answer": "Comparison + justified choice.",
                "rationale": "Evaluate alternatives; justify with criteria.",
                "success": "Compares accurately; uses criteria; coherent justification."
            }
        ]
    else:  # dok == 4
        items = [
            {
                "type": "Performance Task (Extended)",
                "text": f"{v[0].capitalize()} and {v[2]} a multi-step product/project that demonstrates this standard over time; include checkpoints and rubrics.",
                "answer": "Project plan, artifacts, reflections, final product.",
                "rationale": "Sustained synthesis; iterative refinement.",
                "success": "Coherent plan; evidence across checkpoints; rubric-referenced quality."
            },
            {
                "type": "Research/Portfolio",
                "text": f"{v[0].capitalize()} a real-world problem aligned to the standard; {v[4]} and {v[5]} your solution using multiple sources.",
                "answer": "Research log + prototype/solution + defense.",
                "rationale": "Investigation + defense across sources/time.",
                "success": "Triangulated evidence; viable solution; defended decisions."
            }
        ]

    # Attach DOK justification to each
    for it in items:
        it["dok"] = dok
        it["dok_why"] = DOK_DEFS[dok]
    return items

def make_activities(standard: str, subject: str, grade: str, dok: int):
    v = dok_verbs(dok)
    acts = []

    if dok == 1:
        acts = [
            {
                "title": "Vocabulary & Concept Sort",
                "task": f"Students {v[0]} and {v[1]} key terms/examples related to: {standard}.",
                "materials": "Word cards, definitions, example cards",
                "evidence": "Completed sort; quick exit ticket",
                "teacher": "Model 1–2 examples; check for accuracy."
            },
            {
                "title": "Guided Practice",
                "task": f"Students {v[2]} a simple procedure aligned to the standard with teacher think-aloud.",
                "materials": "Mini whiteboards or notebook",
                "evidence": "Correct steps; quick show-what-you-know",
                "teacher": "Corrective feedback on steps."
            }
        ]
    elif dok == 2:
        acts = [
            {
                "title": "Compare–Contrast Organizer",
                "task": f"In pairs, students {v[2]} two examples/non-examples and {v[3]} how/why they fit the standard.",
                "materials": "T-chart or Venn diagram",
                "evidence": "Completed organizer with reasons",
                "teacher": "Prompt for precise language from the standard."
            },
            {
                "title": "Structure to Purpose",
                "task": f"Students {v[1]} parts/features and {v[3]} how each supports the goal in the standard.",
                "materials": "Annotated sample, sticky notes",
                "evidence": "Annotations linking parts to purpose",
                "teacher": "Ask 'How do you know?' follow-ups."
            }
        ]
    elif dok == 3:
        acts = [
            {
                "title": "Evidence-Based Seminar",
                "task": f"Students {v[0]} examples and {v[1]} claims with cited evidence aligned to: {standard}.",
                "materials": "Text/data excerpts; discussion stems",
                "evidence": "Recorded claims + evidence citations",
                "teacher": "Press for warrants and counterexamples."
            },
            {
                "title": "Design–Evaluate",
                "task": f"Teams {v[2]} two solution paths, then {v[1]} which better meets criteria; present justification.",
                "materials": "Rubric, criteria chart",
                "evidence": "Comparison table; justified choice",
                "teacher": "Probe assumptions; require criteria."
            }
        ]
    else:  # dok == 4
        acts = [
            {
                "title": "Investigation/Project Cycle",
                "task": f"Students {v[0]} a problem aligned to the standard, {v[1]} sources, {v[2]} a product, and {v[5]} their approach.",
                "materials": "Research planner; checkpoints",
                "evidence": "Artifacts across checkpoints; final product",
                "teacher": "Coach milestones; calibrate with rubric."
            },
            {
                "title": "Real-World Application",
                "task": f"Learners {v[3]} and iterate on a solution for an authentic audience; reflect using rubric language.",
                "materials": "Community brief; rubric",
                "evidence": "Prototype + reflection + feedback",
                "teacher": "Arrange feedback; ensure standards alignment."
            }
        ]

    for a in acts:
        a["dok"] = dok
        a["dok_why"] = DOK_DEFS[dok]
    return acts
