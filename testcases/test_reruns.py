def test_function(request):
    execution_count = request.node.execution_count
    if execution_count:
        print(f"当前重试轮数：{execution_count}")
    assert False
    # 测试逻辑