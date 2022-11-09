# mypkg라는 패키지에서 operation 모듈 가져오기
# from mypkg import operation as o, geometry as g
# from mypkg import geometry
# 패키지 초기화 해주는 파일 __init__.py 에 리스트로 선언해주면 아래가 가능
# __all__ = [원하는 모듈들]
from mypkg import *

print(operation.add(5, 7))
print(operation.mul(5, 7))

# mypkg라는 패키지에서 geometry 모듈 가져오기
# import mypkg.geometry as geometry

print(geometry.triangle_area(3, 5))
print(geometry.rectangle_area(4, 4))
