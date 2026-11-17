# aixcelerate-mood-guesser
My first Python AI project - Happy or Sad Mood Guesser
# AI Mood Guesser

This is my first AI project for the AIXcelerate selection task. It is a simple Python program that predicts whether a sentence expresses a Happy or Sad mood.

## Level 3: Testing

**Accuracy on the 5 practice sentences: 100%**

1. **Which sentence was closest to going wrong, and why?**

   "Today was a great day" was closest to going wrong because it did not contain any clue words from my lists. Both scores were zero, so my program selected Happy because I chose Happy when there was a tie.

2. **One change that would make my program better:**

   I would add more useful clue words and improve the program to understand negative words such as "not".

## Learning Questions

1. **Total score of "good party today" and its mood:**

   +2 + 1 + 0 = +3. The mood is Happy because the total score is positive.

2. **Total score of "bad exam day" and its mood:**

   -2 + 0 - 1 = -3. The mood is Sad because the total score is negative.

3. **Why did "exam" get a score of 0, and is this good or bad?**

   The word "exam" appeared once in a Happy sentence and once in a Sad sentence. So its score became zero. This is useful because the word alone does not indicate a particular mood.

4. **Why is "not good" labelled Happy, and how could it be fixed?**

   The word "good" has a positive score of +2, but the program does not understand the meaning of "not". It can be improved by detecting negative words and understanding the context of sentences.

## AI Declaration

I used an AI tool: **Yes**

What I asked it:

I used AI to understand the task, get help with Python code, debug errors and learn how mood prediction works.

## Reflection

The hardest part was selecting the correct clue words and understanding how the program predicts the mood of a sentence. I learned about Python functions, loops, lists, conditions and dictionaries. I also learned how a basic machine learning model can learn word scores from examples.
