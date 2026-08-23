# What $300,000 in Education Failed to Teach Me

There is a moment in my first year of medical school where I stopped taking notes mid-lecture.

My biostatistics professor had just said something. Not dramatically — almost in passing, the way you mention rain in the forecast. He moved to the next slide. My classmates kept writing.

I sat there with my hand frozen above the keyboard, because I had just realized something that made me quietly furious.

I had paid over two hundred thousand dollars for an undergraduate education at a good school. I took statistics. I got solid grades. I learned p-values, confidence intervals, hypothesis testing, the whole apparatus. And nobody, not once in four years, had told me the most important thing about any of it.

## The gap you don't notice until you do

Here is what every college statistics course teaches: how to determine whether a result is statistically significant. You learn the threshold, you learn the tests, you learn to calculate whether something is probably real or probably chance.

Here is what they don't teach: that *real* and *meaningful* are completely different questions.

My professor said it plainly. "Statistical significance tells you if an effect exists. Clinical significance tells you if it matters."

Then he moved on. As though that weren't the entire point.

I raised my hand and asked him to go back to the slide. After class I approached him.

"That distinction — that's the most important thing you said today, isn't it?"

He smiled, a little wearily. "I hope so. I try to emphasize it."

"I don't think it landed. You said it the same way you said everything else."

"You're probably right."

I've thought about that exchange more than almost anything else from that year. He knew. He had known for a long time. He said it every year and watched it fail to land every year, and had apparently made peace with the failure in a way I found genuinely upsetting.

## When true stops meaning anything

Consider what the distinction actually implies. You can prove something works — mathematically, rigorously, published in a peer-reviewed journal — and it can still be useless.

A company studies a weight-loss supplement. Ten thousand participants, six months. Result: the supplement group loses eight-tenths of a pound more than placebo.

With ten thousand participants that is statistically significant. It is real. Not luck, not noise, not measurement error. The supplement genuinely causes slightly more weight loss.

The marketing writes itself. *Clinically proven. Statistically significant results.* Both statements are true.

Also true: eight-tenths of a pound over six months is nothing. You could lose that by skipping dessert twice.

Significance says the effect is real. Significance says nothing about whether the effect matters. My education taught me to detect the first and never taught me to ask the second.

## The mechanism that breaks people's brains

Here is the part that changes how you read everything afterward.

**With enough participants you can prove almost anything has an effect, no matter how small.**

Sample size and detectable effect size are inversely related. Study a hundred people and you can only detect large effects. Study ten thousand and you can detect tiny ones. Study a hundred thousand and you can demonstrate that almost anything does *something*.

The mathematics does not care whether that something matters.

Which means that every headline announcing that a study proves X may be technically accurate and practically meaningless. Not fraud. Not bad science. Just the natural consequence of how significance testing works when you scale the sample.

## What it looks like in a real decision

Your doctor suggests a statin. "Studies show it reduces heart attack risk."

The studies are real. The effect is real. Statistically significant, replicated, solid evidence.

What the studies show is that for people with no prior heart disease, you need to treat roughly a hundred people with statins for five years to prevent one nonfatal heart attack — and around a hundred and fifty to prevent one stroke. Not one death. One heart attack. [^8]

So a hundred people take a daily medication for five years. They deal with potential side effects. They spend money on pills and visits. They become, in a small but real way, patients — people who take something every morning because a professional told them to.

And one of them benefits. The other ninety-nine were going to be fine anyway.

Is that good medicine? I genuinely don't know. It depends entirely on how a given person weighs the tradeoffs. If you're frightened of heart attacks and don't mind pills, maybe it's clearly worth it. If you'd rather not medicalize your life for a one-in-a-hundred shot, maybe not. Both positions are defensible, and the statistics don't resolve the disagreement. They only quantify it well enough that you can disagree precisely.

What makes me want to flip a table is this: my education taught me to trust *statistically significant* as a seal of quality without ever teaching me that significance says nothing about magnitude. And I went into a profession where I would be the one saying it to people.

## The question that should be taught first

Medicine has a metric for exactly this. Number needed to treat: how many people must be treated for one person to benefit.

Some calibration, with the caveat that every one of these numbers depends on the population and the endpoint being counted. Antibiotics for strep throat, single digits. Blood pressure medication after a stroke, low double digits. Aspirin given during an acute heart attack, a few dozen. Statins for primary prevention in low-risk people, around a hundred for a nonfatal heart attack — falling to forty or seventy in higher-risk groups. [^9]

All of these interventions are statistically significant. All of them work in the technical sense. And a number needed to treat in the single digits versus one in the hundreds describes wildly different clinical realities — one is close to a cure, the other is a lottery ticket with side effects.

I don't know whether other fields have an equivalent metric. They should, because it's the only question that finally matters: *how much do you have to do to get one unit of the thing you actually care about?*

## Why nobody teaches this first

I've thought a lot about why the gap exists, and I don't think it's negligence.

Statistics courses teach machinery — how to run tests, calculate p-values, interpret intervals. The mechanics are complex enough to fill a semester. By the time you've learned how to determine whether something is significant, there's no time left to ask what significance means.

Or maybe it's simpler than that. Teaching a procedure is easier than teaching judgment. You can test whether a student computes a p-value correctly. You cannot easily test whether they can weigh whether a finding is worth acting on. So the curriculum optimizes for what it can grade, which is a specific instance of the incentive problem from Chapter Five wearing academic robes.

The result is people who leave university able to detect effects without being able to evaluate whether those effects matter. That is not a gap. It's a chasm, and it runs directly through the middle of every conversation a physician has with a patient about whether to start a medication.

## The pattern generalizes

This isn't unique to statistics.

We teach people to write code without teaching them to ask whether the code should exist. We teach financial modeling without teaching when a model misleads more than it illuminates. We teach argumentation without teaching when to change your mind.

The technical skill is easier to package, test, and grade. The judgment is harder to systematize. And the judgment is the entire point.

## What I'm left with

I'm now roughly six hundred thousand dollars into my education, counting both degrees. The single most valuable thing I've learned might be the distinction between statistical and clinical significance — the idea that numbers can be true without being meaningful.

Not anatomy. Not biochemistry. Not diagnostic algorithms. That.

It should have been week one of introductory statistics. Instead it was an aside in a medical school lecture that most people missed, because nothing in the delivery signaled it was the point.

I caught it because I happened to be paying attention at the right moment. My classmates didn't, and not because they aren't brilliant — they are the fastest learners I have ever been around. They missed it for the same reason I nearly did. It was said in the same tone as everything else.

## What this means for the rest of the book

If training has a gap this large in something this central, the reader should want to know what else it has. That's most of what the remaining chapters are about.

But there's a sharper implication for the argument in Chapter Six. I've spent several chapters asking for more data to reach patients. This chapter is the reason that request carries an obligation: information handed to someone who has been taught to read *significant* as *important* isn't empowerment. It's a new way to be misled, and the misleading will feel authoritative because it comes with numbers attached.

Data abundance without this distinction produces confident, well-documented, badly reasoned decisions at scale. Which is roughly what we have now — except the people making them have medical degrees.

---
