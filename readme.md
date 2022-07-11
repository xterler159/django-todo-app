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
