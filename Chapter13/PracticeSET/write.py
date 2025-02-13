

for i in range(1,8):
    with open(f"Problem{i}.py", "w") as f:
        question = f"'''{i}. '''"

        f.write(question)
        
    