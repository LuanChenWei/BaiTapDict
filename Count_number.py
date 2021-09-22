
def count(chuoi,num_words):
    num_words = {"key": "value"}
    text_list = chuoi.split()
    my_list = 0
    for i in text_list:

        if i == num_words.get("key"):
            my_list += 1
    return my_list

my_string = "ngày xửa ngày xưa"


dict = {"word": "ngày"}

deploy = count(my_string, dict)

print(deploy)