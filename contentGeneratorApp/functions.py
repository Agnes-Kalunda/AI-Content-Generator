import os
import openai
from django.conf import settings
from decouple import config

openai.api_key = config('OPENAI_API_KEYS')



def generateBlogTopicIdeas(topic, audience, keywords):
    blog_topics = []

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate 5 blog topic ideas on the following topic: {}\nAudience: {}\nKeywords: {} \n*'.format(topic, audience, keywords),
        temperature=0.7,
        max_tokens=250,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']

        else:
            return []
        
    else:
        return []
    
    # Split the response into lines and add them to the blog_topics list
    lines = res.split('\n')
    for line in lines:
        if line.strip():  # Skip empty lines
            blog_topics.append(line)

    return blog_topics





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
    
    if 'choices' in response:
        if len(response['choices']) > 0:
            res = response['choices'][0]['text']
        else:
            res = None

    else:
        res = None

    # Split the response into lines and add them to the section_headings list
    section_headings = []
    lines = res.split('\n')
    for line in lines:
        if line.strip():  # Skip empty lines
            section_headings.append(line)

    return section_headings

# res= generateBlogTopicIdeas(topic, keywords).replace('\n', '')
# b_list = res.split('*')
# for blog in b_list:
#     blog_topics.append(blog)
#     print('\n')
#     print(blog)