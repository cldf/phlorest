from phlorest import Metadata
from phlorest.scaffold import PhlorestTemplate


def test_template(tmp_path):
    PhlorestTemplate().render(tmp_path, Metadata(id='x'))
    assert tmp_path.joinpath('x', 'etc', 'taxa.csv').exists()
