---
layout: post
title: "Changing UX Patterns in the world of Agentic AI systems"
date:   2026-03-24 22:08:00 -0500
categories: ai
tags: ["Agentic AI", "UX Design", "Knowledge Work", "AI Trust"]
---

## Speed was never the point

In the early days of enterprise software, one of the most celebrated milestones a product team could hit was a sub-100ms API response time. Dashboards glowed green. Engineering blogs were written. Users, we were told, would abandon any experience that made them wait more than a few hundred milliseconds.

That assumption was built on a specific model of computing — the lookup. The user asks. The system retrieves. The user moves on. In that world, speed was everything, because the system was just a fast librarian.

We are no longer living in that world.

![A two-panel comic strip: in 2023 the boss demands faster AI responses, in 2025 the same boss demands slower ones]({{ '/assets/images/boss_comic_strip.png' | relative_url }})
*The same boss. Two years apart. In 2026, the complaint is not that the AI was wrong — it is that it answered too fast to be trusted.*

## The wrong benchmark carries forward

The AI products being built today are still being evaluated on latency benchmarks that were designed for a fundamentally different task. We built the reflex, and now we are shipping it into contexts that require reflection.

The problem is not that fast AI responses are bad. The problem is that we are importing a metric that was right for retrieval and applying it to reasoning — and the two are not the same thing.

When a knowledge worker asks an AI agent to review a clinical trial protocol and flag statistical design risks, they are not asking for the fastest retrieval. They are asking for the most thorough, defensible, and correct analysis. Those are different jobs. And the UX that serves them well is not the same UX.

## What trust looks like in high-stakes knowledge work

Think about the domains where agentic AI is being positioned to do real knowledge work: medical research, pharmaceutical development, legal analysis, financial risk modeling, architectural review of complex systems. These are fields where the cost of a wrong answer is not measured in seconds of delay — it is measured in consequences.

Watch what happens when you interview a seasoned professional in any of these fields. Ask a senior oncologist a complex diagnostic question. They do not answer immediately. They pause. They ask a clarifying question. They say "let me look at that again." The deliberateness of the response is not a deficiency — it is a signal of competence. It is what trust looks like before it is earned.

Early attempts at shipping AI into clinical decision support learned this the hard way. The systems that responded instantly — confident, fast, polished — made clinicians uneasy. Not because the answers were always wrong, but because the confidence did not match what clinicians knew the problem required. A question that deserved ten minutes of careful analysis was answered in two seconds, and the clinician's instinct was: *this thing does not understand what I am asking*.

## A fictitious afternoon in a research lab

Imagine a medical research team using an AI assistant to analyze a new therapy candidate for a rare autoimmune condition. The researcher submits a compound profile and asks: *What are the likely off-target interaction risks given this receptor binding affinity, and are there any precedents in the trial literature we should be aware of?*

This is not a lookup question. It requires the system to traverse molecular interaction databases, cross-reference published trial adverse event profiles, apply pharmacokinetic reasoning, and synthesize findings into a structured risk assessment. It is, in the most literal sense, the work of a trained scientist.

![AI medical research assistant showing multi-step reasoning in progress]({{ '/assets/images/medical_ai_thinking_state.png' | relative_url }})
*An AI research assistant working through a multi-step reasoning chain across molecular data and trial literature — the visible progress is not overhead, it is evidence of work.*

Now, imagine two versions of this assistant.

| | **Version A** | **Version B** |
|---|---|---|
| **Response time** | Under 3 seconds | ~4 minutes |
| **What the researcher sees** | A short paragraph, two risks stated with confidence | Step-by-step progress: molecular screening, conflicting studies flagged, sample size noted, precedent trial surfaced |
| **Visible reasoning** | None | Full, auditable |
| **Researcher's ability to push back** | None — the answer simply arrives | At every step — they can redirect before the conclusion |
| **Trust earned** | Based entirely on faith in the output | Based on observed rigour in the process |

Which version does the researcher trust?

Version A might even be right more often, statistically. But Version B earns trust in a way that Version A structurally cannot. The researcher can see the work. They can audit the reasoning. They can decide where they agree and where they want to push back. The deliberation is the product.

## The UX of visible thinking

This is the design shift that most AI product teams have not yet made. The interaction model that evolved for instant-response APIs — empty state, spinner, response — does not communicate anything about how hard the question was or how carefully the system worked.

In deliberative agentic AI, the in-progress state becomes the most important surface in the entire experience.

![Comparison of instant response versus deliberative AI in drug discovery]({{ '/assets/images/ai_response_comparison_ui.png' | relative_url }})
*Left: an instant-response model returns a short answer immediately. Right: a deliberative agent surfaces its reasoning steps, data sources checked, and confidence signals — the wait is part of the answer.*

Consider what a well-designed deliberative progress state communicates to a user:

- *We are taking your question seriously.*
- *Here is where we are looking and why.*
- *Here is what we have found so far and what remains uncertain.*
- *When we give you an answer, you will know the basis for it.*

None of that is possible in an instant response model. The answer arrives, naked of context, asking the user to take it on faith. In low-stakes domains that is fine. In high-stakes knowledge work, it is a liability.

## But not every domain works this way

It would be a mistake to argue that deliberative AI is always the right model. There are entire categories of AI use where fast, direct responses are exactly what the user needs and expects — and where a slow, reflective experience would be absurd.

A drive-through ordering system needs to confirm your meal in under two seconds. A real-time language translation service needs to keep pace with speech. A customer service triage system routing an inbound call has milliseconds. In all of these contexts, the task is well-defined, the stakes per interaction are low, and the user's expectation is immediate confirmation, not collaborative analysis.

![Two contrasting AI use cases: low-stakes instant versus high-stakes deliberative]({{ '/assets/images/fast_vs_deliberative_ai_domains.png' | relative_url }})
*Left: a low-stakes transactional interaction where instant response is the right design. Right: a high-stakes analysis task where visible deliberation builds trust and enables the user to engage with the reasoning.*

The distinction that matters here is not task complexity alone — it is the nature of the consequences and the role the user plays. In transactional contexts, the user is a consumer of a decision. In knowledge work contexts, the user is a collaborator in one. Those two relationships demand fundamentally different experiences.

The mistake the industry is making is shipping the transactional model into the collaborative context, because the benchmark infrastructure was built for the former.

## The trust curve

There is a subtle but important dynamic at work here that goes beyond individual task quality. Over time, users in high-stakes domains will calibrate their trust not just based on whether an AI got the answer right, but on whether the AI demonstrated that it understood how hard the question was.

A model that always answers in two seconds, regardless of the complexity of the question, is communicating something to its user: *I am treating all questions the same.* That is not reassuring to someone who knows that the questions are not the same.

A model that takes longer on harder questions — and makes that visible — is communicating something very different: *I understand the stakes, and I am working accordingly.* That calibration is itself a form of intelligence.

This is, incidentally, not a novel dynamic in human expertise. We do not trust doctors who answer without hesitation. We trust doctors who say "I want to look at this more carefully before I give you a recommendation." The hesitation is the competence signal.

## What product teams should be building

The implications for product design are significant. For agentic AI in knowledge-intensive domains, product teams need to invest heavily in the in-progress experience, not just the response format.

This means:
- **Transparent reasoning chains** — user-visible steps that show what the agent is doing, not just a spinner
- **Intermediate surfacing** — partial findings shared as they emerge, not held until the final answer
- **Confidence differentiation** — explicit signals where the agent is more or less certain, and why
- **Pause and redirect** — the ability for the user to redirect the agent mid-task based on what they see in the reasoning chain

These are not refinements. They are the product. For a knowledge worker whose professional reputation depends on the quality of their analysis, understanding *how* the AI reached its answer is at least as important as the answer itself.

## The case for async: come back when it is ready

There is a design pattern that the industry has not yet fully embraced, but which follows naturally from everything above: the asynchronous answer.

Not every question needs to be answered in the same session. In fact, some of the most valuable questions a knowledge worker poses to an AI agent are ones that genuinely require hours — or longer — to answer well. Cross-referencing a clinical literature corpus. Stress-testing a financial model against multiple market scenarios. Running a full legal precedent sweep across decades of case law. For tasks of that depth, the right UX is not a spinner with a progress bar. It is a notification.

*Your analysis is ready. Come back when you are.*

This sounds simple, but it represents a profound shift in how we think about the human-AI interaction loop. The current mental model — inherited from the web request — assumes that the user is waiting and the system must fill that wait as quickly as possible. The async model flips this: the system works at the pace the problem demands, and the user returns on their own terms.

The civilizations in Douglas Adams' *The Hitchhiker's Guide to the Galaxy* understood this intuitively. When they needed the answer to the ultimate question of life, the universe, and everything, they did not ask for a fast API. They commissioned a computer called Deep Thought — and then they waited.

![A two-panel comic: beings ask Deep Thought for the ultimate answer, Deep Thought tells them to return in 7.5 million years; their descendants return and receive the answer: 42]({{ '/assets/images/deep_thought_comic.png' | relative_url }})
*Deep Thought had the right idea. The answer took 7.5 million years. The beings who came back still did not know what to do with it — because they had forgotten the question. A lesson in async UX: make sure the context travels with the answer.*

The comedic point Adams was making — that the answer is useless without remembering the question — is actually a sharp design insight. Async AI answers carry a UX responsibility that synchronous ones do not: the system must return not just the answer, but the full context of what was asked, why it was asked, what path the reasoning took, and what the user should do next. An answer that arrives hours later with no surrounding context is nearly as useless as "42."

What this means in practice for product teams:

- **Persistent reasoning artifacts** — the thinking trail must be stored and returned alongside the answer, not discarded once the response is generated
- **Re-entry context panels** — when the user returns to a completed analysis, the first screen should re-establish what was asked and what the agent found, before presenting conclusions
- **Notification with summary** — the delivery mechanism (email, push, in-app) should include a one-line summary so the user can decide *when* and *how* to engage with the full result
- **Versioned answers** — for long-running tasks, interim checkpoints should be saved so the user can see how the answer evolved as more data was processed

What this looks like in practice is less radical than it sounds. A well-designed async experience has three moments: the quiet handoff when the task begins (*"I have started working on this — you can close this window"*), the re-entry landing when the user returns (*here is what you asked, here is what was found, here is how to go deeper*), and the reasoning trail that makes the answer auditable long after the session ends.

![Elegant async AI UX showing three states: a ready notification, a re-entry context card with the original question and summary, and a collapsible reasoning timeline]({{ '/assets/images/async_answer_ux.png' | relative_url }})
*A well-designed async answer experience: the notification surfaces the summary, the re-entry card restores the original question, and the reasoning timeline lets the user audit the thinking before diving into the conclusions.*

The async pattern is not a workaround for slow AI. It is an acknowledgment that some questions deserve the kind of time and rigor that no human knowledge worker could sustain in a single sitting — and that the right answer to *how long will this take* is sometimes: *longer than you want to wait right now, and that is fine.*


## A new latency to optimize for

The industry will eventually get here. The latency benchmarks will not disappear — they should not, because they remain the right metric for the right domains. But alongside them, a new benchmark will emerge: the quality of the in-progress experience in deliberative agents.

How much useful signal can the system surface during its thinking? How well does the visible reasoning reflect the actual reasoning? How effectively does the progress state help the user calibrate their trust before they receive the final output?

Those are the questions worth optimizing for when the task is not retrieval but reasoning. And the sooner product teams realize that fast is not always better — that in many of the most valuable contexts, the pause is what earns the trust — the better they will serve the users they are building for.

---

*The most important thing an agentic AI can show a user is not the answer. It is the thinking behind the answer. That is what knowledge work has always rewarded in the people who do it. The tools are catching up.*
