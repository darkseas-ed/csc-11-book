from invoke import task


@task
def build(c):
    print("Building!")
    c.run("jupyter-book build .")

@task
def push(c):
    print("Pushing book to github.")
    c.run("ghp-import -n -p -f ./_build/html")
