def batch_isinstance(obj, parents):
    for p in parents:
        if isinstance(obj, p):
            return True
    return False
