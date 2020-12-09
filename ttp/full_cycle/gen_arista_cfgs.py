from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
import yaml
from pprint import pprint


def load_yaml_file(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


def generate_configs(template_file, j2_vars):
    env = Environment(undefined=StrictUndefined, lstrip_blocks=True, trim_blocks=True)
    env.loader = FileSystemLoader(".")

    template = env.get_template(template_file)
    return template.render(**j2_vars)


if __name__ == "__main__":

    arista_vars = load_yaml_file("arista_vars.yaml")
    # pprint(arista_vars)

    template_file = "arista.j2"

    config = generate_configs(template_file, arista_vars)
    print(config)
