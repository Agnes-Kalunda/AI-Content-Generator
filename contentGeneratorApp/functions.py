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





def generateBlogSectionTitles(topic, audience, keywords):
    blog_sections = []

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate 10 blog section titles for the provided blog topic: {}\nAudience: {}\nKeywords: {} \n*'.format(topic, audience, keywords),
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
            blog_sections.append(line)

    return blog_sections



def generateBlogSectionDetails(blogTopic, sectionTopic, audience, keywords):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt='Generate detailed blog section write up for the following blog section heading , using the blog title, audience and keywords provided.\nBlog Title: {}\nBlog Section Heading: {}\nAudience: {}\nKeywords: {}\n\n'.format(blogTopic, sectionTopic, audience, keywords),
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        best_of=1,
        frequency_penalty=0,
        presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
            cleanedRes = res.replace('.\n', '<br>')
            return cleanedRes

        else:
            return ''
        
    else:
        return ''






