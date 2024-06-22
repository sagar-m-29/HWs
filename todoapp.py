class Todo():
    def __init__(self, description):
        self.description = description
    
    def __str__(self):
        return self.description
    
    def __eq__(self, other):
        return isinstance(other, Todo) and self.description == other.description 
    # Got it to work, but don't fully understand. Just understand we make each instance of the class the same if their string descriptions match up.

class Todos():

    def __init__(self):
        self.todos = []

    def add(self,todo_description):
        todo_to_add = Todo(todo_description)

        if todo_description == "" or todo_description == " " or todo_description == "  ":
            print("Error, cannot add empty string.")
        elif todo_to_add in self.todos:
            print("This is already in your todos.")
        else:
            self.todos.append(Todo(todo_description))
            print(f"{todo_description} has been added to your todos.")

    def list_todos(self):
        for todo in self.todos:
            print(todo)

    def remove(self, removal_description):

        todo_to_remove = Todo(removal_description)

        if todo_to_remove in self.todos:
            self.todos.remove(todo_to_remove)
            print(f"{removal_description} has been checked off from your todos.")
        else:
            print(f"Error, '{removal_description}' is not in your todos.")

        # WHY DOESN'T THIS WORK???
        # if Todo(todo_description) in self.todos:
        #     self.todos.remove(Todo(todo_description))
        # else:
        #     print(f"Error, {removal_description} is not in your todos.")
            
    def run(self):
        while True:
            command = input("What would you like to do? list, add, or remove? Type the respective. Type exit to end program ")

            if command == "add":
                while True:
                    description = input("What would you like to add? Type done to finish ")

                    if description.lower() == "done":
                        break
                    else:
                        self.add(description)

            elif command == "list":
                self.list_todos()

            elif command == "remove":
                while True:
                    description = input("What would you like to remove? Type done to finish ")

                    if description.lower() == "done":
                        break
                    else:
                        self.remove(description)

            elif command == "exit":
                break

            else:
                print(f"{command} is an invalid command. Please try again.")

# Now you can create an instance and run it
t = Todos()
t.run()
        

# t = Todos()
# while True:
#     command = input("What would you like to do? list, add, or remove? Type the respective. Type exit to end program ")
    
#     if command == "add":

#         while True:
#             description = input("What would you like to add? Type done to finish ")

#             if description.lower() == "done":
#                 break
#             else:
#                 t.add(description)

#     elif command == "list":
#         t.list_todos()

#     elif command == "remove":

#         while True:
#             description = input("What would you like to remove? Type done to finish ")

#             if description.lower() == "done":
#                 break
#             else:
#                 t.remove(description)

#     elif command == "exit":
#         break

#     else: 
#         print(f"{command} is an invalid command. Please try again.")

        












# items = []
# while True:
#     command = input("What would you like to do? list, add, or remove? Type the respective. Type exit to end program ")

#     if command == "add":

#         while True:
#             description = input("What would you like to add? Type done to finish ")

#             if description.lower() == "done":
#                 break
#             else:
#                 items.append(description) 

#     elif command == "list":
#         for i in items:
#             print(i) 

#     elif command == "remove":
#         while True:
#             removal_description = input("What would you like to remove? Type done to finish ")

#             if removal_description.lower() == "done":
#                 break
#             else:
#                 if removal_description in items:
#                     items.remove(removal_description) 
#                 else:
#                     print(f"Error, {removal_description} is not in your todos.")

#     elif command == "exit":
#         break

#     else: 
#         print(f"{command} is an invalid command. Please try again.")








# # class Todo():
# #     def __init__(self, description):
# #         self.description = description
    
# #     def __str__(self):
# #         return self.description

# # items = []
# # while True:
# #     command = input("What would you like to do? list, add, or delete? ")

# #     if command == "add":

# #         while True:
# #             description = input("What would you like to add? Type done to finish ")

# #             if description.lower() == "done":
# #                 break
# #             else:
# #                 t = Todo(description)
# #                 items.append(t) 

# #     elif command == "list":
# #         for i in items:
# #             print(i) # Can't figure this out

# #     elif command == "remove":
# #         while True:
# #             removal_description = input("What would you like to remove? Type done to finish ")

# #             if removal_description.lower() == "done":
# #                 break
# #             else:
# #                 if removal_description in items:
# #                     items.remove(removal_description) 
# #                 else:
# #                     print(f"Error, {removal_description} is not in your todos.")

# #     elif command == "exit":
# #         break

# #     else: 
# #         print(f"{command} is an invalid command. Please try again.")





    





# # to_do_inputs = []

# # while True:
# #     inputs = input("What's on your to-do list? Type 'finished' when finished. ")

# #     if input == "finished":
# #         break
# #     else:
# #         to_do_inputs.append(inputs) 

# # print(to_do_inputs)

# # while True:
# #     completed_tasks_questions = input(f"Which tasks have been completed from {to_do_inputs}? Type 'finished' when finished. ").split()

# #     for i in completed_tasks_questions:
# #         if i in to_do_inputs:
# #             to_do_inputs.remove(i)
            
# #         print(f"The remaining tasks to complete are: {to_do_inputs}")

# #     if len(to_do_inputs) == 0:
# #         print("Congrats, you are done!")

# #     elif "finished" in completed_tasks_questions:
# #         print("Program has ended")
# #         break

        

