from pathlib import Path

import yaml

def yaml_loader(yaml_path: Path):
        """
        Utility method to load method from a .yml file into the tests.
        
        :param yaml_path: Relative path to the .yml file
        :type yaml_path: Path
        """
        with open (yaml_path, "r") as f:
            data = yaml.safe_load()
        return data["products"]