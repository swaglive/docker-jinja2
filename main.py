import os
import jinja2


def render():
    # Construct Template object from env var
    # Render to output file
    input = os.environ['RENDER__INPUT']
    output_file = os.environ['RENDER__OUTPUT_FILE']
    env = jinja2.Environment()
    template = env.from_string(input)
    content = template.render({'env': os.environ})
    with open(output_file, 'w') as fp:
        fp.write(content)


if __name__ == '__main__':
    render()
