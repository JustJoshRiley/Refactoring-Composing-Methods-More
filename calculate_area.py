# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(list):  # TODO: Rename this function to reflect what it's doing.
    m = list[0]
    for value in list:
        if value > m:
            m = value
    return m


list = [5, -1, 43, 32, 87, -100]
print(get_max_value(list))

############################
def split_sentence_by_space(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(split_sentence_by_space('If you were a vegetable, you’d be a ‘cute-cumber.'))