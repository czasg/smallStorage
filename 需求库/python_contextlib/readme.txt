# context management

-> this is the most common way to manage context
with open(fileName, open_model) as file:
    file.read()

-> for a class
class Object:
    def __enter__(self):
        do_something_before_call_this_object()
        return self

    def __exit__(self):
        do_something_after_this_object_done()
with Object() as O:
    O.other_func()

-> using contextlib way, it is decorator
from contextlib import contextmanager
@contextmanager
def func():
    do_something_before_yield()  -> it will run before the main
    yield
    do_something_after_yield()  -> it will run after the main is done
|
with func():
    run_the_main_func()  -> it will run between the above two ways

from contextlib import closing
with closing(no_context_management_func) as c:
    running()  -> it still run although no thing run after or before it

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
