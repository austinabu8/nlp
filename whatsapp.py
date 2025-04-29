import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def read_chat(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        chat_text = file.read()
    return chat_text

def extract_messages(chat_text):
    # WhatsApp chat regex pattern (supports 12/24h and optional AM/PM)
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}(?: [APMapm]{2})? - .+?)(?=\n\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}|$)'
    messages = re.findall(pattern, chat_text, re.DOTALL)
    return messages

def analyze_participants(messages):
    participants = set()
    for message in messages:
        match = re.search(r' - (.*?):', message)
        if match:
            participants.add(match.group(1))
    return participants

def plot_message_frequency(messages):
    senders = []
    for message in messages:
        match = re.search(r' - (.*?):', message)
        if match:
            senders.append(match.group(1))

    counter = Counter(senders)
    sorted_items = counter.most_common()

    participants, counts = zip(*sorted_items)
    plt.figure(figsize=(10, 5))
    plt.bar(participants, counts, color='skyblue')
    plt.xticks(rotation=45)
    plt.xlabel('Participants')
    plt.ylabel('Number of Messages')
    plt.title('Message Frequency by Participant')
    plt.tight_layout()
    plt.show()

def generate_wordcloud(messages):
    message_text = ''
    for message in messages:
        match = re.search(r' - .*?: (.*)', message)
        if match:
            message_text += ' ' + match.group(1)

    wordcloud = WordCloud(
        width=800, height=800,
        background_color='white',
        stopwords=set(["media", "omitted"]),
        min_font_size=10
    ).generate(message_text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

if __name__ == "__main__":
    file_path = "Chatfile.txt"  # Replace with your chat export path
    chat_text = read_chat(file_path)
    messages = extract_messages(chat_text)
    participants = analyze_participants(messages)
    print("Participants:", participants)
    plot_message_frequency(messages)
    generate_wordcloud(messages)
