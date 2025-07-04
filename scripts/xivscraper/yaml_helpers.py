import yaml


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedDumper, self).increase_indent(flow, False)

def dump_indented_yaml(data, indent=2):
   return yaml.dump(data, Dumper=IndentedDumper, default_flow_style=False, indent=indent)
