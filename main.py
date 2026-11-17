
# AI Mood Guesser
# AIXcelerate Task 1

# Training data
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# LEVEL 1: Count Happy and Sad sentences

def count_moods(data):
    happy = 0
    sad = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy = happy + 1
        else:
            sad = sad + 1

    return happy, sad


# LEVEL 2: Guess the mood

# My roll number ends in 5, so I use 5 words in each list.

happy_words = ["won", "friends", "surprise", "excited", "tasty"]
sad_words = ["lost", "failed", "upset", "missed", "lonely"]


def guess_mood(sentence):

    sentence = sentence.lower()

    # Remove punctuation from the sentence
    for symbol in ".,!?;:'\"()-":
        sentence = sentence.replace(symbol, "")

    words = sentence.split()

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count = happy_count + 1

        if word in sad_words:
            sad_count = sad_count + 1

    if happy_count > sad_count:
        return "Happy"

    elif sad_count > happy_count:
        return "Sad"

    else:
        # I choose Happy when both scores are equal.
        return "Happy"


# LEVEL 3: Test the program

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]

print("Mood Count:")
print(count_moods(train_data))

print("\nMood Predictions:")

correct = 0

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Predicted:", predicted_mood)
    print("Actual:", actual_mood)

    if predicted_mood == actual_mood:
        correct = correct + 1

accuracy = (correct / len(practice_data)) * 100

print("\nAccuracy:", accuracy, "%")


# BONUS: Learn word scores from training data

def learn_scores(data):

    scores = {}

    for sentence, mood in data:

        sentence = sentence.lower()

        for symbol in ".,!?;:'\"()-":
            sentence = sentence.replace(symbol, "")

        words = sentence.split()

        for word in words:

            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] = scores[word] + 1

            else:
                scores[word] = scores[word] - 1

    return scores


def guess_mood_learned(sentence):

    scores = learn_scores(train_data)

    sentence = sentence.lower()

    for symbol in ".,!?;:'\"()-":
        sentence = sentence.replace(symbol, "")

    words = sentence.split()

    total_score = 0

    for word in words:
        if word in scores:
            total_score = total_score + scores[word]

    if total_score > 0:
        return "Happy"
    else:
        return "Sad"


print("\nBonus: Learned Predictions")

for sentence, actual_mood in practice_data:
    print(sentence, "->", guess_mood_learned(sentence))
