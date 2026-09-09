import google.generativeai as genai

API_KEY = '<REDACTED>'
genai.configure(api_key=API_KEY)

# Update this line:
model = genai.GenerativeModel("gemini-3.8-flash")



def chat_with_bot(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()


print("Welcome to Gemini Chatbot! Type 'exit' to quit.\n")
while True:
    user = input("You: ")
    if user.strip().lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    bot = chat_with_bot(user)
    print("Chatbot:", bot)