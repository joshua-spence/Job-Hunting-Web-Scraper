# noinspection PyUnresolvedReferences
from Monster import monster
# noinspection PyUnresolvedReferences
from Indeed import indeed

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

c = monster(a, b)
d = indeed(a, b)

# myJobs = c.find_all('h2', string=lambda text: a in text.lower())
# print(len(myJobs))
#
# if len(myJobs) < 1:
#     print("No jobs found")
# else:
#     print("Search results from Monster: ")
#     print("\n")
#     for j in myJobs:
#         link = j.find('a')['href']
#         print(j.text.strip())
#         print(f"Apply here: {link}\n")


# role = True
#
# while role:
#
#     print("Chose job role: ")
#     c = input()
#     if c == "/exit":
#         break
#
#     myJobs = results.find_all('h2', string=lambda text: c in text.lower())
#     print(len(myJobs))
#
#     if len(myJobs) < 1:
#         continue
#     else:
#         print("Serch results from Monster: ")
#         print("\n")
#         for j in myJobs:
#             link = j.find('a')['href']
#             print(j.text.strip())
#             print(f"Apply here: {link}\n")
#         break
