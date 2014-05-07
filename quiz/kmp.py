#!/usr/bin/env python
# encoding: utf-8

BACK_POS = {}


def next_pos(sub_str, pos_):
    if sub_str in BACK_POS:
        pos_info = BACK_POS[sub_str]
    else:
        pos_info = [0]
        len_sub_str = len(sub_str)
        for index in range(1, len_sub_str):
            if sub_str[pos_info[-1]] == sub_str[index]:
                pos = pos_info[-1] + 1
            else:
                pos = 0
            pos_info.append(pos)
        BACK_POS[sub_str] = pos_info
    return pos_ - pos_info[pos_]


def kmp_index(main_str, sub_str):
    len_main_str = len(main_str)
    len_sub_str = len(sub_str)
    index_main_str = 0
    index_sub_str = 0
    while index_main_str < len_main_str:
        if sub_str[index_sub_str] == main_str[index_main_str]:
            # match
            if index_sub_str == len_sub_str - 1:
                return index_main_str - len_sub_str + 1
            else:
                index_sub_str += 1
        else:
            # no match
            match_length = index_sub_str + 1
            index_sub_str = next_pos(sub_str, match_length-1)
        index_main_str += 1
    return None


def simple_index(main_str, sub_str):
    start = 0
    length = len(main_str)
    length_sub_str = len(sub_str)
    while start + length_sub_str < length:
        for index, char in enumerate(sub_str):
            if char == main_str[start + index]:
                continue
            else:
                break
        else:
            return start
        start += 1

if __name__ == '__main__':
    assert simple_index('absfsfc', 'sfs') == 2
    assert simple_index('absfsfc', 'sfa') is None
    assert simple_index('absfsfc', 'abs') == 0
    print 'All simple done.'

    assert kmp_index('absfsfc', 'sfs') == 2
    assert kmp_index('absfsfc', 'sfa') is None
    assert kmp_index('absfsfc', 'abs') == 0
    assert kmp_index('absfsfc', 'f') == 3
    print 'All kmp done.'
