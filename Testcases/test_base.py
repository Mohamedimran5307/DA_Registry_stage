import pytest


# @pytest.mark.flaky(reruns=3)
@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass
