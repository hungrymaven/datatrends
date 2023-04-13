import openai

# Replace 'your_api_key' with your actual API key
openai.api_key = "your_api_key"

# Example: prompt for the OpenAI API
prompt = "What are the most important variables for improving marketing campaigns?"

# Example: call the OpenAI API to generate a response
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated response
print(response.choices[0].text.strip())
