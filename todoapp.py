to_do_inputs = []

while True:
    inputs = input("What's on your to-do list? Type 'finished' when finished. ").split()
    to_do_inputs.extend(inputs) # .extend() vs .append()

    if "finished" in inputs:
        inputs.remove("finished")
        to_do_inputs.remove("finished") # .remove() vs .pop()
        break

print(to_do_inputs)

while True:
    completed_tasks_questions = input(f"Which tasks have been completed from {to_do_inputs}? Type 'finished' when finished. ").split()

    for i in completed_tasks_questions:
        if i in to_do_inputs:
            to_do_inputs.remove(i)
            
        print(f"The remaining tasks to complete are: {to_do_inputs}")

    if len(to_do_inputs) == 0:
        print("Congrats, you are done!")

    elif "finished" in completed_tasks_questions:
        print("Program has ended")
        break

        

