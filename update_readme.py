import datetime
import random

quotes = [
    "Build things that matter.",
    "Dream big. Start small. Ship fast.",
    "Code today. Change tomorrow.",
    "AI will not replace you, but people using AI will.",
    "Consistency beats talent."
]

quote = random.choice(quotes)

time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start_q = "<!--QUOTE_START-->"
end_q = "<!--QUOTE_END-->"

start_t = "<!--TIME_START-->"
end_t = "<!--TIME_END-->"

content = content.split(start_q)[0] + start_q + "\n\n" + quote + "\n\n" + end_q + content.split(end_q)[1]
content = content.split(start_t)[0] + start_t + "\n\n" + time + "\n\n" + end_t + content.split(end_t)[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
