from .bubble import bubble_sort
from .heap import heap_sort
from .insertion import insertion_sort
from .merge import merge_sort
from .quick import quick_sort
from .radix import radix_sort
from .selection import selection_sort

registry = {}


def add_entry(name: str, func):
    registry[name] = func


add_entry("bubble_sort", bubble_sort)
add_entry("insertion_sort", insertion_sort)
add_entry("selection_sort", selection_sort)
add_entry("merge_sort", merge_sort)
add_entry("quick_sort", quick_sort)
add_entry("radix_sort", radix_sort)
add_entry("heap_sort", heap_sort)
