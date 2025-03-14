from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data,chunk_size=4):

    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i+=1
        if i==chunk_size :
            yield chunk
            chunk=[]
    yield chunk 
