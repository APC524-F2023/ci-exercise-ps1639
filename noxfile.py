import nox


@nox.session
def tests(session):
    session.install("-e", ".[tests]")
    session.install("pytest", "uncertainties")

    session.run("pytest")
