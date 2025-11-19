def get_num_words(filepath):
        with open(filepath) as f:
            contents = f.read()
            words = contents.split()
            n = len(words)
        return n
def get_symbol_num(filepath):
      char_dict = {}
      with open(filepath) as f:
            contents = f.read()
            lowercase = contents.lower()
      for char in lowercase:
            if char in char_dict:
                  char_dict[char] +=1
            else:
                  char_dict[char]= 1
      return char_dict
def sort_on(items):
      return items["num"]
def sorting_char(char_dic):
      result_list = []
      for char, count in char_dic.items():
            sorted_dic = {
                  "char" : char,
                  "num" : count,
            }
            result_list.append(sorted_dic)
      result_list.sort(reverse=True, key=sort_on)
      return result_list