def get_bot_response(user_input):

    if user_input is None:
        return "Please say something."
    
    responses = {
        "hello": "Hello! How can I help you today?",
        "bye": "Goodbye! Have a nice day!",
    }
    return responses.get(user_input.lower(), "I'm not sure how to answer that.")
