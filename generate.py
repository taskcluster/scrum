import yaml


THEMES_TPL = """\
# Themes

Themes are large focus areas than span the Mozilla organization and are pertinent and addressable by the Taskcluster team.

The following are the current themes:

{toc}

To update this information, edit `data/themes.yml` and run `generate.py`.

{body}
"""

INITIATIVES_TPL = """\
# Initiatives

An _initiative_ is a collection of one or more milestones that, taken together, address one or more themes. Initiatives map to major projects that the Taskcluster team would like to accomplish, and can be either new functionality or substantial reworks of existing functionality. Depending on the project area, an initiative can be a thin wrapper around a single milestone if that milestone is high value and self-contained.

The following are the current initiatives:

{toc}

To update this information, edit `data/initiatives.yml` and run `generate.py`.

{body}
"""

def load(filename):
    return yaml.safe_load(open(filename))


def load_data():
    global THEMES, INITIATIVES
    THEMES = load("data/themes.yml")
    INITIATIVES = load("data/initiatives.yml")


def fix_themes():
    for id, theme in THEMES.items():
        print(f'fixing theme {id}')
        assert 'description' in theme
        assert 'title' in theme


def write_themes():
    print("writing gen/themes.md")
    with open("gen/themes.md", "w") as f:
        toc = []
        body = []
        for id, theme in sorted(THEMES.items()):
            toc.append(f'* [{theme["title"]}](#{id})')
            theme_body = [
                f'## {id}',
                f'*{theme["title"]}*',
                '',
                theme['description'],
                '',
                '*Associated Initiatives:*',
                '',
            ]
            for init_id, init in INITIATIVES.items():
                if id in init['themes']:
                    theme_body.append(f'* [{init["title"]}](./initiatives.md#{init_id})')
            theme_body.append('')

            body.append('\n'.join(theme_body))

        toc = '\n'.join(toc)
        body = "\n\n".join(body)

        f.write(THEMES_TPL.format(toc=toc, body=body))

def fix_initiatives():
    for id, init in INITIATIVES.items():
        print(f'fixing init {id}')
        assert 'description' in init
        assert 'title' in init
        if 'theme' in init:
            init['themes'] = [init['theme']]
            del init['theme']
        assert 'themes' in init
        for theme_id in init['themes']:
            assert theme_id in THEMES

def write_initiatives():
    print("writing gen/initiatives.md")
    with open("gen/initiatives.md", "w") as f:
        toc = []
        body = []
        for id, init in sorted(INITIATIVES.items()):
            toc.append(f'* [{init["title"]}](#{id})')
            init_body = [
                f'## {id}',
                f'*{init["title"]}*',
                '',
                init['description'],
                '',
                f'*Addresses {"Themes" if len(init["themes"]) != 1 else "Theme"}:*',
                '',
            ]
            for theme_id in init['themes']:
                init_body.append(f'* [{THEMES[theme_id]["title"]}](./themes.md#{theme_id})')
            init_body.append('')

            body.append('\n'.join(init_body))

        toc = '\n'.join(toc)
        body = "\n\n".join(body)

        f.write(INITIATIVES_TPL.format(toc=toc, body=body))

def main():
    load_data()
    fix_themes()
    fix_initiatives()
    write_themes()
    write_initiatives()

main()
