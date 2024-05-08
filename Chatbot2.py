from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot("SimpleChatBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Function to get response from the chatbot
def get_response(user_input):
    return chatbot.get_response(user_input)

# Main function to interact with the chatbot
def main():
    print("Simple ChatBot:")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("ChatBot:", response)

if name == "__main__":
    main()