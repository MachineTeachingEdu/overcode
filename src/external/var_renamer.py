from redbaron import RedBaron


class VariableNameClashException(Exception):
    """Exception raised when a variable name change results in a clash
    with another variable which already has that name.

    Attributes:
        var_name -- the new variable name that resulted in the clash
        message -- explanation of the error
    """

    def __init__(self, var_name):
        self.var_name = var_name
        self.message = message = f"""Clash detected! Another variable 
                    in the source code already has the name '{self.var_name}'"""
        super().__init__(self.message)


def rename_var(src_code: str, var_name: str, new_var_name: str) -> str:
    """
    Rename variables in a provided source code.

    Args:
        src_code     -- string representing source code of a syntactically-correct
                        Python program
        var_name     -- variable to rename
        new_var_name -- the string to rename it to. It's the caller's
                        responsibility to confirm that this is a legal
                        Python identifier
    Returns:
        A new string similar to src_code except with ALL OCCURRENCES
        of var_name renamed to new_var_name

        Raises a VariableNameClashException if it detects a clash with the new variable name
        provided.

    PS:
        Docs for RedBaron can be found on: https://redbaron.readthedocs.io/en/latest/tuto.html
    """
    red = RedBaron(src_code)

    # The "name" arg makes it search only for NameNodes in the Syntax Tree
    if red.find("name", value=new_var_name):
        raise VariableNameClashException(new_var_name)
    else:
        vars = red.find_all("name", value=var_name)
        for var in vars:
            var.value = new_var_name
        return red.dumps()
