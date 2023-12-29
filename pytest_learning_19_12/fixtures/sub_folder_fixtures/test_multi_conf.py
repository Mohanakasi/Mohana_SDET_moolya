import pytest
pytestmark = [pytest.mark.check_multi_confs]
@pytest.mark.usefixtures("setup_file", "file_data_create", "file_read")
class Test_conf_ops:

    def test_files1(self, file_read):
        res = file_read.readline()
        assert 'sample' in res


