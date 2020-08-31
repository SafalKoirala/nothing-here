# letter counter app
print("Letter Counter APP")
message = input("Enter a message:")
counter = input("Which letter do you want to count in your message??:")
result = (message.lower().count(counter.lower()))
print(f"Your message has {result} {counter}'s in it")  # printing using f-strings
