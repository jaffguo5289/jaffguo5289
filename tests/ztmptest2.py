import pytest
@pytest.fixture
def testAdd(a,b):
  return (a + b)

@pytest.fixture
def ztmptest2():
  print("hello 2 from tests/ztmptest2...")
  assert testAdd(1,2)==3
  
ztmptest2()
