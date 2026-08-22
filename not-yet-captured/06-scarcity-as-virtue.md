# Scarcity as Virtue

There is a peculiar sensibility in medicine that took me most of a year to name. A friend and I started calling it an anti-abundance mentality, which is clumsy but close enough. It is the reflex that greets every new source of information — a continuous monitor, a whole-body scan, a patient portal, a wearable that logs something nobody asked it to log — with suspicion rather than curiosity. The default assumption is that more information is dangerous until proven otherwise.

To people who work in technology this looks backwards to the point of parody. In tech, data abundance is obviously good. More signal means better models, faster iteration, clearer patterns. Storage costs approach zero, so you capture everything and figure out later what mattered. The idea that you would deliberately collect *less* information about a system you are responsible for keeping alive strikes a software engineer as something between negligence and superstition.

Medicine has internalized scarcity as a virtue. And here is the part that took me longest to accept: it did so for reasons that are not stupid.

I want to be careful, because the easy version of this chapter writes itself and it is wrong. The easy version says doctors are technophobes, the establishment protects itself, and if everyone would just embrace data things would improve. That version is satisfying, and it will not survive five minutes with anyone who has actually watched a patient get hurt by a test they did not need.

The real argument is narrower and, I think, harder to dismiss. Medicine is applying one category of reasoning to two categories of thing. It treats gathering information and taking action as the same kind of risk, requiring the same kind of justification, subject to the same standing presumption against excess. They are not the same kind of risk, and the conflation of them is where most of the damage gets done.

## Why doctors learned to say no

Medical training is an extended exercise in restraint. You learn early that every intervention carries risk — radiation exposure, false positives that trigger cascading procedures, the anxiety of knowing something ambiguous about your body. Resources are genuinely finite in ways they aren't in tech: operating room time, specialist availability, someone's actual kidney. A software team that over-provisions servers wastes money. A clinical team that over-provisions interventions wastes people.

More importantly, you are taught that ordering lots of tests is the mark of a bad doctor. It suggests you don't know what you're looking for. The impressive attending is the one who needs fewer data points to reach the right diagnosis. Clinical acumen shows up as parsimony.

This makes sense in context. Shotgunning labs because you're intellectually lazy *is* bad medicine. The doctor who orders a comprehensive metabolic panel, complete blood count, lipid panel, thyroid function, vitamin levels, and tumor markers for a patient with a headache isn't being thorough — they're avoiding the harder work of clinical reasoning. The test does not think for you. Ordering all of them is a way of outsourcing a decision you have not made, and the outsourcing is visible to anyone senior enough to read the chart.

So restraint becomes sophistication. Scarcity becomes a North Star.

I want to sit with that longer than the argument strictly requires, because it is the load-bearing objection to everything that follows. The parsimony reflex is not decoration. It does real work. It is, among other things, the mechanism by which medicine polices its own laziness, and nobody has proposed a better one. A profession that could not tell the difference between the clinician who reasons and the clinician who orders would be a worse profession, and patients would be the ones paying the difference. Any argument for abundance that cannot say what replaces that function is not an argument. It is a complaint.

## When the constraint disappears

The problem is that the mentality persists after the constraint that produced it has vanished.

This is not unique to medicine. Every institution carries rules whose original justification expired quietly, without anyone noticing, because the rule had become identity rather than technique. What makes medicine's version consequential is that the expired rule now governs what people are permitted to know about their own bodies.

Consider what actually happened with continuous glucose monitoring. When the first CGM devices reached the market around 1999 and 2000, enthusiasm cooled fast, even inside the research community. The sensors drifted. The FDA approved the first device only as a supplement to standard home glucose monitoring — occasional use, not everyday use. [Cite: PMC8120065; ScienceDirect S187140211730303X]

Read the objections from that period and you find they are not primarily technical. Physicians argued that patients did not need continuous data when a quarterly A1C was sufficient. The listed barriers were lack of FDA approval for insulin dosing, cost and variable reimbursement, the need for recalibration, and lack of physician training in interpreting results. Physicians themselves were named as a major barrier to implementation, facing time demands impossible to meet in a brief visit, unclear reimbursement, medico-legal exposure, and the ordinary uncertainty that attends anything new. [Cite: PMC4717493]

That is a complete inventory of reasonable-sounding reasons to wait. Every one of them is about the system's capacity to absorb the information rather than about whether the information was true or useful. Notice that distinction, because it recurs. Almost none of the resistance to any of these technologies has been a claim that the data is wrong. It has been a claim that the data is inconvenient, and the two get argued in the same tone.

Then the evidence arrived. Patients could see patterns in real time, adjust behavior, catch dangerous swings before they became events. By 2016 — seventeen years after the first device — sensor accuracy was good enough that the FDA approved continuous readings to replace fingerstick testing altogether. [Cite: HealthCentral, CGM overview] "Too much data" had become standard of care. Seventeen years.

Pulse oximetry is the same story on a longer clock, and it is worth telling in full because the ending is so familiar that the beginning sounds invented. The technology was developed in the early 1970s. The first commercial device in Japan was regarded as a useful research instrument but not a clinically viable one; roughly two hundred units sold. [Cite: PMC11330276] It did not become widely available until the 1980s, and there was still live debate in the late 1990s about whether routine pulse oximetry was warranted for emergency department patients. [Cite: ACP Hospitalist, Newman] In 1988, Thomas Neff proposed treating oxygen saturation as a fifth vital sign — a suggestion that now reads as self-evident and at the time was a proposal that had to be argued for. [Cite: ACP Hospitalist; CHEST S0012-3692(16)30698-5] By the end of that decade it had become standard for monitoring anesthesia and joined the ECG as routine for critically ill patients.

Roughly forty years, then, from proof of concept to a device whose absence from a room would now constitute a deficiency. There is no clinician practicing today who would defend the forty years. There are many who would have participated in it.

Liquid biopsy is the same story happening in the present tense, where we can watch it rather than reconstruct it. Adoption for excluding patients from targeted therapy has been slow, driven largely by concern about false negatives; current guidance is that a negative liquid biopsy should be followed by tissue sequencing. [Cite: College of American Pathologists] The stated barriers are workflow integration, the need for clinician training in interpretation and limitations, and a lack of protocol standardization. [Cite: PMC12140778] The objections are the familiar set: false positives leading to unnecessary treatment and psychological distress, false negatives delaying diagnosis, an unsettled regulatory picture, and the management of incidental findings.

Meanwhile the evidence accumulates anyway, the way it did before. PADA-1 demonstrated improved progression-free survival using liquid biopsy to guide therapy. plasmaMATCH found ninety-six to ninety-nine percent concordance between liquid biopsy and tissue sequencing. [Cite: Nature s43856-025-00885-9] Multi-cancer early detection tests are moving from curiosity to product while the profession is still deciding how it feels.

Three technologies, three decades apart, one sequence. A technology becomes feasible. The people who built it are enthusiastic. The establishment resists, citing practical concerns, absent evidence, false positives, cost, and workflow disruption. Contrarians use it anyway and study it. Evidence accumulates over ten to twenty years. The establishment accepts it, grudgingly. And then — this is the step that matters most — the delay gets described retroactively as appropriate caution.

That last step is what guarantees the cycle repeats. It converts a fifteen-year institutional failure into a story about prudence, and a profession that tells itself that story has learned nothing it can carry to the next technology. The lag is remarkably consistent, roughly fifteen to twenty-five years from proof of concept to mainstream acceptance. That number does not track how long the technology needed to mature. It tracks how long the institution needed to stop objecting.

## Four reasons the reflex outlives its reason

If the pattern is this legible, why does it keep happening? I can identify four mechanisms, and they compound.

The first is training trauma. Medical education rewards doing less and punishes shotgunning tests, which is correct as pedagogy and disastrous as permanent disposition. After years of being graded on restraint, abundance does not feel like a neutral option with tradeoffs. It feels like a professional failure — like being caught not knowing. This is the difference between a technique and an identity, and the distinction is not academic: you can update a technique when the evidence changes. Updating an identity costs something, and people are reluctant to pay it in front of colleagues.

The second is legitimate bad experience. Every doctor who has practiced long enough has seen the patient whose incidental finding led to a biopsy, which led to a complication, which led to an outcome worse than the disease that was never there. These stories have weight, and they should. But the precautionary principle gets overapplied in a specific and asymmetric way: because abundance *can* cause harm, the default becomes scarcity. The harm from information is vivid and attributable. The harm from its absence is invisible and unattributed. Nobody tells the story of the cancer that would have been caught, because nobody knows it was there.

The third is payment models frozen at old economics. Reimbursement still treats testing as expensive even as the underlying cost collapses. Insurance will pay for a comprehensive metabolic panel and not for continuous metabolic monitoring, though the second might prevent the emergency the first missed. The system's architecture assumes a scarcity the economics no longer support, and culture follows architecture far more reliably than it follows argument. This is the least glamorous item on the list and probably the most powerful.

The fourth is status. Clinical judgment is demonstrated by needing less data to reach the answer, so any tool that makes diagnosis easier threatens the demonstration. The physician who catches early sepsis from experience and intuition is impressive in a way the physician who catches it from an alert is not, even when the second one catches it earlier and the patient does better. I do not think this is usually conscious. I think it is a selection pressure applied gently and constantly to how clinicians describe their own competence, and therefore to which tools they are eager to adopt.

None of these four is stupid. Three of them are load-bearing. That is exactly what makes the reflex durable, and why "be more open to technology" is a sentiment rather than a strategy.

## The distinction the whole argument rests on

Here is the claim this chapter exists to make.

Abundance of data is usually good. Information is cheap to gather, cheap to store, cheap to analyze. Continuous monitoring, comprehensive panels, patient-generated health data — these should default to yes when the technology allows it and the patient wants it.

Abundance of action is often bad. Interventions carry real risk and real cost. You should not do procedures that will not change management. Selective decision-making is correct here, and the restraint medicine has built around it is a genuine achievement rather than a bug to be engineered away.

Any business owner understands this instinctively in their own domain. You have a hundred ideas. Each change carries a starting cost and training friction that scale across the whole operation, so you want to be confident the gains will exceed the temporary loss across the team. That is discipline about *action*. It is not an argument for knowing less about your business. Nobody has ever improved an operation by deliberately reducing its instrumentation, and if a consultant proposed it you would stop taking their calls.

The error is applying intervention-logic to information-gathering. They are different categories and they need different heuristics.

Once you separate them, the profession's own rhetoric starts to sound strange. "First, do no harm" is a principle about interventions. It has been quietly extended into something closer to *first, gather no information that might lead someone to take an action*, which is not the same principle and does not follow from it. Getting a scan is not an intervention. Looking at your own glucose data is not an intervention. Having continuous vitals monitored is not an intervention. The harm, when it comes, comes from what is done in response to the information — which is precisely why the two deserve separate rules rather than one shared presumption.

Collapsing them does not produce caution. It produces paralysis, and then dresses the paralysis in the language of prudence.

## The real objection, which is not philosophical

I said the easy version of this chapter is wrong, and this is where that matters most.

The actual reason clinicians resist more data is not that they believe less information is better. Almost none of them believe that, and if you ask directly they will say so. The reason is that they have no good way to process what they would receive.

A continuous glucose monitor generates thousands of data points. If a physician has to eyeball raw traces during a fifteen-minute appointment, abundance is not a gift. It is a burden, a medico-legal liability, and one more thing that will not fit in the visit. The instinct to refuse it is not obscurantism. It is triage, and triage is a skill.

But notice what kind of problem that is. If the same system says *A1C equivalent 7.2 percent, nocturnal hypoglycemia clustering on Tuesday nights, likely related to Monday evening dosing* — then abundance becomes useful immediately and obviously, and no clinician on earth would refuse it.

Healthcare has abundance at the collection layer and extreme scarcity at the interpretation layer. We have monitors, wearables, cheap sequencing, ambient capture. We have one clinician's attention for fifteen minutes. The mismatch between those two numbers is the whole problem, and it is an infrastructure problem rather than a fundamental constraint.

This is worth stating plainly, because it changes what the argument is asking for. I am not asking clinicians to absorb more. Asking a physician to review a thousand data points in a fifteen-minute visit is not a reform; it's a joke with a bad punchline. I am saying that the correct response to "we cannot process this" is to build the processing layer — and that the refusal has been standing in for the building for about two decades now.

[SCENE NEEDED — one paragraph, from rotations: a moment where the information existed and could not be used. A chart with everything in it and no time to read it, a monitor alarming into an empty hallway, a patient arriving with a wearable export nobody opened. This is the chapter's most important scene and I won't invent it; it has to be a real one, with the texture of the actual room.]

## The reframe

The calculation medicine currently runs is: *what is the harm of this extra test?* Radiation. False positives. Cascading procedures. Patient anxiety. Cost. Each of those is real, and each is countable, which is part of why they dominate the conversation.

The reframe is: *what is the harm of not having this information when we need it?* The patient whose cancer would have been visible and wasn't looked for. The diabetic whose dangerous pattern was invisible between quarterly checks. The cardiac event that continuous monitoring would have flagged and standard vitals missed.

These harms are real too. They are simply not attributable. Nobody writes a case report about the diagnosis that was never made, because there is nothing to write about — the patient went home, and the thing that was going to happen happened later, to a different doctor, in a different building, with no visible line connecting the two.

So the ledger is kept in a currency that systematically favors one side. The costs of information are itemized. The costs of its absence dissolve into the general background of people getting sick, which is what we expect people to do anyway.

I am not asking for the burden of proof to be reversed. I am asking for it to be symmetrical. Show me evidence that abundant data causes net harm in a given modality, and show me evidence that it produces net benefit, and let each modality prove itself either way. Right now the asymmetry is the default: abundance must demonstrate benefit, while scarcity is assumed safe, and the assumption is never itself put to the test.

CGMs won this argument with evidence rather than rhetoric. Studies showed better outcomes. The skeptics were proven wrong by data about data. Early cancer detection and longitudinal health tracking will have to win the same way, modality by modality, and they should. What they should not have to do is win against a presumption that was never examined.

## What this costs on the receiving end

Everything above is an argument about institutions. Here is the version that matters, which is what the reflex feels like from the chair.

You are told a test isn't necessary. That may be entirely correct. It may also be the output of a reimbursement rule, a training reflex, or a fifteen-minute visit with no room in it — and from where you are sitting, all four are indistinguishable. They arrive in the same sentence, in the same tone, from a person you have no particular reason to doubt.

You ask for your own data and meet friction that is difficult to interpret. The stated reason is that you might misunderstand it, or worry unnecessarily, or make a bad decision. Sometimes that concern is genuine and well founded. But the paternalism is barely concealed even when it is well meant, and patients hear it clearly. The message is that information about your body is yours in principle and someone else's in practice.

This, more than any individual technology fight, is what I think the profession is actually risking. When physicians reflexively dismiss things patients find valuable, and when the gap between what is technically possible and what is clinically permitted grows wide enough to see from outside, patients do not conclude that medicine is being careful. They conclude that medicine is hiding something, or protecting something, or simply isn't interested. And then they leave — not the healthcare system, which they still need, but its authority, which they stop consulting first.

I see the destination of that trajectory every week in the startup ecosystem. It takes one company with real distribution and anti-medicine messaging to convert a diffuse feeling of alienation into a market. The people building that company do not need to be right. They need to be more interested in the patient's question than the establishment was. That is a low bar, and we keep failing to clear it.

## What restraint was actually for

I said at the start that the parsimony reflex does real work, and I want to end there rather than pretend otherwise.

The scarcity mentality is load-bearing for quality in the current system. It prevents genuine waste. It prevents genuine harm. It is the mechanism that separates the clinician who reasons from the clinician who orders, and nobody has built a replacement for that function. You cannot simply remove it and expect the structure to stand.

So the argument is not: abandon restraint. The argument is that restraint was always about *action*, and somewhere along the way it was extended to cover *information*, and the extension was never examined because it never had to be. When tests were expensive and invasive, the two moved together closely enough that nobody needed to separate them. They do not move together anymore. A sleep mask that logs biometrics passively and cheaply has no meaningful relationship to an exploratory laparotomy, and a rule that governs both is not a rule. It is a habit with a rule's reputation.

Separating them gives medicine a way to become pro-data without becoming reactive and wasteful. Keep the discipline exactly where it belongs, on the decision to act. Move the default on gathering, one modality at a time, as each proves itself — and hold the profession to noticing when it does.

The culture will not change through argument. It will change the way it changed for CGMs and for pulse oximetry: through specific victories that accumulate until the old posture becomes untenable. Virtues do not yield to reasoning. They yield when the world makes the old virtue obsolete and the new one necessary.

Which raises the obvious objection, and it is a good one. If the parsimony instinct is this well founded, and the harms of overtesting this well documented, why should anyone accept an argument for abundance from someone who has not yet watched a patient absorb the consequences of an incidental finding?

That is the right question, and it deserves a full answer rather than a paragraph. The next chapter is that answer.

---

*[Draft — Wave 1. Citations inline in brackets, moving to Notes at compile; sources are those compiled for the seed essay and need verification against primary literature before typesetting (see `writing-plan.md` §6.2). One scene marked as needed.]*
