import os
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEYS

def generateBlogTopicIdeas(topic, keywords):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate blog topic ideeas on the following topic: {} \n'.format(topic, keywords),
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    return response.choices[0].text