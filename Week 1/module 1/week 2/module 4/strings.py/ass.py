
# Simple Email Spam Filter

email = input("Enter the email content: ")

spam_keyword = ("free", "Goal")
email_lowercase = email.lower()

result = any(keyword in email_lowercase for keyword in spam_keyword)

print(result)
