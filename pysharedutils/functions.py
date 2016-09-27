from importlib import import_module

__all__ = [
    'import_by_path',
]


def import_by_path(path):
    """
    :param path: The path to the class that has to be imported.

    Imports a class or module by path(dot syntax)
    Raise ImportError if the import failed.
    """
    splited_path = path.rsplit('.', 1)
    if len(splited_path) == 1:
        module_path = splited_path[0]
        class_name = None
    elif len(splited_path) == 2:
        module_path, class_name = splited_path
    else:
        msg = '{path} is not a valid module path'.format(
            path=path
        )
        raise ImportError(msg)

    module = import_module(module_path)

    if class_name:
        return getattr(module, class_name)
    return module
