def task_hello():
    """hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["hello.txt"],
        }

def task_build():
    """Build the jupyter book"""
    d = {
        'actions': ['jupyter-book', 'build', '../csc-11-book']
    }
    return d
