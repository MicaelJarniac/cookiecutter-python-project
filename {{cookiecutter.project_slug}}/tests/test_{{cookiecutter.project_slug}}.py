from {{ cookiecutter.project_slug }} import make_greeting


def test_make_greeting():
    assert (
        make_greeting("{{ cookiecutter.full_name }}")
        == "Hello, {{ cookiecutter.full_name }}. Welcome to your new project!"
    )
