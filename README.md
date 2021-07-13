# pytility
Utilities for simplify some operations in python. @WIP

Example:
```python
from pytility.ext.pydantic import models_compare

new_status = StatusModel(**some_attrs)
last_status: StatusModel = statusStore.get(status.id)

# Returns a list with tuple of models with field as last element containing differed attributes.
diff: List[Tuple[BaseModel, BaseModel, String]] = models_compare(
  new=new_status,
  old=last_status,
  fields=status.__fields_set__,
)
```
