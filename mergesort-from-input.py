{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 import sys\
\
def get_names_to_sort():\
\
    names_to_sort = []\
\
    for line in sys.stdin:\
        name_and_attributes = line.split()\
        if name_and_attributes[1] == '0':\
            names_to_sort.append([name_and_attributes[0], int(name_and_attributes[2])])\
\
    sorted_names = mergesort(names_to_sort)\
\
    return sorted_names\
\
def mergesort(name_list):\
    length = len(name_list)\
    if length > 1:\
        med_index = length // 2\
        left = mergesort(name_list[0:med_index])\
        right = mergesort(name_list[med_index : length])\
        name_list = merge(left, right)\
    \
    return name_list\
    \
def merge(left, right):\
    merged_list = []\
    pl = 0\
    pr = 0\
    \
    while pl < len(left) and pr < len(right):\
        if left[pl][1] <= right[pr][1]:\
            merged_list.append(left[pl])\
            pl += 1\
        else:\
            merged_list.append(right[pr])\
            pr += 1\
\
    while pl < len(left) and pr == len(right):\
        merged_list.append(left[pl])\
        pl += 1\
\
    while pl == len(left) and pr < len(right):\
        merged_list.append(right[pr])\
        pr += 1\
\
    return merged_list\
\
def main():\
    output = get_names_to_sort()\
    o_string = ""\
    \
    for name in output:\
        o_string += name[0] + "\\n"\
\
    print(o_string[:-1])\
    \
\
main()\
\
\
\
\
\
\
\
}