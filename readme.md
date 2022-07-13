# Todolist with django

## Database models
- Collection
  - id (UUIDField)
  - name (CharField)
  - slug (SlugField)

- Task
  - id (UUIDField)
  - description (TextField)
  - collection (ForeignKey)

## Features
[  ] Add a collection  
[  ] Delete a collection  
[  ] Delete a collection  
[  ] Prevent adding an existing collection  
[  ] Add a task  
[  ] Remove a task  
[  ] Show tasks in a collection  
