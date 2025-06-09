# 📄 Python Docstrings vs Multiline Comments


# ✅ Docstring Example (used for documentation and accessible via help())
def greet(name):
    """
    Greets the user with their name.

    Parameters:
    name (str): The name of the user

    Returns:
    str: A greeting message
    """
    return f"Hello, {name}!"


print(greet("Sudip"))
print(help(greet))  # Displays the docstring content

print("-" * 50)

# ❌ This is not a docstring — just a multiline comment (ignored by Python)
"""
This section is about performing setup logic.
Used for internal explanation only, not shown in help().
"""
# ✅ Multi-line Comment using #
# This section might include
# multiple lines of comment,
# but it won't be accessible through help()

# ✅ Module-level docstring (top of the file if this were a real module)
"""
This module provides examples of docstrings vs comments.
Use docstrings to document functions, classes, and modules.
Use comments for explanations.
"""
