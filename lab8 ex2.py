feedback = input("Enter your feedback: ")

target_words = ["bad", "hate", "stupid"]

for word in target_words:
    feedback = feedback.replace(word, "****")
    feedback = feedback.replace(word.capitalize(), "*****")
    feedback = feedback.replace(word.upper(), "******")

print("Filtered Feedback:", feedback)