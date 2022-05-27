
def read_file_content():
    file = open('story.txt', 'r')
    read_data = file.read()
    return(read_data)



from collections import Counter

def count_word(file_name):
        with open('story.txt') as f:
                return Counter(f.read().split())

print("Frequency :",count_word("story.txt")) 



  
    