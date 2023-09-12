import os
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEYS

def generateBlogTopicIdeas():
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate blog topic ideas on cryptocurrency',
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)