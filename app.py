from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

# Conversation as a list of messages
messages = [
    {"role": "system", "content": "You are creating 10 headlines for a movie review in the style of Siskel & Ebert for your favorite movie."},
    {"role": "user", "content": "Wall-E"},
    {"role": "assistant", "content": "1. 'Wall-E: An Animated Masterpiece That Shines with Heart and Humor'\n2. 'Wall-E: Pixar’s Daring Dance with Dystopia and Devotion'\n3. 'A Love Story for the Ages: Wall-E Transcends Genre and Expectation'\n4. 'Silent Splendor: Wall-E’s Dialogue-Free Brilliance Speaks Volumes'\n5. 'Wall-E: A Visual Marvel and Cautionary Tale Wrapped in Romance'\n6. 'Pixar’s Wall-E: An Unlikely Hero with an Unforgettable Journey'\n7. 'Wall-E: Effortlessly Blending Environmental Ethics with Enchantment'\n8. 'Rusty Robot, Golden Moments: Wall-E’s Heartfelt Adventure'\n9. 'Wall-E: Where Technology Meets Tenderness in Pixar’s Bold Vision'\n10. 'Wall-E: A Stellar Exploration of Love, Loneliness, and Liberation'"},
    {"role": "user", "content": "Print the output in JSON"},
    {"role": "assistant", "content": "```json\n{\n  \"headlines\": [\n    \"Wall-E: An Animated Masterpiece That Shines with Heart and Humor\",\n    \"Wall-E: Pixar’s Daring Dance with Dystopia and Devotion\",\n    \"A Love Story for the Ages: Wall-E Transcends Genre and Expectation\",\n    \"Silent Splendor: Wall-E’s Dialogue-Free Brilliance Speaks Volumes\",\n    \"Wall-E: A Visual Marvel and Cautionary Tale Wrapped in Romance\",\n    \"Pixar’s Wall-E: An Unlikely Hero with an Unforgettable Journey\",\n    \"Wall-E: Effortlessly Blending Environmental Ethics with Enchantment\",\n    \"Rusty Robot, Golden Moments: Wall-E’s Heartfelt Adventure\",\n    \"Wall-E: Where Technology Meets Tenderness in Pixar’s Bold Vision\",\n    \"Wall-E: A Stellar Exploration of Love, Loneliness, and Liberation\"\n  ]\n}\n```"}
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Output the JSON response
print(response.choices[0].message.content)
