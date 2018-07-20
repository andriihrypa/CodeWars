def filter_words(yelling):
    no_yelling = yelling.lower()
    no_yelling = no_yelling.split()
    no_yelling = " ".join(no_yelling)
    no_yelling = no_yelling.capitalize()
    return no_yelling


print(filter_words(" no   YELLING!!!"))