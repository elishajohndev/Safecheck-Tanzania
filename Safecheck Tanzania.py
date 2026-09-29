print("====SAFE CHECK TZ====")
message=input("Enter the message you want to check:")
print("you entered:")
print(message)

suspicious_words = [
    # Prize and reward scams
    "you have won",
    "claim your prize",

    # Account and security threats
    "your account has been blocked",
    "your account will be closed",
    "your account is temporarily suspended",
    "verify your identity",
    "verify your account",
    "confirm your account",
    "security alert",

    # Urgency
    "urgent",
    "immediately",
    "act now",

    # Money requests
    "send money",
    "make a paynment",
    "pay now",
    "your paynment has failed",

    # Personal information
    "password",
    "otp",
    "pin",
    "verification code",

    # Suspicious actions
    "click this link",
    "open this link",
]
message_lower = message.lower()
risk_score = 0
for word in suspicious_words:
    if word in message_lower:
        print("Warning sign detected:", word)

        if word == "your account will be closed":
            risk_score = risk_score + 2
        elif word == "security alert":
            risk_score = risk_score + 1
        elif word == "verify your identity":
            risk_score = risk_score + 2
        else:
            risk_score = risk_score + 1
if "http://" in message_lower or "https://" in message_lower or "www." in message_lower:
       print("Warning sign detected: Link found")
       risk_score = risk_score + 2
       
if risk_score == 0:
    print("Risk level: SAFE")
elif risk_score <= 2:
    print("Risk level: SUSPICIOUS")
else:
    print("Risk level: HIGH RISK")

if risk_score == 0:
    print("Recommendation: The message appears safe but stay cautious.")
elif risk_score <= 2:
    print("Recommendation: Be careful. verify the sender before taking action")
else:
    print("Recommendation: Do not click or share personal information. Verify the sender through an official source.")


