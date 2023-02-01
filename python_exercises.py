###############################################
# Python Alıştırmalar

# Python Exercises
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.

# TASK 1: Examine the types of data structures.
###############################################

x = 8
type(x)  # output: int

y = 3.2
type(y)  # output: float

z = 8j + 18
type(z)  # output: complex

a = "Hello World"
type(a)  # output: str

b = True
type(b)  # output: bool

c = 23 < 22
type(c)  # output: bool

l = [1, 2, 3, 4, "String", 3.2, False]
type(l)  # output: list

d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)  # output: dict

t = ("Machine Learning", "Data Science")
type(t)  # output: tuple

s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)  # output: set

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

# TASK 2: Convert all letters of the given string expression to uppercase. Put space("") instead of commas and periods, separate them word by word.

# Expected output: ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']
###############################################

text = "The goal is to turn data into information, and information into insight."
words_uppercase = [word.upper() for word in text.replace(",", "").replace(".", "").split(" ")]
words_uppercase  # output: ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.

# TASK 3: Do the following tasks for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
# Step 1: Look at the number of elements of the given list.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
# Step 2: Call the elements at index zero and ten.
first = lst[0]
tenth = lst[10]
print(f"First: {first}, Tenth: {tenth}")

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
# Step 3: Create a list ["D","A","T","A"] from the given list.
new_list = lst[0:4]
new_list

# Adım 4: Sekizinci index'teki elemanı silin.
# Step 4: Delete the element in the eighth index.
lst.pop(8)
lst  # output: ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

# Adım 5: Yeni bir eleman ekleyin.
# Step 5: Add a new element.
lst.append("LOVE_MIUUL")
lst  # output: ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 'LOVE_MIUUL']

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
# Step 6: Re-add element "N" to the eighth index.
lst.insert(8, "N")
lst  # output: ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 'LOVE_MIUUL']

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

# TASK 4: Apply the following steps to the given dictionary structure.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.
# Step 1: Access the key values.
dict.keys()  # output: dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])

# Adım 2: Value'lara erişiniz.
# Step 2: Access the values.
dict.values()  # output: dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Step 3: Update the value 12 of the Daisy key to 13.
dict["Daisy"] = ["England", 13]

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Step 4: Add a new key, value:  key is Ahmet, value is [Turkey,24].
dict["Ahmet"] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.
# Step 5: Delete Antonio from dictionary.
dict.pop("Antonio")

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.

# TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists and returns these lists.
###############################################

l = [2, 13, 18, 93, 22]


def odds_evens(numbers: list[int]) -> (list[int], list[int]):
    """Takes in a list of numbers and returns two lists => odds, evens

    Args:
        numbers: list of int numbers

    Returns:
        odds: list of odd numbers
        evens: list of even numbers

    """
    odds = [number for number in numbers if number % 2 != 0]
    evens = [number for number in numbers if number % 2 == 0]
    return odds, evens


odds_evens(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

# TASK 6: In the list given below, there are the names of the students who won degrees in engineering and medicine faculties.
# Respectively, the first three students represent the success rank of the engineering faculty, while the last three students belong to the rank of the medical faculty.
# Print student grades specific to faculty using enumarate.
###############################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler):  # ogrenci refers to student
    if i < 3:
        print(f"{ogrenci}, Mühendislik Fakültesi")  # "Mühendislik Fakültesi" refers to "Engineering Faculty"
    else:
        print(f"{ogrenci}, Tıp Fakültesi")  # "Tıp Fakültesi" refers to "Medical Faculty"

"""
With list comprehension (not preferred, since less readable)
print(*((f"{ogrenci}, Mühendislik") if i < 3 else (f"{ogrenci}, Tıp") for i, ogrenci in enumerate(ogrenciler)), sep="\n")
"""
###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

# TASK 7: Below are 3 lists. In the lists, there is a course code, credit and quota information, respectively. Print course information using zip.
###############################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]
print(list(zip(ders_kodu, kredi, kontenjan)))
###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

# TASK 8: Below are 2 sets.
# You are asked to define a function; If the 1st set of cluster includes the 2nd set of cluster, print the common elements. If it does not then print the elements of the 2nd set that doesn't occure in the first set.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def print_intersection_or_difference(first_cluster: set, second_cluster: set):
    """Prints intersection values if first cluster includes second cluster otherwise prints second cluster's values that are not in first cluster.

    Args:
        first_cluster: set of cluster
        second_cluster: set of cluster


    """
    result = None
    if set(first_cluster).issuperset(second_cluster):
        result = set(first_cluster).intersection(second_cluster)
    else:
        result = set(second_cluster).difference(first_cluster)
    print(result)


print_intersection_or_difference(kume1, kume2)  # output: {'qcut', 'miuul', 'function', 'lambda'}
#  print_intersection_or_difference(kume2, kume1)  # output: {'data', 'python'}
