marks = {
"Ankit":95,
"bipul":50,
"ram":88

}
# print(marks.items())
print(marks.keys())
print(marks.values())
# print(marks.get("Ankit"))
marks.update({"Ankit":85})
print(marks)
print(marks.get("sweeta")) 
marks.pop("bipul")
print(marks)