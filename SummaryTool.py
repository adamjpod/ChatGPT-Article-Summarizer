import os
from newspaper import Article
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)



def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article_content = article.text
        print("Article Content Extracted")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please summarize the following article: {article_content}"}
            ]
        )

        summary = completion.choices[0].message.content
        print(f"Summary: {summary}")

    except Exception as e:
        print(f"Error: {e}")


url = input("Enter the article URL: ") # https://newsroom.bugatti.com/press-releases/the-new-bugatti-tourbillon-makes-its-debut
summarize_article(url)