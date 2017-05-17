def build(array, base=10):
    if array is None:
        return False
    if not array:
        return []
    ele = max(array)
    dig = len(str(abs(ele)))
    curr_array = array
    for digit in range(dig):
        buckets = [[] for _ in range(base)]
        for item in curr_array:
            buckets[(item//(base**digit))%base].append(item)
        curr_array = []
        for bucket in buckets:
            curr_array.extend(bucket)
    return curr_array
