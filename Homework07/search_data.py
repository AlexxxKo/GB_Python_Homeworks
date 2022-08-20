def search_data(word, data):
    if len(data) > 0:
        is_data = []
        for item in data:
            if word in item:
                is_data.append(item)
        return is_data
    else:
        return None
