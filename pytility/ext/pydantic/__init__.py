from typing import List, Set, Tuple, TypeVar

String = TypeVar('String', bound=str)


def models_compare(
    fields: Set[String], new: BaseModel, old: BaseModel
) -> List[Tuple[BaseModel, BaseModel, String]]:

    result: List[Tuple[BaseModel, BaseModel, String]] = []
    for field in fields:
        old_attr = getattr(old, field)
        new_attr = getattr(new, field)
        if new_attr != old_attr:
            if isinstance(new_attr, BaseModel):
                logger.warning(
                    'Nested model expected, '
                    'running recursive strategy',
                )
                sub_diff = compare(
                    (new_attr.__fields_set__ - exclude_fields),
                    new_attr,
                    old_attr,
                )
                result.extend(sub_diff)
            result.append((new, old, field))
            continue
    return result
