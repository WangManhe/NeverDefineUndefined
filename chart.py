x1,y1,x2,y2=map(int,input().split())
if x1-x2==19-1 or x2-x1==19-1:
    # 两点分别在两侧(上下)
    # 两种情况取最小值:
    # 走左边(上边的左半部分,左侧一条边,下边的左半部分)
    # 走右边(上边的右半部分,右侧一条边,下边的右半部分)
    print(min( 19-1 + y1-1  + y2-1
             , 19-1 + 19-y1 + 19-y2))
elif y1-y2==19-1 or y2-y1==19-1:
    # 两点分别在两侧(左右)
    # 两种情况取最小值:
    # 走上方(左边的上半部分,顶部一条边,右边的上半部分)
    # 走下方(左边的下半部分,底部一条边,右边的下半部分)
    print(min( 19-1 + x1-1  + x2-1
             , 19-1 + 19-x1 + 19-x2 ))
else:
    # 两点在相邻或相同的边上
    # 可以直接计算横纵坐标的差的和
    print(abs(x1-x2)+abs(y1-y2))