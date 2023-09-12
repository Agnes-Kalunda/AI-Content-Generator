import os
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEYS

blog_topics = []

def generateBlogTopicIdeas(topic, keywords):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate blog topic ideeas on the following topic: {}\nKeywords: {} \n*'.format(topic, keywords),
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    return response.choices[0].text



def generateBlogSectionHeadings(topic, keywords):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate blog section headings and section titles, based on the following blog section topics.\nTopic: {}\nKeywords: {}\n*'.format(topic, keywords),
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    return response.choices[0].text




# res= generateBlogTopicIdeas(topic, keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#     blog_topics.append(blog)
#     print('\n')
#     print(blog)