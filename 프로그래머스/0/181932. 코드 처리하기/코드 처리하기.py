def solution(code):
    mode = 0
    ret = []

    for idx in range(len(code)):
        char = code[idx]
        if mode == 0:
            if char != "1":
                if idx % 2 == 0:
                    ret.append(char)
            else:
                mode = 1
        elif mode == 1:
            if char != "1":
                if idx % 2 == 1:
                    ret.append(char)
            else:
                mode = 0

    if not ret:
        return "EMPTY"
    return ''.join(ret)
