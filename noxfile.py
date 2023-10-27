import nox


@nox.session
def tests(session):
    # Install the project using `pip` and include the `tests` extra.
    session.install(".")

    # Run the tests using the `nox -s tests` command.
    session.run("nox", "-s", "tests")
