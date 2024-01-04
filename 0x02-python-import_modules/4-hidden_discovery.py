#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_of_names = dir(hidden_4)
    for i in range(len(list_of_names)):
        if (list_of_names[i])[:2] == "__":
            continue
        print(list_of_names[i])
