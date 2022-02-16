# standardize_names(character_name)
def standardize_names(character_name : str) -> str:
    return('-'.join(character_name.strip().split()))


# standardize_title(title)
def standardize_title(title : str) -> str:
    output = []
    for i ,word in enumerate(title.split()):
        output.append(word.title())
    return(' '.join(output))
       

# standardize_text(text)
def standardize_text(text : str) -> str:
    output = []
    for i ,word in enumerate(text.strip().split('. ')):
        new_word = word.replace(word[0] , word[0].upper(),1)
        output.append(new_word)
    return('.'.join(output))


# title_creator(text)
def title_creator(text : str) -> str:
    output = []
    for _ ,word in enumerate(text.split()):
        new_word = word.capitalize()
        output.append(new_word)
    return(f'--------------------{(" ".join(output))}--------------------')


# text_merge(text_of_blog_a, text_of_blog_b)
def text_merge(blog_a : str, blog_b : str) -> str:

    blog_a_splited = blog_a.strip().split()
    blog_b_splited = blog_b.strip().split()

    merged_list = []

    for i ,word_a in enumerate(blog_a_splited):
        if i < 1:
            merged_list.append(word_a.capitalize())
        elif word_a == blog_a_splited[-1]:
            word_without_dot = word_a.strip('.')
            merged_list.append(word_without_dot)
        else:
            merged_list.append(word_a)
    
    for i ,word_b in enumerate(blog_b_splited):
        if i < 1:
            merged_list.append(word_b.lower())
        else:
            merged_list.append(word_b)
    
    merged_list = ' '.join(merged_list).split('. ')

    output = []

    for i in range(len(merged_list)):
        capital_letter = merged_list[i][0].upper()
        new_phrase = merged_list[i].replace(merged_list[i][0],capital_letter,1)
        output.append(new_phrase)

    output = '. '.join(output)
    return output