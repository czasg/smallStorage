from notebook.re_cza import reRuler
"""
*可以表示为{0,}
+可以表示为{1,}
?可以表示为{0,1}

[匹配-—] 只能匹配到这里面的某一个字，无法具体匹配其字串
此时我们可以使用 (?:匹配|-|—)这样就可以了

(?<=(href=)) 表示匹配以(href=)开发的字符串，并且存储到分组中
(?=(href=)) 表示匹配以(href=)结尾的字符串，并且存储到分组中
(?<=(?:href=)) 表示匹配以(href=)开发的字符串，但不存储到分组中
(?=(?:href=)) 表示匹配以(href=)结尾的字符串，但不存储到分组中
"""
if __name__ == "__main__":
    test1 = 'czaissg'
    handle = reRuler('.*')
    print(handle.handle.findall(test1))