key_value = {}
key_value [2] = 56
key_value ["name"] = "rakesh"
key_value [1] = 23
key_value ["america"] = "canada"
key_value [40] = 56
key_value ['india'] = 'home'
print ("key_value", key_value)
print("Task 3:-\nKeys and Values sorted",
       "in alphabetical order by the value")
    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
print(sorted(key_value.items(), key=lambda kv:
                 (kv[1], kv[0])))
 
 
def main():
    # function calling
    
dictionary()
 
 
# main function calling
if __name__ == "__main__":
    main()